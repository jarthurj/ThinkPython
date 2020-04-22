import time

known = {0:0, 1:1}

def fibonacci(n):
	if n in known:
		return known[n]
	res = fibonacci(n-1) + fibonacci(n-2)
	known[n] = res
	return res

def fibonacci2(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fibonacci2(n - 1) + fibonacci2(n - 2)

if __name__ == '__main__':
	n = 35


	start = time.time()
	print(fibonacci(n))
	t1 = time.time() - start
	start = time.time()
	print(fibonacci2(n))
	t2 = time.time() - start

	print(t1, t2)