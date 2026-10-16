# Final submission checklist

Repository: https://github.com/Yeashu/DevOps-Capstone

Latest evidence run: https://github.com/Yeashu/DevOps-Capstone/actions/runs/38946260879 (in progress).
Previous run verified both clean images and GHCR publication; its final Grafana browser selector failed: https://github.com/Yeashu/DevOps-Capstone/actions/runs/38944998841.

| Module | Verified evidence | Remaining |
| --- | --- | --- |
| M1 | Working API CRUD, migrated PostgreSQL, real desktop/mobile screenshots | Complete |
| M2 | All 69 tests passed locally and on hosted PostgreSQL; pytest source logs and PNGs | Complete |
| M3 | Public repository, more than ten meaningful commits, exclusions and history image | Complete |
| M4 | Both images built; three services healthy; non-root IDs; browser captures | Complete |
| M5 | Tests/build/scans and both SHA-tagged GHCR pushes passed | Fully green run; both package screenshots captured |
| M6 | Both images scanned clean; strict HIGH/CRITICAL failure gate; explanation and scan PNGs | Complete |
| M7 | Validated IaC and real 20-resource plan; AWS apply underway | Active VPC/EKS/workers, Console captures, destroy and completion capture |
| M8 | Kind Helm deployment, two replicas per tier, pods/Services/Helm/Ingress outputs | Include final Ingress browser capture |
| M9 | Metrics output and PNGs; two Prometheus targets UP; Grafana datasource verified | Final populated Grafana screenshot |
| M10 | README, architecture, demo runbook | Live/recorded commit → pipeline → deployment walkthrough |

- [x] Public GitHub URL and meaningful commit history
- [x] All 69 backend tests pass
- [x] Frontend tests and production build pass
- [x] Compose starts all three healthy services
- [x] Real browser and non-root evidence
- [x] Both Trivy image scans pass unchanged severity gates
- [x] Both images published using full commit SHA tags
- [x] Terraform init, validate and non-empty AWS plan
- [x] Helm deployment, replicas, Services and Ingress on Kind
- [x] Metrics output and both Prometheus targets UP
- [ ] Final Grafana screenshot and green evidence run
- [x] GHCR package page screenshots
- [ ] AWS Console VPC/EKS/worker evidence
- [ ] Terraform destroy completion and residual-resource audit
- [ ] Presentation completed or recording linked

See [evidence index](screenshots.md) for files and provenance. Authored configuration alone does not establish runtime completion.
