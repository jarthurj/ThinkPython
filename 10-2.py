def capitalize_all(listOfWords):
	bigres = list()
	for x in listOfWords:
		res = list()
		for y in x:
			res.append(y.upper())
		bigres.append(res)
	return bigres


if __name__ == '__main__':
	words = [["butt", "ass", 'poop'], ["shit"]]
	print(capitalize_all(words))