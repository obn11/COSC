from pprint import pprint
from collections import deque

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


def bfs_tree(adj_list, start):
    """'"""
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
    

    
#
    


def path_length(parent, start, end, length=0):
    """'"""
    if end == start:
        return 0
    if parent[end] == start:
        length += 1
        return length
    else:
        children = []
        for i in range(len(parent)):
            if parent[i] == start:
                children.append(i)
        if len(children) == 0:
            result = float('inf')
        else:
            result = min(path_length(parent, q, end, length+1) for q in children)
        return result
  
  
def reaching_vertices(adj_list, target):
    lst = []
    lst.append(target)
    for i in range(len(adj_list)):
        parent = bfs_tree(adj_list, i)
        if parent[target] != None:
            lst.append(i)
    return lst

def dfs_loop2(adj_list, node, state, parent, stack):
    """'"""
    for child in adj_list[node]:
        child = child[0]
        if state[child] == 0:
            state[child] = 1
            parent[child] = node
            dfs_loop2(adj_list, child, state, parent, stack)
    state[node] = 2
    stack.append(node)
    return state, stack

graph_string = """\
D 6
1 2
1 4
1 3
2 4
2 5
4 5
5 0
0 3
"""

adj_list = adjacency_list(graph_string)
print(dfs_loop2(adj_list, 1, [2,0,0,2,0,0], [None, None, None, None, None, None], [3, 0]))