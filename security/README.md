# Security gates and explanation

The AST interpreter accepts numbers, known constants, arithmetic and explicitly approved functions. It rejects attributes, imports, indexing, strings and comprehensions. Length, node-count, depth, exponent and factorial bounds keep individual requests inexpensive. Invalid API requests must not persist a row.

CI runs Bandit SAST, pip-audit SCA and Trivy secret detection. `aquasecurity/trivy-action@v0.36.0` checks both built images, including OS packages and application dependencies. HIGH or CRITICAL findings return exit code 1, including unfixed findings. There is no blanket ignore file or continue-on-error bypass. Both scans must pass before either image is published.

New CVEs may block unchanged source. Update the affected package or base image and rebuild; a passing test job alone does not mean an image passed security scanning.

## Required 2–3 sentence scan explanation

Complete this after the first actual scan:

> Trivy scanned the backend and frontend container images for vulnerabilities in OS packages and application dependencies. The reports showed [actual HIGH/CRITICAL counts and CVE identifier if any]; either image having a HIGH or CRITICAL finding blocks publication. A clean result means no such known vulnerabilities were detected in the scanned inventory using that scan database, not that every possible security issue is absent.

**Current result: not scanned in this session.** Download `trivy-backend` and `trivy-frontend` workflow artifacts and capture the Actions scan steps before replacing this statement. The reference project's result is not evidence for Orbit.

Actual `.env`, state, plans and credential variable files are ignored. Compose's checked-in password is explicitly a local demo value. Kubernetes secrets are created interactively; base64 is encoding, not encryption. The notebook is a shared classroom demo without user authentication.
