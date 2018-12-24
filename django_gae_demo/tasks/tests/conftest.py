import pytest

from rest_framework.test import APIClient


@pytest.fixture
def app(db):
    return APIClient()
