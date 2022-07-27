from collections import Counter

from search import *
import heapq
from csp import Relation, CSP


class LCFSFrontier(Frontier):
	"""Implements a frontier appropriate for lowest-cost-first."""

	def __init__(self):
		"""The constructor takes no argument. It initialises the
		container to an empty stack."""
		self.container = []

	# add more code if necessary

	def add(self, path):
		cost = self.cost(path)
		heapq.heappush(self.container, (cost, path))

	def cost(self, path):
		cost = 0
		for arc in path:
			cost += arc.cost
		return cost

	def __iter__(self):
		"""The object returns itself because it is implementing a __next__
		method and does not need any additional state for iteration."""
		return self

	def __next__(self):
		if len(self.container) > 0:
			path = heapq.heappop(self.container)
			return path[1]
		else:
			raise StopIteration  # don't change this one


def select(population, error, max_error, r):
	endlist = []
	running_total = 0
	for var in population:
		running_total += (max_error - error(var))
		endlist.append((var, running_total))

	T = running_total * r
	for var in endlist:
		if var[1] > T:
			return var[0]


def estimate(time, observations, k):
	distance = euclidean_distance
	combine = majority_element
	out = knn_predict(time, observations, distance, combine, k)
	return out


def euclidean_distance(v1, v2):
	total_squared = 0
	if type(v1) == list:
		for i in range(len(v1)):
			total_squared += (v1[i]-v2[i])**2
		return (total_squared)**(1/2)
	else:
		return abs(v1-v2)



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


if __name__ == '__main__':
	observations = [
		(-1, 1),
		(0, 0),
		(-1, 1),
		(5, 6),
		(2, 0),
		(2, 3),
	]

	for time in [-1, 1, 3, 3.5, 6]:
		print(estimate(time, observations, 2))