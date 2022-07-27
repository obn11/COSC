from csp import *
import itertools
import copy
from collections import OrderedDict


def generate_and_test(csp):
	names, domains = zip(*csp.var_domains.items())
	for values in itertools.product(*domains):
		assignment = {x: v for x, v in zip(names, values)}
		if all(satisfies(assignment, constraint) for constraint in csp.constraints):
			yield assignment


def arc_consistent(csp):
	csp = copy.deepcopy(csp)
	to_do = {(var, constraint) for constraint in csp.constraints for var in scope(constraint)}
	while to_do:
		var, constraint = to_do.pop()
		other_vars = scope(constraint) - {var}
		new_domain = set()
		for xval in csp.var_domains[var]:
			assignment = {var: xval}
			for yvals in itertools.product(*[csp.var_domains[other_var] for other_var in other_vars]):
				assignment.update({other_var: yval for other_var, yval in zip(other_vars, yvals)})
				if satisfies(assignment, constraint):
					new_domain.add(xval)
					break
		if csp.var_domains[var] != new_domain:
			for other_constraint in set(csp.constraints) - {constraint}:
				if var in scope(other_constraint):
					for other_varE in scope(other_constraint):
						if var != other_varE:
							to_do.add((other_varE, other_constraint))
			csp.var_domains[var] = new_domain
	return csp


if __name__ == '__main__':
	domains = {x: set(range(10)) for x in "twofur"}
	domains.update({'c1': {0, 1}, 'c2': {0, 1}})  # domains of the carry overs

	cryptic_puzzle = CSP(
		var_domains=domains,
		constraints={
		lambda t, f: t != 0 and f != 0,
		lambda t, f, w, o, r, u: len({t, f, w, o, r, u}) == 6,
		lambda o, r, c1: o + o == r + 10 * c1,
		lambda w, u, c1, c2: w + w + c1 == u + 10 * c2,
		lambda t, o, f, c1, c2: t + t + c2 == o + 10 * f
		})

	new_csp = arc_consistent(cryptic_puzzle)
	solutions = []
	for solution in generate_and_test(new_csp):
		solutions.append(sorted((x, v) for x, v in solution.items()
		                        if x in "twofur"))
	print(len(solutions))
	solutions.sort()
	print(solutions[0])
	print(solutions[5])