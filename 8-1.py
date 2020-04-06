def print_reverse(word):
	for x in range(-1, -len(word) - 1, -1):
		print(word[x])


if __name__ == "__main__":
	print_reverse("assface")