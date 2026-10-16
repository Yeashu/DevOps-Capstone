# Final submission checklist

Repository: https://github.com/Yeashu/DevOps-Capstone

Latest evidence run: https://github.com/Yeashu/DevOps-Capstone/actions/runs/38946260879 (**success**).
Previous run verified both clean images and GHCR publication; its final Grafana browser selector failed: https://github.com/Yeashu/DevOps-Capstone/actions/runs/38944998841.

| Module | Verified evidence | Remaining |
| --- | --- | --- |
| M1 | Working API CRUD, migrated PostgreSQL, real desktop/mobile screenshots | Complete |
| M2 | All 69 tests passed locally and on hosted PostgreSQL; pytest source logs and PNGs | Complete |
| M3 | Public repository, more than ten meaningful commits, exclusions and history image | Complete |
| M4 | Both images built; three services healthy; non-root IDs; browser captures | Complete |
| M5 | Tests/build/scans and both SHA-tagged GHCR pushes passed | Complete: green run and both package screenshots captured |
| M6 | Both images scanned clean; strict HIGH/CRITICAL failure gate; explanation and scan PNGs | Complete |
| M7 | Real plan/apply succeeded; active VPC, two subnets, EKS and two Ready workers; Console captures included | Destroy and completion capture |
| M8 | Kind and EKS Helm deployments, two replicas per tier, pods/Services/Helm/Ingress outputs | Complete: actual Ingress browser capture included |
| M9 | Kind and EKS metrics, both targets UP, live Grafana panels and screenshots verified | Complete: populated Grafana screenshot included |
| M10 | README, architecture, runbook and captioned actual EKS rollout recording | Submit the recording; explain the project at the scheduled presentation |

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
- [x] Final Grafana screenshot and green evidence run
- [x] GHCR package page screenshots
- [x] AWS Console VPC/EKS/worker evidence
- [ ] Terraform destroy completion and residual-resource audit
- [x] Recorded technical walkthrough linked in DEMO.md (live presentation, if required by the instructor, remains the student’s session)

See [evidence index](screenshots.md) for files and provenance. Authored configuration alone does not establish runtime completion.
