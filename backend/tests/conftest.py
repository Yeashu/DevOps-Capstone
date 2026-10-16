"""Temporary migrated databases only; DATABASE_URL never selects the test database."""
import os

import pytest


@pytest.fixture
def client(tmp_path, monkeypatch):
    from alembic import command
    from alembic.config import Config
    from fastapi.testclient import TestClient
    from sqlalchemy import create_engine, text
    from sqlalchemy.engine import make_url
    from sqlalchemy.orm import sessionmaker

    test_url = os.getenv("TEST_DATABASE_URL", f"sqlite:///{tmp_path}/orbit_test.db")
    parsed = make_url(test_url)
    if parsed.get_backend_name() != "sqlite" and not (parsed.database or "").endswith("_test"):
        pytest.fail("TEST_DATABASE_URL must point to a database ending in _test")
    monkeypatch.setenv("DATABASE_URL", test_url)
    from app import database
    from app.main import app

    test_engine = create_engine(
        test_url,
        connect_args={"check_same_thread": False} if parsed.get_backend_name() == "sqlite" else {},
    )
    monkeypatch.setattr(database, "engine", test_engine)
    import app.main as main
    monkeypatch.setattr(main, "engine", test_engine)
    command.upgrade(Config("alembic.ini"), "head")
    with test_engine.begin() as connection:
        connection.execute(text("DELETE FROM calculations"))
    factory = sessionmaker(bind=test_engine, expire_on_commit=False)

    def override_db():
        with factory() as session:
            yield session

    app.dependency_overrides[database.get_db] = override_db
    try:
        with TestClient(app) as test_client:
            yield test_client
    finally:
        app.dependency_overrides.clear()
        with test_engine.begin() as connection:
            connection.execute(text("DELETE FROM calculations"))
        test_engine.dispose()
