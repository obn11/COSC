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
	clausi = list(dumpy(kb))
	sety = set({})
	prevSety = set({})
	first = True
	while prevSety != sety or first == True:
		first = False
		prevSety = sety.copy()
		for prop in clausi:
			if len(prop[1]) == 0:
				sety.add(prop[0])
			elif len([True for x in prop[1] if x in sety]) == len(prop[1]):
				sety.add(prop[0])
	return sety


def dumpy(kb):
	return clauses(kb)


def main():
	kb = """
	good_programmer :- correct_code.
	correct_code :- good_programmer.
	"""

	print(", ".join(sorted(forward_deduce(kb))))


if __name__ == '__main__':
	main()

