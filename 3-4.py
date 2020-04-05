def do_twice(f, s):
	f(s)
	f(s)

def print_twice(s):
	print(s)
	print(s)

def do_four(f, s):
	do_twice(f, s)
	do_twice(f, s)
if __name__ == '__main__':
	do_twice(print_twice, 'spam')
	print(" ")
	do_four(print, 'spam')
