# Validation record — 16 October 2026

This record distinguishes executed checks from authored configuration. No evidence from a different project is used.

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
