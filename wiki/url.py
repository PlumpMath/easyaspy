import urllib.parse as _parse

def get(stub):
	return "https://en.wikipedia.org/wiki/{0}".format(stub)

def to_title(url):
	"https://wikipedia.org/wiki/Mathematics/ -> Mathematics"
	return _parse.unquote(url.split('/wiki/')[-1].split('#')[0]).replace("_"," ")

def from_title(title):
	"Mathematics -> https://en.wikipedia.org/wiki/Special:Export/Mathematics"
	return get("Special:Export/{0}".format(_parse.quote(title.replace(" ","_"))))

def identify(url):
	"https://wikipedia.org/wiki/Some_Article -> True"
	return 'wikipedia.org' in url[:30]

