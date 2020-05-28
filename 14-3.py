import anagram_sets
import shelve
import os
def store_anagrams(in_dict):
	if not os.path.exists('anagram_shelf.db'):
		s = shelve.open('anagram_shelf.db', 'c')
		for x in in_dict:
			s[x] = in_dict[x]
		s.close()


def read_anagrams(search_key):
	s = shelve.open('anagram_shelf.db')
	print(s[search_key])
	s.close()

if __name__ == '__main__':
	store_anagrams(anagram_sets.anagram_dictionary())

	search_key = ''.join(sorted('stop'))
	read_anagrams(search_key)