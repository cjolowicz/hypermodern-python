import pytest


@pytest.fixture
def mock_sleep(mocker):
    return mocker.patch("time.sleep")
