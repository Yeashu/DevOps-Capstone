# DevOps presentation narration

This is the expanded script for a presentation of about five minutes. It contains approximately **615 words**. Read at a comfortable pace; the final video will follow the audio you provide. Do not try to fit the narration into the existing 2:29 reference cut.

The slide headings below are cues and are not part of the narration. Each section matches the corresponding slide in the [11-slide presentation](orbit-capstone-slides.pptx). Use the [plain-text script](voiceover-script.txt) for uninterrupted reading.

## Video length guidance

The supplied grading rubric and saved Session 21 instructions do not specify a video duration. The previous under-three-minute target was the owner's preference, now replaced by a target of about five minutes. The supplied screenshot cuts off the separate “Video Requirements” section, so any duration rule there remains unverified. Five minutes is a working target, not a confirmed course rule.

## Read aloud

### 1. Project overview

For my capstone, I built a complete DevOps workflow around Orbit, a simple scientific calculator. My focus was on how the application moves from source code to a working deployment, including testing, containers, security checks, cloud infrastructure, and monitoring.

### 2. Application architecture

The application has a browser frontend, a FastAPI backend, and a PostgreSQL database. The backend provides the calculation and notebook APIs. Keeping saved calculations in the database means they remain available when application containers are replaced. This gave me a small, working application to use throughout the DevOps process.

### 3. Testing and code quality

Before building images, I added automated tests to check the application. The backend has sixty-nine passing tests, and the frontend has its own tests and build check. I used isolated test databases so testing would not affect saved application data. These checks run in the pipeline, so a failed test prevents later build and publication steps.

### 4. Docker

I containerized the application and used Docker Compose to start the frontend, backend, and database together. This made the setup consistent and easy to reproduce. The frontend uses a multi-stage Docker build, keeping build tools out of the final runtime image. Both application containers run without root privileges, and health checks help confirm the services are ready.

### 5. GitHub Actions and the registry

I used Git and GitHub to track the implementation through meaningful commits. The repository excludes credentials, local environment files, and generated dependencies. I then created a GitHub Actions pipeline that starts on pushes to main. It runs the tests and frontend build, checks the running application, builds both images, and scans them before publishing. The exact scanned images go to GitHub Container Registry with commit-based tags, so I can trace a deployed image back to its source version.

### 6. Security

For security, the pipeline includes source checks, dependency checks, secret scanning, and Trivy image scans. The image scans fail on high or critical vulnerabilities. The backend initially failed this gate. I updated the runtime and removed unused packaged libraries to resolve the findings. Both final image scans passed, and I kept the original security rule in place.

### 7. Terraform and AWS

For the cloud environment, I used Terraform to define the infrastructure in code. The plan and apply created twenty resources in the Mumbai region, including a VPC, two public subnets in different availability zones, an EKS cluster, and its worker group. I verified that both workers were Ready. Terraform made the setup reviewable, repeatable, and easier to remove after the demonstration.

### 8. Kubernetes and Helm

I used Helm to deploy and manage the application on Kubernetes. The backend and frontend each had two replicas. ClusterIP Services provided internal access, and Ingress routed browser and API requests. Readiness checks helped control when pods received traffic. PostgreSQL used persistent storage, so replacing application pods did not remove the notebook. The chart also managed the database migration job during upgrades.

### 9. Monitoring

I added Prometheus and Grafana to monitor the application. Prometheus collected request and latency metrics from the backend, and both application targets reported UP. Grafana showed populated request and response-time panels. These measurements helped verify that the application was handling traffic after deployment.

### 10. Deployment verification

After a successful pipeline, I updated the real EKS deployment using Helm from my local terminal. I verified the new commit through the health endpoint and checked that saved calculations survived the rollout. The separate automatic EKS Actions job was skipped, so this cloud update used the authenticated CLI. The pipeline also tested deployment in a temporary Kind cluster.

### 11. Cleanup

Finally, I ran Terraform destroy and checked for remaining AWS resources, including the cluster, workers, network resources, and recorded volumes. I also removed temporary access credentials. The cloud screenshots show the deployment before this cleanup. The repository preserves the source, configuration, original logs, screenshots, and presentation materials so the full workflow can be reviewed.

## Recording and editing

Record the complete narration at a natural pace and send the audio file here. The presentation video will be edited around your actual speech, using the matching slides, captured evidence, and relevant excerpts from the original live demonstration. Short pauses between sections are useful; no exact per-slide timings are required.

The EKS deployment in the evidence used the authenticated local Helm CLI after green CI. The automatic EKS Actions job was skipped. Keep that distinction in the narration. The AWS infrastructure has been destroyed, and the visual evidence is historical.
