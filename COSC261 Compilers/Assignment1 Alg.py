def lcs1(s1, s2, i=None, j=None, array=None):
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
            result = lcs1(s1, s2, i-1, j-1, array) + end
        else: #ending string is different
            drop1 = lcs1(s1, s2, i-1, j, array)
            drop2 = lcs1(s1, s2, i, j-1, array)
            if len(drop1) > len(drop2):
                result = drop1
            else:
                result = drop2
    array.update({(i, j): result})
    return result



def lcs(s1, s2):
    """Find's the length of the longest common substring between the two
    input strings.
    Oliver Neville 20.4.20"""
    n_rows = len(s1)
    n_cols = len(s2)
    table = [n_cols * [0] for row in range(n_rows)]
    if s1 == "" or s2 == "":
        return ""    
    for row in range(0, n_rows):
        for col in range(0, n_cols):
            if s1[row] == s2[col]:
                table[row][col] = table[row-1][col-1] + 1
            else:
                table[row][col] = max(table[row-1][col], table[row][col-1]
                                      , table[row-1][col-1])
    string = create_string(s1, s2, table)
    return string

def create_string(s1, s2, table):
    """Helper function to lcs, creates the lcs from the input table"""
    n_rows = len(s1)
    n_cols = len(s2)
    lcs_str = ""
    row = 1
    col = 1
    done = False
    changer = True
    changec = True
    if table[0][0] > 0:
        lcs_str += s1[0]
    while done != True:
        if row + col == n_rows + n_cols - 2:
            done = True        
        if table[row][col] > table[row-1][col] and changer == True:
            lcs_str += s1[row]
        elif table[row][col] > table[row][col-1] and changec == True:
            lcs_str += s2[col]
        if row < n_rows-1:
            row += 1
        else:
            changer = False
        if col < n_cols-1:
            col += 1
        else:
            changec = False
    return lcs_str

def print_table(table):
    """Pretty(ish) print of table, row by row"""
    n_rows = len(table)
    n_cols = len(table[0])
    s = "    "
    z = "  "
    for x in range(n_cols):
        z += "______"
        if x < 11:
            s += "  |{}:".format(x)
        else:
            s += " |{}:".format(x)
    print(s)
    print(z)
    for i in range(n_rows):
        print(f"{i}:|", end='')
        for j in range(n_cols):
            print(f"{table[i][j]:5}", end='')
        print() # Line break between rows
    pass

class EditNode:
    """An Item to put into an edit distnace table. Operations must be a
    list of tuples in the form [('O', 'Line1', 'Line1'),...] where O is an
    operation"""
    def __init__(self, distance=0, operations=None):
        """initialiser"""
        if operations == None:
            operations = []
        self.distance = distance
        self.operations = operations

    def add(self, operation):
        """'"""
        self.operations += operation
        if operation[0] != 'C':
            self.distance += 1

    def copy_node(self, node):
        """'"""
        self.distance = node.distance
        self.operations = node.operations
        
    def __repr__(self):
        """'"""
        string = ""
        string += "Distance = {}\n".format(str(self.distance))
        string += "Operations = {}".format(str(self.operations))
        return string
    
    def __str__(self):
        """'"""
        string = ""
        string += "Dist = {}\n".format(str(self.distance))
        string += "Oper. = {}".format(str(self.operations))
        return string

def line_edits1(s1, s2):
    """Returns a list of tuples containing the edits that need to be made to
    get from s1 to s2 to another"""
    l1 = [" "] + s1.splitlines()
    l2 = [" "] + s2.splitlines() 
    n_rows = len(l1)
    n_cols = len(l2)
    table = [n_cols * [EditNode(0, [])] for row in range(n_rows)]
    for row in range(n_rows):
        for col in range(n_cols):
            if row == 0 and col != 0:
                table[0][col].copy_node(table[0][col-1])
                table[0][col].add(('I', "", l2[col])) 
            elif row != 0 and col == 0:
                table[row][0].copy_node(table[row-1][0])
                table[row][0].add(('D', l1[row], ""))
            elif row != 0 and col != 0:
                if l1[row] == l2[col]:
                    table[row][col].copy_node(table[row-1][col-1])
                    table[row][col].add(('C', l1[row], l2[col]))
                else:
                    choice = e_min(table[row-1][col-1], table[row-1][col], table[row][col-1])
                    if choice == 'S':
                        table[row][col].copy_node(table[row-1][col-1])
                        table[row][col].add(('S', l1[row], l2[col]))
                    elif choice == 'D':
                        table[row][col].copy_node(table[row-1][col])
                        table[row][col].add(('D', l1[row], ""))
                    else: #choice == 'I'
                        table[row][col].copy_node(table[row][col-1])
                        table[row][col].add(('I', "", l2[col]))
                        
    answer = table[len(l1)-1][len(l2)-1].operations
    return answer
    
                    
                    
                    
def e_min(s, d, i):
    """takes in 3 options and find's the minimum distance, 
    returning the string 'S' 'D' or 'I'.sdi are all type EditNode
    this was done as a way to sort the priority of SDI"""
    mini = s.distance
    output = 'S'
    if d.distance < mini:
        mini = d.distance
        output = 'D'
    if i.distance < mini:
        mini = s.distance
        output = 'I'
    return output

def line_edits2(s1, s2):
    """Returns a list of tuples containing the edits that need to be made to
    get from s1 to s2 to another"""
    l1 = [" "] + s1.splitlines()
    l2 = [" "] + s2.splitlines()
    n_rows = len(l1)
    n_cols = len(l2)
    table = [n_cols * [[]] for row in range(n_rows)]
    
    for row in range(n_rows):
        for col in range(n_cols):
            if row == 0 and col != 0:
                table[row][col] = table[row][col-1] + [('I', "", l2[col])] 
                
            elif row != 0 and col == 0:
                table[row][col] = table[row-1][col] + [('D', l1[row], "")]
                
            elif row != 0 and col != 0:
                if l1[row] == l2[col]:
                    table[row][col] = table[row-1][col-1] + [('C', l1[row], l2[col])]
                    
                else:
                    choice = e_min(table[row-1][col-1], table[row-1][col], table[row][col-1])
                    
                    if choice == 'S':
                        table[row][col] = table[row-1][col-1] + [('S', l1[row], l2[col])]
                        
                    elif choice == 'D':
                        table[row][col] = table[row-1][col] + [('D', l1[row], "")]
                        
                    else: #choice == 'I'
                        table[row][col] = table[row][col-1] + [('I', "", l2[col])]
                        
    answer = table[len(l1)-1][len(l2)-1]
    return answer

    
    
def e_min(sub, dell, ins):
    """takes in 3 options and find's the minimum distance, 
    returning the string 'S' 'D' or 'I'. sdi are all tuple filled lists"""
    distance_s = 0
    for tup_s in sub:
        if tup_s[0] != 'C':
            distance_s += 1
    distance_d = 0
    for tup_d in dell:
        if tup_d[0] != 'C':
            distance_d += 1
    distance_i = 0
    for tup_i in ins:
        if tup_i[0] != 'C':
            distance_i += 1
    minimum = distance_s
    output = 'S'
    if distance_d < distance_s:
        minimum = distance_d
        output = 'D'
    if distance_i < minimum:
        minimum = distance_i
        output = 'I' 
    return output


def line_edits(s1, s2):
    """Returns a list of tuples containing the edits that need to be made to
    get from s1 to s2 to another"""
    l1 = [" "] + s1.splitlines()
    l2 = [" "] + s2.splitlines()
    n_rows = len(l1)
    n_cols = len(l2)
    table = [n_cols * [[]] for row in range(n_rows)]
    
    for row in range(n_rows):
        for col in range(n_cols):
            if row == 0 and col != 0:
                table[row][col] = table[row][col-1] + [('I', "", l2[col])] 
                
            elif row != 0 and col == 0:
                table[row][col] = table[row-1][col] + [('D', l1[row], "")]
                
            elif row != 0 and col != 0:
                if l1[row] == l2[col]:
                    table[row][col] = table[row-1][col-1] + [('C', l1[row], l2[col])]
                    
                else:
                    choice = e_min(table[row-1][col-1], table[row-1][col], table[row][col-1])
                    
                    if choice == 'S':
                        table[row][col] = table[row-1][col-1] + [('S', l1[row], l2[col])]
                        
                    elif choice == 'D':
                        table[row][col] = table[row-1][col] + [('D', l1[row], "")]
                        
                    else: #choice == 'I'
                        table[row][col] = table[row][col-1] + [('I', "", l2[col])]
    
    answer = table[len(l1)-1][len(l2)-1]
    answer = process(answer) 
    return answer

def process(answer):
    """'"""
    new = [] 
    for i in answer:
        if i[0] == 'S':
            lcss = lcs1(i[1], i[2])
            str1 = i[1]
            for c in i[1]:
                if len(lcss) != 0 and lcss[0] == c:
                    lcss = lcss[1:]
                else:
                    tup = str1.partition(c)
                    str1 = tup[0] + "[[" + tup[1] + "]]" + tup[2]
                    
            lcss = lcs1(i[1], i[2])
            str2 = i[2]
            for b in i[2]:
                if len(lcss) != 0 and lcss[0] == b:
                    lcss = lcss[1:]
                else:
                    tup = str2.partition(b)
                    str2 = tup[0] + "[[" + tup[1] + "]]" + tup[2]
            tup = ("S", str1, str2)
            new.append(tup)
            
        else:
            new.append(i)
    return new
                    


def nested(nums):
    n = nums
    c = 0
    for i in range(n):
        for j in range(i * i):
            c += 1
    return c
    
    
    
def tupleise(value, items, i=0, tuplist=0):
    """returns a list of tuples in the form (value, items[i])
    where i is in range 0 to length items"""
    if tuplist == 0:
        tuplist = []
    if i == len(items):
        return tuplist
    else:
        tuplist.append((value, items[i]))
        i += 1
        return tupleise(value, items, i, tuplist)
    
    
def things1(list1, list2):
    stuff = []
    for thing1 in list1:
        for thing2 in list2:
            if thing2 > thing1:
                stuff.append((thing1, thing2))
    return stuff
        
def things(list1, list2, stuff=0, i=0):
    if stuff == 0:
        stuff = []
    if i != len(list1):
        stuff = thingshelp(list1, list2, stuff, i)

        i += 1
        return things(list1, list2, stuff, i)
    else:
        return stuff
    
    
    
def thingshelp(list1, list2, stuff, i, j=0):
    if j != len(list2):
        if list2[j] > list1[i]:
            stuff.append((list1[i], list2[j]))
        j += 1
        return thingshelp(list1, list2, stuff, i, j)
    else:
        return stuff
    
def max_num_movies(movie_list, time=0, count=0):
    """Return a count of the maximum number of movies that can be watched.
       Elements in movie_list are (start_time_in_mins, end_time_in_mins) pairs.
    """
    if len(movie_list) != 0:
        mini = my_min(movie_list)
        movie = movie_list.pop(mini)
        option1 = max_num_movies(movie_list, time, count)
        if movie[0] >= time + 3:
            option2 = max_num_movies(movie_list, movie[1], count+1)
            answer = max(option1, option2)
        else:
            answer = option1
        return answer
    else:
        return count
    #i-1

def my_min(movie_list):
    current = 0
    i = 0
    while i < len(movie_list) - 1:
        if movie_list[i][0] <= movie_list[current][0]:
            current = i
        i += 1
    return current

movie_times = [
    (299, 330),
    (250, 350),
    (280, 297),
    (340, 360),
    (360, 380),
    (300, 337)
]
#print(max_num_movies(movie_times))

import sys
sys.setrecursionlimit(2000)

class Song:
    """An song to (maybe) put in a playlist. Weight must be an int."""
    def __init__(self, rating, duration_in_minutes):
        self.rating = rating
        self.duration = duration_in_minutes

    def __repr__(self):
        """The representation of a song"""
        return "({}, {})".format(self.rating, self.duration)

def max_total_rating(songs, total_duration, n=None, array=None):
    """Return the maximum total rating achievable by taking a subset of the first
       'n' songs to fit within a playlist of the given total_duration.
    """
    if array == None:
        array = {}
    
    if n is None:
        n = len(songs)
    
    if n == 0 or total_duration <= 0:
        return 0
    else:
        if (total_duration, n ) in array:
            answer = array[(total_duration, n)]
        else:
            
            if (total_duration, n - 1) in array:
                max_without_nth_song = array[(total_duration, n - 1)]
            else:
                max_without_nth_song = max_total_rating(songs, total_duration, n - 1)
                array.update({(total_duration, n - 1): max_without_nth_song})
                
            if songs[n - 1].duration > total_duration:
                answer = max_without_nth_song
            else:
                if (total_duration - songs[n-1].duration, n - 1) in array:
                    max_with_nth_song = array[(total_duration - songs[n-1].duration, n - 1)]
                else:
                    max_with_nth_song = max_total_rating(songs, total_duration - songs[n-1].duration, n - 1) + songs[n-1].rating
                    array.update({(total_duration - songs[n-1].duration, n - 1)})
                answer = max(max_without_nth_song, max_with_nth_song)
            
        return answer





def longest_common_subsequence(list1, list2):

    if len(list1) == 0:
        result = []
    elif len(list2) == 0:
        result = []
    else:
        if list1[-1] == list2[-1]:
            end = list2[-1]
            result = longest_common_subsequence(list1[:-1], list2[:-1]) + [end]
        else: #ending string is different
            drop1 = longest_common_subsequence(list1[:-1], list2)
            drop2 = longest_common_subsequence(list1, list2[:-1])
            if len(drop1) > len(drop2):
                result = drop1
            else:
                result = drop2
    return result

s1 = open('PLY_parser.py').read()
s2 = open('PLY_parser_B.py').read()
p = line_edits(s1, s2)
for i in p:
    print(i)

list1 = [19, 5, 5, 0, 13, 5, 0, 1, 14, 7, 21, 1]
list2 = [19, 5, 5, 0, 20, 8, 5, 0, 7, 21, 19]
#print(longest_common_subsequence(list1, list2))