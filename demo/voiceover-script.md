# Voice-over script for the 2:29 video

Use this script with [the silent MP4](orbit-capstone-video.mp4). Read the text in the right-hand column. The times are cue points, not spoken text. Aim for roughly 110–125 words per minute and leave short pauses between scenes.

The AWS scenes are historical captures. The recorded deployment uses the local Helm CLI after a successful pipeline; the automatic EKS Actions job was skipped.

| Video time | Read aloud |
| --- | --- |
| 00:00–00:06 | This is Orbit, my Python scientific calculator with a PostgreSQL notebook. |
| 00:06–00:13 | Degree mode returns sine of thirty as zero point five. |
| 00:13–00:18 | All sixty nine backend tests pass using an isolated test database. |
| 00:18–00:22 | Git tracks meaningful commits and excludes secrets. |
| 00:22–00:28 | Docker Compose runs three healthy services: frontend, backend, and PostgreSQL. |
| 00:28–00:33 | Both application containers run as non-root users. |
| 00:33–00:40 | Every push to main runs tests, builds, scans, and container publication. |
| 00:40–00:45 | The backend image uses the exact Git commit identifier. |
| 00:45–00:50 | The frontend image uses the same SHA tagging scheme. |
| 00:50–00:54 | Trivy finds no high or critical backend vulnerabilities. |
| 00:54–00:59 | The frontend scan also passes. Either scan can block publication. |
| 00:59–01:04 | Terraform plans twenty real resources in Mumbai. |
| 01:04–01:09 | Apply completes successfully, creating the VPC and EKS infrastructure. |
| 01:09–01:14 | This AWS Console capture shows the project VPC. |
| 01:14–01:17 | Two public subnets span separate availability zones. |
| 01:17–01:20 | The EKS control plane is active. |
| 01:20–01:25 | Both worker nodes are Ready. |
| 01:25–01:30 | Helm manages the application, Ingress controller, and monitoring releases. |
| 01:30–01:35 | Two backend and two frontend replicas run alongside PostgreSQL. |
| 01:35–01:39 | ClusterIP Services provide access inside Kubernetes. |
| 01:39–01:44 | Ingress routes the website and API to their respective services. |
| 01:44–01:48 | FastAPI exposes Prometheus request and latency metrics. |
| 01:48–01:52 | Both backend targets report UP in Prometheus. |
| 01:52–01:57 | Grafana displays live request rate and latency panels. |
| 01:57–02:02 | After green CI, a local Helm upgrade updates EKS. |
| 02:02–02:08 | The health check reports the new commit. The notebook persists. |
| 02:08–02:15 | Terraform destroy completes. These are historical AWS captures from before cleanup. |
| 02:15–02:22 | An independent audit confirms no project cluster, VPC, workers, or volumes remain. |
| 02:22–02:29 | Temporary access credentials are removed. All source and evidence remain in the repository. |

## Short pronunciation guide

- **FastAPI:** fast A P I
- **PostgreSQL:** post-gress Q L
- **CI:** C I
- **SHA:** shah, or say “commit identifier”
- **VPC:** V P C
- **EKS:** E K S
- **Grafana:** grah-fah-nah
- **Prometheus:** pro-mee-thee-us

For a live explanation of the slides, use [the slide-by-slide speaker notes](presentation-notes.md).
