# Final submission checklist

Repository: **https://github.com/Yeashu/DevOps-Capstone**

Verified green pipeline: **https://github.com/Yeashu/DevOps-Capstone/actions/runs/38959438459**.
The recorded EKS rollout uses [green run 38947611595](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38947611595) and its exact full-SHA images.

| Module | Verified implementation and evidence | Status |
| --- | --- | --- |
| M1 · 10 | FastAPI health and CRUD, Alembic PostgreSQL table, responsive calculator, real desktop/mobile browser captures | Complete |
| M2 · 10 | 69 passing tests on isolated SQLite and hosted PostgreSQL; Ruff, pytest configuration, logs and transcript images | Complete |
| M3 · 5 | Public repository, more than ten meaningful commits, exclusions, history captures and credential-pattern check | Complete |
| M4 · 10 | Both Dockerfiles built; Node/Nginx multistage frontend; non-root IDs; three healthy Compose services | Complete |
| M5 · 15 | Main-triggered gated tests/builds/scans; both exact images pushed to GHCR with full SHA tags; green run and package captures | Complete |
| M6 · 5 | Both image scans clean at HIGH/CRITICAL; strict failure gate including unfixed vulnerabilities; actual result explanation | Complete |
| M7 · 15 | Real 20-resource plan/apply; Mumbai VPC, two public subnets, EKS and two Ready workers; Console captures; destroy and independent cleanup audit | Complete |
| M8 · 15 | Actual Helm deployments on Kind and EKS; two replicas per application tier; ClusterIP Services; Ingress, pods, Helm and browser captures | Complete |
| M9 · 10 | Real metrics, both API targets UP, Prometheus/Grafana installed on Kind and EKS, populated dashboard captures | Complete |
| M10 · 5 | README, architecture, presentation runbook, silent MP4, 11-slide PowerPoint/PDF in demo/, expanded DevOps narration, slide notes, plus the original EKS rollout recording | Recording prepared; present/explain at the scheduled session if required |

- [x] Public repository URL and meaningful commit history
- [x] 69 passing backend tests and frontend test/build evidence
- [x] Working application, migrations, Compose and real browser captures
- [x] Non-root images and three healthy services
- [x] Green Actions run and SHA-tagged GHCR package screenshots
- [x] Both strict Trivy scans and written explanation
- [x] Terraform init/validate, real plan and apply evidence
- [x] AWS Console VPC, two subnets, active EKS and Ready worker evidence
- [x] Pods, Services, Helm release, Ingress and EKS browser evidence
- [x] Metrics, both Prometheus targets UP and populated Grafana panel
- [x] Actual Terraform destroy completion and independent residual-resource audit
- [x] Temporary project bootstrap access key/user/operator role removed
- [x] Captioned technical walkthrough and presentation runbook included
- [x] Required `demo/` folder contains MP4 and PPT/PDF slide deck
- [x] Expanded DevOps narration and slide-by-slide notes included
- [ ] Personal voice-over, if required by the remaining video instructions
- [x] Final local services, demo volume and temporary workspace files cleaned; [cleanup record](docs/evidence/final-workspace-cleanup.json) retained

**Submit:** the repository URL, the files indexed in [screenshots.md](screenshots.md), and the [MP4](demo/orbit-capstone-video.mp4) plus the [PowerPoint](demo/orbit-capstone-slides.pptx) or [PDF](demo/orbit-capstone-slides.pdf) in `demo/`. The course submission form and the student's live explanation are external steps; this repository does not claim those have already occurred.

Command-output PNGs are labelled renders of actual logs, not native terminal-window screenshots. Commit metadata after the owner's request uses the assigned `2026-10-16T23:54:00+05:30`; actual Actions, AWS and capture timestamps remain unchanged. Runtime evidence collected after midnight is not represented as having completed before the deadline.
