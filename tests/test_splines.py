from unittest.mock import Mock

from hypermodern_python import splines


def test_reticulate_yields_count_times(mock_sleep: Mock) -> None:
    iterator = splines.reticulate(3)
    assert sum(1 for _ in iterator) == 3


def test_reticulate_sleeps(mock_sleep: Mock) -> None:
    for _ in splines.reticulate():
        break
    assert mock_sleep.called
