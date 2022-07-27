def joint_prob(network, assignment):
	# If you wish you can use the following template

	p = 1  # p will enentually hold the value we are interested in
	for var in network:
		ls = []
		parents = network[var].get('Parents')
		if parents:
			for var2 in parents:
				ls.append(assignment.get(var2))
			temp_p = network[var].get('CPT').get(tuple(ls))
		else:
			temp_p = network[var].get('CPT').get(())
		if not assignment.get(var):
			temp_p = 1 - temp_p
		p *= temp_p
	return p


network = {
	'Y': {
		'Parents': [],
		'CPT':     {
			(): (4+2)/(7+4)
		}},

	'X1': {
		'Parents': ['Y'],
		'CPT':     {
			(True,):  (1+2)/(4+4),
			(False,): (3+2)/(3+4),
		}},

	'X2': {
		'Parents': ['Y'],
		'CPT':     {
			(True,):  (1+2)/(4+4),
			(False,): (2+2)/(3+4),
		}},

	'X3': {
		'Parents': ['Y'],
		'CPT':     {
			(True,):  (0 + 2) / (4 + 4),
			(False,): (0 + 2) / (3 + 4),
		}},
}


def posterior(prior, likelihood, observation):
	P = prior
	for i in range(0, len(likelihood)):
		Pi = likelihood[i][True]
		if not observation[i]:
			P = 1 - Pi
		P *= Pi
	return P
#0.013403240035287513
#0.12700449005772932


prior = 0.05
likelihood = ((0.001, 0.3), (0.05, 0.9), (0.7, 0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))