from search import *
import math
import heapq

MOVE_COST = 5
GUESSING = True


class RoutingGraph(Graph):

	def __init__(self, graph_str):
		graph = graph_str.strip('\t').splitlines()
		for i, row in enumerate(graph):
			graph[i] = row.strip('\t')
		self.graph = graph
		s_nodes = []
		g_nodes = []
		nrows = len(self.graph)
		ncols = len(self.graph[1])
		row = 1
		col = 0
		while row < nrows - 1:
			while col < ncols - 1:
				test = self.graph[row][col]
				if test == "S":
					s_nodes.append((row, col, math.inf))
				elif test.isdigit():
					s_nodes.append((row, col, int(test)))
				elif str(test) == 'G':
					g_nodes.append((row, col))
				col += 1
			row += 1
			col = 1
		self.s_nodes = s_nodes
		self.goals = g_nodes

	def starting_nodes(self):
		return self.s_nodes

	def estimated_cost_to_goal(self, node):
		if not GUESSING:
			return 0
		# Manhattan Distance
		row, col, _ = node
		dists = []
		for goal in self.goals:
			grow, gcol = goal
			dists.append(abs(grow - row) + abs(gcol - col))
		return min(dists)*MOVE_COST

	def is_goal(self, node):
		row, col, _ = node
		return str(self.graph[row][col]) == "G"

	def outgoing_arcs(self, tail_node):
		out = []
		row, col, fuel = tail_node
		if fuel > 0:
			dirs = [('N', -1, 0),
			        ('E', 0, 1),
			        ('S', 1, 0),
			        ('W', 0, -1)]
			block_symbols = ["X", "|", "-", "+"]
			for direction in dirs:
				action, drow, dcol = direction
				if self.graph[row + drow][col + dcol] not in block_symbols:
					out.append(Arc(tail=tail_node, head=(row + drow, col + dcol, fuel - 1), action=action, cost=5))
		if self.graph[row][col] == 'F' and fuel < 9:
			out.append(Arc(tail=tail_node, head=(row, col, max(fuel, 9)), action="Fuel up", cost=15))
		return out

	def __str__(self):
		tstr = ''
		for line in self.graph:
			tstr += line + '\n'
		return tstr


class AStarFrontier(Frontier):

	def __init__(self, graph):
		"""The constructor takes no argument. It initialises the
		container to an empty heap."""
		self.heap = []
		self.item_num = 0
		self.graph = graph
		self.expanded = []

	def add(self, path):
		if path[-1].head not in self.expanded:  # pruning
			cost = 0
			for arc in path:
				cost += arc.cost
			cost += self.graph.estimated_cost_to_goal(path[-1].head)
			self.item_num += 1
			add = (cost, self.item_num, path)
			heapq.heappush(self.heap, add)

	def __iter__(self):
		"""The object returns itself because it is implementing a __next__
		method and does not need any additional state for iteration."""
		return self

	def __next__(self):
		if self.heap:
			path = heapq.heappop(self.heap)[-1]
			if path[-1].head not in self.expanded:
				self.expanded.append(path[-1].head)
			return path
		else:
			raise StopIteration


def print_map(map_graph, frontier, solution):
	for node in frontier.expanded:
		if node is not None:
			row, col, _ = node
			if map_graph.graph[row][col] not in ['G', 'S'] and not map_graph.graph[row][col].isdigit():
				tstr = map_graph.graph[row]
				tstr = tstr[:col] + '.' + tstr[col + 1:]
				map_graph.graph[row] = tstr
	if solution is not None:
		for arc in solution:
			row, col, _ = arc.head
			if map_graph.graph[row][col] not in ['G', 'S'] and not map_graph.graph[row][col].isdigit():
				tstr = map_graph.graph[row]
				tstr = tstr[:col] + '*' + tstr[col + 1:]
				map_graph.graph[row] = tstr
	print(map_graph)


if __name__ == '__main__':
	map_str = """\
	+---------+
	|         |
	|    G    |
	|         |
	+---------+
	"""

	map_graph = RoutingGraph(map_str)
	frontier = AStarFrontier(map_graph)
	solution = next(generic_search(map_graph, frontier), None)
	print_map(map_graph, frontier, solution)
