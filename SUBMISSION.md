# Final submission checklist

Repository URL: https://github.com/Yeashu/DevOps-Capstone

The repository is public and the initial implementation commits are pushed. [The first hosted run](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38943294699) passed application/tests/browser/configuration checks and failed at the backend image's security gate. A Dockerfile fix is prepared locally; a new successful scan is still required. A code file alone does not establish full module credit.

| Module | Present implementation / local checks | Still required for final submission |
| --- | --- | --- |
| M1 · 10 | PostgreSQL Compose stack and real browser smoke test passed | Download the existing desktop/mobile screenshots into the submission |
| M2 · 10 | **All 69 tests passed on hosted PostgreSQL**, including all 17 API cases; Ruff passed | Submit hosted pytest output/terminal image and XML artifact |
| M3 · 5 | Public GitHub repository; ≥10 meaningful commits; exclusions present | Attach the repository URL and existing commit-history image |
| M4 · 10 | Both images built; all three Compose services healthy; real browser demo passed | Verify revised backend build; submit Compose/UI/non-root evidence |
| M5 · 15 | Main-triggered test/build/scan/publish workflow; full SHA tags; optional delivery | Successful Actions URL and actual GHCR package screenshots |
| M6 · 5 | Both scans ran; frontend clean; backend findings documented; explanation completed | Verify the remediated backend scan and capture both actual scan steps |
| M7 · 15 | VPC/EKS/node-group/EBS code; hosted init and validate passed | Real non-empty AWS plan/apply, Console VPC/EKS/worker evidence and destroy |
| M8 · 15 | Namespace, complete chart, two API/UI replicas, Services, Ingress, PVC/probes | Successful install; pods, Services, Helm list, Ingress browser evidence |
| M9 · 10 | Metrics route, endpoint discovery, Grafana values and six panels | Real metrics, both Prometheus targets UP, populated Grafana panel |
| M10 · 5 | README, architecture and presentation runbook | Live/recorded commit → pipeline → deployment demonstration |

- [x] GitHub repository public or instructor access confirmed
- [x] All 69 backend tests pass against the chosen test database
- [x] Frontend tests/build pass
- [x] Initial Compose stack and browser verified
- [ ] Green Actions run URL: **pending**
- [ ] GHCR backend and frontend SHA tags visible
- [x] Both initial Trivy reports inspected; `security/README.md` explanation updated
- [ ] Remediated backend image passes the unchanged security gate
- [ ] Terraform validate and non-empty plan captured
- [ ] Real AWS VPC, two subnets, EKS and worker group shown
- [ ] Helm install, two replicas per tier, Services and Ingress verified
- [ ] Metrics output, Prometheus targets and Grafana panels captured
- [ ] Presentation completed or recording link: **pending**
- [ ] Cloud load balancers, PVC/EBS volumes and Terraform resources cleaned up
- [ ] Actual `terraform destroy` completion captured
- [ ] No credentials or sensitive state/logs included in Git history

Capture instructions and artifact names are indexed in [screenshots.md](screenshots.md). There is no claimed grade until these runtime items are evaluated.
