def check_fermat(a, b, c, n):
	if a ** n + b ** n == c ** n and n > 2:
		print("holy smokes fermat was wrong")
	else:
		print('NEIN!')

if __name__ == '__main__':
	a = int(input("a?"))
	b = int(input("b?"))	
	c = int(input("c?"))	
	n = int(input("n?"))	

	check_fermat(a, b, c, n)