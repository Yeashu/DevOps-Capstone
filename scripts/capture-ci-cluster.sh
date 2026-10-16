#!/usr/bin/env bash
# Ephemeral GitHub runner demonstration; no AWS credentials or resources.
set -euo pipefail
cd "$(dirname "$0")/.."
: "${COMMIT_SHA:?A full scanned image commit SHA is required}"
mkdir -p docs/evidence docs/screenshots
export ORBIT_PYTHON=python
python -m pip install --disable-pip-version-check pillow
gunzip -c /tmp/orbit-backend-image/image.tar.gz | docker load
gunzip -c /tmp/orbit-frontend-image/image.tar.gz | docker load
kind load docker-image --name orbit "orbit-backend:$COMMIT_SHA" "orbit-frontend:$COMMIT_SHA"
kubectl apply -f k8s/namespace.yaml
python - <<'PY'
import base64, json, secrets, subprocess
password = secrets.token_urlsafe(32)
data = {'POSTGRES_PASSWORD': password,
        'DATABASE_URL': f'postgresql+psycopg://orbit:{password}@orbit-postgres:5432/orbit'}
manifest = {'apiVersion': 'v1', 'kind': 'Secret', 'type': 'Opaque',
            'metadata': {'name': 'orbit-database', 'namespace': 'orbit'},
            'data': {k: base64.b64encode(v.encode()).decode() for k, v in data.items()}}
subprocess.run(['kubectl', 'create', '-f', '-'], input=json.dumps(manifest), text=True, check=True)
PY
helm upgrade --install traefik oci://ghcr.io/traefik/helm/traefik \
  -n ingress-system --create-namespace --set service.type=ClusterIP \
  --set ingressClass.isDefaultClass=false --wait --timeout 5m
helm upgrade --install orbit helm/orbit -n orbit \
  --set backend.tag="$COMMIT_SHA" --set frontend.tag="$COMMIT_SHA" \
  --set ingress.className=traefik --wait --wait-for-jobs --timeout 8m
grafana_password=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
printf '::add-mask::%s\n' "$grafana_password"
export GRAFANA_PASSWORD="$grafana_password"
python - <<'PY'
import base64, json, os, subprocess
manifest = {'apiVersion': 'v1', 'kind': 'Secret', 'type': 'Opaque',
            'metadata': {'name': 'grafana-admin', 'namespace': 'monitoring'},
            'data': {k: base64.b64encode(v.encode()).decode() for k, v in {
                'admin-user': 'admin', 'admin-password': os.environ['GRAFANA_PASSWORD']}.items()}}
subprocess.run(['kubectl', 'create', '-f', '-'], input=json.dumps(manifest), text=True, check=True)
PY
bash scripts/install-monitoring.sh
kubectl port-forward -n ingress-system svc/traefik 8080:80 > /tmp/orbit-ingress-forward.log 2>&1 &
ingress_pid=$!
kubectl port-forward -n monitoring svc/prometheus-server 9090:80 > /tmp/orbit-prometheus-forward.log 2>&1 &
prometheus_pid=$!
kubectl port-forward -n monitoring svc/grafana 3001:80 > /tmp/orbit-grafana-forward.log 2>&1 &
grafana_pid=$!
kubectl port-forward -n orbit svc/orbit-backend 8000:8000 > /tmp/orbit-backend-forward.log 2>&1 &
backend_pid=$!
trap 'kill "$ingress_pid" "$prometheus_pid" "$grafana_pid" "$backend_pid" 2>/dev/null || true' EXIT
export APP_URL=http://orbit.localhost:8080
export PROMETHEUS_URL=http://localhost:9090
export GRAFANA_URL=http://localhost:3001
for url in "$APP_URL/api/health" "$PROMETHEUS_URL/-/ready" "$GRAFANA_URL/api/health" http://localhost:8000/ready; do
  for attempt in {1..60}; do
    if curl --fail --silent "$url" > /dev/null; then break; fi
    sleep 2
  done
  curl --fail --silent "$url" > /dev/null
done
python scripts/generate-traffic.py --url "$APP_URL" --seconds 90 | tee docs/evidence/cluster-traffic.txt
curl --fail --silent http://localhost:8000/metrics > docs/evidence/metrics.txt
curl --fail --silent "$PROMETHEUS_URL/api/v1/targets" > docs/evidence/prometheus-targets.json
bash scripts/capture-cluster.sh
kubectl get pods -n orbit -l 'component in (backend,frontend,postgres)' -o wide > docs/evidence/cluster-running-application-pods.txt
npm --prefix scripts install --ignore-scripts
./scripts/node_modules/.bin/playwright install --with-deps chromium
node scripts/capture-browser.mjs
cp docs/screenshots/01-application-desktop.png docs/screenshots/ingress-application.png
for name in kubernetes-pods kubernetes-services kubernetes-ingress helm-list metrics cluster-running-application-pods; do
  python scripts/render-transcript.py "docs/evidence/$name.txt" "docs/screenshots/$name.png" --title "Orbit | $name"
done
echo 'Real Kind/Helm/Ingress/Prometheus/Grafana evidence captured. This is not an AWS EKS deployment.'
