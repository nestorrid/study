import pytest
from app import app


@pytest.fixture(name='client')
def flask_client():
    app.testing = True
    yield app.test_client()


@pytest.fixture(name='runner')
def flask_runner():
    return app.test_cli_runner()
