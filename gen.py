from ._main import *
from .seq import *

def file(filename, struct, *data):
    lines = zip(*data)
    with write(filename) as f:
        for line in lines:
            f.write(struct.format(*line))

