# DevOps narration for the 2:29 walkthrough

Read this as a simple overview of the DevOps work. Keep the calculator introduction brief. The screenshots are supporting evidence; there is no need to name each image or match every screen change with a sentence.

This version is about 262 words. Aim for roughly 110–120 words per minute, allowing brief pauses. Use the [plain-text copy](voiceover-script.txt) if recording software needs a script without formatting.

## Read aloud

For my capstone, I used a simple scientific calculator to demonstrate a complete DevOps workflow. My main focus was building, testing, deploying, and monitoring the application.

I used Git and GitHub to manage the code and track changes. I added automated tests to check that the application worked before building its Docker images.

With Docker, I packaged the frontend, backend, and database into a stack that starts with one command. This made the application easier to run in a consistent environment.

I created a GitHub Actions pipeline that runs on every push to main. It runs tests, builds the images, and scans them with Trivy. Images are published to GitHub Container Registry only after these checks pass. Each image uses a commit ID so I can identify the exact version.

For AWS, I used Terraform to create the network and EKS cluster, including two public subnets and a worker group. Keeping this setup in code made it repeatable and easier to manage.

I used Kubernetes and Helm to deploy the application. The frontend and backend each had two replicas, and Ingress provided access to the application.

For monitoring, I connected Prometheus and Grafana. This let me check application traffic and response times after deployment.

After the pipeline passed, I updated the EKS deployment using Helm from my local terminal. I checked the deployed version and confirmed that the saved data was still available.

Finally, I destroyed the AWS resources to avoid ongoing costs and checked for anything left behind. The repository contains the code, configuration, screenshots, and documentation for the complete workflow.

## Optional pacing guide

These times are approximate topic cues, not text to read aloud.

| Time | Topic |
| --- | --- |
| 00:00–00:13 | Capstone goal and brief application introduction |
| 00:13–00:33 | Git, tests and Docker |
| 00:33–00:59 | GitHub Actions, Trivy and container publication |
| 00:59–01:25 | Infrastructure as code and AWS provisioning |
| 01:25–01:44 | Kubernetes, Helm, replicas and Ingress |
| 01:44–01:57 | Prometheus and Grafana monitoring |
| 01:57–02:08 | Verifying the actual EKS update |
| 02:08–02:29 | Teardown, residual-resource checks and evidence |

The EKS upgrade used the authenticated local Helm CLI after a successful pipeline. The optional automatic EKS Actions job was skipped. The cloud screenshots show the completed deployment before teardown.

[Silent MP4](orbit-capstone-video.mp4) · [Slide presentation notes](presentation-notes.md)
