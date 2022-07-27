import re


def clauses(knowledge_base):
	"""Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 2 Aug 2021

    """
	ATOM = r"[a-z][a-zA-Z\d_]*"
	HEAD = rf"\s*(?P<HEAD>{ATOM})\s*"
	BODY = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
	CLAUSE = rf"{HEAD}(:-{BODY})?\."
	KB = rf"^({CLAUSE})*\s*$"

	assert re.match(KB, knowledge_base)

	for mo in re.finditer(CLAUSE, knowledge_base):
		yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")


def forward_deduce(kb):
	kb = list(clauses(kb))
	derived = set()
	tderived = 0
	while tderived != derived:
		tderived = derived.copy()
		for pred in kb:
			if all([atom in derived for atom in pred[1]]):
				derived.add(pred[0])
	return derived


def construct_perceptron(weights, bias):
	"""Returns a perceptron function using the given paramers."""

	def perceptron(input):
		tot = 0
		for i in range(len(input)):
			tot += weights[i] * input[i]
		tot += bias
		return int(tot >= 0)

	return perceptron  # this line is fine


def max_value(tree):
	if type(tree) != list:
		return tree
	else:
		return max([min_value(X) for X in tree])


def min_value(tree):
	if type(tree) != list:
		return tree
	else:
		return min([max_value(X) for X in tree])


if __name__ == '__main__':
	game_tree = [[1, 2], [3]]

	print(min_value(game_tree))
	print(max_value(game_tree))
