# Evidence index

Actual browser captures and labelled renders of real command output are committed under `docs/screenshots/`; source logs are retained under `docs/evidence/`. No screenshots or successful command results are fabricated. Transcript PNGs are not original terminal-window screenshots.

Verified evidence includes the working local Compose UI, all 69 pytest cases, healthy services, non-root IDs, backend metrics, both clean Trivy reports, a deployed Helm release on Kind, pods/Services/Ingress and two Prometheus targets UP. The non-empty AWS Terraform plan is included as source text and numbered PNGs. The final Grafana capture and green run are included. AWS apply, EKS application/monitoring verification and Console captures are complete; cleanup is pending; see [SUBMISSION.md](SUBMISSION.md) for remaining items.

- [Recorded EKS rollout](docs/recordings/orbit-eks-rollout.webm) · [captioned player](docs/recordings/index.html)
- [Updated EKS SHA](docs/screenshots/eks-updated-version.png)
- [Notebook after rollout](docs/screenshots/eks-after-rollout.png)
- [AWS VPC Console](docs/screenshots/aws-vpc-console.png)
- [Two public subnets](docs/screenshots/aws-subnets-console.png)
- [Active EKS Console](docs/screenshots/aws-eks-console.png)
- [Two Ready workers in AWS Console](docs/screenshots/aws-eks-workers-console.png)
- [Application on EKS through Ingress](docs/screenshots/eks-application-desktop.png)
- [EKS Prometheus targets](docs/screenshots/eks-prometheus-targets.png)
- [EKS Grafana dashboard](docs/screenshots/eks-grafana-dashboard.png)
- [Green Actions run](docs/screenshots/github-actions-success.png)
- [Populated Grafana dashboard](docs/screenshots/16-grafana-dashboard.png)
- [Application through Ingress](docs/screenshots/ingress-application.png)
- [Desktop calculator](docs/screenshots/01-application-desktop.png)
- [Mobile calculator](docs/screenshots/02-application-mobile.png)
- [Passing tests](docs/screenshots/pytest-03.png)
- [Healthy Compose services](docs/screenshots/docker-compose-status.png)
- [Non-root users](docs/screenshots/non-root-users.png)
- [Running Kubernetes pods](docs/screenshots/kubernetes-pods.png)
- [ClusterIP Services](docs/screenshots/kubernetes-services.png)
- [Helm release](docs/screenshots/helm-list.png)
- [Prometheus targets](docs/screenshots/15-prometheus-targets.png)
- [Backend clean scan](docs/screenshots/trivy-backend-02.png)
- [Frontend clean scan](docs/screenshots/trivy-frontend.png)
- [Backend GHCR SHA tags](docs/screenshots/ghcr-backend.png)
- [Frontend GHCR SHA tags](docs/screenshots/ghcr-frontend.png)
- [GitHub commit history](docs/screenshots/github-commit-history.png)
- [Terraform plan source](docs/evidence/terraform-plan.txt)

The Kind cluster was created by [run 38944998841](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38944998841). Its final Grafana screenshot failed after the live datasource query passed. [Run 38946260879](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38946260879) corrects that selector. Kind evidence is not described as AWS EKS evidence.

## Required live captures

Run from the root after `.venv` has the backend requirements and Pillow installed:

```bash
./scripts/capture-evidence.sh
./scripts/capture-cluster.sh
```

The first command builds and starts Compose, executes the full tests, captures non-root IDs and `/metrics`, and runs Playwright on the real API-backed UI. The second reads your current cluster, so check `kubectl config current-context` first. The helpers retain source text and label transcript renders. For strict terminal screenshot requirements, also capture the actual terminal window displaying those commands using your operating system screenshot shortcut.

| Module | Capture | Filename / source |
| --- | --- | --- |
| M1, M4 | Desktop UI through Compose | `01-application-desktop.png` |
| M1 | Responsive mobile UI | `02-application-mobile.png` |
| M1 | Degree calculation and invalid-domain handling | `03-degrees.png`, `04-domain-error.png` |
| M2 | **Full** passing `pytest -v`, including API cases | `pytest-*.png` plus terminal capture |
| M3 | Public repository and ≥10 commits | `git-history.png` plus GitHub commits page |
| M4 | Three healthy Compose services / non-root IDs | `docker-compose-status.png`, `non-root-users.png` |
| M5 | Green Actions workflow | GitHub browser capture + actual run URL in `SUBMISSION.md` |
| M5 | Both GHCR image package pages with full SHA tags | Manual package page captures |
| M6 | Both real Trivy image scan steps | Actions browser captures + downloaded report artifacts |
| M7 | Terraform non-empty plan | `terraform-plan-*.png` + redacted source plan text |
| M7 | AWS Console region, VPC, two subnets, EKS/worker group | Manual authenticated AWS Console captures |
| M7 | Actual destroy completion | `terraform-destroy.png` + completion log |
| M8 | Pods, Services, Helm release | `kubernetes-pods.png`, `kubernetes-services.png`, `helm-list.png` |
| M8 | UI through Ingress | `ingress-application.png` |
| M9 | Real backend `/metrics` | `metrics.png` |
| M9 | Both application targets UP | `15-prometheus-targets.png` |
| M9 | Populated live dashboard | `16-grafana-dashboard.png` |
| M10 | Recorded end-to-end change/deploy or live demo | Recording URL / presentation session |

The workflow's `browser-and-compose-evidence` artifact contains the first four UI captures from the successful browser job in the initial run. `pytest-evidence` contains all 69 passing backend tests. Both are already available even though a later security job failed. A subsequent run must verify the replacement backend image before claiming that image is tested and clean.

## Cluster browser and monitoring captures

Forward the Ingress controller to port 8080, Prometheus to 9090, and Grafana to 3001 as documented in the README. Generate live traffic for at least a minute, then run:

```bash
export APP_URL=http://orbit.localhost:8080
export PROMETHEUS_URL=http://localhost:9090
export GRAFANA_URL=http://localhost:3001
read -rs GRAFANA_PASSWORD
export GRAFANA_PASSWORD
node scripts/capture-browser.mjs
unset GRAFANA_PASSWORD
cp docs/screenshots/01-application-desktop.png docs/screenshots/ingress-application.png
```

This overwrites the numbered app captures using the current APP_URL. The browser smoke JSON records that URL. Preserve Compose captures first if you need both sets. The tool checks live API health, both Prometheus targets and actual Grafana metric values before taking the corresponding evidence. Keep screenshots of passwords, access keys, tokens and raw state out of your submission.

For Terraform, capture `terraform plan -no-color` and `terraform destroy -no-color` output only from the real project lifecycle. Never create fake successful plan/apply/destroy text. Review logs for sensitive values before committing them.
