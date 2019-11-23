"""Test cases for the splines module."""
from unittest.mock import Mock

from hypermodern_python import splines


async def test_reticulate_yields_count_times(mock_sleep: Mock) -> None:
    """Test if reticulate yields <count> times."""
    iterator = splines.reticulate(3)
    assert sum([1 async for _ in iterator]) == 3


async def test_reticulate_sleeps(mock_sleep: Mock) -> None:
    """Test if reticulate sleeps."""
    async for _ in splines.reticulate():
        break
    assert mock_sleep.called
