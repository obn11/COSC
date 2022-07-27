import random


def is_valid_expression(object, function_symbols, leaf_symbols):
	booly = False
	if type(object) == int or object in leaf_symbols:
		booly = True
	elif type(object) != list or len(object) != 3 or object[0] not in function_symbols:
		pass
	elif (type(object[1]) == int or object[1] in leaf_symbols) and (type(object[2]) == int or object[2] in leaf_symbols):
		booly = True
	else:
		booly = is_valid_expression(object[1], function_symbols, leaf_symbols) and is_valid_expression(object[2], function_symbols, leaf_symbols)
	return booly


def depth(expression):
	if type(expression) in [int, str]:
		return 0
	else:
		return max(depth(expression[1]), depth(expression[2])) + 1


def evaluate(expression, bindings):
	if type(expression) is int:
		return expression
	elif type(expression) is str:
		return bindings[expression]
	elif type(expression) is list and len(expression) == 3:
		return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))


def random_expression(function_symbols, leaves, max_depth):
	if random.randint(0, 1) == 1 or max_depth <= 0:
		return random.choice(leaves)
	else:
		return [random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth-1), random_expression(function_symbols, leaves, max_depth-1)]


def generate_rest(initial_sequence, expression, length):
	listy = []
	i = len(initial_sequence)
	n = len(initial_sequence)
	bindings = {'i': i, 'x': initial_sequence[i-2], 'y': initial_sequence[i-1], '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
	while len(listy) < length:
		t = evaluate(expression, bindings)
		listy.append(t)
		i += 1
		bindings['i'] = i
		bindings['x'] = bindings['y']
		bindings['y'] = listy[i-1-n]
	return listy


def predict_rest(sequence):
	done = False
	test_sequence_init = sequence[0:2]
	test_sequence_rest = sequence[2:]
	while not done:
		expression = random_expression(['+', '-', '*'], ['x', 'y', 'i'] + list(range(-2, 3)), 3)
		rest = generate_rest(test_sequence_init, expression, len(test_sequence_rest))
		if rest == test_sequence_rest:
			print("Expression: " + str(expression))
			done = True
	return generate_rest(sequence, expression, 5)


if __name__ == '__main__':
	sequence = [0, -1, 1, 0, 1, -1, 2, -1]
	print(predict_rest(sequence))


def check_diversity(expressions, max_depth):
	d = [0]*max_depth
	for i in expressions:
		d[depth(i)] += 1
	print(d)