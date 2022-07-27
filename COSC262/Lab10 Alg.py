from collections import namedtuple
Node = namedtuple("Node", ["value", "left", "right"])

def binary_search_tree(nums, is_sorted=False, index1=0, index2=None):
    """Return a balanced binary search tree with the given nums
       at the leaves. is_sorted is True if nums already sorted.
       Inefficient because of slicing but more readable.
    """
    if not is_sorted:
        nums = sorted(nums)
        index2 = len(nums)
    n = index2 - index1
    if n == 1:
        tree = Node(nums[index1], None, None)  # A leaf
    else:
        mid = index1 + (n // 2)  # Halfway (approx)
        left = binary_search_tree(nums, True, index1, mid)
        right = binary_search_tree(nums, True, mid, index2)
        tree = Node(nums[mid - 1], left, right)
    return tree

def print_tree(tree, level=0):
    """Print the tree with indentation"""
    if tree.left is None and tree.right is None: # Leaf?
        print(2 * level * ' ' + f"Leaf({tree.value})")
    else:
        print(2 * level * ' ' + f"Node({tree.value})")
        print_tree(tree.left, level + 1)
        print_tree(tree.right, level + 1)
        
import matplotlib.pyplot as plt


class Vec:
    """A simple vector in 2D. Can also be used as a position vector from
       origin to define points.
    """
    point_num = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.label = 'P' + str(Vec.point_num)
        Vec.point_num += 1

    def __add__(self, other):
        """Vector addition"""
        return Vec(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Vector subtraction"""
        return Vec(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scale):
        """Multiplication by a scalar"""
        return Vec(self.x * scale, self.y * scale)

    def dot(self, other):
        """Dot product"""
        return self.x * other.x + self.y * other.y

    def lensq(self):
        """The square of the length"""
        return self.dot(self)

    def in_box(self, bottom_left, top_right):
        """True iff this point (self) lies within or on the
           boundary of the given rectangular box area"""
        return bottom_left.x <= self.x <= top_right.x and bottom_left.y <= self.y <= top_right.y

    def __getitem__(self, axis):
        return self.x if axis == 0 else self.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)
        
    
class KdTree:
    """A 2D k-d tree"""
    LABEL_POINTS = True
    LABEL_OFFSET_X = 0.25
    LABEL_OFFSET_Y = 0.25    
    def __init__(self, points, depth=0, max_depth=10):
        """Initialiser, given a list of points, each of type Vec, the current
           depth within the tree (0 for root), used during recursion, and the
           maximum depth allowable for a leaf node.
        """
        if len(points) < 2 or depth >= max_depth: # Ensure at least one point per leaf
            self.is_leaf = True
            self.points = points
        else:
            self.is_leaf = False
            self.axis = depth % 2  # 0 for vertical divider (x-value), 1 for horizontal (y-value)
            points.sort(key=lambda p: p[self.axis])
            halfway = len(points) // 2
            self.coord = points[halfway - 1][self.axis]
            self.leftorbottom = KdTree(points[:halfway], depth + 1, max_depth)
            self.rightortop = KdTree(points[halfway:], depth + 1, max_depth)
            
def range_query(tree, low, high):
    """Return a list of the numbers in range min to max
       inclusive within the given binary search tree.
    """
    matches = []
    if tree.left is None and tree.right is None:  # Leaf?
        if low <= tree.value <= high:
            matches.append(tree.value)
    else: # Internal node
        if low <= tree.value and tree.left is not None:
            matches += range_query(tree.left, low, high)
        if high > tree.value and tree.right is not None:
            matches += range_query(tree.right, low, high)
    return matches            

    def points_in_range(self, query_rectangle):
        """Return a list of all points in the tree 'self' that lie within or on the 
           boundary of the given query rectangle, which is defined by a pair of points
           (bottom_left, top_right).
        """        
        if self.is_leaf:
            #matches = all points in node.points lying within rectangle
            matches = [x for x in self.points if x.in_box(query_rectangle)]
        else:
            matches = []
            if rectangle and left (or bottom) half space is not empty:
                matches += points_in_range(node.left, query_rectangle)
            if rectangle and right (or top) half space is not empty:
                matches += points_in_range(node.right, query_rectangle)
        return matches    

point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
points = [Vec(*tup) for tup in point_tuples]
tree = KdTree(points)
in_range = tree.points_in_range((Vec(0, 3), Vec(5, 19)))
print(sorted(in_range))
    
    def plot(self, axes, top, right, bottom, left, depth=0):
        """Plot the the kd tree. axes is the matplotlib axes object on
           which to plot; top, right, bottom, left are the x or y coordinates
           the bounding box of the plot.
        """

        if self.is_leaf:
            axes.plot([p.x for p in self.points], [p.y for p in self.points], 'bo')
            if self.LABEL_POINTS:
                for p in self.points:
                    axes.annotate(p.label, (p.x, p.y),
                    xytext=(p.x + self.LABEL_OFFSET_X, p.y + self.LABEL_OFFSET_Y))
        else:
            if self.axis == 0:
                axes.plot([self.coord, self.coord], [bottom, top], '-', color='gray')
                self.leftorbottom.plot(axes, top, self.coord, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, bottom, self.coord, depth + 1)
            else:
                axes.plot([left, right], [self.coord, self.coord], '-', color='gray')
                self.leftorbottom.plot(axes, self.coord, right, bottom, left, depth + 1)
                self.rightortop.plot(axes, top, right, self.coord, left, depth+1)
        if depth == 0:
            axes.set_xlim(left, right)
            axes.set_ylim(bottom, top)
       
    
    def __repr__(self, depth=0):
        """String representation of self"""
        if self.is_leaf:
            return depth * 2 * ' ' + "Leaf({})".format(self.points)
        else:
            s = depth * 2 * ' ' + "Node({}, {}, \n".format(self.axis, self.coord)
            s += self.leftorbottom.__repr__(depth + 1) + '\n'
            s += self.rightortop.__repr__(depth + 1) + '\n'
            s += depth * 2 * ' ' + ')'  # Close the node's opening parens
            return s
        
def main():
    point_tuples = [(1, 3), (10, 20), (5, 19), (0, 11), (15, 22), (30, 5)]
    points = [Vec(*tup) for tup in point_tuples]
    tree = KdTree(points)
    print(tree)
    axes = plt.axes()
    tree.plot(axes, 25, 35, 0, 0)
    plt.show()
    


def leftmost_vertex(polygon, p):
    """'"""
    current = polygon[0]
    for i in polygon:
	if is_ccw(p, current, i) == True:
	    current = i
    return current