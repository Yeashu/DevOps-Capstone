# Troubleshooting and optional challenge

These are diagnosis steps and reproducible exercises, **not claims of failures observed and repaired on a running Orbit cluster in this session**. Record your actual symptoms, logs, root cause, repair and verification when you perform the challenge.

| Symptom | Inspect | Likely cause / repair | Verify |
| --- | --- | --- | --- |
| UI loads but calculation fails | Browser network `/api/calculations`, `docker compose logs backend` | Backend/database down; fix connectivity or invalid expression | POST returns 201; history reloads |
| API Ready probe fails | `kubectl logs -n orbit job/orbit-migrate-1`, backend init logs | Migration failed, Secret URL wrong, PostgreSQL not ready | Job Complete; `/ready` returns 200 |
| ImagePullBackOff | `kubectl describe pod -n orbit POD` | Wrong SHA, private GHCR package, local image not loaded | Correct tag/pull Secret; pod Running |
| Pending PostgreSQL | `kubectl get pvc -n orbit`, `kubectl describe pvc -n orbit CLAIM` | Storage class or EBS CSI/Pod Identity missing | PVC Bound; database Ready |
| Ingress 404 | `kubectl describe ingress -n orbit orbit` | Host header or Ingress class/controller mismatch | `/` and `/api/health` both reach correct services |
| Nginx cannot resolve backend | Nginx pod logs and Services | Missing release-specific Service/config | Chart ConfigMap points to `orbit-backend:8000` |
| Prometheus target absent/down | Targets API, endpoint discovery labels, `kubectl get endpoints -n orbit` | Wrong namespace/label, no Ready endpoints | Both `orbit-api` endpoints UP |
| Grafana panel empty | Explore Prometheus datasource; query `sum(up{job="orbit-api"})` | Missing scrapes, datasource URL, or insufficient rate window | Generate traffic for a minute; graph populates |
| Deployment job skipped | Repository variables and job condition | DEPLOY_TO_EKS not true, non-main ref, publication failed | Bootstrap then enable; never remove security gates |
| Deployment job cannot reach EKS | Runner network, private endpoint, `admin_cidrs` | Hosted/dynamic runner not allowed | Use registered in-VPC or fixed-IP capstone runner |
| Terraform provider cannot start | `terraform validate` and provider logs | Session sandbox/process/socket restriction | Run in a normal local terminal or CI configuration job |

## Local-cluster challenge

Use only your disposable Orbit Minikube deployment, not a shared course/production cluster. Save the successful chart values and baseline state first. Introduce **one issue at a time**, diagnose it, and restore before moving on.

```bash
kubectl config current-context
kubectl get pods,svc,ingress -n orbit
helm get values orbit -n orbit -a > /tmp/orbit-baseline-values.yaml
```

**Wrong image tag:** point the frontend at an intentionally nonexistent local tag, inspect pod events for ImagePullBackOff, then restore via Helm using the same valid image settings as your initial install.

```bash
kubectl set image deployment/orbit-frontend frontend=orbit-frontend:missing-demo-tag -n orbit
kubectl get pods -n orbit
kubectl describe pods -n orbit -l app=orbit,component=frontend
helm upgrade --install orbit helm/orbit -n orbit -f /tmp/orbit-baseline-values.yaml \
  --wait --wait-for-jobs --timeout 10m
```

**Wrong Service selector:** break the backend selector, inspect EndpointSlices and a failed API request, then restore the expected selector.

```bash
kubectl patch svc orbit-backend -n orbit --type merge -p '{"spec":{"selector":{"component":"missing-demo"}}}'
kubectl get endpointslices -n orbit -l kubernetes.io/service-name=orbit-backend
kubectl patch svc orbit-backend -n orbit --type merge -p '{"spec":{"selector":{"component":"backend"}}}'
kubectl get endpointslices -n orbit -l kubernetes.io/service-name=orbit-backend
```

**Wrong Ingress host:** request with a mismatched Host header to observe default-controller routing; repeat with the configured host and confirm `/api/health` succeeds. This does not require changing cluster resources.

Keep before/after logs and browser screenshots and write your own root-cause explanation. The application replicas, endpoint counts, health response and metric scrape should all recover after each repair.
