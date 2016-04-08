from datetime import datetime as _dt

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

