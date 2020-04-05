def eval_loop():
	eval_in = input()
	while eval_in != 'done':
		print(eval(eval_in))
		eval_in = input()

def eval_loop_rec():
	eval_in = input()
	if eval_in == 'done'
		return None
	print(eval(eval_in))
	eval_loop_rec()


if __name__ == '__main__':
	eval_loop()