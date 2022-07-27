from collections import deque

def format_sequence(converters_info, source_format, destination_format):
    """Take a graph converters_info and return the shortest path from source_format
    to destination_format"""
    adj_list = adjacency_list(converters_info)
    parents = bfs_tree(adj_list, source_format)
    path = shortest_path(parents, source_format, destination_format)
    return path
    
    
    
def adjacency_list(graph_str):
    """Converts a graph string into an adjacency list"""
    lines = process_string(graph_str)
    n = int(lines[0][1])
    table = [[] for row in range(n)]
    if lines[0][0] == 'D':
        listy = type_d(lines,table)
    else: #'u'
        listy = type_u(lines,table)
    return listy
def process_string(graph_str):
    """'"""
    lines = graph_str.splitlines()
    newlist = []
    for line in lines:
        newlist.append(line.split())
    return newlist
def type_u(lines,table):
    """'"""
    index = 1
    if len(lines[0]) == 2:
        while index < len(lines):
            i = int(lines[index][0])
            j = int(lines[index][1])
            tup1 = (j, None)
            table[i].append(tup1)
            tup2 = (i, None)
            table[j].append(tup2)
            index += 1
    else: #weighted
        while index < len(lines):
            i = int(lines[index][0])
            j = int(lines[index][1])
            w = int(lines[index][2])
            tup1 = (j, w)
            table[i].append(tup1)
            tup2 = (i, w)
            table[j].append(tup2)
            index += 1
    return table
def type_d(lines,table):
    """'"""
    index = 1
    if len(lines[0]) == 2:
        while index < len(lines):
            i = int(lines[index][0])
            j = int(lines[index][1])
            tup = (j, None)
            table[i].append(tup)
            index += 1
    else: #weighted
        while index < len(lines):
            i = int(lines[index][0])
            j = int(lines[index][1])
            w = int(lines[index][2])
            tup = (j, w)
            table[i].append(tup)
            index += 1
    return table



def bfs_tree(adj_list, start):
    """Preforms a bfs on a graph"""
    n = len(adj_list)
    state = [0]*n
    parent = [None]*n
    queue = deque()
    queue.append(start)
    state[start] = 1
    return bfs_loop(adj_list, queue, state, parent)
def bfs_loop(adj_list, queue, state, parent):
    """'"""
    while len(queue) != 0:
        node = queue.popleft()
        for child in adj_list[node]:
            child = child[0]
            if state[child] == 0:
                state[child] = 1
                parent[child] = node
                queue.append(child)
        state[node] = 2
    return parent

def shortest_path(parent, s, t):
    """finds shortest path between 2 nodes, s and t, using a parent array"""
    if s == t:
        return [s]
    else:
        if parent[t] == None:
            return "No solution!"
        else:
            return shortest_path(parent, s, parent[t]) + [t]
    
    
    
    
def bubbles(physical_contact_info):
    """seporates a graph into components"""
    adj = adjacency_list(physical_contact_info)
    bubble = components(adj)
    return bubble
    
    
def components(adj):
    """'"""
    n = len(adj)
    state = [0]*n 
    q = deque() 
    components = []
    for i in range(n):
        if state[i] == 0:
            previous = []
            for item in state:
                previous.append(item)
            state[i] = 1
            q.append(i)
            state, q = bfs_loop2(adj, q, state)
            new_component = []
            for j in range(len(state)):
                if previous[j] != state[j]:
                    new_component.append(j)
            components.append(new_component)
    return components
def bfs_loop2(adj_list, queue, state):
    """'"""
    while len(queue) != 0:
        node = queue.popleft()
        for child in adj_list[node]:
            child = child[0]
            if state[child] == 0:
                state[child] = 1
                queue.append(child)
        state[node] = 2
    return state, queue

def starting_order(dependencies):
    """returns a valid topological ordering of a graph"""
    adj = adjacency_list(dependencies)
    topo = topological(adj)
    return topo

def topological(adj):
    """'"""
    n = len(adj)
    state = [0]*n
    parent = [None]*n
    s = []
    for i in range(n):
        if state[i] != 2:
            state[i] = 1
            dfs_loop2(adj, i, state, parent, s)
    s.reverse()
    return s


def dfs_loop2(adj_list, node, state, parent, s):
    """'"""
    for child in adj_list[node]:
        child = child[0]
        if state[child] == 0:
            state[child] = 1
            parent[child] = node
            dfs_loop2(adj_list, child, state, parent, s)
    state[node] = 2
    s.append(node)
    
def which_walkways(campus_map):
    """Returns the minimum spanning tree of a graph to represent the least amount
    of lamps that could be lit and still have a connected campus."""
    adj = adjacency_list(campus_map)
    parent = prim(adj, 0)
    min_tree = prims(parent)
    return min_tree

def prim(adj, s):
    """'"""
    n = len(adj)
    in_tree = [False]*n
    distance = [float('inf')]*n
    parent = [None]*n
    distance[s] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj[u]:
            if in_tree[v] == False and weight < distance[v]:
                distance[v] = weight
                parent[v] = u
    return parent

def prims(parent):
    """'"""
    listy = []
    for i in range(len(parent)):
        if parent[i] != None:
            if parent[i] > i:
                tup = (i, parent[i])
            else:
                tup = (parent[i], i)
            listy.append(tup)
    return listy
    
    
def next_vertex(in_tree, distance):
    """'"""
    done = False
    current = distance.index(max(distance))
    for j in range(len(distance)):
        if distance[j] <= distance[current] and in_tree[j] == False:
            current = j
    return current

def maximum_energy(city_map, depot_position):
    """Returns the energy required for a return trip to the furthest point
    and back"""
    adj = adjacency_list(city_map)
    distance = dijkstra(adj, depot_position)
    dist2 = []
    for i in range(len(distance)):
        if distance[i] == float('inf'):
            dist2.append(-1)
        else:
            dist2.append(distance[i])
    largest = max(dist2)
    return largest * 2
                  
                        
                        
def dijkstra(adj_list, start):
    """'"""
    n = len(adj_list)
    in_tree = [False]*n
    distance = [float('inf')]*n
    parent = [None]*n
    distance[start] = 0
    while not all(in_tree):
        u = next_vertex(in_tree, distance)
        in_tree[u] = True
        for v, weight in adj_list[u]:
            if in_tree[v] == False and distance[u] + weight < distance[v]:
                distance[v] = distance[u] + weight
                parent[v] = u
    return distance


city_map = """\
U 4 W
0 2 5
0 3 2
3 2 2
"""

print(maximum_energy(city_map, 0))
print(maximum_energy(city_map, 1))
print(maximum_energy(city_map, 2))