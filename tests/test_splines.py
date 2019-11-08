from hypermodern_python import splines


def test_reticulate_yields_count_times():
    iterator = splines.reticulate(3)
    assert sum(1 for _ in iterator) == 3
