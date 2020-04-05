def do_n(f, n, s):
	if n <= 1:
		return f(s)
	else:
		f(s)
		return do_n(f, n-1, s)


if __name__ == '__main__':
	do_n(print, 5, 'spam')