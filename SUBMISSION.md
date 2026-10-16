# Final submission checklist

Repository URL: https://github.com/Yeashu/DevOps-Capstone

The code is prepared locally. Confirm remote visibility and push the commits before submitting the URL. Items remain unchecked until supported by this project's actual runtime evidence. A code file alone does not establish full module credit.

| Module | Present implementation / local checks | Still required for final submission |
| --- | --- | --- |
| M1 · 10 | FastAPI CRUD, scientific evaluator, Alembic schema, responsive HTML UI | Run PostgreSQL stack; capture browser and health |
| M2 · 10 | 69 collected tests; **52 engine tests passed**; isolated migrated test DB fixture | Install dependencies; pass all 17 API cases; capture full `pytest -v` |
| M3 · 5 | Meaningful local commits; secret/build exclusions | Push; verify public/instructor access; capture ≥10 commits |
| M4 · 10 | Backend Dockerfile, Node → unprivileged Nginx Dockerfile, Compose | Build/run; capture three healthy services, non-root IDs, localhost:3000 |
| M5 · 15 | Main-triggered test/build/scan/publish workflow; full SHA tags; optional delivery | Successful Actions URL and actual GHCR package screenshots |
| M6 · 5 | Both image scans block HIGH/CRITICAL; reports retained | Actual Trivy output and completed 2–3 sentence explanation |
| M7 · 15 | VPC/EKS/node-group/EBS code; fmt passed; offline init completed | Full validate/plan, real apply, AWS Console VPC/EKS, real destroy |
| M8 · 15 | Namespace, complete chart, two API/UI replicas, Services, Ingress, PVC/probes | Successful install; pods, Services, Helm list, Ingress browser evidence |
| M9 · 10 | Metrics route, endpoint discovery, Grafana values and six panels | Real metrics, both Prometheus targets UP, populated Grafana panel |
| M10 · 5 | README, architecture and presentation runbook | Live/recorded commit → pipeline → deployment demonstration |

- [ ] GitHub repository public or instructor access confirmed
- [ ] All 69 backend tests pass against the chosen test database
- [ ] Frontend tests/build pass
- [ ] Compose stack and browser verified
- [ ] Green Actions run URL: **pending**
- [ ] GHCR backend and frontend SHA tags visible
- [ ] Both Trivy reports inspected; `security/README.md` explanation updated
- [ ] Terraform validate and non-empty plan captured
- [ ] Real AWS VPC, two subnets, EKS and worker group shown
- [ ] Helm install, two replicas per tier, Services and Ingress verified
- [ ] Metrics output, Prometheus targets and Grafana panels captured
- [ ] Presentation completed or recording link: **pending**
- [ ] Cloud load balancers, PVC/EBS volumes and Terraform resources cleaned up
- [ ] Actual `terraform destroy` completion captured
- [ ] No credentials or sensitive state/logs included in Git history

Capture instructions and artifact names are indexed in [screenshots.md](screenshots.md). There is no claimed grade until these runtime items are evaluated.
