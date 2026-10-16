# Evidence index

Existing PNGs are **labelled renders of real command output**. They are not application screenshots and do not prove a cloud deployment. The original text logs are in `docs/evidence/`.

| Existing evidence | What it proves |
| --- | --- |
| `docs/screenshots/calculator-unit-tests-*.png` | 52 scientific engine tests pass; API cases are not included |
| `docs/screenshots/frontend-build.png` | Four frontend tests and production build pass |
| `docs/screenshots/git-history.png` | At least ten meaningful local commits |
| `docs/screenshots/terraform-init.png` | Actual offline initialization with cached provider; initial cache origin was unauthenticated |
| `docs/evidence/terraform-validate.txt` | Actual blocked validation, not a successful validation claim |
| `docs/evidence/dependency-install.txt` | Backend dependency installation unavailable in this session |

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
| M4 | Three healthy Compose services / non-root IDs | `docker-compose.png`, `non-root-users.png` |
| M5 | Green Actions workflow | Manual GitHub browser capture + actual run URL in `SUBMISSION.md` |
| M5 | Both GHCR image package pages with full SHA tags | Manual package page captures |
| M6 | Both real Trivy image scan steps | Actions browser captures + downloaded report artifacts |
| M7 | Terraform non-empty plan | `terraform-plan.png` + full original plan text |
| M7 | AWS Console region, VPC, two subnets, EKS/worker group | Manual authenticated AWS Console captures |
| M7 | Actual destroy completion | `terraform-destroy.png` + completion log |
| M8 | Pods, Services, Helm release | `kubernetes-pods.png`, `kubernetes-services.png`, `helm-list.png` |
| M8 | UI through Ingress | `ingress-application.png` |
| M9 | Real backend `/metrics` | `metrics.png` |
| M9 | Both application targets UP | `15-prometheus-targets.png` |
| M9 | Populated live dashboard | `16-grafana-dashboard.png` |
| M10 | Recorded end-to-end change/deploy or live demo | Recording URL / presentation session |

The workflow's `browser-and-compose-evidence` artifact produces the first four UI captures on a successful network-enabled run. `pytest-evidence` contains the full backend test result. Download these after the first green workflow; their existence in configuration is not a completed capture.

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
