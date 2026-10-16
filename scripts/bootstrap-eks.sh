#!/usr/bin/env bash
# Run after Terraform apply and aws eks update-kubeconfig. Does not create AWS resources.
set -euo pipefail
cd "$(dirname "$0")/.."
: "${ORBIT_EKS_CONTEXT:?Set ORBIT_EKS_CONTEXT to the EKS context shown by kubectl config get-contexts}"
config_file=$(mktemp)
trap 'rm -f "$config_file"' EXIT
chmod 600 "$config_file"
kubectl config view --minify --context "$ORBIT_EKS_CONTEXT" --raw > "$config_file"
export KUBECONFIG="$config_file"
kubectl cluster-info
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/storageclass-eks.yaml
if ! kubectl get secret orbit-database -n orbit >/dev/null 2>&1; then
  python3 scripts/create-db-secret.py
fi
# ClusterIP plus port-forward demonstrates Ingress without creating an AWS LB.
helm upgrade --install traefik oci://ghcr.io/traefik/helm/traefik \
  -n ingress-system --create-namespace \
  --set service.type=ClusterIP --set ingressClass.isDefaultClass=false \
  --wait --timeout 10m
printf '%s\n' 'EKS bootstrap complete. Deploy Orbit with ingress.className=traefik and database.persistence.storageClass=gp3.' \
  'Forward the controller: kubectl port-forward -n ingress-system svc/traefik 8080:80' \
  'Use the configured Ingress hostname at port 8080. This setup does not create a public load balancer.'
