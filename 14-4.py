import os


def walk(dirname):
	"""
	dirname: top of directory that is being searched
	"""
	try:
		dir_list = os.listdir(dirname)
	except:
		return []
	files_and_dirs = []
	# print(dirname)
	for thing in dir_list:
		print(thing)
		if os.path.isfile(os.path.join(dirname, thing)):
			files_and_dirs.append(thing)
		else:
			files_and_dirs.extend(walk(os.path.join(dirname,thing)))
	print(dirname)
	return files_and_dirs

def filter(in_list):
	out_list = []
	for x in in_list:
		if x[-4:] == '.txt':
			out_list.append(x)
	return out_list


if __name__ == '__main__':
	# print(walk("C:\\Users\\Johnny"))
	print(filter(walk("C:\\Users\\Johnny")))


