import csv
import logging

from wiktionary import translate
from wordcount import words_by_frequency


def de_and_eng():
	for word, count in words_by_frequency():
		if count < 7:
			logging.info("skipping %r (%d)", word, count)
			# skip infrequently used words
			continue

		try:
			stuff = translate(word)
		except Exception:
			logging.exception("Ignored word %r", word)
		else:
			# print word.encode("utf8"), count
			# print stuff.encode("utf8")
			yield word.encode("ascii", "xmlcharrefreplace"), stuff.encode("ascii", "xmlcharrefreplace").replace("\n", "<br>")

def main():
	with open("chaotic_german.csv", "w") as f:
		for de, eng in de_and_eng():
			f.write("{}\t{}\n".format(
				de.replace("\n", " ").replace("\t", " "),
				eng.replace("\n", " ").replace("\t", " ")))


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	main()
