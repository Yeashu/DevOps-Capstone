# Submission evidence

Browser PNGs are actual captures of Orbit, GitHub, AWS, Prometheus and Grafana. Command-output PNGs are explicitly labelled rendered transcripts of real source logs retained in `docs/evidence/`; they are not native terminal-window screenshots. Capture and hosted run timestamps are actual. Owner-assigned Git timestamps do not establish an earlier completion time.

| Module | Main evidence |
| --- | --- |
| M1, M4 | [Desktop application](docs/screenshots/01-application-desktop.png), [mobile](docs/screenshots/02-application-mobile.png), [degrees](docs/screenshots/03-degrees.png), [domain error](docs/screenshots/04-domain-error.png) |
| M2 | [Pytest 1](docs/screenshots/pytest-01.png), [2](docs/screenshots/pytest-02.png), [3](docs/screenshots/pytest-03.png); [hosted PostgreSQL source log](docs/evidence/hosted-pytest.txt) |
| M3 | [GitHub commit history](docs/screenshots/github-commit-history.png), [history credential-pattern check](docs/evidence/git-history-secret-check.json) |
| M4 | [Healthy services](docs/screenshots/docker-compose-status.png), [non-root users](docs/screenshots/non-root-users.png) |
| M5 | [Green pipeline](docs/screenshots/github-actions-success.png), [backend SHA tags](docs/screenshots/ghcr-backend.png), [frontend SHA tags](docs/screenshots/ghcr-frontend.png) |
| M6 | [Backend scan 1](docs/screenshots/trivy-backend-01.png), [2](docs/screenshots/trivy-backend-02.png), [frontend scan](docs/screenshots/trivy-frontend.png), [explanation](security/README.md) |
| M7 | [Terraform plan source](docs/evidence/terraform-plan.txt), numbered `terraform-plan-*.png`, [apply completion](docs/screenshots/terraform-apply-03.png), [VPC Console](docs/screenshots/aws-vpc-console.png), [two subnets](docs/screenshots/aws-subnets-console.png), [active EKS](docs/screenshots/aws-eks-console.png), [two Ready workers](docs/screenshots/aws-eks-workers-console.png) |
| M7 cleanup | [Actual destroy completion](docs/screenshots/terraform-destroy.png), [full resumed log](docs/evidence/terraform-destroy.txt), [first interrupted attempt](docs/evidence/terraform-destroy-first-attempt.txt), [independent AWS audit](docs/evidence/aws-cleanup-audit.json), [audit transcript](docs/screenshots/aws-cleanup-audit.png) |
| M8 on EKS | [Pods](docs/screenshots/eks-pods.png), [nodes](docs/screenshots/eks-nodes.png), [Services](docs/screenshots/eks-services.png), [Helm](docs/screenshots/eks-helm-list.png), [Ingress](docs/screenshots/eks-ingress.png), [Bound PVC](docs/screenshots/eks-pvc.png), [browser through Ingress](docs/screenshots/eks-application-desktop.png) |
| M9 on EKS | [Metrics source](docs/evidence/eks-metrics.txt), numbered `eks-metrics-*.png`, [Prometheus targets UP](docs/screenshots/eks-prometheus-targets.png), [populated Grafana](docs/screenshots/eks-grafana-dashboard.png) |
| M10 | [92-second actual rollout](docs/recordings/orbit-eks-rollout.webm), [captions](docs/recordings/orbit-eks-rollout.vtt), [player](docs/recordings/index.html), [updated SHA](docs/screenshots/eks-updated-version.png), [notebook after rollout](docs/screenshots/eks-after-rollout.png), [runbook](DEMO.md) |

Separate `kubernetes-*`, `helm-list.png`, `15-prometheus-targets.png`, `16-grafana-dashboard.png` and `ingress-application.png` show the successful disposable **Kind** demonstration in [run 38946260879](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38946260879). The explicitly named `eks-*` and `aws-*` evidence shows the real AWS lifecycle. A Completed migration Job is expected; the five application pods are Running/Ready.

The recording shows an authenticated **local Helm rollout after CI passed**; the optional hosted persistent EKS deployment job was disabled. It is not described as an automatic hosted EKS deployment.

To reproduce evidence, use `scripts/capture-evidence.sh` for Compose and `scripts/capture-cluster.sh` for your selected cluster. Browser capture checks real API responses, responsive layout, both Prometheus targets and positive Grafana query data before saving. Cloud resources were destroyed after capture; local Compose can still run at http://localhost:3000.
