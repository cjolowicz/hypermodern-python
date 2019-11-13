"""Package-wide test fixtures."""
from unittest.mock import Mock

import pytest
from pytest_mock import MockFixture


@pytest.fixture
def mock_sleep(mocker: MockFixture) -> Mock:
    """Mock for time.sleep."""
    return mocker.patch("time.sleep")
