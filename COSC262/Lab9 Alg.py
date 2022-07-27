def leftmost_vertex(polygon, p):
    """'"""
    current = polygon[0]
    i = 0
    while i < len(polygon):
        if is_ccw(p, current, polygon[i]):
            current = polygon[i]
    i += 1
    return current

class Vec:
    """A simple vector in 2D. Also used as a position vector for points"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
        
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        return Vec(self.x * scale, self.y * scale)
        
    def dot(self, other):
        return self.x * other.x + self.y * other.y
        
    def lensq(self):
        return self.dot(self)

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)

def signed_area(a, b, c):
    """Twice the area of the triangle abc.
       Positive if abc are in counter clockwise order.
       Zero if a, b, c are colinear.
       Otherwise negative.
    """
    p = b - a
    q = c - a
    return p.x * q.y - q.x * p.y

def is_on_segment(p, a, b):
    """'"""
    v = a-b
    pa = p-a
    pb = p-b
    pal = pa.lensq()
    pbl = pb.lensq()
    vl = v.lensq()
    return pal <= vl and pbl <= vl and signed_area(p, a, b) == 0
    
def is_ccw(a, b, c):
    """True iff triangle abc is counter-clockwise"""
    area = signed_area(a, b, c) # As earlier
	 # May want to throw an exception if area == 0
    return area > 0  

def intersecting(a, b, c, d):
    """'"""
    return is_ccw(a,d,b) != is_ccw(a,c,b) and is_ccw(c,a,d) != is_ccw(c,b,d)

def is_strictly_convex(vertices):
    """'"""
    output = True
    i = -1
    while i < len(vertices)-1:
	    a = vertices[i-1]
	    b = vertices[i]
	    c = vertices[i+1]
	    if is_ccw(a, b, c) == False:
	        output = False
	    i += 1
    return output


    
def gift_wrap(points):
    """ Returns points on convex hull in CCW using the Gift Wrap algorithm"""
    # Get the bottom-most point (and left-most if necessary).
    assert len(points) >= 3
    bottommost = min(points, key=lambda p: (p.y, p.x))
    hull = [bottommost]
    done = False
    
    # Loop, adding one vertex at a time, until hull is (about to be) closed.
    while not done:
        candidate = None
        # Loop through all points, looking for the one that is "rightmost"
        # looking from last point on hull
        for p in points:
            if p is hull[-1]:
                continue
            if candidate == None or is_ccw(hull[-1], p, candidate) == True:  # ** FIXME **
                candidate = p
        if candidate is bottommost:
            done = True    # We've closed the hull
        else:
            hull.append(candidate)

    return hull

class PointSortKey:
    """A class for use as a key when sorting points wrt bottommost point"""
    def __init__(self, p, bottommost):
        """Construct an instance of the sort key"""
        self.direction = p - bottommost
        self.is_bottommost = self.direction.lensq() == 0  # True if p == bottommost
        
    def __lt__(self, other):
        """Compares two sort keys. p1 < p2 means the vector the from bottommost point
           to p2 is to the left of the vector from the bottommost to p1.
        """
        if self.is_bottommost:
            return True   # Ensure bottommost point is less than all other points
        elif other.is_bottommost:
            return False  # Ensure no other point is less than the bottommost
        else:
            area = self.direction.x * other.direction.y - other.direction.x * self.direction.y
            return area > 0

def simple_polygon(points):
    """'"""
    anchor = min(points, key=lambda p: (p.y, p.x))
    simply_poly = sorted(points, key=lambda p: PointSortKey(p, anchor))
    return simply_poly
    
def graham_scan(points):
    """'"""
    l = simple_polygon(points)
    h = [l[0], l[1], l[2]]
    i = 3
    while i < len(points):
	    while not is_ccw(h[-2], h[-1], l[i]):
	        h.pop()
	    h.append(l[i])
	    i += 1
    return h


def leftmost_vertex(polygon, p):
    """'"""
    current = polygon[0]
    for i in polygon:
	if is_ccw(p, current, i) == True:
	    current = i
    return current