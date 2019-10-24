import time


def reticulate(count=-1):
    spline = 0
    while count < 0 or spline < count:
        time.sleep(1)
        spline += 1
        yield spline
