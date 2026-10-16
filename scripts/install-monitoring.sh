#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
kubectl apply -f k8s/namespace.yaml
if ! kubectl get secret grafana-admin -n monitoring >/dev/null 2>&1; then
  printf 'Choose a Grafana administrator password: ' >&2
  read -rs grafana_password
  printf '\n' >&2
  if [ "${#grafana_password}" -lt 12 ]; then
    echo 'Use at least 12 characters.' >&2
    exit 1
  fi
  secret_file=$(mktemp)
  trap 'rm -f "$secret_file"' EXIT
  chmod 600 "$secret_file"
  printf 'admin-user=admin\nadmin-password=%s\n' "$grafana_password" > "$secret_file"
  kubectl create secret generic grafana-admin -n monitoring --from-env-file="$secret_file"
  unset grafana_password
fi
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo add grafana https://grafana.github.io/helm-charts
helm repo update
kubectl create configmap orbit-dashboard -n monitoring \
  --from-file=orbit.json=monitoring/orbit-dashboard.json \
  --dry-run=client -o yaml | kubectl apply -f -
kubectl label configmap orbit-dashboard -n monitoring grafana_dashboard=1 --overwrite
helm upgrade --install prometheus prometheus-community/prometheus \
  -n monitoring -f monitoring/prometheus-values.yaml --wait --timeout 10m
helm upgrade --install grafana grafana/grafana \
  -n monitoring -f monitoring/grafana-values.yaml --wait --timeout 10m
printf '%s\n' 'Forward Prometheus: kubectl port-forward -n monitoring svc/prometheus-server 9090:80' \
  'Forward Grafana: kubectl port-forward -n monitoring svc/grafana 3001:80'
