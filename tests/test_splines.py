from hypermodern_python import splines


def test_reticulate_yields_count_times(mock_sleep):
    iterator = splines.reticulate(3)
    assert sum(1 for _ in iterator) == 3


def test_reticulate_sleeps(mock_sleep):
    for _ in splines.reticulate():
        break
    assert mock_sleep.called
