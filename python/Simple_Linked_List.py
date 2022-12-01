"""Simple Linked List

https://exercism.org/tracks/python/exercises/simple-linked-list
"""

class Node:
    """A node of a linked list.

    Parameters:
    :param value: int - The value of the node.
    :param next: Node - The next node in the linked list.
    
    Attributes:
    :_value: - The value of the node.
    :_next: - The next node in the linked list.
    
    Methods:
    :value(): - Return the value of the node.
    :next(): - Return the next node in the linked list.

    Raises:
    None
    """
    def __init__(self, value: int, next: "Node") -> "Node":
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next

class LinkedList:
    """Representation of a LIFO linked list.

    Parameters:
    :param values: list[int]=[] - An initial set of values used to create the linked list.
    
    Attributes:
    :_head: - The current head node.
    :_nodes: - The nodes of the linked list in a list.
    
    Methods:
    :head(): - Return the last node of the linked list.
    :push(value): - Add a new node to the end of the linked list.
    :pop(): - Return the value of and remove from the linked list the current head node.
    :reversed(): - Return the reversed values of the linked list.
    
    Raises:
    :EmptyListException: - Raised if the linked list is empty.
    """
    def __init__(self, values: list[int]=[]) -> "LinkedList":
        self._head = None
        self._nodes = []
        for v in values:
            self.push(v)

    def __len__(self):
        return len(self._nodes)

    def __iter__(self):
        return iter([n.value() for n in self._nodes[::-1]])

    def head(self) -> "Node":
        if not self._nodes:
            raise EmptyListException("The list is empty.")
        return self._head

    def push(self, value: int) -> None:
        self._head = Node(value, self._head)
        self._nodes.append(self._head)

    def pop(self) -> int:
        if not self._nodes:
            raise EmptyListException("The list is empty.")
        node = self._head
        self._head = self._head.next()
        self._nodes.pop()
        return node.value()

    def reversed(self) -> "LinkedList":
        return LinkedList(self)

class EmptyListException(Exception):
    """Exception raised when the linked list is empty.

    Parameters:
    :param message: str - A message to provide with the error.

    Attributes:
    :_message: str - An explanation of the error.

    Methods:
    None

    Raises:
    None
    """
    def __init__(self, message: str):
        self._message = message
