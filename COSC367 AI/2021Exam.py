def myLen(tree, leny=0):
	if type(tree) != list:
		return 1
	else:
		for node in tree:
			if type(node) != list:
				leny += 1
			else:
				leny += myLen(node)
		return leny


def num_crossovers(parent_expression1, parent_expression2):
	return myLen(parent_expression1) * myLen(parent_expression2)


def num_parameters(unit_counts):
	sum = 0
	for i in range(len(unit_counts)):
		if i > 0:
			sum += (unit_counts[i-1]+1)*unit_counts[i]
	return sum


if __name__=='__main__':
	print(num_parameters([2, 4, 2]))