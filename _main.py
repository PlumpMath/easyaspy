from datetime import datetime as _dt
import codecs as _codecs
import os as _os

def now():
    return _dt.now().timestamp()

def time(fn):
    start = now()
    result = fn()
    return now() - start, result

def times(seq):
    start = now()
    for s in seq:
        yield now() - start, s
        start = now()

open = lambda x,y: _codecs.open(x, y, 'utf-8')
read = lambda x: open(x, 'r')
write = lambda x: open(x, 'w')
append = lambda x: open(x, 'a')

def lines(filename):
    with read(filename) as f:
        for line in f:
            yield line

def trim(seq):
    for s in seq:
        yield s.strip()

def ls(dirname='.'):
    return _os.listdir(dirname)

def complement(fn):
    return lambda b: not fn(b)

