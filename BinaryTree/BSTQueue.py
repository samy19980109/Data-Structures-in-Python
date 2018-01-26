"""binary tree code and examples
"""


from Queue1 import Queue


class BinaryTree:
    """
    A Binary Tree, i.e. arity 2.
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
        Return whether tree rooted at self contains value.

        @param BinaryTree self: binary tree to search for value
        @param object value: value to search for
        @rtype: bool

        >>> t = BinaryTree(5, BinaryTree(7), BinaryTree(9))
        >>> t.__contains__(7)
        True
        """
        # if self.left is None and self.right is None:
        #     return self.value == value
        # else:
        #     return (self.value == value
        #             or (self.left is not None and self.left.contains(value))
        #             or (self.right is not None and self.right.contains(value)))
        return (self.value == value
                or (self.left is not None and value in self.left)
                or (self.right is not None and value in self.right))


def evaluate(b):
    """
    Evaluate the expression rooted at b.  If b is a leaf,
    return its float value.  Otherwise, evaluate b.left and
    b.right and combine them with b.value.

    Assume:  -- b is a non-empty binary tree
             -- interior nodes contain value in {"+", "-", "*", "/"}
             -- interior nodes always have two children
             -- leaves contain float value

     @param BinaryTree b: binary tree representing arithmetic expression
     @rtype: float

    >>> b = BinaryTree(3.0)
    >>> evaluate(b)
    3.0
    >>> b = BinaryTree("*", BinaryTree(3.0), BinaryTree(4.0))
    >>> evaluate(b)
    12.0
    """
    if b.left is None and b.right is None:
        return b.value
    else:
        return eval("{} {} {}".format(evaluate(b.left),
                                      b.value,
                                      evaluate(b.right)))


def postorder_visit(t, act):
    """
    Visit BinaryTree t in postorder and act on nodes as you visit.

    @param BinaryTree|None t: binary tree to visit
    @param (BinaryTree)->Any act: function to use on nodes
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.value)
    >>> postorder_visit(b, f)
    2
    6
    4
    10
    14
    12
    8
    """
    if t is None:
        pass
    else:
        postorder_visit(t.left, act)
        postorder_visit(t.right, act)
        act(t)
    # exercise: do this as a method!


def inorder_visit(root, act):
    """
    Visit each node of binary tree rooted at root in order and act.

    @param BinaryTree|None root: binary tree to visit
    @param (BinaryTree)->object act: function to execute on visit
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.value)
    >>> inorder_visit(b, f)
    2
    4
    6
    8
    10
    12
    14
    """
    if root is None:
        pass
    else:
        inorder_visit(root.left, act)
        act(root)
        inorder_visit(root.right, act)
    # exercise: do this as a method!


def visit_level(t, n, act):
    """
    Visit each node of BinaryTree t at level n and act on it.  Return
    the number of nodes visited visited.

    @param BinaryTree|None t: binary tree to visit
    @param int n: level to visit
    @param (BinaryTree)->Any act: function to execute on nodes at level n
    @rtype: int

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.value)
    >>> visit_level(b, 2, f)
    2
    6
    10
    14
    4
    >>> visit_level(b, 17, f)
    0
    """
    # key idea: n keeps track of current depth
    # *and* depth wrt children of t is one less
    # than depth wrt t
    #
    # what if t is None?
    if t is None:
        return 0
    # how do I know when to act?
    if n == 0:
        act(t)
        return 1
    # what if I'm not deep enough yet?
    elif n > 0:
        return (visit_level(t.left, n - 1, act)
                + visit_level(t.right, n - 1, act))
    # what if I've exceeded depth?
    else:
        return 0


def levelorder_visit(t, act):
    """
    Visit BinaryTree t in level order and act on each node.

    @param BinaryTree|None t: binary tree to visit
    @param (BinaryTree)->Any act: function to use during visit
    @rtype: None

    >>> b = BinaryTree(8)
    >>> b = insert(b, 4)
    >>> b = insert(b, 2)
    >>> b = insert(b, 6)
    >>> b = insert(b, 12)
    >>> b = insert(b, 14)
    >>> b = insert(b, 10)
    >>> def f(node): print(node.value)
    >>> levelorder_visit(b, f)
    8
    4
    12
    2
    6
    10
    14
    """
    # this approach uses iterative deepening
    (visited, n) = (visit_level(t, 0, act), 0)
    while visited > 0:
        n += 1
        visited = visit_level(t, n, act)


# assume binary search tree order property
def bst_contains(node, value):
    """
    Return whether tree rooted at node contains value.

    Assume node is the root of a Binary Search Tree

    @param BinaryTree|None node: node of a Binary Search Tree
    @param object value: value to search for
    @rtype: bool

    >>> bst_contains(None, 5)
    False
    >>> bst_contains(BinaryTree(7, BinaryTree(5), BinaryTree(9)), 5)
    True
    """
    if node is None:
        return False
    elif node.value > value:
        return bst_contains(node.left, value)
    elif node.value < value:
        return bst_contains(node.right, value)
    else:
        return True


def insert(node, value):
    """
    Insert value in BST rooted at node if necessary, and return new root.

    Assume node is the root of a Binary Search Tree.

    @param BinaryTree node: root of a binary search tree.
    @param object value: value to insert into BST, if necessary.
    @rtype: BinaryTree

    >>> b = BinaryTree(5)
    >>> b1 = insert(b, 3)
    >>> print(b1)
    5
        3
    <BLANKLINE>
    """
    return_node = node
    if not node:
        return_node = BinaryTree(value)
    elif value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    else:  # nothing to do
        pass
    return return_node


if __name__ == "__main__":
    import doctest
    doctest.testmod()
