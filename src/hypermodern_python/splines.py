"""Utilities for spline manipulation."""
import asyncio
from typing import AsyncIterator


async def reticulate(count: int = -1) -> AsyncIterator[int]:
    """Reticulate splines.

    Args:
        count: Number of splines to reticulate

    Yields:
        A reticulated spline

    Example:
        >>> from hypermodern_python import splines
        >>> a, b = splines.reticulate(2)
        >>> a, b
        (1, 2)

    """
    spline: int = 0
    while count < 0 or spline < count:
        await asyncio.sleep(1)
        spline += 1
        yield spline
