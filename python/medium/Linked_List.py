"""Linked List

https://exercism.org/tracks/python/exercises/linked-list
"""

class Node:
    """A node of a linked list.

    Parameters:
    :param value: int - The value of the node.
    :param next: Node - The next node in the linked list.
    :param prev: Node - The previous node in the linked list.
    
    Attributes:
    :_value: int - The value of the node.
    :_next: Node - The next node in the linked list.
    :_prev: Node - The previous node in the linked list.
    
    Methods:
    :value(): Return the value of the node.
    :next(): Return the next node in the linked list.
    :prev(): Return the previous node in the linked list.
    
    Raises:
    None
    """
    def __init__(self, value, next=None, prev=None):
        self._value = value
        self._next = next
        self._prev = prev

    def value(self):
        return self._value

    def next(self):
        return self._next

    def prev(self):
        return self._prev


class LinkedList:
    """A doubly linked list.

    Parameters:
    None
    
    Attributes:
    :length: int - The length of the linked list.
    :head: Node - The first node in the linked list.
    :tail: Node - The last node in the linked list.
    
    Methods:
    :push(value: int): Add a node with the given value to the front of the linked list.
    :pop(): Remove and return the node at the front of the linked list.
    :shift(): Remove and return the node at the end of the linked list.
    :unshift(value: int): Add a node with the given value to the end of the linked list.
    :__len__(): Return the length of the linked list.
    :__iter__(): Iterate through the nodes in the linked list.
    :delete(value: int): Remove the first node with the given value from the linked list.
    
    Raises:
    IndexError: If trying to pop or shift an empty list.
    ValueError: If trying to delete a value not found in the list.
    """
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def push(self, value: int):
        node = Node(value)

        if self.length == 0:
            self.tail = node
        else:
            self.head._next = node

        node._prev = self.head
        self.head = node

        self.length += 1

    def pop(self) -> int:
        if self.length == 0:
            raise IndexError("List is empty")

        head = self.head
        self.head = self.head._prev

        self.length -= 1

        return head.value()

    def shift(self) -> int:
        if self.length == 0:
            raise IndexError("List is empty")

        tail = self.tail
        self.tail = self.tail._next

        self.length -= 1

        return tail.value()

    def unshift(self, value: int):
        node = Node(value)

        if self.length == 0:
            self.head = node
        else:
            self.tail._prev = node

        node._next = self.tail
        self.tail = node

        self.length += 1

    def __len__(self) -> int:
        return self.length

    def __iter__(self):
        node = self.head

        while node != self.tail:
            yield node.value()
            node = node._prev

    def delete(self, value: int):
        if self.length == 0:
            raise ValueError("Value not found")

        node = self.head

        while node != self.tail and node.value() != value:
            node = node._prev

        if node.value() != value:
            raise ValueError("Value not found")

        if node == self.head:
            self.head = self.head._prev
        elif node == self.tail:
            self.tail = self.tail._next
        else:
            node._next._prev = node._prev
            node._prev._next = node._next

        self.length -= 1
