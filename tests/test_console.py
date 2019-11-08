import click.testing
import pytest

from hypermodern_python import console


@pytest.fixture
def runner():
    return click.testing.CliRunner()


@pytest.fixture
def mock_splines_reticulate(mocker):
    mock = mocker.patch("hypermodern_python.splines.reticulate")
    mock.return_value = [1, 2, 3]
    return mock


def test_main_succeeds(runner, mock_splines_reticulate):
    result = runner.invoke(console.main)
    assert result.exit_code == 0
