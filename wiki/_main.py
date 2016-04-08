from . import url as _url
from .. import web as _web
from ..seq import unique as _unique
from lxml.etree import iterparse as _iterparse

import re as _re

def links(text):
	titles = _unique(title.split('|')[0] for title in _re.findall(r'\[\[([^\]\[]*)\]\]', text))
	return (title for title in titles if ':' not in title and '{' not in title)

def edges(title):
	return ((title, link) for link in links(str(_web.elements(_url.from_title(title),name='text')[0])))

def xml(filename):
	seq = _iterparse(filename)

	for evt, elem in seq:
		elem.tag = elem.tag.split('http://www.mediawiki.org/xml/export-0.10/}')[-1]
		yield elem
		elem.clear()
		while elem.getprevious() is not None:
			del elem.getparent()[0]

