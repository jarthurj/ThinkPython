def is_triangle(a, b, c):
	if a + b < c or c + b < a or c + a < b:
		print("NO")
	elif a + b == c or c + b == a or c + a == b:
		print("Degenerate")
	else:
		print("YES")


if __name__ == '__main__':
	A = int(input("A?"))
	B = int(input("B?"))
	C = int(input("C?"))

	is_triangle(A, B, C)