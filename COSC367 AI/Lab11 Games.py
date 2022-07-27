import math


def min_value(tree):
	if type(tree) != list:
		return tree
	else:
		return min([max_value(item) for item in tree])


def min_action_value(tree):
	if type(tree) != list:
		return None, tree
	else:
		listy = [max_value(item) for item in tree]
		value = min(listy)
		action = listy.index(value)
		return action, value


def max_value(tree):
	if type(tree) != list:
		return tree
	else:
		return max([min_value(item) for item in tree])


def max_action_value(tree):
	if type(tree) != list:
		return None, tree
	else:
		listy = [min_value(item) for item in tree]
		value = max(listy)
		action = listy.index(value)
		return action, value


def minimax(position, depth, maximizing, alpha=-math.inf, beta=math.inf):
	if depth == 0:
		return evalu(position)
	if type(position) != list:
		return position
	if maximizing:
		maxi = -math.inf
		for child in position:
			tmax = minimax(child, depth-1, False, alpha, beta)
			maxi = max(tmax, maxi)
			alpha = max(alpha, tmax)
			if beta <= alpha:
				break
		return maxi
	else:
		mini = math.inf
		for child in position:
			tmin = minimax(child, depth - 1, True, alpha, beta)
			mini = min(tmin, mini)
			beta = min(beta, tmin)
			if beta <= alpha:
				break
		return mini


def evalu(position):
	return 0


if __name__ == '__main__':
	game_tree = [1, 2, [3]]

	value = minimax(game_tree, 100, False)
	print("Best action if playing min:")
	print("Worst guaranteed utility:", value)
	print()
	value = minimax(game_tree, 100, True)
	print("Best action if playing max:")
	print("Best guaranteed utility:", value)