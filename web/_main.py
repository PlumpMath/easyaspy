from bs4 import BeautifulSoup as _bs
import requests as _r

def parse(url):
	"Parse url into BeautifulSoup object."
	return _bs(url,"lxml")

def get(url):
	"Download content at url."
	return parse(_r.get(url).text)

def elements(url,name=None):
	"Return all elements of type <name> from url."
	return get(url).find_all(name) if name else get(url).find_all()

