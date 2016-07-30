import os
import os.path
import urllib
import logging


def lookup(pagename):
	PATH = "./wiktionary_cache/"
	logging.info("Looking up %r", pagename)
	cache_file = os.path.join(PATH, "{}.json".format(pagename.encode("utf8")))
	try:
		with file(cache_file) as f:
			return f.read()
	except IOError:
		data = download_json(pagename)
		with file(cache_file, "w") as f:
			f.write(data)
		return data


def download_json(pagename):
	url = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(urllib.quote(pagename.encode("utf8")))
	logging.info("Downloading %r", url)
	return urllib.urlopen(url).read()
