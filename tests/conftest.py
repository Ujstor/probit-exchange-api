import pytest
from website import create_app
from website.api_auth import Probit
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

ID = os.environ.get('ID')
SECRET = os.environ.get('SECRET')


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture
def probit():
    probit = Probit(ID, SECRET)
    return probit
