"""A broken implementation of a recursive search for the optimal path through
   a grid of weights.
   Richard Lobb, January 2019.
"""
INFINITY = float('inf')

def read_grid(filename):
    """Read from the given file an n x m grid of integer weights.
       The file must consist of n lines of m space-separated integers.
       n and m are inferred from the file contents.
       Returns the grid as an n element list of m element lists.
       THIS FUNCTION DOES NOT HAVE BUGS.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid



    

    
def file_cost(filename):
    """The cheapest cost from row 1 to row n (1-origin) in the grid of integer
       weights read from the given file
    """
    return print(grid_cost2(read_grid(filename)))



def print_table(table):
    """Pretty(ish) print of table, row by row"""
    n_rows = len(table)
    n_cols = len(table[0])
    for i in range(n_rows):
        print(f"{i}:", end='')
        for j in range(n_cols):
            print(f"{table[i][j]:5}", end='')
        print() # Line break between rows
    
def grid_cost(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    cost_cache = {}
    n_rows = len(grid)
    n_cols = len(grid[0])
    
    def cell_cost(row, col):
        """The cost of getting to a given cell in the current grid."""
        if (row, col) in cost_cache:
            return cost_cache[(row, col)]
        else:
            if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
                cost_cache[(row, col)] = INFINITY
                return INFINITY  # Off-grid cells are treated as infinities
            else:
                cost = grid[row][col]
                if row != 0:
                    cost += min(cell_cost(row - 1, col + delta_col) for delta_col in range(-1, 2))
                cost_cache[(row, col)] = cost
                return cost
            
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best


def grid_cost2(grid):
    """The cheapest cost from row 1 to row n (1-origin) in the given
       grid of integer weights.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])
    table = [n_cols * [0] for row in range(n_rows)]
    for row in range(n_rows):  # For each row
        for col in range(n_cols):   # For each column            
            if row == 0:
                table[row][col] = grid[row][col]
            else:
                if col - 1 < 0:
                    last = [table[row - 1][col], table[row - 1][col + 1]]
                elif col + 1 > n_cols - 1:
                    last = [table[row - 1][col - 1], table[row - 1][col]]
                else:
                    last = [table[row - 1][col - 1], table[row - 1][col], table[row - 1][col + 1]]
                table[row][col] = grid[row][col] + min(last)
    best = min(table[n_rows-1][col] for col in range(n_cols))
    return best

def coins_reqd(value, coinage):
    """A version that doesn't use a list comprehension""" 
    numCoins = [[]] * (value + 1)
    for amt in range(1, value + 1):
        minimum = 0
        for c in coinage:
            if amt >= c:
                coin_count = my_sum(numCoins[amt - c])  # Num coins required to solve for amt - c
                if minimum == 0 or coin_count < my_sum(minimum[0]):
                    mini = numCoins[amt - c]
                    minimum = (mini, c)
        done = False
        i = 0
        while not done:
            if i >= len(minimum[0]):
                temp = []
                for q in range(len(minimum[0])):
                    temp.append(minimum[0][q])
                temp.append((minimum[1], 1))
                numCoins[amt] = temp
                done = True            
            elif minimum[0][i][0] == minimum[1]:
                temp = []
                for q in range(len(minimum[0])):
                    if q == i:
                        temp.append((minimum[0][i][0], minimum[0][i][1] + 1))
                    else:
                        temp.append(minimum[0][q])
                numCoins[amt] = temp
                done = True
            i += 1
    answer = my_sort(numCoins[value])
    return answer

def my_sum(tuplist):
    """helper"""
    tot = 0
    if tuplist is [] or 0:
        return 0
    else:
        for n in tuplist:
            tot += n[1]
        return tot
    
def my_sort(tuplist):
    """helper"""
    maxi = (0, 0)
    newlist = []
    done = False
    while not done:
        for q in tuplist:
            if q[0] > maxi[0]:
                maxi = q
        if maxi in tuplist:
            tuplist.remove(maxi)
            newlist.append(maxi)
        if len(tuplist) == 0:
            done = True
        else:
            maxi = (0, 0)
    return newlist
        
    

import sys
sys.setrecursionlimit(2000)

class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"


def max_value(items, capacity, array=None, i=0):
    if array == None:
        array = {}
    if (i, capacity) in array:
        return array[(i, capacity)]
    if i == len(items) or capacity == 0:
        result = 0
    elif items[i].weight > capacity:
        result = max_value(items, capacity, array, i+1)
    else:
        ignore = max_value(items, capacity, array, i+1)
        take = items[i].value + max_value(items, capacity - items[i].weight, array, i+1)
        result = max(ignore, take)
    array.update({(i, capacity): result})
    return result
        
items = [
    Item(45, 3),
    Item(45, 3),
    Item(80, 4),
    Item(80, 5),
    Item(100, 8)]

