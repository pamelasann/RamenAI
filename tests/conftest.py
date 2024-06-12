""" import os
import tempfile """

import pytest
from ramenai.app import app as appli

# from ramenai.db import get_db, init_db


@pytest.fixture
def app():
    # Aqui database
    appli.testing = True
    yield appli


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
