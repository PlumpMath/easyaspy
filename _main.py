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

def read(filename):
	with _codecs.open(filename,'r','utf-8') as f:
		return f.read()

def ls(dirname='.'):
	return _os.listdir(dirname)

def complement(fn):
	return lambda b: not fn(b)

