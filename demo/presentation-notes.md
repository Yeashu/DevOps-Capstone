# Read-aloud presentation notes

Use these notes with [the PowerPoint](orbit-capstone-slides.pptx) or [the PDF](orbit-capstone-slides.pdf). These are the same notes embedded in the PowerPoint. For the 2:29 video, use the shorter [timed voice-over script](voiceover-script.md).

## Slide 1: Orbit scientific calculator

Hello, this is Orbit, my scientific calculator capstone. The application evaluates scientific expressions and saves calculations in a PostgreSQL notebook. I will show the application, the quality gates, the AWS deployment, and the evidence collected before cleanup.

## Slide 2: Application architecture

The frontend calls a FastAPI backend. The calculator uses a bounded expression parser rather than unrestricted Python evaluation. PostgreSQL stores the notebook, and Alembic owns schema changes. The API supports creating, listing, updating and deleting calculations. Health, readiness and Prometheus metrics have separate endpoints.

## Slide 3: Tests and code quality

The backend suite has sixty nine passing tests covering calculations and API behavior. Tests use an isolated database, with SQLite locally and disposable PostgreSQL in GitHub Actions. The production notebook is never the test database. Ruff checks Python code, and the frontend has four tests plus a production build.

## Slide 4: Docker and local development

Docker Compose starts the complete stack with one command. Health checks confirm that the frontend, backend and database are ready. The backend and frontend run as non-root users. The frontend Dockerfile uses a Node build stage and an Nginx runtime stage. The local demo is stopped now after evidence collection.

## Slide 5: GitHub Actions and GHCR

Every push to main starts the pipeline. Tests and the frontend build must pass before the images reach publication. The pipeline scans both images and publishes those exact images to GitHub Container Registry using full commit SHA tags. It also deploys to a temporary Kind cluster. The overall run is green. The separate automatic EKS job is disabled, so the recorded EKS upgrade uses the local authenticated Helm CLI.

## Slide 6: Trivy security gate

Trivy scans the operating system and packaged dependencies inside both container images. The initial backend image triggered the gate. Updating the runtime and removing unused vendored installer libraries resolved the findings. Both final images report zero high or critical findings. The workflow still fails on those severities, including unfixed vulnerabilities.

## Slide 7: Terraform and AWS EKS

Terraform planned and provisioned twenty real resources in the Mumbai region. The infrastructure includes a VPC, two public subnets in different availability zones, an EKS control plane and a managed worker group. The actual AWS Console capture shows two Ready workers. These are historical captures because the infrastructure has since been destroyed.

## Slide 8: Kubernetes and Helm on EKS

Helm manages the application on EKS. Both the backend and frontend have two running replicas. PostgreSQL uses persistent storage. ClusterIP Services provide internal access, and Ingress routes the root path to the frontend and API traffic to FastAPI. A migration job completes during release upgrades, while readiness checks keep traffic away from unready application pods.

## Slide 9: Prometheus and Grafana

The backend exposes Prometheus-formatted metrics. Prometheus scrapes both backend replicas, and both targets report UP. Grafana shows populated request and latency panels. The error panel has no series in this capture. The screenshot shows actual metrics from the EKS deployment. This demonstrates that the monitoring stack observes the application, rather than just running alongside it.

## Slide 10: Recorded deployment update

The original recording shows the calculator on EKS, a successful pipeline, and an upgrade to that pipeline’s exact published commit. I ran the Helm upgrade through the authenticated local CLI. The backend health endpoint then reported the new SHA, and the notebook still contained the saved calculations after pod replacement. The automatic EKS Actions job remained skipped. This is evidence of a real deployment update, with the delivery mechanism stated clearly.

## Slide 11: Cleanup and submission

Terraform destroy completed, and the independent audit confirmed removal of the project cluster, VPC, active workers, recorded volumes and related network resources. Temporary IAM access was also removed. The source, evidence screenshots, silent video and slide deck remain in the public repository. The demo folder contains the mandatory MP4 and the PowerPoint and PDF copies. Thank you.
