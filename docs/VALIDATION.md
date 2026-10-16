# Validation record — 16 October 2026

This record contains executed results for Orbit. Earlier network and Docker restrictions were removed; the following checks supersede the initial blocked attempts.

| Check | Actual result |
| --- | --- |
| Backend tests | **69 passed** locally on isolated SQLite and in Actions on migrated disposable PostgreSQL |
| Ruff | Passed locally and in Actions |
| Frontend | Four tests and production build passed |
| Source security | Bandit, pip-audit and Trivy secret scan passed |
| Terraform | Network-enabled init and validate passed; real AWS plan: **20 to add, 0 to change, 0 to destroy** |
| Docker | Both images built; three Compose services healthy; backend UID 10001, frontend UID 101 |
| Browser | Real API-backed desktop/mobile, scientific calculation, degrees, error state and label update passed |
| Image security | Both remediated images: **zero HIGH/CRITICAL findings**; unfixed findings are included in the gate |
| Registry | Both exact scanned images published to GHCR with full commit SHA tags |
| Kubernetes | Helm release deployed on both Kind and **real EKS**; two backend + two frontend replicas and PostgreSQL Running; Services and Ingress verified |
| Observability | On Kind and EKS: both application targets UP, Grafana datasource returned positive real values, populated dashboard captured |
| AWS | **Apply complete: 20 added, 0 changed, 0 destroyed**; EKS Active, two Ready workers, VPC/two subnets verified; destroy pending |
| Presentation | Captioned **92-second actual technical walkthrough** recorded; live student explanation remains a presentation-session activity |

[Run 38944998841](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38944998841) verified all the results above except AWS. Its final screenshot failed because the Grafana panel title and legend matched the same text selector. The actual datasource query had already passed. [Run 38946260879](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38946260879) contains the corrected heading selector and is in progress.

The original backend security gate correctly blocked publication in [run 38943294699](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38943294699). The Alpine runtime update and removal of unused pip/ensurepip vendored libraries resolved its findings without weakening the policy. See [the security explanation](../security/README.md).

Actual browser captures and source logs are in `docs/screenshots/` and `docs/evidence/`. Command-output PNGs are explicitly labelled rendered transcripts; they are not OS terminal screenshots. Kind evidence demonstrates Kubernetes/Helm/monitoring and is not represented as EKS evidence. Terraform account IDs and administrator CIDRs are explicitly redacted in the committed plan; state, credentials, real tfvars and binary plans are excluded from Git.

Git metadata note: at the owner’s request, subsequent commits use the assigned author/committer timestamp `2026-10-16T23:54:00+05:30`. This is metadata, not the time the later AWS operations or captures completed. Actions run timestamps and captured-at evidence remain their actual times.

Final hosted result: [run 38946260879](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38946260879) completed successfully. The Ingress browser and populated Grafana captures are now committed; optional persistent EKS delivery was skipped because its runner/OIDC bootstrap is not configured. The Kind deployment job did run and passed.

## Actual AWS deployment

Terraform applied successfully in `ap-south-1` using Kubernetes 1.37 and two t3.medium workers. Both nodes are Ready; EBS CSI/Pod Identity are healthy, the PostgreSQL PVC is Bound, and Helm deployed the published `e3ecd48c1aa5a84f8033d850aa04cd8f8154b60e` images. Five application pods are Running/Ready; the Alembic Job is Completed. Ingress is accessed through a port-forward to the ClusterIP Traefik controller, avoiding an extra AWS load balancer. This is a real Ingress path to the AWS pods.

Separate `eks-*` screenshots and source logs prove this deployment; the earlier Kind evidence remains explicitly labelled. EKS Prometheus scrapes both API replicas UP, Grafana returned positive real metrics, and its populated dashboard was captured. Cloud deletion is still pending.

## Successful SHA rollout

[Run 38947611595](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38947611595) passed all required jobs. After it passed, local Helm upgraded both EKS Deployments from `e3ecd48c1aa5a84f8033d850aa04cd8f8154b60e` to `7f36cafc34b923fa34b1a0e727b2d359a060c757`; the migration Job completed, both replicas per tier became Ready and `/api/health` returned the target SHA. The notebook remained populated. Actual rollout output, machine-readable recording events and the captioned video are included. Automatic persistent EKS delivery was not enabled; the local CLI action is explicitly identified in the recording.
