""" import os
import tempfile """

import pytest
from ramenai.app import app as appli

# from ramenai.db import get_db, init_db


@pytest.fixture
def app():
    # Aqui database
    appli.config["SERVER_NAME"] = "127.0.0.1:5000"
    appli.config["APPLICATION_ROOT"] = "/"
    appli.config["PREFERRED_URL_SCHEME"] = "http"
    appli.testing = True
    yield appli


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
