import pytest
from musify import app

""" Initialize the testing environment

Creates an app for testing that has the right configuration
"""

@pytest.fixture
def client():
    """Configure the app for testing
    Sets the configuration variable to test the app

    return: app
    """
    client = app.test_client()
    yield  client