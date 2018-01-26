""" Tree class and functions
"""


from csc148_queue import Queue


class Tree:
    """
    A bare-bones Tree ADT that identifies the root with the entire tree.

    === Attributes ===
    @param object value: value of root node
    @param list[Tree|None] children: child nodes
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
        # NEVER have a mutable default parameter...
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
        return ('{}({}, {})'.format(self.__class__.__name__, repr(self.value),
                                    repr(self.children))
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
           17
        19
           23
        >>> t3 = Tree(29, [Tree(31), t1])
        >>> print(t3)
           31
        29
              17
           19
              23
        """
        root_str = indent * " " + str(self.value)
        mid = len([c
                   for c in self.children
                   if c is not None]) // 2
        left_str = [c.__str__(indent + 3)
                    for c in self.children
                    if c is not None][: mid]
        right_str = [c.__str__(indent + 3)
                     for c in self.children
                     if c is not None][mid:]
        return '\n'.join(right_str + [root_str] + left_str)

    def __contains__(self, v):
        """
        Return whether Tree self contains v.

        @param Tree self: this tree
        @param object v: value to search this tree for

        >>> t = Tree(17)
        >>> t.__contains__(17)
        True
        >>> t = descendants_from_list(Tree(19), [1, 2, 3, 4, 5, 6, 7], 3)
        >>> t.__contains__(5)
        True
        >>> t.__contains__(18)
        False
        """
        # if len([c
        #         for c in self.children
        #         if c is not None]) == 0:
        #     return self.value == v
        # else:
        #     return (self.value == v
        #             or any([c.__contains__(v)
        #                     for c in self.children
        #                     if c is not None]))
        return (self.value == v
                or any([v in c
                        for c in self.children
                        if c is not None]))


class BinaryTree(Tree):
    """ Trees with branching factor of 2.

    === Attributes ===
    @param BinaryTree|None left: left child, aliases children[0]
    @param BinaryTree|None right: right child, aliases children[1]
    """

    def __init__(self, value=None, left=None, right=None):
        """ Create BinaryTree self with value, left and right children.

        Extends Tree

        @param BinaryTree self: this binary tree
        @param object value:
        @param BinaryTree|None left:
        @param BinaryTree|None right:
        @rtype: None
        """
        Tree.__init__(self, value, [left, right])

    # create properties left and right as aliases for
    # children[0] and children[1]
    def _set_left(self, left):
        self.children[0] = left

    def _get_left(self):
        return self.children[0]

    left = property(_get_left, _set_left)

    def _set_right(self, right):
        self.children[1] = right

    def _get_right(self):
        return self.children[1]

    right = property(_get_right, _set_right)


def leaf_count(t):
    """
    Return the number of leaves in Tree t.

    @param Tree t: tree to count the leaves of
    @rtype: int

    >>> t = Tree(7)
    >>> leaf_count(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> leaf_count(t)
    6
    """
    if len([c
            for c in t.children
            if c is not None]) == 0:
        return 1
    else:
        return sum([leaf_count(c)
                    for c in t.children
                    if c is not None])


def height(t):
    """
    Return length of longest path, + 1, in tree rooted at t.

    @param Tree t:
    @rtype: int

    >>> t = Tree(5)
    >>> height(t)
    1
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> height(t)
    3
    """
    if len([c
            for c in t.children
            if c is not None]) == 0:
        return 1
    else:
        return 1 + max([height(c)
                        for c in t.children
                        if c is not None])


def flatten(t):
    """ Return a list of all values in tree rooted at t.

    @param Tree t:
    @rtype: list

    >>> t = Tree(5)
    >>> flatten(t)
    [5]
    >>> t = descendants_from_list(Tree(7), [0, 1, 3, 5, 7, 9, 11, 13], 3)
    >>> L = flatten(t)
    >>> L.sort()
    >>> L == [0, 1, 3, 5, 7, 7, 9, 11, 13]
    True
    """
    if len([c
            for c in t.children
            if c is not None]) == 0:
        return [t.value]
    else:
        return [t.value] + sum([flatten(c)
                                for c in t.children
                                if c is not None], [])


def count_if(t, p):
    """ Return number of values that satisfy p in t.

    Assume that all values in t are valid input for p.

    >>> t = Tree(7)
    >>> def p(v): return v > 6
    >>> count_if(t, p)
    1
    >>> t = descendants_from_list(Tree(9), [3, 5, 7, 11], 2)
    >>> count_if(t, p)
    3
    """
    # if len([c
    #         for c in t.children
    #         if c is not None]) == 0:
    #     return 1 if p(t.value) else 0
    # else:
    #     return  (1 if p(t.value) else 0) + sum([count_if(c, p)
    #                     for c in t.children
    #                     if c is not None])
    return (1 if p(t.value) else 0) + sum([count_if(c, p)
                                           for c in t.children
                                           if c is not None])


def arity(t):
    """
    Return maximum branching factor of t

    @param Tree t: the tree to find arity of
    @rtype: int

    >>> tn2 = Tree(2, [Tree(4), Tree(4.5), Tree(5), Tree(5.75)])
    >>> tn3 = Tree(3, [Tree(6), Tree(7)])
    >>> tn1 = Tree(1, [tn2, tn3])
    >>> arity(tn1)
    4
    """
    if t.children == []:
        return 0
    else:
        branching_factors = [arity(c) for c in t.children]
        branching_factors.append(len(t.children))
        return max(branching_factors)


# helpful helper function
def descendants_from_list(t, list_, arity):
    """
    Populate Tree t's descendants from list_, filling them
    in in level order, with up to arity children per node.
    Then return t.

    @param Tree t: tree to populate from list_
    @param list list_: list of values to populate from
    @param int arity: maximum branching factor
    @rtype: Tree

    >>> descendants_from_list(Tree(0), [1, 2, 3, 4], 2)
    Tree(0, [Tree(1, [Tree(3), Tree(4)]), Tree(2)])
    """
    q = Queue()
    q.add(t)
    list_ = list_.copy()
    while not q.is_empty():  # unlikely to happen
        new_t = q.remove()
        for i in range(0, arity):
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
