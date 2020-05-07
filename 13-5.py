import string
import random
def choose_from_hist(l):
	hist = {}
	for x in l:
		hist[x] = hist.get(x, 0) + 1


def punctuation_mapping():
	punc = str.punctuation + '”' + '“' + '—'+ '—'+ '‘' + '’' + '”'
	punc_dict = {}
	for x in punc:
		punc_dict[ord(x)] = None
	return punc_dict