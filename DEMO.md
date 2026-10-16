# Presentation and live demonstration

A real [92-second technical walkthrough](docs/recordings/orbit-eks-rollout.mp4) and [captions](docs/recordings/orbit-eks-rollout.vtt) are included. To use the captioned player, run `python3 -m http.server 8765 --bind 127.0.0.1` from the root and open http://localhost:8765/docs/recordings/. It shows the EKS calculator, successful run 38947611595, a local Helm rollout to `7f36cafc34b923fa34b1a0e727b2d359a060c757`, the updated health version and the persistent notebook. The hosted optional EKS delivery job was skipped; the recording accurately identifies the local CLI rollout.

The final rubric requires an actual commit → pipeline → deployment update. The default CI pipeline publishes images; automatic deployment is deliberately opt-in until AWS and the deployment role/runner are configured. Do this preparation before presenting.

## Prepare

1. Run all backend/frontend tests, build Compose and capture browser evidence.
2. Push the local commits to the GitHub repository; confirm access and GHCR package visibility.
3. Provision the AWS infrastructure with Terraform, update kubeconfig, and capture the plan, AWS VPC/EKS/worker group pages.
4. Set `ORBIT_EKS_CONTEXT` and run `./scripts/bootstrap-eks.sh` for the namespace, EKS storage class, database secret and Traefik controller. Deploy with `ingress.className=traefik` and port-forward its Service for the demo. A public LoadBalancer instead requires appropriate AWS integration and a DNS record.
5. Configure the environment, OIDC role, runner and variables described in README. Bootstrap the chart with a previously successful SHA.
6. Install monitoring, open the app through Ingress, and start the traffic generator. Check both Prometheus endpoints UP and a populated Grafana panel.
7. Keep pipeline, app, cluster terminal, metrics and dashboard visible in separate tabs.

## Suggested six-minute explanation

| Time | Demonstrate |
| --- | --- |
| 0:00–1:00 | Orbit's purpose; `sqrt(144)+2^3=20`; DEG `sin(30)=0.5`; label/delete notebook entries |
| 1:00–2:00 | Architecture; FastAPI/database/frontend boundaries; migration; test isolation and real pytest output |
| 2:00–3:00 | Non-root containers; meaningful commit history; gated pipeline and SHA-tagged images |
| 3:00–4:00 | Trivy reports and one actual result; Terraform VPC/EKS; explain node group and cost teardown |
| 4:00–5:00 | Helm release, two replicas each, Services, Ingress and probes |
| 5:00–6:00 | Live metrics and dashboard; explain what request rate and p95 latency mean |

Allow additional time to watch the actual CI and rollout; its duration is not a six-minute guarantee.

## Commit → green pipeline → updated deployment

Change the visible tagline in `frontend/index.html`, for example from `Made for curious minds.` to `Made for scientific curiosity.`. This is a real, reviewable change.

```bash
git add frontend/index.html
git commit -m "Refine the calculator footer for the capstone presentation"
git push origin main
git rev-parse HEAD
```

Open that commit's Actions run. Watch PostgreSQL-backed tests, frontend build, source security, live browser test, both image builds/scans, GHCR publication and the optional delivery job. Verify all required jobs are green. A skipped deployment does not demonstrate automatic delivery.

```bash
kubectl rollout status deployment/orbit-backend -n orbit
kubectl rollout status deployment/orbit-frontend -n orbit
kubectl get deployment/orbit-frontend -n orbit \
  -o jsonpath='{.spec.template.spec.containers[0].image}'
```

The image tag must match the commit shown by `git rev-parse HEAD`. Refresh the Ingress application and show the updated footer. `/api/health` reports the same backend SHA. Show that the database notebook survives the rollout and Grafana still receives requests.

If using Argo CD instead, leave direct CI deployment disabled, publish the app commit first, update both tags in `gitops/values.yaml` to that successful app SHA, commit the desired-state update, and show Argo CD sync and the actual cluster images. Do not imply that pushing to GHCR alone updated the cluster.

## Clean up and submit

Capture real pods, Services, Helm list, Ingress, metrics, Prometheus and Grafana evidence. Save the Actions URL and recording link in `SUBMISSION.md`. Uninstall the demo releases, remove the application's retained PVC, verify load balancers/EBS are gone, run Terraform destroy, capture its completion and check the Console. Complete the actual scan explanation and checklist.
