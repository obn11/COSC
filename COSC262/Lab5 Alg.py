class Item:
    """An item to (maybe) put in a knapsack"""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        
    def __repr__(self):
        return f"Item({self.value}, {self.weight})"


def max_value2(items, capacity):
    """'"""
    n_cols = capacity
    n_rows = len(items)
    table = [(n_cols+2) * [[0, []]] for row in range(n_rows)]
    for i in range(n_rows):  # For each row
        for c in range(n_cols+2):   # For each column  
            if c == 0:
                table[i][c] = [0, []]
            elif items[i].weight >= c:
                temp = table[i-1][c]
                table[i][c] = temp
            else:
                ignore = table[i-1][c]
                valuet = items[i].value + table[i-1][c - items[i].weight][0]
                if valuet > ignore[0]:
                    temp = []
                    temp.append(valuet)
                    temp2 = [items[i]]
                    if table[i-1][c - items[i].weight][1] != []:
                        temp2 += table[i-1][c - items[i].weight][1]
                    temp.append(temp2)           
                    table[i][c] = temp
                else:
                    table[i][c] = ignore
    best = max(table[n_rows-1][col] for col in range(n_cols+2))
    best = tuple(best)
    return best
    
def my_max(list1, list2):
    """helper for max_value2"""
    if list1[0] > list2[0]:
        return list1
    else:
        return list2
    
    
    
            
def max_value(items, capacity, array=None, i=0):
    """'"""
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

def print_table(table):
    """Pretty(ish) print of table, row by row"""
    n_rows = len(table)
    n_cols = len(table[0])
    for i in range(n_rows):
        print(f"{i}:", end='')
        for j in range(n_cols):
            print(f"{table[i][j]:5}", end='')
        print() # Line break between rows
        
#n_rows = len(items)
#for i in range(n_rows, -1, -1):
#    print(i)

def table_print(table):
    """'"""
    for i in table:
        print(i)

def lcs(s1, s2, i=None, j=None, array=None):
    """'"""
    if i == None:
        i = len(s1)-1
        j = len(s2)-1
        array = {}
    if (i, j) in array:
        return array[(i, j)]
    if i == -1:
        result = ""
    elif j == -1:
        result = ""
    else:
        if s1[i] == s2[j]:
            end = s2[j]
            result = lcs(s1, s2, i-1, j-1, array) + end
        else: #ending string is different
            drop1 = lcs(s1, s2, i-1, j, array)
            drop2 = lcs(s1, s2, i, j-1, array)
            if len(drop1) > len(drop2):
                result = drop1
            else:
                result = drop2
    array.update({(i, j): result})
    return result

def longest_common_subsequence(list1, list2, i=None, j=None, array=None):
    """'"""
    if i == None:
        i = len(list1)-1
        j = len(list2)-1
        array = {}
    if (i, j) in array:
        return array[(i, j)]
    if i == -1:
        result = []
    elif j == -1:
        result = []
    else:
        if list1[i] == list2[j]:
            end = list2[j]
            result = longest_common_subsequence(list1, list2, i-1, j-1, array) + [end]
        else: #ending string is different
            drop1 = longest_common_subsequence(list1, list2, i-1, j, array)
            drop2 = longest_common_subsequence(list1, list2, i, j-1, array)
            if len(drop1) > len(drop2):
                result = drop1
            else:
                result = drop2
    array.update({(i, j): result})
    return result
    
    
list1 = [1, -1, 3, 5, 7, 9, 5, 3, 2, 11]
list2 = [1, -1, 3, 5, 7, 9, 5, 3, 2, 11]
print(longest_common_subsequence(list1, list2))