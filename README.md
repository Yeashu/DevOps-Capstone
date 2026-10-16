# Orbit · Scientific Calculator

A simple scientific calculator built in **Python with FastAPI**, with a responsive HTML/CSS/JavaScript interface and a PostgreSQL calculation notebook. Evaluate expressions, switch radians/degrees, revisit saved calculations, label them, and delete them.

Repository: **https://github.com/Yeashu/DevOps-Capstone**

Mandatory submission files: [demo/](demo/) contains the MP4 video and PPT/PDF slide deck.

Jump to the [recorded video and all 75 evidence images](#evidence-and-presentation).

**[Green CI run](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38959438459):** all 69 backend tests, frontend checks, the three-service Compose/browser demo, Terraform/Helm validation, both strict Trivy image scans, SHA-tagged GHCR publishing, and real Helm/Ingress/Prometheus/Grafana verification on Kind passed. Screenshots and original logs are included. Real AWS provisioning also passed: VPC, two public subnets, active EKS, two Ready workers, Helm application deployment and live Prometheus/Grafana on EKS are verified. Cloud Console, application and dashboard captures are included. **AWS teardown is complete** and an independent audit confirms no remaining project cluster, VPC, worker instances, database/root volumes, network interfaces or load balancers. The local demo has been stopped and temporary build files removed; restart it with `docker compose up --build`. See [validation results](docs/VALIDATION.md), [evidence](screenshots.md), [recorded EKS rollout](docs/recordings/orbit-eks-rollout.mp4) and [the submission checklist](SUBMISSION.md).

## Evidence and presentation

### Play the full capstone walkthrough

https://github.com/user-attachments/assets/7b1f9094-c3e5-47e2-8b87-f6ab246e94d6

**[Play the 2:29 video](https://yeashu.github.io/DevOps-Capstone/recordings/?v=silent149r2)** · **[Jump to AWS Console evidence at 01:09](https://yeashu.github.io/DevOps-Capstone/recordings/?v=silent149r2&t=69.133)**

[Download submission MP4](demo/orbit-capstone-video.mp4) · [Short subtitles](docs/recordings/orbit-capstone-walkthrough.vtt) · [Original 92-second live rollout](docs/recordings/orbit-eks-rollout.mp4) · [Presentation runbook](DEMO.md)

[PowerPoint slides](demo/orbit-capstone-slides.pptx) · [PDF slides](demo/orbit-capstone-slides.pdf) · [Timed voice-over script](demo/voiceover-script.md) · [Slide-by-slide speaking notes](demo/presentation-notes.md)

The **2-minute 29-second silent walkthrough covers all ten modules**, including Terraform plan/apply, the actual AWS VPC and subnets, active EKS cluster and Ready workers, Kubernetes, Prometheus, Grafana, and completed teardown. It uses brief evidence views, roughly 3–7 seconds each, plus clips from the original live demo. Short on-screen labels replace narration; the video has no audio track. AWS resources were destroyed after evidence collection.

If the inline attachment reports “Bad Gateway,” use the separate video player above or download the MP4. The player has clickable chapters and brief on-screen subtitles. For local playback, run `python3 -m http.server 8765 --bind 127.0.0.1` and open http://localhost:8765/docs/recordings/.

Each module below has a main image followed by links to its other images. All **75 evidence images** are included. Browser screenshots are actual captures; command-output images are labelled renders of actual logs. The cloud resources were destroyed after capture. Git metadata uses the owner's assigned timestamp; actual run and capture timestamps are retained.

### M1 · Scientific calculator

![M1 · Scientific calculator](docs/screenshots/01-application-desktop.png)

**More application images:** [Mobile calculator](docs/screenshots/02-application-mobile.png) · [Degree mode](docs/screenshots/03-degrees.png) · [Domain error](docs/screenshots/04-domain-error.png)

### M2 · Testing and code quality

![M2 · Testing and code quality](docs/screenshots/pytest-03.png)

**Other full-suite pages:** [pytest 01](docs/screenshots/pytest-01.png) · [pytest 02](docs/screenshots/pytest-02.png)

**Hosted PostgreSQL tests:** [hosted pytest 01](docs/screenshots/hosted-pytest-01.png) · [hosted pytest 02](docs/screenshots/hosted-pytest-02.png) · [hosted pytest 03](docs/screenshots/hosted-pytest-03.png)

**Calculator engine tests:** [calculator unit tests 01](docs/screenshots/calculator-unit-tests-01.png) · [calculator unit tests 02](docs/screenshots/calculator-unit-tests-02.png)

### M3 · Git and GitHub

![M3 · Git and GitHub](docs/screenshots/git-history.png)

**More commit history:** [github commit history](docs/screenshots/github-commit-history.png)

### M4 · Docker and Compose

![M4 · Docker and Compose](docs/screenshots/docker-compose-status.png)

**More container and build evidence:** [non root users](docs/screenshots/non-root-users.png) · [frontend build](docs/screenshots/frontend-build.png) · [hosted browser summary](docs/screenshots/hosted-browser-summary.png)

### M5 · CI/CD pipeline and GHCR

![M5 · CI/CD pipeline and GHCR](docs/screenshots/github-actions-success.png)

**Published images and configuration:** [Backend SHA tags](docs/screenshots/ghcr-backend.png) · [Frontend SHA tags](docs/screenshots/ghcr-frontend.png) · [hosted configuration](docs/screenshots/hosted-configuration.png)

### M6 · Trivy security scans

![M6 · Trivy security scans](docs/screenshots/trivy-backend-02.png)

**Other scan reports:** [trivy backend 01](docs/screenshots/trivy-backend-01.png) · [trivy frontend](docs/screenshots/trivy-frontend.png)

### M7 · AWS infrastructure with Terraform

![M7 · AWS infrastructure with Terraform](docs/screenshots/aws-eks-workers-console.png)

**Initialization and validation:** [terraform init](docs/screenshots/terraform-init.png) · [terraform validate](docs/screenshots/terraform-validate.png)

**All plan pages:** [Page 1](docs/screenshots/terraform-plan-01.png) · [Page 2](docs/screenshots/terraform-plan-02.png) · [Page 3](docs/screenshots/terraform-plan-03.png) · [Page 4](docs/screenshots/terraform-plan-04.png) · [Page 5](docs/screenshots/terraform-plan-05.png) · [Page 6](docs/screenshots/terraform-plan-06.png) · [Page 7](docs/screenshots/terraform-plan-07.png) · [Page 8](docs/screenshots/terraform-plan-08.png) · [Page 9](docs/screenshots/terraform-plan-09.png) · [Page 10](docs/screenshots/terraform-plan-10.png) · [Page 11](docs/screenshots/terraform-plan-11.png)

**Apply output:** [Page 1](docs/screenshots/terraform-apply-01.png) · [Page 2](docs/screenshots/terraform-apply-02.png) · [Page 3](docs/screenshots/terraform-apply-03.png)

**Other AWS Console views:** [VPC](docs/screenshots/aws-vpc-console.png) · [Two public subnets](docs/screenshots/aws-subnets-console.png) · [Active EKS](docs/screenshots/aws-eks-console.png)

### AWS teardown and credential cleanup

![AWS teardown and credential cleanup](docs/screenshots/terraform-destroy.png)

**Cleanup audits:** [Resource cleanup audit](docs/screenshots/aws-cleanup-audit.png) · [Credential cleanup audit](docs/screenshots/aws-bootstrap-cleanup.png)

### M8 · Kubernetes and Helm

![M8 · Kubernetes and Helm](docs/screenshots/eks-pods.png)

**More EKS cluster evidence:** [eks nodes](docs/screenshots/eks-nodes.png) · [eks services](docs/screenshots/eks-services.png) · [eks ingress](docs/screenshots/eks-ingress.png) · [eks helm list](docs/screenshots/eks-helm-list.png) · [eks pvc](docs/screenshots/eks-pvc.png)

**Application through Ingress:** [eks application desktop](docs/screenshots/eks-application-desktop.png) · [eks application mobile](docs/screenshots/eks-application-mobile.png)

**Separate Kind demonstration:** [kubernetes pods](docs/screenshots/kubernetes-pods.png) · [cluster running application pods](docs/screenshots/cluster-running-application-pods.png) · [kubernetes services](docs/screenshots/kubernetes-services.png) · [kubernetes ingress](docs/screenshots/kubernetes-ingress.png) · [helm list](docs/screenshots/helm-list.png) · [ingress application](docs/screenshots/ingress-application.png)

### M9 · Prometheus and Grafana

![M9 · Prometheus and Grafana](docs/screenshots/eks-grafana-dashboard.png)

**Local metrics output:** [metrics 01](docs/screenshots/metrics-01.png) · [metrics 02](docs/screenshots/metrics-02.png) · [metrics 03](docs/screenshots/metrics-03.png)

**EKS metrics output:** [eks metrics 01](docs/screenshots/eks-metrics-01.png) · [eks metrics 02](docs/screenshots/eks-metrics-02.png) · [eks metrics 03](docs/screenshots/eks-metrics-03.png)

**More EKS monitoring evidence:** [eks monitoring pods](docs/screenshots/eks-monitoring-pods.png) · [eks prometheus targets](docs/screenshots/eks-prometheus-targets.png)

**Separate Kind monitoring:** [15 prometheus targets](docs/screenshots/15-prometheus-targets.png) · [16 grafana dashboard](docs/screenshots/16-grafana-dashboard.png)

### M10 · Deployment demonstration

![M10 · Deployment demonstration](docs/screenshots/eks-after-rollout.png)

**More rollout evidence:** [Updated commit SHA](docs/screenshots/eks-updated-version.png)

### Reports, logs and submission documents

- [Completed rubric checklist](SUBMISSION.md)
- [Evidence provenance and submission index](screenshots.md)
- [Executed validation results](docs/VALIDATION.md)
- [Trivy findings and remediation explanation](security/README.md)
- [Troubleshooting exercises](docs/TROUBLESHOOTING.md)
- [Optional GitOps setup](gitops/README.md)
- [Verified green pipeline](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38959438459)
- [Recorded rollout's pipeline](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38947611595)

<details>
<summary>All original command logs and machine-readable evidence</summary>

These files include earlier failed or blocked attempts for provenance. Use the validation record and completed checklist above for the final results.

- [actions-run.json](docs/evidence/actions-run.json)
- [aws-bootstrap-cleanup.json](docs/evidence/aws-bootstrap-cleanup.json)
- [aws-cleanup-audit.json](docs/evidence/aws-cleanup-audit.json)
- [browser-local.txt](docs/evidence/browser-local.txt)
- [browser-smoke-eks.json](docs/evidence/browser-smoke-eks.json)
- [browser-smoke-first-hosted.json](docs/evidence/browser-smoke-first-hosted.json)
- [browser-smoke-kind.json](docs/evidence/browser-smoke-kind.json)
- [browser-smoke.json](docs/evidence/browser-smoke.json)
- [calculator-unit-tests.txt](docs/evidence/calculator-unit-tests.txt)
- [cluster-helm-releases.txt](docs/evidence/cluster-helm-releases.txt)
- [cluster-running-application-pods.txt](docs/evidence/cluster-running-application-pods.txt)
- [cluster-traffic.txt](docs/evidence/cluster-traffic.txt)
- [dependency-install.txt](docs/evidence/dependency-install.txt)
- [docker-compose-status.txt](docs/evidence/docker-compose-status.txt)
- [docker-compose.txt](docs/evidence/docker-compose.txt)
- [eks-helm-list.txt](docs/evidence/eks-helm-list.txt)
- [eks-ingress.txt](docs/evidence/eks-ingress.txt)
- [eks-metrics.txt](docs/evidence/eks-metrics.txt)
- [eks-monitoring-pods.txt](docs/evidence/eks-monitoring-pods.txt)
- [eks-nodes.txt](docs/evidence/eks-nodes.txt)
- [eks-pods.txt](docs/evidence/eks-pods.txt)
- [eks-prometheus-targets.json](docs/evidence/eks-prometheus-targets.json)
- [eks-pvc.txt](docs/evidence/eks-pvc.txt)
- [eks-rollout.txt](docs/evidence/eks-rollout.txt)
- [Final workspace cleanup](docs/evidence/final-workspace-cleanup.json)
- [eks-services.txt](docs/evidence/eks-services.txt)
- [frontend-build.txt](docs/evidence/frontend-build.txt)
- [git-history-secret-check.json](docs/evidence/git-history-secret-check.json)
- [git-history.txt](docs/evidence/git-history.txt)
- [helm-list.txt](docs/evidence/helm-list.txt)
- [hosted-browser-summary.txt](docs/evidence/hosted-browser-summary.txt)
- [hosted-configuration.txt](docs/evidence/hosted-configuration.txt)
- [hosted-pytest.txt](docs/evidence/hosted-pytest.txt)
- [hosted-trivy-backend-before.txt](docs/evidence/hosted-trivy-backend-before.txt)
- [hosted-trivy-frontend.txt](docs/evidence/hosted-trivy-frontend.txt)
- [kubernetes-ingress.txt](docs/evidence/kubernetes-ingress.txt)
- [kubernetes-pods.txt](docs/evidence/kubernetes-pods.txt)
- [kubernetes-services.txt](docs/evidence/kubernetes-services.txt)
- [metrics.txt](docs/evidence/metrics.txt)
- [non-root-users.txt](docs/evidence/non-root-users.txt)
- [prometheus-targets.json](docs/evidence/prometheus-targets.json)
- [pytest.txt](docs/evidence/pytest.txt)
- [rollout-demo.json](docs/evidence/rollout-demo.json)
- [static-validation.txt](docs/evidence/static-validation.txt)
- [terraform-apply.txt](docs/evidence/terraform-apply.txt)
- [terraform-destroy-first-attempt.txt](docs/evidence/terraform-destroy-first-attempt.txt)
- [terraform-destroy-summary.txt](docs/evidence/terraform-destroy-summary.txt)
- [terraform-destroy.txt](docs/evidence/terraform-destroy.txt)
- [terraform-init.txt](docs/evidence/terraform-init.txt)
- [terraform-plan.txt](docs/evidence/terraform-plan.txt)
- [terraform-validate-live.txt](docs/evidence/terraform-validate-live.txt)
- [terraform-validate.txt](docs/evidence/terraform-validate.txt)
- [test-collection.txt](docs/evidence/test-collection.txt)
- [trivy-backend.txt](docs/evidence/trivy-backend.txt)
- [trivy-frontend.txt](docs/evidence/trivy-frontend.txt)

</details>

To reproduce the evidence, run `./scripts/capture-evidence.sh` for Compose and `./scripts/capture-cluster.sh` for your selected live cluster. The browser capture checks actual API responses, both Prometheus targets and positive Grafana query results before saving its images.


## Run the application

With Docker running, from this directory:

```bash
docker compose up --build
```

Open **http://localhost:3000**. API documentation: http://localhost:8000/docs. Compose includes a classroom-only password; copy `.env.example` to `.env` to replace it. Use URL-safe letters, digits, hyphens and underscores in the Compose password because it is interpolated into a URL. The Kubernetes secret helper correctly encodes arbitrary passwords.

```text
sqrt(144) + 2^3   → 20
sin(pi / 2)      → 1       RAD
sin(30)          → 0.5     DEG
log(1000)        → 3       base 10
ln(e)            → 1
factorial(5)     → 120
```

Use explicit multiplication (`2*pi`) and parentheses. Press Enter or Calculate to evaluate and save. The classroom notebook is shared; there are no user accounts. Calculations use floating-point arithmetic; the UI displays 12 significant digits while the API retains the full floating-point result.

## Architecture and files

```mermaid
flowchart LR
    U[Browser] --> I[Ingress / Nginx]
    I -->|/| F[HTML and JavaScript UI · 2 replicas]
    I -->|/api| B[FastAPI · 2 replicas]
    B --> P[(PostgreSQL notebook)]
    J[Alembic migration Job] --> P
    B -->|/metrics| M[Prometheus]
    M --> G[Grafana]
    C[Commit] --> T[Tests · quality · source security]
    T --> E[Compose and browser test]
    E --> S[Both image builds and Trivy gates]
    S --> R[GHCR · commit SHA]
    R --> D[Optional Helm delivery through OIDC]
    D --> I
    TF[Terraform] --> AWS[VPC · two subnets · EKS workers · EBS CSI]
```

| Area | Files |
| --- | --- |
| Python API and restricted expression parser | `backend/app/` |
| Alembic migration | `backend/alembic/versions/0001_calculations.py` |
| Engine and API tests | `backend/tests/`, `backend/pytest.ini` |
| Responsive frontend and Node build | `frontend/` |
| Non-root Dockerfiles and three-service stack | `backend/Dockerfile`, `frontend/Dockerfile`, `docker-compose.yml` |
| GitHub Actions | `.github/workflows/ci.yml` |
| AWS infrastructure | `terraform/` |
| Kubernetes and Helm | `k8s/`, `helm/orbit/` |
| Prometheus and Grafana | `monitoring/` |
| Optional Argo CD workflow | `gitops/` |
| Live screenshot capture | `scripts/`, `screenshots.md` |

## Development and testing

Containers and CI use Python 3.13 and Node 24. Plain HTML/JavaScript satisfies the rubric's HTML frontend option. Its Node production build validates JavaScript and produces Nginx assets without a browser framework.

```bash
python3.13 -m venv .venv
.venv/bin/pip install -r backend/requirements-dev.txt pillow
cd backend
../.venv/bin/alembic upgrade head
../.venv/bin/uvicorn app.main:app --reload --port 8000
```

Host development defaults to a local SQLite file. **Compose and Helm use PostgreSQL.** Alembic owns the schema in both modes; application startup does not call `create_all`. For the full UI with same-origin API routing, use Compose.

Run checks from the repository root:

```bash
cd backend
../.venv/bin/pytest -v
../.venv/bin/ruff check app tests alembic
cd ../frontend
npm ci --ignore-scripts
npm test
npm run build
```

API tests apply migrations to isolated temporary SQLite databases by default. CI sets `TEST_DATABASE_URL` to a disposable PostgreSQL database named `orbit_test`, exercising the same API tests against PostgreSQL. The test fixture never chooses its database using production `DATABASE_URL`, refuses external database names without `_test`, and clears that dedicated test table between tests. Do not point it at shared data.

Engine-only tests need just pytest: `cd backend && ../.venv/bin/pytest -v tests/test_calculator.py`.

## API and database

| Method | Endpoint | Behavior |
| --- | --- | --- |
| GET | `/health`, `/api/health` | Process health and image version |
| GET | `/ready` | Database/schema readiness; 503 when unavailable |
| GET | `/metrics` | Prometheus request counters and latency histogram |
| POST | `/api/evaluate` | Evaluate without saving |
| POST | `/api/calculations` | Evaluate and persist; 201 |
| GET | `/api/calculations?limit=50&offset=0` | Newest-first notebook |
| GET | `/api/calculations/{id}` | Read a calculation |
| PUT | `/api/calculations/{id}` | Change its label |
| DELETE | `/api/calculations/{id}` | Delete; 204 |

```bash
curl -X POST http://localhost:8000/api/calculations \
  -H 'Content-Type: application/json' \
  -d '{"expression":"sin(30)","angle_mode":"deg","label":"Trig example"}'
```

The `calculations` table stores `id`, `expression`, `result`, `angle_mode`, `label`, and `created_at`. Invalid math returns 422 without saving; unknown IDs return 404. A bounded AST interpreter accepts only arithmetic, known constants and approved one-argument functions. There is no `eval`, import, attribute access or arbitrary Python execution.

## Docker

The backend uses a Python build stage and runtime UID 10001. The frontend uses a **Node build stage followed by unprivileged Nginx**, UID 101, internally listening on 8080. Compose publishes only localhost:3000 and localhost:8000. PostgreSQL health gates API startup; the API applies migrations before serving.

```bash
docker compose up --build -d --wait
docker compose ps
docker compose exec -T backend id
docker compose exec -T frontend id
docker compose down
```

`down` preserves notebook data. Add `-v` only to erase the local demo database.

## CI/CD and security

Every push to `main`, pull request to `main`, and manual dispatch runs:

1. PostgreSQL-backed pytest and Ruff; frontend tests/build; Bandit SAST, pip-audit SCA and Trivy secret detection; Terraform/Helm checks.
2. The complete Compose stack and Playwright browser checks with desktop/mobile screenshot artifacts.
3. Both image builds and Trivy vulnerability scans. **Any HIGH or CRITICAL finding blocks the run, including unfixed CVEs.**
4. Publication of the exact scanned images only after **both** scans succeed. Pull requests do not publish.
5. Optional EKS delivery using the same full commit SHA.

Image names are `ghcr.io/yeashu/devops-capstone/backend:<full-sha>` and `ghcr.io/yeashu/devops-capstone/frontend:<full-sha>`. No deployment uses `latest`. GitHub's scoped automatic token publishes; AWS OIDC handles cloud access. Reports and browser evidence are retained as Actions artifacts. See [security notes](security/README.md).

Delivery is disabled until bootstrap is complete. Configure a GitHub Environment named `capstone`, an AWS OIDC role restricted to `repo:Yeashu/DevOps-Capstone:environment:capstone`, and a Linux self-hosted runner labelled `capstone` with AWS CLI, kubectl and access to EKS. Helm is installed by its setup action. An in-VPC runner reaches the private endpoint; an external runner needs a fixed egress `/32` in `admin_cidrs`. Grant the role `eks:DescribeCluster` on this cluster and pass its ARN as Terraform's `deploy_principal_arn` for namespace access.

Set variables `DEPLOY_TO_EKS=true`, `AWS_ROLE_ARN`, `AWS_REGION`, `EKS_CLUSTER`, `INGRESS_HOST`, and optionally `INGRESS_CLASS` (delivery defaults to `traefik`). An administrator must first create the namespace, database Secret, storage class and Ingress controller. Make GHCR packages public, or set chart `imagePullSecrets`. Keep direct delivery disabled when using the optional Argo CD workflow, so both systems do not manage the same release.

## Kubernetes and Helm

With a running Minikube profile, Docker and Helm:

```bash
./scripts/deploy-local.sh
kubectl get pods -n orbit
kubectl get svc -n orbit
helm list -n orbit
kubectl port-forward -n ingress-nginx svc/ingress-nginx-controller 8080:80
```

Open **http://orbit.localhost:8080** through the actual Ingress. If your browser does not resolve `.localhost`, add a local DNS/hosts entry. CLI check: `curl -H 'Host: orbit.localhost' http://127.0.0.1:8080/api/health`.

The helper uses an explicit Minikube context. Manual installation to your chosen cluster is:

```bash
kubectl apply -f k8s/namespace.yaml
python3 scripts/create-db-secret.py
helm upgrade --install orbit ./helm/orbit -n orbit --wait --wait-for-jobs --timeout 10m
```

Load local images first or set both component repositories and tags to published GHCR images. The chart provides two replicas each, ClusterIP Services, Ingress, ConfigMap, PVC and a single migration Job per release revision. Backend init containers wait for the schema instead of competing to run migrations. Completed migration pods are expected; application pods must be Running/Ready. New migrations require updating the expected revision in the readiness init script.

For EKS, apply `k8s/storageclass-eks.yaml` and set `database.persistence.storageClass=gp3`. Terraform installs EBS CSI with Pod Identity permissions. The optional HPA needs metrics-server and retains a minimum of two backend replicas. PostgreSQL PVCs intentionally survive Helm uninstall; remove them deliberately during final cleanup.

## Terraform and AWS

The code defines a VPC, two public subnets in different AZs, internet gateway, EKS, managed worker group, EBS CSI/Pod Identity and optional scoped CI access. Public-subnet workers avoid a NAT Gateway in this temporary classroom setup. The public API is CIDR restricted and a private endpoint is enabled. No SSH ingress is created.

```bash
aws sso login --profile YOUR_PROFILE
export AWS_PROFILE=YOUR_PROFILE
cd terraform
cp terraform.tfvars.example terraform.tfvars
# Edit your public IPv4 /32, region and desired cluster version.
terraform init
terraform fmt -check
terraform validate
terraform plan -out=orbit.tfplan
terraform apply orbit.tfplan
terraform output kubeconfig_command
```

Verify the default Kubernetes 1.36 is available in your region with `aws eks describe-cluster-versions`; see the [AWS EKS lifecycle](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html). Credentials use the AWS chain, never committed files. Plans, state and real `.tfvars` are gitignored. The first hosted configuration job installed the locked AWS provider with HashiCorp signature verification and successfully ran Terraform validation and Helm lint. The original offline initialization record is retained separately.

After updating kubeconfig, return to the repository root, set `ORBIT_EKS_CONTEXT` to the EKS context name, and run `./scripts/bootstrap-eks.sh`. It creates the namespace, storage class, Secret and a Traefik Ingress controller with a ClusterIP Service. Install Orbit using published repositories/SHA tags, `--set database.persistence.storageClass=gp3 --set ingress.className=traefik`. Forward `svc/traefik` in `ingress-system` to port 8080 and open your configured Ingress hostname at that port. This demonstrates real Ingress routing without an additional public AWS load balancer. The [official Traefik chart](https://github.com/traefik/traefik-helm-chart) supports the OCI installation used by the helper.

After evaluation, uninstall application, monitoring and Ingress releases, delete application PVCs, and verify load balancers/volumes are removed while the cluster still exists. Then run `terraform destroy`, capture its real completion output, and check `terraform state list` and the AWS Console. Do not destroy another coursework stack. The recorded lifecycle applied this configuration and subsequently destroyed its resources; see the cleanup evidence below.

## Prometheus and Grafana

```bash
./scripts/install-monitoring.sh
kubectl port-forward -n monitoring svc/prometheus-server 9090:80
# Separate terminal:
kubectl port-forward -n monitoring svc/grafana 3001:80
# Separate terminal; generate real metrics without filling the notebook:
python3 scripts/generate-traffic.py --url http://orbit.localhost:8080 --seconds 180
```

Check both `orbit-api` targets are UP at http://localhost:9090/targets. Grafana at http://localhost:3001 uses `admin` and the password chosen during installation. **Orbit · Application Metrics** includes request rate, p95 latency, per-route requests, error ratio, replica health and total requests. Allow at least two scrapes and one minute of traffic for rate panels. Monitoring storage is ephemeral for this demo.

## Reference and lessons

The [ClinicDesk reference](https://github.com/Datman701/devops_capstone) was reviewed as a structural benchmark. Orbit's calculator domain, interpreter, notebook schema, tests, UI and deployment files were authored for this project. The reference application and its screenshots were not copied.

Discuss test database isolation, readiness versus liveness, a single migration owner, scans before publishing, and why configuration files alone do not prove a deployment. Add your own observations after completing the live demonstration.
