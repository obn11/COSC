def load_file(file_name):
    """ Reads integers from a file.
    The file should have one integer per line """
    with open(file_name) as infile:
        integers = [int(line) for line in infile.read().splitlines()]
    return integers

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

def memoize(input1, input2, array=None, i=0, j=0):
    """general memoized form of a recursive function.
    with i and j representing how the recursion is traversed. Inputs are 
    lists in this case"""
    if array == None:
        array = {}
    if (i, j) in array:
        return array[(input1[i], input2[j])]
    if basecase == True:
        result = basevalue 
    else:
        #recursion
        result = memoize(input1[i+1], input2[j+1], array)
    array.update({(i, j): result})
    return result

def bottum_up_dp(input1, input2):
    """how a 2d table is set up and used for dp. input1 is a list, input 2 an int"""
    n_cols = len(input1)
    n_rows = input2
    table = [n_cols * [0] for row in range(n_rows)]
    for row in range(n_rows):  # For each row
        for col in range(n_cols):   # For each column      
            #'recursion'
            if basecase == True:
                table[row][col] = basevalue
            else:
                option1 = table[row+change][col]
                option2 = value + table[row+change][col-change]
                table[row][col] = best(option1, option2)
    best = best(table[n_rows-1][col] for col in range(n_cols))
    return best
                
def print_table(table):
    """Pretty(ish) print of table, row by row"""
    n_rows = len(table)
    n_cols = len(table[0])
    for i in range(n_rows):
        print(f"{i}:", end='')
        for j in range(n_cols):
            print(f"{table[i][j]:5}", end='')
        print() # Line break between rows