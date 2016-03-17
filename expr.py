from .seq import *
from parser import expr as _expr

def is_list(x):
	return type(x) is list

def is_str(x):
	return type(x) is str

def is_empty(x):
	return len(x) is 0

def is_parseable(x):
	try:
		_expr(x)
		return True
	except:
		return False

def symbols(s):
	return filter(lambda x: x != '', unpack(_expr(s).tolist()))

def unpack(st):
    if is_list(st) and not is_empty(st):
        car,*cdr = st
        for s in chain(unpack(car),unpack(cdr)):
            yield s
    elif is_str(st):
        yield st

def symbols_from_lines(seq):
	return map(symbols,filter(is_parseable,seq))

def functions(seq):
	return map(key,filter(lambda x: value(x) == '(', pairwise(seq)))

