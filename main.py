import logging

from wiktionary import translate
from wordcount import words_by_frequency


def main():
	for word, count in words_by_frequency():
		try:
			stuff = translate(word)
		except Exception:
			logging.exception("Ignored word %r", word)
		else:
			print word.encode("utf8"), count
			# print stuff.encode("utf8")


if __name__ == '__main__':
	logging.basicConfig(level=logging.INFO)
	main()
