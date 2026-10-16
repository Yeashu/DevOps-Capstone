# Security gates and explanation

The AST interpreter accepts numbers, known constants, arithmetic and explicitly approved functions. It rejects attributes, imports, indexing, strings and comprehensions. Length, node-count, depth, exponent and factorial bounds keep individual requests inexpensive. Invalid API requests must not persist a row.

CI runs Bandit SAST, pip-audit SCA and Trivy secret detection. `aquasecurity/trivy-action@v0.36.0` checks both built images, including OS packages and application dependencies. HIGH or CRITICAL findings return exit code 1, including unfixed findings. There is no blanket ignore file or continue-on-error bypass. Both scans must pass before either image is published.

New CVEs may block unchanged source. Update the affected package or base image and rebuild; a passing test job alone does not mean an image passed security scanning.

## Observed scan result

The [first hosted run](https://github.com/Yeashu/DevOps-Capstone/actions/runs/38943294699) passed source SAST/SCA/secret scanning, but its backend image gate failed. Source dependency auditing alone does not cover the operating-system packages and libraries vendored inside an image's packaging tools.

Trivy scanned both container images, including operating-system packages and Python dependencies. The original backend reported 63 OS findings (61 HIGH, 2 CRITICAL) and four HIGH Python findings, including CVE-2025-47273, a path-traversal vulnerability in pip's vendored setuptools PackageIndex; the frontend reported zero findings at the configured severity. The gate correctly blocked publication until the backend could be remediated and rescanned.

The other Python findings were GHSA-6v7p-g79w-8964 (vendored msgpack) and CVE-2026-97687 / CVE-2026-97689 (vendored urllib3). The actual installed pip `vendor.txt` and SBOM list msgpack 1.1.2, setuptools 70.3.0 and urllib3 2.7.0. Installing newer standalone versions would not replace these bundled copies.

## Prepared remediation — awaiting the next hosted scan

`backend/Dockerfile` now uses the published `python:3.13-alpine3.24` base for both stages, upgrades Alpine runtime packages, removes pip from the built application virtual environment and the base interpreter, and removes the bundled ensurepip installer wheel. The running API and Alembic require their installed libraries and executables, not a package installer. This removes build-only vulnerable code from the runtime image rather than hiding scan findings.

The HIGH/CRITICAL gate, unfixed-vulnerability policy and application requirements are unchanged. **A clean replacement-image scan is not yet verified.** Rebuild and rerun the workflow; if additional runtime CVEs remain, address those exact reports before publishing. The [original backend report](../docs/evidence/hosted-trivy-backend-before.txt) and [frontend report](../docs/evidence/hosted-trivy-frontend.txt) are retained.

Actual `.env`, state, plans and credential variable files are ignored. Compose's checked-in password is explicitly a local demo value. Kubernetes secrets are created interactively; base64 is encoding, not encryption. The notebook is a shared classroom demo without user authentication.
