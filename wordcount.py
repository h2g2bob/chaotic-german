from collections import defaultdict
import logging
import operator
import os
import os.path
import re


def words_from_file(f):
	for line in f:
		for word in re.findall(ur'\b\w+\b', line.decode('utf8'), re.U):
			yield word


def words_in_all_files():
	PATH = u"./subtitle_files/"
	for filename in os.listdir(PATH):
		with file(os.path.join(PATH, filename)) as f:
			for word in words_from_file(f):
				yield word


def words_by_frequency():
	words = defaultdict(int)
	for word in words_in_all_files():
		words[word] += 1

	return tuple(sorted(words.items(), key=operator.itemgetter(1), reverse=True))
