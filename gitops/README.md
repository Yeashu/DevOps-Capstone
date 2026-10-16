# Optional GitOps

The homework also requests GitOps. The Argo CD Application reads the chart and `gitops/values.yaml`. Argo CD must already be installed. This session has not installed or synced it.

1. Let CI publish both images, then make them pullable by the cluster.
2. Bootstrap the namespace, database Secret, storage class and Ingress controller.
3. Replace both `local` tags in `gitops/values.yaml` with the same successful full commit SHA. For EKS, add the gp3 storage class and real ingress host overrides.
4. Keep direct `DEPLOY_TO_EKS` disabled so CI and Argo CD do not manage the same release.
5. Apply `gitops/application.yaml`, inspect Argo CD's rendered resources, then sync manually.
6. For changes, let CI publish first, commit that SHA to the GitOps values, and sync again. Enable auto-sync only after validating the complete flow.

The checked-in local tags are placeholders and cannot pull from GHCR. A commit updates desired state; Argo CD compares it with the cluster and reconciles differences. The default presentation may instead use the automated Helm delivery job.
