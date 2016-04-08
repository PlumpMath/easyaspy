from itertools import *
import codecs as _codecs

first = next
key = lambda x: x[0]
value = lambda x: x[1]
identity = lambda x: x

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

def size(seq):
	"[10,11,12] -> 3"
	return sum(1 for x in seq)

def lmap(fn, seq):
	return list(map(fn, seq))

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

def write(filename, msg):
	with _codecs.open(filename, 'a', 'utf-8') as f:
		f.write(str(msg))
	return msg

def output(filename, seq):
	return (write(filename.format(i), s) for i, s in enumerate(seq))

