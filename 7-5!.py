import math

def estimate_pi():
	coeff = (2 * math.sqrt(2)) / 9801
	k = 0
	running_total = 0
	while True:
		kth_numerator = math.factorial(4 * k) * (1103 + 26390 * k)
		kth_denominator = (math.factorial(k) ** 4) * 396 ** (4 * k)
		kth =  kth_numerator / kth_denominator
		running_total += kth
		k += 1
		if kth < 1e-15:
			running_total *= coeff
			return 1 / running_total


if __name__ == '__main__':
	print(estimate_pi(), math.pi)