import statistics
from collections import Counter
from itertools import product
from math import isclose

def euclidean_distance(v1, v2):
	total_squared = 0
	for i in range(len(v1)):
		total_squared += (v1[i]-v2[i])**2
	return (total_squared)**(1/2)


def majority_element(labels):
	count = Counter()
	for element in labels:
		count[element] += 1
	return max(count, key=count.get)


def knn_predict(input, examples, distance, combine, k):
	k_nearist = []
	for ex in examples:
		dist = distance(input, ex[0])
		if len(k_nearist) < k:
			k_nearist.append((ex, dist))
		elif dist == max(neigh[1] for neigh in k_nearist):
			k_nearist.append((ex, dist))
		elif dist < max(neigh[1] for neigh in k_nearist):
			td = max(neigh[1] for neigh in k_nearist)
			for i in range(len(k_nearist)-1, -1, -1):
				if k_nearist[i][1] == td:
					k_nearist.pop(i)
			k_nearist.append((ex, dist))

	combinable = [item[0][1] for item in k_nearist]
	return combine(combinable)


def construct_perceptron(weights, bias):
	"""Returns a perceptron function using the given paramers."""

	def perceptron(input):
		a = 0
		for i in range(len(input)):
			a += (input[i]*weights[i])
		a += bias
		return int(a >= 0)

	return perceptron


def accuracy(classifier, inputs, expected_outputs):
	accu_list = []
	for i in range(len(inputs)):
		accu_list.append(classifier(inputs[i]) == expected_outputs[i])
	return sum(accu_list)/len(accu_list)


def accuracy(classifier, inputs, expected_outputs):
	return statistics.mean([classifier(inputs[i]) == expected_outputs[i] for i in range(len(inputs))])


def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
	n = len(weights)
	for _ in range(max_epochs):
		for i in range(len(training_examples)):
			pattern = training_examples[i][0]
			output = construct_perceptron(weights, bias)(pattern)
			target = training_examples[i][1]
			for j in range(n):
				weights[j] = weights[j] + (learning_rate*pattern[j]*(target-output))
			bias = bias + learning_rate*(target-output)
	return (weights, bias)


if __name__ == '__main__':
	weights = [2, -4]
	bias = 0
	learning_rate = 0.5
	examples = [
		((0, 0), 0),
		((0, 1), 1),
		((1, 0), 1),
		((1, 1), 0),
	]
	max_epochs = 50

	weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
	print(f"Weights: {weights}")
	print(f"Bias: {bias}\n")