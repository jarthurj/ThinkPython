def square_root(a, x):
	epilson = 0.0001
	while True:
		y = (x + a / x) / 2
		if abs(y - x) < epilson: break
		x = y
	return y


if __name__ == '__main__':
	print(square_root(25, 12))