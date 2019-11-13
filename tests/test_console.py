from unittest.mock import Mock

from click.testing import CliRunner
import pytest
from pytest_mock import MockFixture

from hypermodern_python import console


@pytest.fixture
def runner() -> CliRunner:
    return CliRunner()


@pytest.fixture
def mock_splines_reticulate(mocker: MockFixture) -> Mock:
    mock = mocker.patch("hypermodern_python.splines.reticulate")
    mock.return_value = [1, 2, 3]
    return mock


def test_main_succeeds(runner: CliRunner, mock_splines_reticulate: Mock) -> None:
    result = runner.invoke(console.main)
    assert result.exit_code == 0


def test_main_prints_progress_message(runner: CliRunner, mock_sleep: Mock) -> None:
    result = runner.invoke(console.main, ["--count=1"])
    assert result.output == "Reticulating spline 1...\n"
