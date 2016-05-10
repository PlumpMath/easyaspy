from itertools import *
from ._main import *
from re import finditer as _find
import codecs as _codecs
import random as _random

first = next
key = lambda x: x[0]
value = lambda x: x[1]
identity = lambda x: x
empty = lambda x: not x

def keys(seq):
    return (key(s) for s in seq)

def values(seq):
    return (value(s) for s in seq)

def integers():
    "None -> [1,2,3,4,5,...]"
    return count(1)

def multiples_of(n):
    "3 -> [3,6,9,...]"
    return map(lambda x: x*n, integers())

def nth(n, seq, default=None):
    "2 [4,5,6] -> 5"
    return next(islice(seq, n, None), default)

def take(n, seq):
    "3 integers() -> [1,2,3]"
    return list(islice(seq, n))

def random():
    for i in integers():
        yield _random.random()

def randof(options):
    options = list(options)
    for i in integers():
        yield _random.choice(options)

def randbool():
    return randof([True, False])

def reduce(fn, seq, initial):
    return list(accumulate(chain([initial],seq),fn))[-1]

def size(seq):
    "[10,11,12] -> 3"
    return sum(1 for x in seq)

def listmap(fn, seq):
    return list(map(fn, seq))

def deeplist(seq):
    return lmap(lambda x: list(x), seq)

def grouper(n, seq, default=None):
    "2 [1,2,3,4,...] -> [(1,2),(3,4),...]"
    args = [iter(seq)] * n
    return zip_longest(*args, fillvalue=default)

def pairwise(seq):
    "[1,2,3,...] -> [(1,2),(2,3),...]"
    a, b = tee(seq)
    next(b, None)
    return zip(a, b)

def flatten(seq):
    "[[1,2],[3,4],...] -> [1,2,3,4,...]"
    return chain.from_iterable(seq)

def unique(seq, key=identity):
    "[1,3,1,2,3,4,2] -> [1,3,2,4]"
    seen = set()
    seen_add = seen.add
    for element in filterfalse(seen.__contains__, map(key, seq)):
        seen_add(element)
        yield element

def duplicates(seq,key=identity):
    "[1,3,1,2,3,4,2] -> [1,3,2]"
    seen = set()
    seen_add = seen.add
    for element in map(key,seq):
        if element in seen:
            yield element
        else:
            seen_add(element)

def split(pred, seq):
    "odd integers() -> [1,4,6,8,...] [1,3,5,7,9,...]"
    t1,t2 = tee(seq)
    return filter(pred, t1), filterfalse(pred, t2)

def chunk(filename, seq):
    def out(i,s):
        with append(filename.format(i)) as f:
            f.write(s)
            return s

    return (out(i,s) for i, s in enumerate(seq))

def itereval(text):
    "'(['a','b','c'], ['d','e','f'], ...)' -> [['a','b','c'],['d','e','f'],...]"
    return (eval(text[a:b]) for a,b in \
        grouper(2, chain([1],
        flatten(map(lambda x: (x[0]+1,x[1]-1),
            map(lambda x: x.span(), 
                _find(r'\],\s?\[', text)))),
                    [-1])))

def chunk_and_cache(seq, name='chunk{0:03d}.py', size=15360):
    return enumerate(
        keys(
            times(
                chunk(name, grouper(size, seq)))))

