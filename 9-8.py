def is_palindrome(number):
	return number == number[::-1]


if __name__=='__main__':
	for x in range(0, 1000000):
		if (is_palindrome(str(x)[2:]) and 
			is_palindrome(str(x + 1)[1:]) and 
			is_palindrome(str(x + 2)[1:5]) and 
			is_palindrome(str(x + 3))):
			print(str(x), str(x+1), str(x+2), str(x+3))