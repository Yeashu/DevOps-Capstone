# Validation record — 16 October 2026

This record distinguishes executed checks from authored configuration. No evidence from a different project is used.

## Hosted validation after the first push

[Run 38943294699](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38943294699) tested commit `2719d20fcd29336c4413f35a75a70cc77f2e9c62` on 16 October 2026. These runtime results supersede the earlier local limitations below:

| Hosted check | Actual result |
| --- | --- |
| Backend tests and lint | **69 tests passed** against migrated disposable PostgreSQL; Ruff passed |
| Frontend tests/build | Passed |
| Source security | Bandit, pip-audit and Trivy secret detection passed |
| Infrastructure configuration | Terraform init with signed provider and validate passed; Helm lint/template and Compose config passed |
| Compose runtime | All three services became healthy |
| Live browser demo | Scientific calculation, degree mode, domain error, responsive layout and label update passed; screenshots uploaded |
| Frontend image | Build and HIGH/CRITICAL scan passed; zero findings at that severity |
| Backend image | Build passed; scan failed with 63 OS findings plus four Python findings |
| GHCR publication | Skipped because both image scans must pass |
| Deployment | Skipped; AWS/bootstrap/runner configuration is also still required |

Source logs are saved as `docs/evidence/hosted-*.txt`. Real UI captures are available in the [browser-and-compose-evidence artifact](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38943294699/artifacts/12064316433). They have not been downloaded to this workspace because local CLI network access is still restricted. The next browser job also captures actual non-root IDs and metrics output.

The backend Dockerfile remediation replaces the Bookworm runtime with Python on Alpine 3.24 and physically removes pip/ensurepip and their vendored libraries after dependency installation. It has been reviewed and its Compose configuration checked locally; **the replacement image has not been built or rescanned here**. No security threshold was relaxed.

## Original local-only checks

| Check | Actual result |
| --- | --- |
| Calculator engine `pytest -v tests/test_calculator.py` | **52 passed**, Python 3.14.7 / pytest 9.1.1 |
| Full suite collection | **69 tests collected**; 17 API/integration cases need backend dependencies |
| Frontend `npm test` | **4 passed** |
| Frontend `npm ci` and `npm run build` | Passed; production assets generated |
| Python compile check | Passed for app, migration, tests and scripts |
| JavaScript and Bash syntax | Passed |
| Compose configuration | `docker compose config --quiet` passed |
| YAML and dashboard JSON parsing | Passed for non-templated configuration |
| Terraform formatting | `terraform fmt -check` passed |
| Terraform initialization | Completed using the matching locally cached AWS provider 6.66.0; offline installation reported unauthenticated |
| Terraform validation | **Blocked**: provider subprocess could not complete its plugin handshake in this session |
| API tests, migrations against a running database | **Not executed**: FastAPI/SQLAlchemy/Alembic are not installed; package retrieval unavailable |
| Docker build and Compose runtime | **Blocked**: session denied access to the Colima Docker socket |
| Browser screenshots | **Blocked**: headless Chrome exited 134 in this restricted session |
| Kubernetes runtime | **Blocked**: session denied connecting to the local Kubernetes API |
| Helm lint/render | **Not executed**: Helm is not installed in the host environment |
| GitHub Actions, GHCR and Trivy | **Not executed** for Orbit; shell network/auth unavailable |
| AWS plan/apply/destroy, console evidence | **Not executed**; no resources provisioned |
| Prometheus/Grafana live evidence | **Not executed**; requires the running cluster |

The 52 passing engine tests cover arithmetic precedence, scientific functions, angle modes, numerical domains, unsafe AST nodes and expression bounds. They do **not** substitute for the 17 API cases. The full suite is collected without importing missing web/database dependencies because those imports happen inside the API fixture; no integration tests were silently skipped or reported as passing.

Raw output is retained under `docs/evidence/`. PNGs generated from terminal output are labelled rendered transcripts, not original terminal screenshots. The successful Terraform initialization used a cached provider directory; a normal network-enabled initialization must verify upstream provider checksums before final submission.

Next verification sequence: install `backend/requirements-dev.txt`, run all 69 pytest cases, run the three-service Compose stack, capture the real UI, push the commits and obtain a green pipeline with real image scans, then perform the AWS/Helm/monitoring deployment and teardown. The configured workflow also runs the missing integration, container and browser checks on a network-enabled runner.
