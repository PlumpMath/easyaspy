from itertools import *

first = next
key = lambda x: x[0]
value = lambda x: x[1]
identity = lambda x: x

def integers():
	"None -> [1,2,3,4,5,...]"
	return count(1)

def take(n,seq):
	"3 integers() -> [1,2,3]"
	return list(islice(seq,n))

def size(seq):
	"[10,11,12] -> 3"
	return sum(1 for x in seq)

def lmap(fn, seq):
	return list(map(fn, seq))

def pairwise(seq):
	"[1,2,3,...] -> [(1,2),(2,3),...]"
	a,b = tee(seq)
	next(b,None)
	return zip(a,b)

def flatten(seq):
	"[[1,2],[3,4],...] -> [1,2,3,4,...]"
	return chain.from_iterable(seq)

def unique(seq,key=identity):
	"[1,3,1,2,3,4,2] -> [1,3,2,4]"
	seen = set()
	seen_add = seen.add
	for element in filterfalse(seen.__contains__,map(key,seq)):
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
	return filter(pred,t1),filterfalse(pred,t2)

