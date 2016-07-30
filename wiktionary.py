import json
import logging
import os
import os.path
import re
import urllib


def translate(word):
	revision = revision_from_page(lookup(word))
	sections = parse_sections(revision)
	german_section = sections["German"]
	meanings = re.findall(ur'^#([^:\*].*)$', german_section, re.M|re.U)
	if not meanings:
		raise ValueError(german_section)
	return u'\n\n'.join(
		meaning.strip()
		for meaning in meanings)


def parse_sections(revision):
	bits = re.split(ur'(?:^|\s)==([^=]+)==(?:$|\s)', revision, re.U)
	return {
		title.strip(): content
		for title, content in
		zip(bits[1::2], bits[2::2])}


def revision_from_page(page):
	data = json.loads(page)
	logging.debug("page for %r is %r", page, data)
	[page_data] = data["query"]["pages"].values()
	[revision_data] = page_data["revisions"]
	return revision_data["*"]


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
	url = "https://en.wiktionary.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(urllib.quote(pagename.encode("utf8")))
	logging.info("Downloading %r", url)
	return urllib.urlopen(url).read()
