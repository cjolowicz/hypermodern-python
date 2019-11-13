"""Utilities for spline manipulation."""
import time
from typing import Iterator


def reticulate(count: int = -1) -> Iterator[int]:
    """Reticulate splines.

    Args:
        count: Number of splines to reticulate

    Yields:
        A reticulated spline

    """
    spline: int = 0
    while count < 0 or spline < count:
        time.sleep(1)
        spline += 1
        yield spline
