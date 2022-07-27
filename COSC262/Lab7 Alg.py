def adjacency_list(graph_str):
    """."""
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

def transpose(adj_list):
    """'"""
    new_list = [[]]*len(adj_list)
    for i in range(len(adj_list)):
        for j in adj_list[i]:
            tup = [(i, j[1])]
            new_list[j[0]] = new_list[j[0]] + tup
    return new_list

def dfs_tree(adj_list, start):
    """'"""
    n = len(adj_list)
    state = [0]*n
    parent = [None]*n
    state[start] = 1
    dfs_loop(adj_list, start, state, parent)
    return parent

def dfs_loop(adj_list, node, state, parent):
    """'"""
    for child in adj_list[node]:
        child = child[0]
        if state[child] == 0:
            state[child] = 1
            parent[child] = node
            dfs_loop(adj_list, child, state, parent)
    state[node] = 1
    
def all_discovered(parent_list):
    """'"""
    output = True
    count = 0
    for i in parent_list:
        if i == None:
            count += 1
    if count >= 2:
        output = False
    return output

def is_strongly_connected(adj_list):
    n = len(adj_list)
    output = True
    for i in range(n):
        if all_discovered(dfs_tree(adj_list, i)) == False:
            output = False
    for j in range(n):
        if all_discovered(dfs_tree(transpose(adj_list), j)) == False:
            output = False
    return output

     """'"""
    done = False
    current = distance.index(max(distance))
    for j in range(len(distance)):
        if distance[j] <= distance[current] and in_tree[j] == False:
            current = j
    return current
        
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
    return (parent, distance)
    
def distance_matrix(adj_list):
    """'"""
    n = len(adj_list)
    table = [n * [float('inf')] for row in range(len(adj_list))]
    for row in range(n):
        table[row][row] = 0
        for i in adj_list[row]:
            table[row][i[0]] = i[1]
    return table

import copy

def floyd(distance):
    """'"""
    table = copy.deepcopy(distance)
    n = len(distance)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if table[i][j] > table[i][k] + table[k][j]:
                    table[i][j] = table[i][k] + table[k][j]
    return table
            


def permutations(s):
    solutions = []
    dfs_backtrack((), s, solutions)
    return solutions


def dfs_backtrack(candidate, input_data, output_data):
    if should_prune(candidate):
        return
    if is_solution(candidate, input_data):
        add_to_output(candidate, output_data)
    else:
        for child_candidate in children(candidate, input_data):
            dfs_backtrack(child_candidate, input_data, output_data)

    
def add_to_output(candidate, output_data):
    output_data.append(candidate)

    
def should_prune(candidate):
    return False

