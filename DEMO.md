# Deployment demonstration

[Presentation video](demo/presentation.mp4) · [PowerPoint](demo/orbit-capstone-slides.pptx) · [PDF](demo/orbit-capstone-slides.pdf) · [Browser player](https://yeashu.github.io/DevOps-Capstone/recordings/?v=presentation)

## Recorded workflow

1. Evaluate scientific expressions through the EKS-hosted application and save results to PostgreSQL.
2. Verify the successful [GitHub Actions run](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38947611595), including tests, image scans and SHA-tagged container publication.
3. Upgrade both EKS application Deployments with Helm to commit `7f36cafc34b923fa34b1a0e727b2d359a060c757`.
4. Confirm that the health endpoint reports the deployed commit and the saved notebook survives the rollout.
5. Verify application metrics in Prometheus and Grafana.
6. Destroy AWS infrastructure and audit for remaining project resources.

## Deployment method

The recorded EKS release used an authenticated local Helm command after CI passed. The optional persistent EKS deployment job in Actions was disabled. CI independently deploys and verifies the application on a temporary Kind cluster.

The EKS demonstration used Traefik Ingress accessed through a local port-forward to the controller. The backend and frontend each had two replicas, ClusterIP Services and readiness checks; PostgreSQL used persistent storage.

## Evidence

- [Original EKS rollout recording](docs/recordings/orbit-eks-rollout.mp4)
- [Helm upgrade output](docs/evidence/eks-rollout.txt)
- [Deployment health version](docs/screenshots/eks-updated-version.png)
- [Notebook after rollout](docs/screenshots/eks-after-rollout.png)
- [Complete screenshot index](screenshots.md)
- [Terraform destroy output](docs/evidence/terraform-destroy.txt)
- [AWS cleanup audit](docs/evidence/aws-cleanup-audit.json)

AWS infrastructure has been removed. Local execution and deployment instructions are in [README.md](README.md).
