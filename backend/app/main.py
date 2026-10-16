import os
import time

from fastapi import FastAPI, HTTPException, Response
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.database import engine
from app.routes import router

app = FastAPI(title="Orbit Scientific Calculator", version="1.0.0")
app.include_router(router)
REQUESTS = Counter("orbit_http_requests_total", "HTTP requests", ["method", "path", "status"])
LATENCY = Histogram("orbit_http_request_duration_seconds", "Request duration", ["method", "path"])


@app.middleware("http")
async def observe(request, call_next):
    started = time.perf_counter()
    status = 500
    try:
        response = await call_next(request)
        status = response.status_code
        return response
    finally:
        if request.url.path not in {"/metrics", "/health", "/ready", "/api/health"}:
            route = request.scope.get("route")
            path = route.path if route else "unmatched"
            REQUESTS.labels(request.method, path, str(status)).inc()
            LATENCY.labels(request.method, path).observe(time.perf_counter() - started)


@app.get("/health")
@app.get("/api/health")
def health():
    return {"status": "ok", "service": "orbit", "version": os.getenv("APP_VERSION", "dev")}


@app.get("/ready")
def ready():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1 FROM calculations LIMIT 1"))
    except SQLAlchemyError as exc:
        raise HTTPException(status_code=503, detail="Database is not ready.") from exc
    return {"status": "ready"}


@app.get("/metrics", include_in_schema=False)
def metrics():
    return Response(content=generate_latest(), headers={"Content-Type": CONTENT_TYPE_LATEST})
