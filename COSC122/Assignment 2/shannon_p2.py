"""
An improved program that plays Shannon's Game.
Students should enter their name and number below!

PLEASE READ THROUGH ALL THE COMMENTS FOR INSTRUCTIONS!

Author:
Date:
"""

import re
import doctest
import time
import sys
# import matplotlib.pyplot as plt


DEFAULT_CORPUS = 'corpus.txt'


def _c_mul(num_a, num_b):
    '''Substitute for c multiply function'''
    return (int(num_a) * int(num_b)) & 0xFFFFFFFF


def nice_hash(input_string):
    """ Takes a string name and returns a hash for the string. This hash value
    will be os independent, unlike the default Python hash function.
    It will also be stable across runs of Python, unlike the default.
    """
    if input_string is None:
        return 0  # empty
    value = ord(input_string[0]) << 7
    for char in input_string:
        value = _c_mul(1000003, value) ^ ord(char)
    value = value ^ len(input_string)
    if value == -1:
        value = -2
    return value


class Frequency(object):
    """
    DO NOT MODIFY THIS CLASS.
    Stores a letter:frequency pair.
    The repr for printing will be of the form <item, frequency>
    See the example below
    >>> f = Frequency('c', 2)
    >>> f.letter
    'c'
    >>> f.frequency
    2
    >>> print(f)
    <'c': 2>
    """

    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.next = None

    def __repr__(self):
        return ('<' +
                repr(self.letter) + ': ' + str(self.frequency) +
                '>')


class SortedFrequencyList(object):
    """
    Stores a collection of Frequency objects as a sorted linked list.
    Items are sorted from the highest frequency to the lowest.
    """

    def __init__(self):
        self.head = None

    def add(self, letter, frequency=1):
        """
        Adds the given letter and frequency combination as a Frequency object
        to the list. If the given letter is already in the list, the given
        frequency is added to its frequency.

        If the updated frequency is greater than the frequency of the previous
        node then it should be moved into order, ie, so that it is after
        all items with the same or greater frequency.

        If the letter is not in the list then the new frequency object should be
        added to the list so that it is after all letters
        with the same or higher frequency.

        #Adding new letters with frequency 1 should be the sole usage case in
        #this assignment and you can make your code more efficient if you treat
        #letters with frequency of 1 as a special case. But, your code should
        #still deal with the more general case, eg, my_list.add('a', 4)

        Of course, if there are no letters in the list
        then the new item should be added at the head.

        The doctests below should make it clear how this method should work.
        Hint: you should have code similar to this in your answers to lab 3 :)

        You will probably want to use a helper function.
        YOU MUST write some more doctests for this method.
        >>> f = SortedFrequencyList()
        >>> f.add('a', 1)
        >>> f
        SFL(<'a': 1>)
        >>> f.add('b', 1)
        >>> f
        SFL(<'a': 1>, <'b': 1>)
        >>> f.add('c', 1)
        >>> f
        SFL(<'a': 1>, <'b': 1>, <'c': 1>)
        >>> f.add('d', 1)
        >>> f
        SFL(<'a': 1>, <'b': 1>, <'c': 1>, <'d': 1>)
        >>> f.add('d', 1)
        >>> f
        SFL(<'d': 2>, <'a': 1>, <'b': 1>, <'c': 1>)
        >>> f.add('c', 1)
        >>> f
        SFL(<'d': 2>, <'c': 2>, <'a': 1>, <'b': 1>)
        >>> f.add('d', 1)
        >>> f
        SFL(<'d': 3>, <'c': 2>, <'a': 1>, <'b': 1>)
        >>> f.add('a', 1)
        >>> f
        SFL(<'d': 3>, <'c': 2>, <'a': 2>, <'b': 1>)
        >>> f.add('b', 2)
        >>> f
        SFL(<'d': 3>, <'b': 3>, <'c': 2>, <'a': 2>)
        >>> f.add('a', 4)
        >>> f
        SFL(<'a': 6>, <'d': 3>, <'b': 3>, <'c': 2>)
        >>> f.add('r', 4)
        >>> f
        SFL(<'a': 6>, <'r': 4>, <'d': 3>, <'b': 3>, <'c': 2>)
        >>> f.add('t', 3)
        >>> f
        SFL(<'a': 6>, <'r': 4>, <'d': 3>, <'b': 3>, <'t': 3>, <'c': 2>)
        >>> f.add('z', 1)
        >>> f
        SFL(<'a': 6>, <'r': 4>, <'d': 3>, <'b': 3>, <'t': 3>, <'c': 2>, <'z': 1>)
        >>> x = SortedFrequencyList()
        >>> x
        SFL()
        >>> x.add('z')
        >>> x
        SFL(<'z': 1>)
        >>> y = SortedFrequencyList()
        >>> y.add('z', 20)
        >>> y
        SFL(<'z': 20>)
        >>> y.add('a')
        >>> y
        SFL(<'z': 20>, <'a': 1>)
        """
        # ---start student section---
        prev = None
        point = self.head
        done = False
        while not done:
            if self.head == None:
                temp = Frequency(letter, frequency)
                temp.next = self.head
                self.head = temp
                done = True
            elif frequency > 1:
                if point.letter == letter:
                    point.frequency += frequency
                    if prev != None and point.frequency > prev.frequency:
                        prev.next = point.next
                        self._insert_in_order(point)
                    done = True
                elif point.next == None:
                    self._insert_in_order(Frequency(letter, frequency))
                    done = True
                else:
                    prev = point
                    point = point.next
            else: #frequency == 1 
                if point.letter == letter:
                    point.frequency += frequency
                    if prev != None:
                        if point.frequency > prev.frequency:
                            prev.next = point.next
                            self._insert_in_order(point)
                    done = True
                elif point.next == None:
                    temp = Frequency(letter, frequency)
                    point.next = temp
                    temp.next = None
                    done = True
                else:
                    prev = point
                    point = point.next
        # ===end student section===
        
    def _insert_in_order(self, frequency):
        """ Takes a Frequency and inserts in to the list so that
        items are sorted from largest to smallest.
        NOTE: The list must contain something for this method to work.
        In general this method should only be called from the add method,
        see the add method docstring for information on how to use this method.
        This is modified from lab 3.
        """
        freq_of_item = frequency.frequency
        if freq_of_item > self.head.frequency:
            frequency.next = self.head
            self.head = frequency
        else:
            curr_freq = self.head
            inserted = False
            while curr_freq.next is not None and not inserted:
                if freq_of_item > curr_freq.next.frequency:
                    
                    frequency.next = curr_freq.next
                    curr_freq.next = frequency
                    inserted = True
                else:
                    curr_freq = curr_freq.next
            # got to end and didn't find
            if not inserted:
                frequency.next = None  # as now at end of list
                curr_freq.next = frequency    

    def remove(self, letter):
        """
        Removes the Frequency object with the given `letter` from the list.
        Does nothing if `letter` is not in the list.
        YOU MUST write some more doctests for this method.

        >>> f = SortedFrequencyList()
        >>> f.add('a', 3)
        >>> f.add('b', 2)
        >>> f.add('c', 1)
        >>> f
        SFL(<'a': 3>, <'b': 2>, <'c': 1>)
        >>> f.remove('b')
        >>> f
        SFL(<'a': 3>, <'c': 1>)
        >>> f.add('b', 2)
        >>> f.remove('x')
        >>> f
        SFL(<'a': 3>, <'b': 2>, <'c': 1>)
        >>> f.remove('a')
        >>> f
        SFL(<'b': 2>, <'c': 1>)
        >>> f.remove('c')
        >>> f
        SFL(<'b': 2>)
        >>> f.remove('x')
        >>> f
        SFL(<'b': 2>)
        >>> f.remove('b')
        >>> f
        SFL()
        >>> f.remove('b')
        >>> f
        SFL()
        """
        # ---start student section---
        done = False
        point = self.head
        if self.head == None:
            done = True
        elif self.head.letter == letter:
            self.head = self.head.next
            done = True
        while not done:
            if point.next == None:
                done = True            
            elif point.next.letter == letter:
                point.next = point.next.next
                done = True
            else:
                point = point.next
        # ===end student section===

    def find(self, letter):
        """
        Returns the Frequency object for the given `letter` in the list, or
        None if the `letter` doesn't appear in the list.
        YOU MUST write some more doctests for this method.

        >>> f = SortedFrequencyList()
        >>> f.add('a', 3)
        >>> f.find('a')
        <'a': 3>
        >>> print(f.find('b'))
        None
        >>> z = SortedFrequencyList()
        >>> print(z.find('x'))
        None
        >>> f = SortedFrequencyList()
        >>> f.add('a', 3)
        >>> f.add('b', 2)
        >>> f.add('c', 1)
        >>> f.find('a')
        <'a': 3>
        >>> f.find('b')
        <'b': 2>
        >>> f.find('c')
        <'c': 1>
        """
        # ---start student section---
        done = False
        point = self.head
        if point == None:
            return None
        while not done:
            if point.letter == letter:
                return point
            elif point.next == None:
                return None
            else:
                point = point.next
            
        # ===end student section===

    def __contains__(self, item):
        # you should use the find method here
        # ---start student section---
        if self.find(item) != None:
            return True
        else:
            return False
        # ===end student section===

    def __iter__(self):
        """ Note this will be used to return a simple list of Frequency items
        eg, list(my_sorted_frequency_list)
        Students shouldn't change this method and don't need to understand it.
        """
        current = self.head
        while current is not None:
            yield current.letter
            current = current.next

    def __repr__(self):
        """ Returns a string representation of the list, eg, SFL(<'e': 2>, <'d': 1>))
        """
        item_strs = []
        current = self.head
        while current is not None:
            item_strs.append(repr(current))
            current = current.next
        return 'SFL(' + ', '.join(item_strs) + ')'



class PrefixItem(object):
    """
    DO NOT MODIFY THIS CLASS.
    Stores a prefix:possibles pair.

    >>> p = PrefixItem('th', SortedFrequencyList())
    >>> p.possibles.add('e', 40)
    >>> p.possibles.add('o', 10)
    >>> p
    PfI('th': SFL(<'e': 40>, <'o': 10>))
    """

    def __init__(self, prefix, possibles):
        """
        Initialises a new PrefixItem with the given letter `prefix` and
        SortedFrequencyList of `possibles`.
        """
        self.prefix = prefix
        self.possibles = possibles

    def __hash__(self):
        return nice_hash(self.prefix)

    def __repr__(self):
        return 'PfI(' + repr(self.prefix) + ': ' + repr(self.possibles) + ')'


class PrefixTable(object):
    """
    A simple hash table for storing prefix:possible combinations using
    PrefixItems internally.
    """

    def __init__(self, slots):
        """
        Initialises the PrefixTable with a number of `slots`. The table cannot
        store more items than the number of slots specified here.
        """
        self.slots = slots
        self.data = [None] * slots

    def store(self, prefix, possibles):
        """
        Stores the given letter `prefix` and list of `possibles` (a
        SortedFrequencyList) in the hash table using a PrefixItem. If the
        item is successfully stored in the table, this method returns
        True, otherwise (for example, if there is no more room left in the
        table) it returns False.
        Make sure you use nice_hash to get the initial hash
        and remember you are using linear probing for clashes.
        YOU MUST write some more doctests for this method.

        >>> p = PrefixTable(1)
        >>> p.store('th', SortedFrequencyList())
        True
        >>> p
        Prefix hash Table
        -----------------
            0: PfI('th': SFL())
        >>> p.store('ca', SortedFrequencyList())
        False
        >>> a = PrefixTable(5)
        >>> nice_hash('th') % 5
        2
        >>> nice_hash('xe') % 5
        1
        >>> nice_hash('hf') % 5
        1
        >>> nice_hash('po') % 5
        1
        >>> nice_hash('io') % 5
        2
        >>> nice_hash('er') % 5
        3
        >>> a.store('th', f)
        True
        >>> a
        Prefix hash Table
        -----------------
            0: None
            1: None
            2: PfI('th': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            3: None
            4: None
        >>> a.store('xe', f)
        True
        >>> a
        Prefix hash Table
        -----------------
            0: None
            1: PfI('xe': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            2: PfI('th': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            3: None
            4: None
        >>> a.store('hf', f)
        True
        >>> a
        Prefix hash Table
        -----------------
            0: None
            1: PfI('xe': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            2: PfI('th': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            3: PfI('hf': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            4: None
        >>> a.store('po', f)
        True
        >>> a
        Prefix hash Table
        -----------------
            0: None
            1: PfI('xe': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            2: PfI('th': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            3: PfI('hf': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            4: PfI('po': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
        >>> a.store('io', f)
        True
        >>> a
        Prefix hash Table
        -----------------
            0: PfI('io': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            1: PfI('xe': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            2: PfI('th': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            3: PfI('hf': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
            4: PfI('po': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
        >>> a.store('xr', f)
        False
        >>> b = PrefixTable(0)
        >>> b.store('xr', f)
        False
        p = PrefixTable(1)
        >>> possibles = SortedFrequencyList()
        >>> possibles.add('b', 2)
        >>> possibles.add('a', 3)
        >>> possibles.add('c', 1)
        >>> p.store('th', possibles)
        >>> True
        >>> p
        Prefix hash Table
        -----------------
            0: PfI('th': SFL(<'a': 3>, <'b': 2>, <'c': 1>))
        >>> p.store('th', possibles)
        False
        p
        Prefix hash Table
        -----------------
            0: PfI('th': SFL(<'a': 6>, <'b': 4>, <'c': 2>))
        # Unclear on if adding a prefix which already existed in the list is meant
        # to add a new item or update the possibles attached to the prefix, I used
        # the later as it makes process corpus much simpler.
        """
        # ---start student section---
        if self.slots == 0:
            return False
        key = nice_hash(prefix) % self.slots
        done = False
        count = 0
        is_stored = False
        while done == False:
            if self.data[key] != None:
                if self.data[key].prefix == prefix:
                    #This section adds the StoredFrequencyList from possibles to
                    #the item already present in the list
                    finished = False
                    point = possibles.head
                    while not finished:
                        if point != None:
                            letter = point.letter
                            frequency = point.frequency
                            self.data[key].possibles.add(letter, frequency)
                            point = point.next
                        else:
                            finished = True
                    done = True
                    is_stored = True
                else:
                    key = (key + 1) % self.slots
                    count += 1
            else:
                self.data[key] = PrefixItem(prefix, possibles)
                done = True
                is_stored = True
            if count == self.slots:
                done = True
        return is_stored
        # ===end student section===

    def fetch(self, prefix):
        """"
        Returns the SortedFrequencyList of possibles associated with the given
        letter `prefix', or None if the `prefix` isn't stored in the table.
        Make sure you use nice_hash to get the initial hash
        and remember you are using linear probing for clashes
        YOU MUST write some more doctests for this method.

        >>> prefix = 'th'
        >>> possibles = SortedFrequencyList()
        >>> possibles.add('e', 40)
        >>> possibles.add('o', 10)
        >>> p = PrefixTable(1)
        >>> p.store(prefix, possibles)
        True
        >>> p.fetch('th')
        SFL(<'e': 40>, <'o': 10>)
        >>> print(p.fetch('ca'))
        None
        """
        # ---start student section---
        key = nice_hash(prefix) % self.slots
        done = False
        count = 0
        while done == False:
            if self.data[key] == None:
                return None            
            elif self.data[key].prefix == prefix:
                return self.data[key].possibles
            else:
                key = (key + 1) % self.slots
                count += 1
            if count == self.slots:
                return None
            
        # ===end student section===

    def __contains__(self, prefix):
        """ Returns True if prefix is in the table, otherwise False"""
        # ---start student section---
        key = nice_hash(prefix) % self.slots
        done = False
        count = 0
        while not done:
            if self.data[key] == None:
                return False
            elif self.data[key].prefix == prefix:
                return True
            else:
                key = (key + 1) % self.slots
                count += 1
            if count == self.slots:
                return False         
        # ===end student section===

    def __repr__(self):
        ans = 'Prefix hash Table\n'
        ans += '-----------------'
        for i, item in enumerate(self.data):
            ans += '\n{:5}: {}'.format(i, repr(item))
        return ans



def process_corpus(corpus, unique_chars):
    """
    Returns a PrefixTable populated with the possible characters that follow
    each character pair in `corpus`. `unique_chars` is the number of unique
    characters in `corpus`.

    The size of the PrefixTable should be chosen by calculating the maximum
    number of character pairs (the square of `unique_chars`). In practice,
    the actual number of unique paris in the corpus will be considerably less
    than this, so we are guaranteed a low load factor.

    WARNING: Clashes may still occur and you must use linear probing
    to resolve clashes

    Note: The ...'s below indicate lines have been chopped out to save space
          Usually the lines will just contain None

    NOTE: YOU MUST write some doctests for the method here! Ones that
    produce more interesting SFL's would be good.


    >>> process_corpus('lazy languid line', 11) #doctest: +ELLIPSIS
    Prefix hash Table
    -----------------
        0: None
       ...
       19: None
       20: PfI('ui': SFL(<'d': 1>))
       21: None
       ...
       41: None
       42: PfI('la': SFL(<'z': 1>, <'n': 1>))
       43: None
       44: PfI('an': SFL(<'g': 1>))
       45: None
       ...
       49: None
       50: PfI('li': SFL(<'n': 1>))
       51: None
       ...
       55: None
       56: PfI('az': SFL(<'y': 1>))
       57: PfI('y ': SFL(<'l': 1>))
       58: None
       59: None
       60: None
       61: PfI('ng': SFL(<'u': 1>))
       62: None
       63: None
       64: PfI('gu': SFL(<'i': 1>))
       65: None
       66: None
       67: None
       68: None
       69: PfI(' l': SFL(<'a': 1>, <'i': 1>))
       70: None
       ...
       93: None
       94: PfI('d ': SFL(<'l': 1>))
       95: None
       96: PfI('in': SFL(<'e': 1>))
       97: None
       98: None
       99: None
      100: None
      101: PfI('zy': SFL(<' ': 1>))
      102: PfI('id': SFL(<' ': 1>))
      103: None
      ...
      120: None
    >>> process_corpus('pitter patter', 7) #doctest: +ELLIPSIS
    Prefix hash Table
    -----------------
        0: None
        1: None
        2: None
        3: PfI('tt': SFL(<'e': 2>))
        4: None
       ...
       19: None
       20: PfI('te': SFL(<'r': 2>))
       21: None
       ...
       29: None
       30: PfI('er': SFL(<' ': 1>))
       31: None
       ...
       33: None
       34: PfI('pa': SFL(<'t': 1>))
       35: None
       ...
       37: None
       38: PfI(' p': SFL(<'a': 1>))
       39: PfI('it': SFL(<'t': 1>))
       40: PfI('r ': SFL(<'p': 1>))
       41: None
       42: PfI('pi': SFL(<'t': 1>))
       43: PfI('at': SFL(<'t': 1>))
       44: None
       ...
       48: None
    >>> process_corpus('riff raff', 5)  #doctest: +ELLIPSIS
    Prefix hash Table
    -----------------
        0: PfI(' r': SFL(<'a': 1>))
        1: None
        2: PfI('ra': SFL(<'f': 1>))
        3: None
        4: None
        5: None
        6: PfI('if': SFL(<'f': 1>))
        7: None
        8: None
        9: None
       10: PfI('ri': SFL(<'f': 1>))
       11: PfI('af': SFL(<'f': 1>))
       12: None
       13: None
       14: None
       15: None
       16: PfI('ff': SFL(<' ': 1>))
       17: None
       18: None
       19: None
       20: None
       21: PfI('f ': SFL(<'r': 1>))
       22: None
       23: None
       24: None
    """
    # ---start student section---
    table = PrefixTable(unique_chars**2)
    done = False
    i = 0
    while i < len(corpus)-2:
        prefix = corpus[i] + corpus[i+1]
        possibles = SortedFrequencyList()
        possibles.add(corpus[i+2])
        table.store(prefix, possibles)
        i += 1
    return table
        
    # ===end student section===


def run_time_trials():
    """ A good place to write code for time trials
    Make sure you use this docstring to explain your code and that
    you write comments in your code to help explain the process.
    """
    pass
    
    

def run_some_trials():
    """ Play some games with various test phrases and settings """
    # play game using whatever you like
    # maybe put an input statement here
    # so you can enter the corpus
    # and settings
    # or just run various games with various settings

    # test_phrases = ['dead war']

    #'Hello isn\'t it a lovely day today.']
    # MAKE SURE you test with various phrases!

    #test_files = [DEFAULT_CORPUS]

    # 'the-yellow-wall-paper.txt',
    # 'hamlet.txt',
    # 'le-rire.txt',
    # 'war-of-the-worlds.txt',
    # 'ulysses.txt',
    # 'war-and-peace.txt']

    #Uncomment the block below to run trials based on the lists of phrases and files above
    #for test_phrase in test_phrases:
        #for corpus_filename in test_files:
            #phrase_length = 0   # for auto-run
            #load_corpus_and_play(corpus_filename, test_phrase, phrase_length)
            #print('\n'*3)

    # check out https://www.gutenberg.org/ for more free books!

    # interactive trial
    # see how long the program takes to guess 'bat man'
    # it will get the first two characters and start asking you
    # if it has the third character correct etc...
    # load_corpus_and_play(corpus_filename, 'ba', 7)
    pass


def test():
    """ Runs doctests """
    # uncomment various doctest runs to check each method/function
    # MAKE sure your submitted code doesn't run tests except
    # MAKE SURE you add some doctests of your own to the docstrings

    # doctest.run_docstring_examples(Frequency, globs=None)
    # doctest.run_docstring_examples(SortedFrequencyList.add, globs=None)
    # doctest.run_docstring_examples(SortedFrequencyList.remove, globs=None)
    # doctest.run_docstring_examples(SortedFrequencyList.find, globs=None)

    # doctest.run_docstring_examples(PrefixTable.store, globs=None)
    # doctest.run_docstring_examples(PrefixTable.fetch, globs=None)
    
    # doctest.run_docstring_examples(process_corpus, globs=None)

    # you can leave the following line uncommented as long as your code
    # passes all the tests the line won't produce any output
    # doctest.testmod()  # run all doctests - this is helpful before you submit

    # Uncomment the call to run_some_trials below to run
    # whatever trials you have setup in that function
    # IMPORTANT: comment out the run_some_trials() line below
    # before you submit your code
    # run_some_trials()

    # IMPORTANT: comment out the run_time_trials() line below
    # before you submit your code
    # run_time_trials()






###############################################################################
################# DO NOT MODIFY ANYTHING INSIDE THE BLOCK BELOW ###############
################## YOU MUST INCLUDE THIS CODE IN YOUR SUBMISSION ##############
###############################################################################
################# There is some code below this block you should read #########
###############################################################################

def fallback_guesses(possibles):
    """
    Returns all characters from a--z, and some punctuation that don't appear in
    `possibles`.
    """
    all_fallbacks = [chr(c) for c in range(ord('a'), ord('z') + 1)] + \
                    [' ', ',', '.', "'", '"', ';', '!', '?']
    return [x for x in all_fallbacks if x not in possibles]


def format_document(doc):
    """
    Re-formats `d` by collapsing all whitespace characters into a space and
    stripping all characters that aren't letters or punctuation.
    """
    from unicodedata import category
    # http://www.unicode.org/reports/tr44/#General_Category_Values
    allowed_types = ('Lu', 'Ll', 'Lo', 'Po', 'Zs')
    #d = unicode(d, 'utf-8')
    #d = str(d, 'utf-8')
    # Collapse whitespace
    doc = re.compile(r'\s+', re.UNICODE).sub(' ', doc)
    doc = u''.join([cat.lower()
                    for cat in doc if category(cat) in allowed_types])
    # Remove .encode() to properly process a unicode corpus
    return doc


def confirm(prompt):
    """
    Asks the user to confirm a yes/no question.
    Returns True/False based on their answer.
    """
    ans = ' '
    while ans[0] not in ('Y', 'y', 'n', 'N'):
        ans = input(prompt + ' (y/n) ')
    return True if ans[0] in ('Y', 'y') else False


def check_guess(next_char, guess):
    """
    Returns True if `guess` matches `next_char`, or asks the user if
    `next_char` is None.
    """
    if next_char is not None:
        return next_char == guess
    else:
        return confirm(" '{}'?".format(guess))


def next_guess(guesses):
    """ Returns the next guess """
    return guesses.pop(0) if len(guesses) else None


def check_guesses(next_char, guesses):
    """
    Runs through `guesses` to check against `next_char` (or asks the user if
    `next_char` is None).
    If a correct guess is found, (guess, count) is returned; otherwise
    (None, count) is returned. Where `count` is the number of guesses
    attempted.
    """
    guess = next_guess(guesses)
    guess_count = 1
    while guess is not None:
        if check_guess(next_char, guess):
            return (guess, guess_count)
        guess = next_guess(guesses)
        guess_count += 1
    # Wasn't able to find a guess
    return (None, guess_count)


def guess_next_char(phrase, progress, table, is_auto):
    """ Takes the full phrase, the progress string, the hash table
    and the is_auto flag and returns the next character once it has
    been guessed successfully. Also returns the number of guesses
    used in this guessing.
    """
    # Figure out what the next character to guess is
    # set it to None if not doing auto
    next_char = phrase[len(progress)].lower() if is_auto else None

    # Find possible guesses
    last_two_chars = progress[-2:].lower()
    guesses = table.fetch(last_two_chars)
    if guesses is None:
        guesses = []
    # Convert guesses into a list
    guesses = list(guesses)

    fallbacks = fallback_guesses(guesses)
    fallbacks = list(fallbacks)

    # Try to guess it from the table
    (guess, guess_count) = check_guesses(next_char, guesses)

    if guess is None:
        # If guessing from the corpus failed, try to guess from the
        # fallbacks
        print(' Exhausted all guesses from the corpus! Just guessing...')
        (guess, current_guess_count) = check_guesses(next_char, fallbacks)
        if guess is None:
            # If that failed, we're screwed!
            print(' Exhaused all fallbacks! Failed to guess phrase.')
            # Give up and exit the program
            sys.exit(1)
        guess_count += current_guess_count
    return guess, guess_count


def play_game(table, phrase, phrase_len=0):
    """
    Plays the game.
      `table` is the table mapping keys to lists of character frequencies.
      `phrase` is the phrase to match, or part of the phrase.
      `phrase_len` is the total length of the phrase or 0 for auto mode
    If `phrase_len` is zero, then the game is played automatically and
    the phrase is treated as the whole phrase. Otherwise the phrase is
    the start of the phrase and the function will ask the user whether
    or not it's guesses are correct - and keep going until phrase_len
    characters have been guessed correctly.

    Given phrase_len is 0 by default leaving out phrase_len from
    calls will auto-run, eg, play_game(table, 'eggs') will auto-run

    Returns the total number of guesses taken and the total time taken
    If in interactive mode the time taken value will be 0.
    """
    start = time.perf_counter()
    # Play the game automatically if phrase_len is 0
    is_auto = phrase_len == 0

    # Set phrase length to length of supplied phrase
    if is_auto:
        phrase_len = len(phrase)

    progress = phrase[0:2]
    gap_line = '_' * (phrase_len - len(progress))
    total_guesses = 0
    print('{}{}  (0)'.format(progress, gap_line))
    while len(progress) < phrase_len:
        guess, count = guess_next_char(phrase, progress, table, is_auto)
        progress += guess
        total_guesses += count
        # Print current progress and guess count for the last letter
        gap_line = '_' * (phrase_len - len(progress))
        print('{}{}  ({})'.format(progress, gap_line, count))
    end = time.perf_counter()
    #print('{}  ({})'.format(progress, count))
    print(' Solved it in {} guesses!'.format(total_guesses))

    # return zero time taken if in interactive mode
    time_taken = end - start if is_auto else 0

    return total_guesses, time_taken


def load_corpus_and_play(corpus_filename, phrase, length=0):
    """ Loads the corpus file and plays the game with the given setttings """
    with open(corpus_filename) as infile:
        print('Loading corpus... ' + corpus_filename)
        corpus = format_document(infile.read())
        print('Corpus loaded. ({} characters)'.format(len(corpus)))
        unique_chars = len(set(corpus))
        table = process_corpus(corpus, unique_chars)
        # print(table)
        _, time_taken = play_game(table, phrase, length)
        if length == 0:
            print('Took {:0.6f} seconds'.format(time_taken))


###############################################################################
#################### DO NOT MODIFY ANYTHING INSIDE THE BLOCK ABOVE ############
############ YOU MUST STILL INCLUDE THE BLOCK ABOVE IN YOUR SUBMISSION ########
###############################################################################



# IMPORTANT - Read all the comments below!!!
# ---------


def main():
    """ Put your calls to testing code here.
    The quiz server will not run this function.
    It will test other functions directly.
    NOTE: also comment out all your tests before submitting
    """
    test()


def random_string(size):
    """Remove me before submission, I might be helpful in for answering the
    short answer questions"""
    from random import randint
    return "".join(
            chr(ord('a') + randint(0, 25)) for _ in range(size)
            )


    # run this code if not being imported
if __name__ == '__main__':
    main()
    # IMPORTANT
    # Your submitted code should output nothing when you run it from Wing
    # Our tests will call functions themselves :)


def flub(n, mult=0):
    if n < 2:
        mult += 1
        print(mult)
        return 3 * n
    else:
        mult += 1
        return 2 * flub(n-2, mult)
    
def weird(root):
    count = 0
    while 1 == 1:
        if root == 10:
            print(count)
            return "Done"
        else:
            count += 1
            root += 1