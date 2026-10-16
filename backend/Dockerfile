ARG PYTHON_IMAGE=python:3.13-alpine3.24
FROM ${PYTHON_IMAGE} AS builder
WORKDIR /build
COPY requirements.txt .
RUN python -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt \
    && /opt/venv/bin/python -m pip uninstall --yes pip

FROM ${PYTHON_IMAGE} AS runtime
# Package installation is a build concern. Remove both copies of pip and the
# ensurepip wheel so its vulnerable vendored libraries are absent at runtime.
# Trivy still scans every remaining runtime package with the original gate.
RUN apk upgrade --no-cache \
    && /usr/local/bin/python -m pip uninstall --yes pip \
    && rm -rf /usr/local/lib/python3.13/ensurepip \
    && addgroup -S -g 10001 orbit \
    && adduser -S -D -u 10001 -G orbit orbit
ENV PATH="/opt/venv/bin:$PATH" PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1
WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY --chown=10001:10001 app ./app
COPY --chown=10001:10001 alembic ./alembic
COPY --chown=10001:10001 alembic.ini .
USER 10001:10001
EXPOSE 8000
HEALTHCHECK --interval=15s --timeout=3s --start-period=20s --retries=5 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2)"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
