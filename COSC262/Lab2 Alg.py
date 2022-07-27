def num_rushes(slope_height, rush_height_gain, back_sliding, count=0):
    """'"""
    if slope_height - rush_height_gain <= 0:
        count += 1
        return count
    else:
        count + 1
        slope_height = slope_height + (back_sliding*0.95**(count+1)) - (rush_height_gain*0.95**(count+1))
        return num_rushes(slope_height, rush_height_gain, back_sliding, count)
  
import sys
sys.setrecursionlimit(100000)

def dumbo_func(data, index=0):
    """Takes a list of numbers and does weird stuff with it"""
    if len(data) >= index:
        return 0
    else:
        if (data[index] // 100) % 3 != 0:
            index += 1
            return 1 + dumbo_func(data, index)
        else:
            index += 1
            return dumbo_func(data, index)

def cycle_length(n, count=0):
    """'"""
    if n == 1:
        count += 1
        return count
    else:
        if n % 2 == 0:
            count += 1
            n = n/2
            return cycle_length(n, count)
        
        else: #n is odd
            count += 1
            n = n*3 + 1
            return cycle_length(n, count)
        
def recursive_divide(x, y, count=0):
    """'"""
    if x - y < 0:
        return count
    else:
        x -= y
        count += 1
        return recursive_divide(x, y, count)

def all_pairs(list1, list):
    tuples = []
    for list1_el in list1:
        for list2_el in list2:
            tuples.append((list1_el, list2_el))
    return tuples
    
def all_pairs(list1, list2, index=0, tuples=0):
    """'"""
    if tuples == 0:
        return all_pairs(list1, list2, index, [])    
    if len(tuples) == len(list1) * len(list2):
        return tuples
    else:
        tuples += helper(list1[index], list2, [])
        index += 1
        return all_pairs(list1, list2, index, tuples)
        
    
def helper(list1_el, list2, tuples):
    if len(list2) == 0:
        return tuples
    else:
        tup = (list1_el, list2[0])
        tuples.append(tup)
        return helper(list1_el, list2[1:], tuples)


def my_enumerate(items, index=0, tuples=0):
    """'"""
    if tuples == 0:
        tuples = []
    if index == len(items):
        return tuples
    else:
        tup = (index, items[index])
        index += 1
        tuples.append(tup)
        return my_enumerate(items, index, tuples)
    
def perms(items, index=0):
    """'"""
    print(output)
    if index == len(items):
        return [()]
    else:
        last = perms(items, index + 1)
        print(last)
        output = []
        for i in last:
            tups = helpy(i, items, [])
            output += tups
        return output
            
def helpy(output_el, items, tuples):
    if len(items) == 0:
        return tuples
    else:
        listy = list(output_el)
        listy.append(items[0])
        tup = tuple(listy)
        tuples.append(tup)
        return helper(output_el, items[1:], tuples)
    pass



def perms3(items):
    if len(items) == 0:
        return [()]
    else:
        output = []
        for i in items:
            rest = items
            rest.remove(i)
            other_perms = perms3(rest)
            for q in other_perms:
                temp = [i] + list(q)
                temp = tuple(temp)
                output.append(temp)
        return output
    

  
def perms2(items, r):
    """'"""
    if r == 0:
        return [()]
    else:
        output = []
        last_answer = perms2(items, r-1)
        for tuples in last_answer:
            for number in items:
                temp = list(tuples)
                temp.append(number)
                temp = tuple(temp)
                output.append(temp)
        return output
    
import random
def perms4(items, output=0, factn=0):
    if factn == 0:
        factn = 1
        for i in range(len(items)):
            factn = factn * (i+1)
    if output == 0:
        output = []
    if len(output) == factn:
        return output
    else:
        random.shuffle(items)
        temp = tuple(items)
        print(my_in(temp, output))
        if my_in(temp, output):
            pass
        else:
            tupy = tuple(items)
            output.append(tupy)
            output = sorted(output)
        return perms4(items, output, factn)
    
def my_in(item, item_list):
    found = False
    for i in item_list:
        if i == item:
            found = True
    return found

def combinations(items, r, output=0):
    """'"""
    print(1)
    if output == 0:
        output = []
    if r == 0:
        return [[]]
    else:
        last_answer = combinations(items, r-1, output)
        print(last_answer)
        for tup in last_answer:
            for number in items[:len(items)-r]:
                temp = tuples
                temp = list(temp)
                temp += [number]
                output.append(temp)
        return output
    
    
"""An incomplete Huffman Coding module, for use in COSC262.
   Richard Lobb, 2 March 2020.
"""
import re

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False

class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
            self.left.__repr__(level + 1) + ',\n' +
            self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count)) # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label) # Add this leaf to the graph


class HuffmanTree:
    """Operations on an entire Huffman coding tree.
    """
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root
        
    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        dicti = {}
        binary = ""
        string = ""
        pointer = self.root
        if text == "":
            return ""
        for i in text:
            done = False
            while not done:
                if type(pointer) == Node:
                    pass
                    
    def find(self, letter, string=""):
        """'"""
        pointer = self.root
        if type(pointer) == Leaf:
            if pointer.char == letter:
                return string
            else:
                string = ""
        if type(pointer) == Node:
            find(pointer.right, letter, string+"0")
            find(pointer.left, letter, string+"1")
            return string 
            
        
    def decode(self, binary):
        """Return the text string that corresponds the given binary string of
           0s and 1s
        """
        string = ""
        done = False
        pointer = self.root
        i = 0
        if binary == "":
            return ""
        while not done:
            if done  == 'almost':
                done = True
            if i == len(binary):
                done = 'almost'
            if type(pointer) == Leaf:
                string += pointer.char
                pointer = self.root 
            if type(pointer) == Node:
                if binary[i] == '0':
                    pointer = pointer.left
                else: #binary[i] == 1
                    pointer = pointer.right
                i += 1
        return string
                
            

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        self.root = None          # *** FIXME ***
        raise NotImplementedError # *** TO BE IMPLEMENTED

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', 'Node(', s)
        self.root = eval(s)


def main():
    """ Demonstrate defining a Huffman tree from its string representation and
        printing and plotting it (if plotting is enabled on your machine).
    """
    tree = HuffmanTree()
    tree_string = """Node(42,
      Node(17,
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(25,
        Node(10,
          Node(5,
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c')))
    """
    tree.build_from_string(tree_string)
    print(tree)
    tree.plot()
    
    # Or you can build the tree directly
    tree2 = HuffmanTree(Node(
      Node(
        Leaf(8, 'b'),
        Leaf(9, 'a')),
      Node(
        Node(
          Node(
            Leaf(2, 'f'),
            Leaf(3, 'd')),
          Leaf(5, 'e')),
        Leaf(15, 'c'))))
    print(tree2)
    tree2.plot()
    
#main()

tree = HuffmanTree(Node(
  Node(
    Leaf(8, 'b'),
    Leaf(9, 'a')),
  Node(
    Node(
      Node(
        Leaf(2, 'f'),
        Leaf(3, 'd')),
      Leaf(5, 'e')),
    Leaf(15, 'c'))))


def fractional_knapsack(capacity, items):
    """'"""
    items = my_sort_f(items)
    i = 0
    value = 0
    done = False
    while not done:
        if i == len(items):
            done = True        
        elif capacity - items[i][2] >= 0:
            value += items[i][1]
            capacity -= items[i][2] 
            i += 1
        else:
            fract = capacity / items[i][2]
            value += (fract*items[i][1])
            i += 1
            done = True
        if i == len(items):
            done = True
    return float(value)
    
def my_sort_f(items):
    """helpy"""
    listy = []
    done = False
    while not done:
        if len(items) > 0:
            maxi = items[0][1]/items[0][2]
            i = 0
            x = 0
            while i < len(items):
                if maxi < items[i][1]/items[i][2]:
                    maxi = items[i][1]/items[i][2]
                    x = i
                i += 1
            listy.append(items.pop(x))
        if len(items) == 0:
            done = True
    return listy

num_calls = 0  # Global counter of mat_mul calls

def mat_mul(m1, m2):
    """Return m1 * m2 where m1 and m2 are square matrices of numbers, represented
       as lists of lists.
    """
    global num_calls # Counter of calls (for marking)
    num_calls += 1   # Increment the count of calls
    n = len(m1)    # Size of the matrix
    assert len(m1[0]) == n and len(m2) == n and len(m2[0]) == n
    mprod = [[sum(m1[i][k] * m2[k][j] for k in range(n)) for j in range(n)]
        for i in range(n)]
    return mprod

def mat_power(m, p):
    """return m ^ p where m is a square matrix and p is an int, represented
       as lists of lists.
    """
    if p == 1:
        return m
    else:
        if p % 2 == 0:
            new = mat_power(m, p/2)
            return mat_mul(new, new)
        else:
            new = mat_power(m, p-1)
            return mat_mul(new, m)

# Raise same m as above to the power of 20.
# Check number of calls to mat_mul.
m = [[1, 2, 3], [0, -1, 3], [2, 4, 1]]
num_calls = 0
m20 = mat_power(m, 20)
if num_calls != 5:
    print(f"Wrong number of calls to mat_mul. Expected 5, got {num_calls}")
for row in m20:
    print(row)

            