# Validation record

Orbit was built and exercised locally, in GitHub Actions, on disposable Kind and on real AWS EKS. The following are executed results, supported by the [evidence index](../screenshots.md).

| Check | Verified result |
| --- | --- |
| Backend tests | **69 passed** locally on isolated SQLite and in Actions on migrated disposable PostgreSQL; Ruff passed |
| Frontend | Four tests and production build passed; real browser checks passed on Compose and EKS |
| Source security | Bandit, pip-audit and Trivy secret scanning passed |
| Containers | Both images built; three Compose services healthy; backend UID 10001 and frontend UID 101 |
| Image security | Both remediated images passed the unchanged HIGH/CRITICAL Trivy gate with zero findings at those severities, including unfixed vulnerabilities |
| Registry | Both exact scanned images published to GHCR with full commit SHA tags |
| Terraform | Network-enabled init/validate passed; actual plan **20 to add, 0 to change, 0 to destroy**; apply **20 added** |
| AWS | Mumbai VPC, two public subnets in separate AZs, active EKS 1.37, two Ready t3.medium workers, EBS CSI and Pod Identity verified |
| Kubernetes | Actual Helm installs on Kind and EKS; two backend + two frontend replicas and PostgreSQL Running/Ready; Services, Ingress and Bound gp3 PVC verified |
| Monitoring | On Kind and EKS: both API targets UP, Grafana datasource returned positive actual metrics, populated dashboard captured |
| Rollout | EKS upgraded to the exact successful pipeline SHA; health returned that SHA and the database notebook survived |
| Cleanup | Terraform destroy completed; empty state and independent AWS residual-resource audit passed; temporary IAM bootstrap user/key/operator role removed |
| Recording | Full 2-minute 29-second narrated evidence guide, original 92-second live EKS rollout, captions and presentation runbook included |

Verified green runs: [38946260879](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38946260879), [38947611595](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38947611595), and [38949107515](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38949107515). The final run linked here validates commit `903a3b1dadc588b93657852dd9ec0e605d56f159`; subsequent cleanup documentation is separate evidence.

## Actual AWS deployment and rollout

Terraform provisioned EKS in `ap-south-1`. Helm initially deployed the published `e3ecd48c1aa5a84f8033d850aa04cd8f8154b60e` images. Five application pods were Running/Ready; the Alembic Job was Completed. Ingress was accessed through a port-forward to the ClusterIP Traefik controller, providing a real Ingress path to the AWS pods without an additional cloud load balancer.

After run 38947611595 passed, **local authenticated Helm** upgraded both EKS Deployments to `7f36cafc34b923fa34b1a0e727b2d359a060c757`. The migration Job completed, both replicas per tier became Ready, `/api/health` returned the target SHA and the notebook remained populated. The actual output, machine-readable recording events and captioned browser video are included. The optional hosted persistent EKS delivery job was disabled; the recording identifies the local CLI rollout accurately.

The explicitly named `eks-*` and `aws-*` evidence shows the real AWS lifecycle. Earlier Kind evidence remains separately labelled.

## Completed cleanup

The first destroy was interrupted while waiting for the worker group; AWS completed that deletion asynchronously. A resumed `terraform destroy` refreshed state and removed the **14 remaining resources**. Both actual logs are retained, with the final completion excerpt rendered as `terraform-destroy.png`.

An independent audit confirms that the project cluster and VPC are absent, no active worker instances remain, the database and both recorded worker root volumes are absent, no project ENIs or load balancers remain, and Terraform state is empty. Temporary bootstrap credentials and the operator IAM role were then removed. The original default AWS profile was verified unchanged. Local Compose remains healthy at http://localhost:3000.

## Security and evidence provenance

The initial backend image security gate correctly blocked publication. Updating the Alpine runtime and physically removing unused pip/ensurepip vendored libraries resolved its findings without weakening severity or unfixed-vulnerability policy. See [the actual scan explanation](../security/README.md).

Browser PNGs are actual captures. Command-output PNGs are labelled renders of actual source logs, not native terminal-window screenshots. Account IDs and administrator CIDRs are explicitly redacted in committed Terraform logs. Real state, tfvars, binary plans, session cookies and credentials are excluded from Git.

**Git metadata:** at the owner's request, commits after that instruction use the assigned author/committer timestamp `2026-10-16T23:54:00+05:30`. This is metadata, not the completion time of later AWS operations. Actual Actions and capture timestamps are unchanged; evidence collected after midnight is not represented as having completed before the deadline.

## Expanded video and Firefox compatibility

The full 2-minute 29-second walkthrough covers all ten modules using genuine source evidence and original live-demo excerpts. The captured AWS Console scenes show the provisioned VPC, two public subnets, active EKS cluster and two Ready workers. Terraform plan/apply/destroy, security, container publishing, Kubernetes, monitoring and cleanup are also included. Synthetic narration and captured evidence are explicitly labelled; the guide does not claim a new live AWS deployment. The original 92-second live recording is preserved separately. Both are provided as H.264 Baseline / MP4 with fast-start metadata. The full guide adds AAC narration and captions.

The concise cut is **148.94 seconds**, with evidence scenes lasting 3–7 seconds. A final single-stream H.264 encode with two-second keyframes fixes stale frames after Firefox chapter jumps. The [Firefox decoder check](evidence/firefox-video-playback.json) confirms a rendered frame at 4.0 seconds and the AWS VPC frame at 69.203 seconds; this checks displayed video frames, not only the playback clock. The separately hosted [player](https://yeashu.github.io/DevOps-Capstone/recordings/?v=short149r2) also avoids the inline attachment route that reported Bad Gateway.
