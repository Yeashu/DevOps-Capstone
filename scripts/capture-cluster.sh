#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
python_bin=${ORBIT_PYTHON:-.venv/bin/python}
mkdir -p docs/evidence docs/screenshots
kubectl get pods -n orbit -o wide | tee docs/evidence/kubernetes-pods.txt
kubectl get svc -n orbit | tee docs/evidence/kubernetes-services.txt
kubectl get ingress -n orbit | tee docs/evidence/kubernetes-ingress.txt
helm list -n orbit | tee docs/evidence/helm-list.txt
kubectl wait -n orbit pod -l app=orbit,component=backend --for=condition=Ready --timeout=180s
kubectl wait -n orbit pod -l app=orbit,component=frontend --for=condition=Ready --timeout=180s
for name in kubernetes-pods kubernetes-services kubernetes-ingress helm-list; do
  "$python_bin" scripts/render-transcript.py "docs/evidence/$name.txt" \
    "docs/screenshots/$name.png" --title "Orbit | $name"
done
echo 'Use the Ingress APP_URL with capture-browser.mjs for genuine cluster browser evidence.'
