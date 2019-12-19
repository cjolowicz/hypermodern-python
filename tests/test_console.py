"""Test cases for the console module."""
from click.testing import CliRunner
import pytest

from hypermodern_python import console


@pytest.fixture
def runner() -> CliRunner:
    """Fixture for invoking command-line interfaces."""
    return CliRunner()


def test_main_succeeds(runner: CliRunner) -> None:
    """Test if console.main succeeds."""
    result = runner.invoke(console.main)
    assert result.exit_code == 0
