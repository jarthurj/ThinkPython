def hypotenuse(a, b):
	asqr = a ** 2 
	bsqr = b ** 2 
	csqrt = (asqr + bsqr) ** (1/2)
	return csqrt


if __name__ == "__main__":
	A = int(input())
	B = int(input())
	print(hypotenuse(A, B))