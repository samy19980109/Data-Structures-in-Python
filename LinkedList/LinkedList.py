""" practice on linked lists
"""


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
        # start with a string s to represent current node.
        s = "{} ->".format(self.value)
        # create a reference to "walk" along the list
        current_node = self.next_
        # for each subsequent node in the list, build s
        while current_node is not None:
            s += " {} ->".format(current_node.value)
            current_node = current_node.next_
        # add "|" at the end of the list
        assert current_node is None, "unexpected non_None!!!"
        s += "|"
        return s

    def __eq__(self, other):
        """
        Return whether LinkedListNode self is equivalent to other.

        @param LinkedListNode self: this LinkedListNode
        @param LinkedListNode|object other: object to compare to self.
        @rtype: bool

        >>> LinkedListNode(5).__eq__(5)
        False
        >>> n1 = LinkedListNode(5, LinkedListNode(7))
        >>> n2 = LinkedListNode(5, LinkedListNode(7, None))
        >>> n1.__eq__(n2)
        True
        """

        node_type = type(self) == type(other)
        return node_type and self.value == other.value and (self.next_
                                                            == other.next_)


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
        # deal with the case where this list is empty
        if self.front is None:
            assert self.back is None and self.size is 0, "ooooops!"
            return "I'm so empty... experiencing existential angst!!!"
        else:
            # use front.__str__() if this list isn't empty
            return str(self.front)

    def __eq__(self, other):
        """
        Return whether LinkedList self is equivalent to
        other.

        @param LinkedList self: this LinkedList
        @param LinkedList|object other: object to compare to self
        @rtype: bool

        >>> LinkedList().__eq__(None)
        False
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.prepend(5)
        >>> lnk.__eq__(lnk2)
        True
        """
        return type(self) == type(other) and self.front == other.front and (
            self.back == other.back and self.size == other.size)

    def delete_after(self, value):
        """
        Remove the node following the first occurrence of value, if
        possible, otherwise leave self unchanged.

        @param LinkedList self: this LinkedList
        @param object value: value just before the deletion
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(2)
        >>> lnk.prepend(2)
        >>> lnk.delete_after(2)
        >>> lnk.size
        1
        >>>
        """
        # Checks if the size of linked list is 0
        if self.size != 0:
            # checks if the value is in the linked list
            if self.__contains__(value):
                # run the loop over to assign current to required node
                current = self.front
                while current.value != value:
                    current = current.next_
                # checks if the value is the last item in the list
                if current.next_ is not None:
                    # if not then break the link and connect to next one
                    current.next_ = current.next_.next_
                    self.size -= 1
        else:
            assert self.back is None and self.front is None, "ooops"

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
        # create the new node
        new_node = LinkedListNode(value)
        # if the list is empty, the new node is front and back
        if self.size == 0:
            assert self.back is None and self.front is None, "ooops"
            self.front = self.back = new_node
        # if the list isn't empty, front stays the same
        else:
            # change *old* self.back.next_ first!!!!
            self.back.next_ = new_node
            self.back = new_node
        # remember to increase the size
        self.size += 1

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

    def delete_front(self):
        """
        Delete LinkedListNode self.front from self.

        Assume self.front is not None

        @param LinkedList self: this LinkedList
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(0)
        >>> lnk.prepend(1)
        >>> lnk.prepend(2)
        >>> lnk.delete_front()
        >>> str(lnk.front)
        '1 -> 0 ->|'
        >>> lnk.size
        2
        >>> lnk.delete_front()
        >>> lnk.delete_front()
        >>> str(lnk.front)
        'None'
        """
        assert self.front is not None, "unexpected None!"
        # if back == front, set it to None
        if self.front == self.back:
            self.back = None
        # set front to its successor
        self.front = self.front.next_
        # decrease size
        self.size -= 1

    def __setitem__(self, index, value):
        """
        Set the value of list at position index to value. Raise IndexError
        if index >= self.size

        @param LinkedList self: this LinkedList
        @param int index: position of list to change
        @param object value: new value for linked list
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(2)
        >>> lnk.prepend(2)
        >>> lnk.prepend(2)
        >>> print(lnk)
        2 -> 2 -> 2 ->|
        >>> lnk.__setitem__(2, 1)
        >>> print(lnk)
        2 -> 2 -> 1 ->|
        >>> lnk = LinkedList()
        >>> lnk.prepend(5)
        >>> print(lnk)
        5 ->|
        >>> lnk[0] = 7
        >>> print(lnk)
        7 ->|
        """
        # Checks if the index in range
        if (-self.size > index
                or index >= self.size):
            raise IndexError("out of range!!!")
        elif index < 0:
            # adjust negative index according to its positive index
            index += self.size
        current_node = self.front
        # going through the index to reach desired index
        for _ in range(index):
            # Raise error if there is a None before reching index
            assert current_node is not None, "unexpected None!!!!!"
            current_node = current_node.next_
        assert current_node is not None, "unexpected None!!!!!"
        current_node.value = value

    def __add__(self, other):
        """
        Return a new list by concatenating self to other.  Leave
        both self and other unchanged.

        @param LinkedList self: this LinkedList
        @param LinkedList other: Linked list to concatenate to self
        @rtype: LinkedList

        >>> lnk1 = LinkedList()
        >>> lnk1.append(5)
        >>> lnk2 = LinkedList()
        >>> lnk2.append(7)
        >>> print(lnk1 + lnk2)
        5 -> 7 ->|
        """
        added_lnk = LinkedList()
        if self.front is None:
            return other
        elif other.front is None:
            return self
        elif other.front is None and self.front is None:
            return added_lnk
        else:
            c1, c2 = self.front, other.front
            while c1 is not None:
                added_lnk.append(c1.value)
                c1 = c1.next_
            while c2 is not None:
                added_lnk.append(c2.value)
                c2 = c2.next_
            return added_lnk

    def insert_before(self, value1, value2):
        """
        Insert value1 into LinkedList self before the first occurrence
        of value2, if it exists.  Otherwise leave self unchanged.

        @param LinkedList self: this LinkedList
        @param object value1: value to insert, if possible
        @param object value2: value to insert value1 ahead of
        @rtype: None

        >>> lnk = LinkedList()
        >>> lnk.prepend(2)
        >>> lnk.prepend(2)
        >>> lnk.prepend(2)
        >>> lnk.insert_before(1, 2)
        >>> print(lnk)
        1 -> 2 -> 2 -> 2 ->|
        """
        if self.__contains__(value2):
            if self.size == 1 or self.front.value == value2:
                self.prepend(value1)
            else:
                current_node, prev_node = self.front, self.front
                while current_node.value != value2:
                    prev_node = current_node
                    current_node = current_node.next_
                prev_node.next_ = LinkedListNode(value1, current_node)

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
        >>> lnk2 = LinkedList()
        >>> print(lnk2.copy())
        I'm so empty... experiencing existential angst!!!
        """
        copy_lnk = LinkedList()
        current = self.front
        if self.size == 0:
            return copy_lnk
        while current is not None:
            assert current is not None, "unexpected None!!!!!"
            copy_lnk.append(current.value)
            current = current.next_
        return copy_lnk

    def __len__(self):
        """
        Return the number of nodes in LinkedList self.

        @param LinkedList self: this LinkedList
        @rtype: int

        >>> lnk = LinkedList()
        >>> len(lnk)
        0
        >>> lnk.prepend(20)
        >>> lnk.prepend(10)
        >>> lnk.delete_front()
        >>> len(lnk)
        1
        """
        # return the size of the LinkedList
        return self.size

    def __getitem__(self, index):
        """
        Return the value at LinkedList self's position index.

        @param LinkedList self: this LinkedList
        @param int index: position to retrieve value from
        @rtype: object

        >>> lnk = LinkedList()
        >>> lnk.append(1)
        >>> lnk.append(0)
        >>> lnk.__getitem__(1)
        0
        >>> lnk[-1]
        0
        """
        # deal with a negative index by adding self.size
        if (-self.size > index
                or index > self.size):
            raise IndexError("out of range!!!")
        elif index < 0:
            index += self.size
        current_node = self.front
        # walk index steps along from 0 to retrieve element
        for _ in range(index):
            assert current_node is not None, "unexpected None!!!!!"
            current_node = current_node.next_
        # return the value at position index
        return current_node.value

    def __contains__(self, value):
        """
        Return whether LinkedList self contains value.

        @param LinkedList self: this LinkedList.
        @param object value: value to search for in self
        @rtype: bool

        >>> lnk = LinkedList()
        >>> lnk.append(0)
        >>> lnk.append(1)
        >>> lnk.append(2)
        >>> 2 in lnk
        True
        >>> lnk.__contains__(3)
        False
        """
        current_node = self.front
        # "walk" the linked list
        while current_node is not None:
            # if any node has a value == value, return True
            if current_node.value == value:
                return True
            current_node = current_node.next_
        # if you get to the end without finding value,
        # return False
        return False

    def remove_first_double(self):
        """
        >>> list_ = LinkedList()
        >>> list_.append(4)
        >>> list_.append(2)
        >>> list_.append(2)
        >>> list_.append(3)
        >>> list_.append(3)
        >>> print(list_.front)
        3 -> 2 -> 2 -> 3 -> 3 ->|
        >>> list_.remove_first_double()
        >>> print(list_.front)
        3 -> 2 -> 3 -> 3 ->|

        """

        c = self.front
        n = c.next_
        while n and c.value != n.value:
            c = c.next_
            n = n.next_
        c.next_ = n.next_

        if c.next_ is None:
            self.back = c
        self.size -= 1

    def merge_list2(self, other):
        """
        >>> l1 = LinkedList()
        >>> l1.append(1)
        >>> l1.append(3)
        >>> l1.append(5)
        >>> l2 = LinkedList()
        >>> l2.append(2)
        >>> l2.append(4)
        >>> l2.append(6)
        >>> l2.append(7)
        >>> l1.merge_list2(l2)
        >>> print(l1)"""
        c1 = self.front
        c2 = other.front
        p1, p2 = c1, c2
        while p2 is not None and c1 is not None:
            while c2.value > c1.value:
                    p1 = c1
                    c1 = c1.next_
            p1.next_ = LinkedListNode(c2.value)
            p1.next_.next_ = c1
            c2 = c2.next_

        c1.next_ = c2
        self.back = other.back









            # p1 = c1
            # c1 = c1.next_
            # if c1.value > c2.value:
            #     p1.next_ = c2
            #     c2.next_ = c1
            #     c2 = p1.next_


    # def reversed_linked_list(self):
    #     """
    #     >>> list_ = LinkedList()
    #     >>> list_.append(2)
    #     >>> list_.append(2)
    #     >>> list_.append(3)
    #     >>> list_.append(3)
    #     >>> print(list_.front)
    #     >>>
    #     3 -> 2 -> 2 -> 3 -> 3 ->|
    #     >>> list_.reversed_linked_list()
    #     >>> print(list_.front)
    #     >>> print(list_.back)
    #     """
    #
    #     # if self.size <= 1:
    #     #     pass
    #     # else:
    #     #     c = self.front
    #     #     b = self.front
    #     #     n = c.next_
    #     #     self.front.next_ = None
    #     #     while n is not None:
    #     #
    #     #         x = n.next_
    #     #         n.next_ = c
    #     #         c = n
    #     #         n = x
    #     #     self.front = c
    #     #     self.back = b
    #
    #
    #  def merge_lists(self, other):
    #      """ Merge two linked lists"""
    #      new = LinkedList()
    #      c1 = self.front
    #      c2 = other.front
    #      while c1 is not None and c2 is not None:
    #          if c1.value < c2.value:
    #              new.front = c1
    #              c1 = c1.next_
    #          else:
    #              new.front = c2
    #              c2 = c2.next_
    #      if c1 is None:
    #         while c2 is not None:
    #             new.back = other.back
    #             new.back = self.back




def merge_list(L1, L2):
    """ addfad
    """
    i1 = 0
    i2 = 0
    L = []
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] < L2[i2]:
            L.append(L1[i1])
            i1 += 1
        else:
            L.append(L2[i2])
            i2 += 1

    return L + L1[i1:] + L2[i2:]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config="pylint.txt")
