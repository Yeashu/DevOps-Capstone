#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p docs/evidence docs/screenshots
python_bin=${ORBIT_PYTHON:-.venv/bin/python}
python_bin=$("$python_bin" -c 'import sys; print(sys.executable)')
docker compose up --build -d --wait --wait-timeout 180 2>&1 | tee docs/evidence/docker-compose.txt
docker compose ps | tee -a docs/evidence/docker-compose.txt
: > docs/evidence/non-root-users.txt
for component in backend frontend; do
  docker compose exec -T "$component" id | tee -a docs/evidence/non-root-users.txt
done
(cd backend && "$python_bin" -m pytest -v) 2>&1 | tee docs/evidence/pytest.txt
(cd frontend && npm ci --ignore-scripts && npm test && npm run build) 2>&1 | tee docs/evidence/frontend-build.txt
git log --oneline --decorate -15 | tee docs/evidence/git-history.txt
curl --fail --silent http://localhost:8000/metrics > docs/evidence/metrics.txt
npm --prefix scripts install --ignore-scripts
./scripts/node_modules/.bin/playwright install chromium
node scripts/capture-browser.mjs
for name in docker-compose non-root-users pytest frontend-build git-history metrics; do
  "$python_bin" scripts/render-transcript.py "docs/evidence/$name.txt" \
    "docs/screenshots/$name.png" --title "Orbit | $name"
done
echo 'Local evidence captured. Cloud, pipeline, Kubernetes and monitoring evidence need their live environments.'
