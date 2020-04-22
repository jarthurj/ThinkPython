import time

known = {'00': 1}

def ack(m, n):
	if m == 0:
		return n + 1
	if m > 0 and n == 0:
		return ack(m - 1, 1)
	if m > 0 and n > 0:
		return ack(m - 1, ack(m, n - 1))


def ack2(m,n):
	mn_str = str(m) + str(n)
	if mn_str in known:
		return known[mn_str]
	if m == 0:
		known[mn_str] = n + 1
		return n + 1
	if m > 0 and n == 0:
		return ack(m - 1, 1)
	if m > 0 and n > 0:
		return ack(m - 1, ack(m, n - 1))




if __name__ == '__main__':
	n = 4
	m = 4
	start = time.time()
	print(ack(m, n))
	t1 = time.time() - start

	start = time.time()
	print(ack2(m, n))
	t2 = time.time() - start

	print(t1, t2)