from . import url as _url
from .. import web as _web
from ..seq import unique as _unique

import re as _re

def edges(title):
	titles = _unique(title.split('|')[0] for title in _re.findall(r'\[\[([^\]\[]*)\]\]',str(_web.elements(_url.from_title(title),name='text')[0])))
	return ((title, x) for x in titles if ':' not in x and '{' not in x)

