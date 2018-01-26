"""exercises with binary trees
"""


class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.

    === Attributes ===
    @param object value: value for this binary tree node
    @param BinaryTree|None left: left child of this binary tree node
    @param BinaryTree|None right: right child of this binary tree node
    """

    def __init__(self, value, left=None, right=None):
        """
        Create BinaryTree self with value and children left and right.

        @param BinaryTree self: this binary tree
        @param object value: value of this node
        @param BinaryTree|None left: left child
        @param BinaryTree|None right: right child
        @rtype: None
        """
        self.value, self.left, self.right = value, left, right

    def __eq__(self, other):
        """
        Return whether BinaryTree self is equivalent to other.

        @param BinaryTree self: this binary tree
        @param Any other: object to check equivalence to self
        @rtype: bool

        >>> BinaryTree(7).__eq__("seven")
        False
        >>> b1 = BinaryTree(7, BinaryTree(5))
        >>> b1.__eq__(BinaryTree(7, BinaryTree(5), None))
        True
        """
        return (type(self) == type(other) and
                self.value == other.value and
                (self.left, self.right) == (other.left, other.right))

    def __repr__(self):
        """
        Represent BinaryTree (self) as a string that can be evaluated to
        produce an equivalent BinaryTree.

        @param BinaryTree self: this binary tree
        @rtype: str

        >>> BinaryTree(1, BinaryTree(2), BinaryTree(3))
        BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
        """
        return "BinaryTree({}, {}, {})".format(repr(self.value),
                                               repr(self.left),
                                               repr(self.right))

    def __str__(self, indent=""):
        """
        Return a user-friendly string representing BinaryTree (self)
        inorder.  Indent by indent.

        >>> b = BinaryTree(1, BinaryTree(2, BinaryTree(3)), BinaryTree(4))
        >>> print(b)
            4
        1
            2
                3
        <BLANKLINE>
        """
        right_tree = (self.right.__str__(
            indent + "    ") if self.right else "")
        left_tree = self.left.__str__(indent + "    ") if self.left else ""
        return (right_tree + "{}{}\n".format(indent, str(self.value)) +
                left_tree)

    def __contains__(self, value):
        """
        Return whether tree rooted at node contains value.

        @param BinaryTree self: binary tree to search for value
        @param object value: value to search for
        @rtype: bool

        >>> BinaryTree(5, BinaryTree(7), BinaryTree(9)).__contains__(7)
        True
        """
        return (self.value == value or
                (self.left and value in self.left) or
                (self.right and value in self.right))


def parenthesize(b):
    """
    Return a parenthesized expression equivalent to the arithmetic
    expression tree rooted at b.

    Assume:  -- b is a binary tree
             -- interior nodes contain value in {'+', '-', '*', '/'}
             -- interior nodes always have two children
             -- leaves contain float value

    @param BinaryTree b: arithmetic expression tree
    @rtype: str

    >>> b1 = BinaryTree(3.0)
    >>> print(parenthesize(b1))
    3.0
    >>> b2 = BinaryTree(4.0)
    >>> b3 = BinaryTree(7.0)
    >>> b4 = BinaryTree("*", b1, b2)
    >>> parenthesize(b4)
    '(3.0 * 4.0)'
    >>> b5 = BinaryTree("+", b4, b3)
    >>> print(parenthesize(b5))
    ((3.0 * 4.0) + 7.0)
    """
    # if tree doesn't exist do nothing
    if b is None:
        return ''
    # if tree is a leaf then return float or symbol
    elif b.left is None and b.right is None:
        return b.value
    # if tree is of one length
    else:
        return ('({} {} {})'.format(parenthesize(b.left), b.value,
                                    parenthesize(b.right)))


def list_longest_path(node):
    """
    List the value in a longest path of node.

    @param BinaryTree|None node: tree to list longest path of
    @rtype: list[object]

    >>> list_longest_path(None)
    []
    >>> list_longest_path(BinaryTree(5))
    [5]
    >>> b1 = BinaryTree(7)
    >>> b2 = BinaryTree(3, BinaryTree(2), None)
    >>> b3 = BinaryTree(5, b2, b1)
    >>> list_longest_path(b3)
    [5, 3, 2]
    """
    if node is None:
        return 0
    # elif node.left is None and node.right is None:
    #     return 1
    else:
        l = 1 + list_longest_path(node.left)
        r = 1 + list_longest_path(node.right)
        if l > r:
            return l
        return r


def list_between(node, start, end):
    """
    Return a Python list of all values in the binary search tree
    rooted at node that are between start and end (inclusive).

    A binary search tree t is a BinaryTree where all nodes in the subtree
    rooted at t.left are less than t.value, and all nodes in the subtree
    rooted at t.right are more than t.value

    @param BinaryTree|None node: binary tree to list values from
    @param object start: starting value for list insertion
    @param object end: stopping value for list insertion
    @rtype: list[object]

    >>> b_left = BinaryTree(4, BinaryTree(2), BinaryTree(6))
    >>> b_right = BinaryTree(12, BinaryTree(10), BinaryTree(14))
    >>> b = BinaryTree(8, b_left, b_right)
    >>> list_between(None, 3, 13)
    []
    >>> list_between(b, 2, 3)
    [2]
    >>> L = list_between(b, 3, 11)
    >>> L.sort()
    >>> L
    [4, 6, 8, 10]
    """
    # Check if the node is None then get base case of empty list
    if node is None:
        return []
    # if the value is in between the two then put the value to list
    # Add the recursive code with it to go left and right and do checking
    elif node.left is None and node.right is None:
        return [node.value] if start <= node.value <= end else []
    else:
        lst = []
        if start <= node.value <= end:
            lst += [node.value]
        return lst + list_between(node.left, start, end) + list_between(node.right, start, end)
    # elif start <= node.value <= end:
    #     return [node.value] + \
    #            list_between(node.left, start, end) + \
    #            list_between(node.right, start, end)
    # # Check for the opposite cases of elif part
    # else:
    #     return list_between(node.left, start, end) + \
    #            list_between(node.right, start, end)
    # # For the last cases if both left and right are None we get empty lists
    # by if statements


def list_leaves_between(t, start, stop):
    """ (BTNode, int, int) -> list
    >>> t = None
    >>> list_leaves_between(t, 5, 9)
    []
    >>> t1 = BinaryTree(4, BinaryTree(2), BinaryTree(5))
    >>> t2 = BinaryTree(9, BinaryTree(8), BinaryTree(10))
    >>> t3 = BinaryTree(7, t1, t2)
    >>> L = list_leaves_between(t3, 3, 8)
    >>> L.sort()
    >>> L
    [5, 8]
    """
    if t is None:
        return []
    elif t.left is None and t.right is None:
        return [t.value] if start <= t.value <= stop else []
    else:
        return list_leaves_between(t.left, start, stop) + \
               list_leaves_between(t.right, start, stop)


def count_shallower(t, n):
    """ Return the number of nodes in tree rooted at t with
    depth less than n.

    @param BinaryTree|None t: binary tree to count
    @param int n: depth below which not to count

    >>> t = BinaryTree(0, BinaryTree(1, BinaryTree(2)), BinaryTree(3))
    >>> count_shallower(t, 2)
    3
    """
    # Check for the base case of None
    if t is None:
        return 0
    # check for t not None and recursive call on left and right till n != 0
    elif n > 0:
        return (1 + count_shallower(t.left, n - 1) +
                count_shallower(t.right, n - 1))
    # Check for n = 0
    else:
        return 0


def swap_even(t, d=0):
    """
    >>> t3 = BinaryTree(5, (BinaryTree(6)))
    >>> t2 = BinaryTree(3, (BinaryTree(4)), t3)
    >>> t = BinaryTree(0, BinaryTree(1, BinaryTree(2)), t2)
    >>> print(t)
    >>> swap_even(t)
    >>> print(t)

    """
    if t is None:
        pass
    else:
        if d % 2 == 0:
            l, r = t.left, t.right
            t.left, t.right = r, l
        swap_even(t.left, d + 1)
        swap_even(t.right, d + 1)


def level_nums(t):
    """
    >>> bt = BinaryTree(4, BinaryTree(5, BinaryTree(7), BinaryTree(8)), BinaryTree(6, BinaryTree(7), BinaryTree(8, BinaryTree(9))))
    >>> level_nums(bt)
    [1, 2, 1]
    """
    q = []
    q.append(t)
    lst = []
    lst.append(len(q))
    while q:
        a, b = False, False
        tree = q.pop(0)
        if tree.left:
            q.append(tree.left)
            a = True
        if tree.right:
            q.append(tree.right)
            b = True
        if a or b:
            lst.append(len(q))
    return lst

def merge_strings(s1, s2):
    """
    >>> s = 'fasdfds'
    >>> f = 'sdfdsfsda'
    >>> merge_strings(s, f)
    """

    s = ''
    i1 = 0
    i2 = 0
    while i1 < len(s1) and i2 < len(s2):
        if s1[i1] < s2[i2]:
            s += s1[i1]
            i1 += 1
        else:
            s += s2[i2]
            i2 += 1
    return s + s1[i1:] + s2[i2:]



# def collect(t, s):
#     """
#     >>> t3 = BinaryTree('b', None, (BinaryTree('d', BinaryTree('e'))))
#     >>> t2 = BinaryTree('c', BinaryTree('e'), BinaryTree('f', BinaryTree('h'), BinaryTree('i')))
#     >>> t = BinaryTree('c', t2, t3)
#     >>> collect(t, s)
#     >>>
#     """
#     if t is None:
#         return False
#     elif t.left is None and t.right is None:
#         if len(s) == 0:
#             return True
#         else:
#             if s in t.value:
#                 return True
#             else:
#                 return False
#     else:
#         l = s
#     else:
#         a = t.value +  collect(t.left)
#         b = t.value + collect(t.right)
#         return a + b

def is_bst(t):
    """
    >>> t = BinaryTree(1, BinaryTree(0), BinaryTree(11, BinaryTree(3), \
    BinaryTree(12)))
    >>> is_bst(t)
    """
    if t is None:
        return True
    elif t.left is None and t.right is None:
        return True
    else:
        return all([is_bst(t.left), is_bst(t.right), t.left.value < t.value,
                    t.right.value > t.value])


if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()
