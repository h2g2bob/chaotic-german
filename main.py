import logging

from wiktionary import lookup
from wordcount import words_by_frequency

def main():
	for word, count in words_by_frequency():
		print word.encode("utf8"), count
		print lookup(word)

if __name__ == '__main__':
	logging.basicConfig(level=logging.DEBUG)
	main()
