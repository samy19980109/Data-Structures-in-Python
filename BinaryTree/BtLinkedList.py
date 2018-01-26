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

    def inorder(self):
        """ Return LinkedList with values of BinaryTree self inorder.

        @param BinaryTree self: this binary tree
        @rtype: LinkedList

        >>> t = BinaryTree(0, BinaryTree(1), BinaryTree(2))
        >>> lnk= t.inorder()
        >>> print(lnk)
        1 -> 0 -> 2 ->|
        >>> t2 = BinaryTree(3, BinaryTree(4), t)
        >>> lnk = t2.inorder()
        >>> print(lnk)
        4 -> 3 -> 1 -> 0 -> 2 ->|
        """
        if self is None:
            return LinkedList()
        else:
            m = LinkedList()
            m.append(self.value)
            if (self.right is None) or (self.left is None):
                if self.left is not None:
                    a = self.left.inorder() + m
                elif self.right is not None:
                    a = m + self.right.inorder()
                else:
                    a = m
            else:
                a = self.left.inorder() + m + self.right.inorder()
            return a

    def preorder(self):
        """ Return LinkedList with values of BinaryTree self in preorder.

        @param BinaryTree self: this binary tree
        @rtype: LinkedList

        >>> t = BinaryTree(0, BinaryTree(1), BinaryTree(2))
        >>> lnk= t.preorder()
        >>> print(lnk)
        0 -> 1 -> 2 ->|
        >>> t2 = BinaryTree(3, BinaryTree(4), t)
        >>> lnk = t2.preorder()
        >>> print(lnk)
        3 -> 4 -> 0 -> 1 -> 2 ->|
        """
        if self is None:
            return LinkedList()
        else:
            m = LinkedList()
            m.append(self.value)
            if (self.right is None) or (self.left is None):
                if self.left is not None:
                    a = m + self.left.preorder()
                elif self.right is not None:
                    a = m + self.right.preorder()
                else:
                    a = m
            else:
                a = m + self.left.preorder() + self.right.preorder()
            return a

    def postorder(self):
        """ Return LinkedList with values of BinaryTree self in postorder.

        @param BinaryTree self: this binary tree
        @rtype: LinkedList

        >>> t = BinaryTree(0, BinaryTree(1), BinaryTree(2))
        >>> lnk= t.postorder()
        >>> print(lnk)
        1 -> 2 -> 0 ->|
        >>> t2 = BinaryTree(3, BinaryTree(4), t)
        >>> lnk = t2.postorder()
        >>> print(lnk)
        4 -> 1 -> 2 -> 0 -> 3 ->|
        """
        if self is None:
            return LinkedList()
        else:
            m = LinkedList()
            m.append(self.value)
            if (self.right is None) or (self.left is None):
                if self.left is not None:
                    a = self.left.postorder() + m
                elif self.right is not None:
                    a = self.right.postorder() + m
                else:
                    a = m
            else:
                a = self.left.postorder() + self.right.postorder() + m
            return a

    def longest(self):
        """ Return LinkedList with values of longest path from root to leaf in
        BinaryTree self.

        @param BinaryTree self: this binary tree
        @rtype: LinkedList

        >>> t = BinaryTree(0, BinaryTree(1))
        >>> t2 = BinaryTree(3, BinaryTree(4), t)
        >>> print(t2.longest())
        3 -> 0 -> 1 ->|
        """
        if self is None:
            return LinkedList()
        else:
            m = LinkedList()
            m.append(self.value)
            if (self.right is None) or (self.left is None):
                if self.left is not None:
                    a = m + self.left.longest()
                    b = m + self.left.longest()
                elif self.right is not None:
                    a = m + self.right.longest()
                    b = m + self.right.longest()
                else:
                    a = m
                    b = m
            else:
                a = m + self.left.longest()
                b = m + self.right.longest()
            if len(b) > len(a):
                return b
            return a


class LinkedListNode:
    """
    Node to be used in linked list

    === Attributes ===
    @param LinkedListNode next_: successor to this LinkedListNode
    @param object value: data this LinkedListNode represents
    """
    def __init__(self, value, next_=None):
        """
        Create LinkedListNode self with data value and successor next_.

        @param LinkedListNode self: this LinkedListNode
        @param object value: data of this linked list node
        @param LinkedListNode|None next_: successor to this LinkedListNode.
        @rtype: None
        """
        self.value, self.next_ = value, next_

    def __str__(self):
        """
        Return a user-friendly representation of this LinkedListNode.

        @param LinkedListNode self: this LinkedListNode
        @rtype: str

        >>> n = LinkedListNode(5, LinkedListNode(7))
        >>> print(n)
        5 -> 7 ->|
        """
        s = "{} ->".format(self.value)
        current_node = self.next_
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s


class LinkedList:
    """
    Collection of LinkedListNodes

    === Attributes ==
    @param: LinkedListNode front: first node of this LinkedList
    @param LinkedListNode back: last node of this LinkedList
    @param int size: number of nodes in this LinkedList
                        a non-negative integer
    """
    def __init__(self):
        """
        Create an empty linked list.

        @param LinkedList self: this LinkedList
        @rtype: None
        """
        self.front, self.back, self.size = None, None, 0

    def __str__(self):
        """
        Return a human-friendly string representation of
        LinkedList self.

        @param LinkedList self: this LinkedList

        >>> lnk = LinkedList()
        >>> print(lnk)
        I'm so empty... experiencing existential angst!!!
        """
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "I'm so empty... experiencing existential angst!!!"
        else:
            return str(self.front)

    def prepend(self, value):
        """
        Insert value before LinkedList self.front.

        @param LinkedList self: this LinkedList
        @param object value: value for new LinkedList.front
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> str(lnk.front)
        '2 -> 1 -> 0 ->|'
        >>> lnk.size
        3
        """
        # Create new node with next_ referring to front
        new_node = LinkedListNode(value, self.front)
        # change front
        self.front = new_node
        # if the list was empty, change back
        if self.size == 0:
            self.back = new_node
        # update size
        self.size += 1

    def append(self, value):
        """
        Insert a new LinkedListNode with value after self.back.

        @param LinkedList self: this LinkedList.
        @param object value: value of new LinkedListNode
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.append(5)
        >>> lnk.size
        1
        >>> print(lnk.front)
        5 ->|
        >>> lnk.append(6)
        >>> lnk.size
        2
        >>> print(lnk.front)
        5 -> 6 ->|
        """
        new_node = LinkedListNode(value)
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        else:
            self.back.next_ = new_node
            self.back = new_node
        self.size += 1

    def __len__(self):
        """
        Return the number of nodes in LinkedList self.

        @param LinkedList self: this LinkedList
        @rtype: int

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(3)
        >>> lnk.size
        2
        """
        return self.size

    def copy(self):
        """
        Return a copy of LinkedList self.  The copy should have
        different nodes, but equivalent values, from self.

        @param LinkedList self: this LinkedList
        @rtype: LinkedList

        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk.prepend(7)
        >>> print(lnk.copy())
        7 -> 5 ->|
        """
        copy_list = LinkedList()
        original_node = self.front
        while original_node is not None:
            copy_list.append(original_node.value)
            original_node = original_node.next_
        return copy_list

    def __add__(self, other):
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        @param LinkedList self: this LinkedList
        @param LinkedList other: Linked list to concatenate to self
        @rtype: LinkedList

        >>> lnk1 = LinkedList()
        >>> lnk1.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(7)
        >>> print(lnk1 + lnk2)
        5 -> 7 ->|
        >>> print(lnk1)
        5 ->|
        >>> print(lnk2)
        7 ->|
        """
        if len(self) == 0:
            return other.copy()
        elif len(other) == 0:
            return self.copy()
        else:
            list1 = self.copy()
            list2 = other.copy()
            list1.back.next_ = list2.front
            list1.back = list2.back
            list1.size += list2.size
            return list1

    def swap_even(self, d=0):



if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()
