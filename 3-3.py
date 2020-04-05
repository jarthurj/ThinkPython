def right_justify(s):
	spaces = 70 - len(s)
	print(str(range(0, spaces + 1)) + s)



if __name__ == "__main__":
	right_justify("butts")