#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
profile=${MINIKUBE_PROFILE:-minikube}
minikube status -p "$profile"
kubectl --context "$profile" cluster-info
docker build -t orbit-backend:local backend
docker build -t orbit-frontend:local frontend
minikube image load -p "$profile" orbit-backend:local orbit-frontend:local
minikube addons enable ingress -p "$profile"
kubectl --context "$profile" apply -f k8s/namespace.yaml
if ! kubectl --context "$profile" get secret orbit-database -n orbit >/dev/null 2>&1; then
  # Secret helper uses the explicit context selected for this script's subprocess.
  KUBECONFIG_FILE=$(mktemp)
  trap 'rm -f "$KUBECONFIG_FILE"' EXIT
  kubectl config view --minify --context "$profile" --raw > "$KUBECONFIG_FILE"
  KUBECONFIG="$KUBECONFIG_FILE" python3 scripts/create-db-secret.py
fi
helm upgrade --install orbit helm/orbit --kube-context "$profile" \
  -n orbit --wait --wait-for-jobs --timeout 10m
kubectl --context "$profile" get pods,svc,ingress -n orbit
printf '%s\n' 'Access the Ingress with:' \
  "kubectl --context $profile port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80" \
  'Then open http://orbit.localhost:8080 (or curl -H "Host: orbit.localhost" http://127.0.0.1:8080).'
