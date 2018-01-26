""" Tree class and functions.
"""


from csc148_queue import Queue


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.
    """

    def __init__(self, value=None, children=None):
        """
        Create Tree self with content value and 0 or more children

        @param Tree self: this tree
        @param object value: value contained in this tree
        @param list[Tree|None] children: possibly-empty list of children
        @rtype: None
        """
        self.value = value
        # copy children if not None
        self.children = children.copy() if children else []

    def __repr__(self):
        """
        Return representation of Tree (self) as string that
        can be evaluated into an equivalent Tree.

        @param Tree self: this tree
        @rtype: str

        >>> t1 = Tree(5)
        >>> t1
        Tree(5)
        >>> t2 = Tree(7, [t1])
        >>> t2
        Tree(7, [Tree(5)])
        """
        # Our __repr__ is recursive, because it can also be called
        # via repr...!
        return ('Tree({}, {})'.format(repr(self.value), repr(self.children))
                if self.children
                else 'Tree({})'.format(repr(self.value)))

    def __eq__(self, other):
        """
        Return whether this Tree is equivalent to other.

        @param Tree self: this tree
        @param object|Tree other: object to compare to self
        @rtype: bool

        >>> t1 = Tree(5)
        >>> t2 = Tree(5, [])
        >>> t1 == t2
        True
        >>> t3 = Tree(5, [t1])
        >>> t2 == t3
        False
        """
        return (type(self) is type(other) and
                self.value == other.value and
                self.children == other.children)

    def __str__(self, indent=0):
        """
        Produce a user-friendly string representation of Tree self,
        indenting each level as a visual clue.

        @param Tree self: this tree
        @param int indent: amount to indent each level of tree
        @rtype: str

        >>> t = Tree(17)
        >>> print(t)
        17
        >>> t1 = Tree(19, [t, Tree(23)])
        >>> print(t1)
        19
           17
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
        29
           31
           19
              17
              23
        """
        root_str = indent * " " + str(self.value)
        return '\n'.join([root_str] +
                         [c.__str__(indent + 3) for c in self.children])


def list_internal(t):
    """
    Return list of values in internal nodes of t.

    @param Tree t: tree to list internal values of
    @rtype: list[object]

    >>> t = Tree(0)
    >>> list_internal(t)
    []
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> L = list_internal(t)
    >>> L.sort()
    >>> L
    [0, 1, 2]
    """
    # check for Tree is leaff
    if len([c for c in t.children
            if c is not None]) == 0:
        # if leaf return an empty list
        return []
    else:
        # if not return t.value and all other c.value by recursive call
        return [t.value] + sum([list_internal(c) for c in t.children
                                if c is not None], [])


def arity(t):
    """
    Return the maximum branching factor (arity) of Tree t.

    @param Tree t: tree to find the arity of
    @rtype: int

    >>> t = Tree(23)
    >>> arity(t)
    0
    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> arity(tn2)
    4
    >>> tn3 = Tree(3, [Tree(6), Tree(7), Tree(9), Tree(4.5)])
    >>> arity(tn3)
    4
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    # check for leaf
    if len([c
            for c in t.children
            if c is not None]) == 0:
        # return 0 because it is max no. of children
        return 0
    else:
        # if not leaf get len of t.children for comparision
        # recursive call on every children and compare with the max
        # of two upper levels
        return max(len(t.children), max([arity(c) for c in t.children
                    if c is not None]))


def contains_test_passer(t, test):
    """
    Return whether t contains a value that test(value) returns True for.

    @param Tree t: tree to search for values that pass test
    @param function[Any, bool] test: predicate to check values with
    @rtype: bool

    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4.5, 5, 6, 7.5, 8.5], 4)
    >>> def greater_than_nine(n): return n > 9
    >>> contains_test_passer(t, greater_than_nine)
    False
    >>> def even(n): return n % 2 == 0
    >>> contains_test_passer(t, even)
    True
    """
    # Check for Tree is leaf
    if len([c
            for c in t.children
            if c is not None]) == 0:
        # Return True if t.value passes test
        return True if test(t.value) else False
    else:
        # Check for t.value test
        tree_test = test(t.value)
        # recursive call on all the children and store in variable
        child_test = any(contains_test_passer(c, test)
                         for c in t.children
                         if c is not None)
        # Check for both root and children
        return tree_test or child_test


def list_if(t, p):
    """
    Return a list of values in Tree t that satisfy predicate p(value).

    Assume p is defined on all of t's values.

    @param Tree t: tree to list values that satisfy predicate p
    @param function[Any, bool] p: predicate to check values with
    @rtype: list[object]

    >>> def p(v): return v > 4
    >>> t = descendants_from_list(Tree(0), [1, 2, 3, 4, 5, 6, 7, 8], 3)
    >>> list_ = list_if(t, p)
    >>> set(list_) == {5, 6, 7, 8}
    True
    >>> list_ = list_if(Tree(8), p)
    >>> set(list_) == {8}
    True
    >>> def p(v): return v % 2 == 0
    >>> list_ = list_if(t, p)
    >>> set(list_) == {0, 2, 4, 6, 8}
    True
    """
    # Check if Tree is a Leaf
    if len([c
            for c in t.children
            if c is not None]) == 0:
        # if Tree is leaf then test node value with p to give value or
        #  empty list
        return [t.value] if p(t.value) else []
    else:
        # again check for t.value for case of tree with one child
        tree_lst = [t.value] if p(t.value) else []
        # recursive code for every child to get a list of child.value
        child_lst = sum([list_if(c, p)
                         for c in t.children
                         if c is not None], [])
        # add and return both lists
        return tree_lst + child_lst


def count(t):
    """
    Return the number of nodes in Tree t.


    @param Tree t: tree to find number of nodes in
    @rtype: int

    >>> t = Tree(17)
    >>> count(t)
    1
    >>>
     t4 = descendants_from_list(Tree(17), [0, 2, 4, 6, 8, 10, 11], 4)
    >>> count(t4)
    8
    """
    # checks if Tree is a leaf
    if len([c
            for c in t.children
            if c is not None]) == 0:
        # returns 1 becasue there is only 1 node
        return 1
    else:
        # Return 1 + recursive sum of nodes for ever children
        return 1 + sum([count(c)
                        for c in t.children
                        if c is not None])

def con(t,d):
    """
    >>> t = Tree("a", [Tree("b"), Tree("c", [Tree("d")]), Tree("r")])
    >>> con(t, 0)
    "a"
    >>> con(t, 2)
    "bcr"
    """
    # if d == 0:
    #     return t.value
    # else:
    #     a = [con(c, d-1) for c in t.children]
    #     s = ''
    #     for val in a:
    #         s += val
    #
    #     return s

    if t is None:
        return ''
    elif d == 0:
        return str(t.value)
    else:
        return ''.join([con(c, d-1) for c in t.children])



# helper function that may be useful in the functions
# above
def gather_lists(list_):
    """
    Concatenate all the sublists of L and return the result.

    @param list[list[object]] list_: list of lists to concatenate
    @rtype: list[object]

    >>> gather_lists([[1, 2], [3, 4, 5]])
    [1, 2, 3, 4, 5]
    >>> gather_lists([[6, 7], [8], [9, 10, 11]])
    [6, 7, 8, 9, 10, 11]
    """
    # new_list = []
    # for l in list_:
    #     new_list += l
    # return new_list
    # equivalent to...
    return sum([l for l in list_], [])


def deepen(t):
    """
    >>> t = Tree(1, [Tree(2), Tree(3)])
    >>> deepen(t)
    >>> repr(t)
    """
    if t is None:
        pass
    else:
        m = t.children[:]
        t.children = [Tree(t.value, t.children)]
        for c in m:
            deepen(c)


# helpful helper function
def descendants_from_list(t, list_, branching):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int branching: maximum branching factor
    @rtype: Tree

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, branching):
            if len(list_) == 0:
                return t  # our work here is done
            else:
                new_t_child = Tree(list_.pop(0))
                new_t.children.append(new_t_child)
                q.add(new_t_child)
    return t


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print('s')
