#!/usr/bin/python3
"""Defines a singly linked list"""


class Node:
    """Node class body"""
    def __init__(self, data, next_node=None):
        """Initialize a Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """Data setter"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Data getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Data setter"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""

    def __init__(self):
        """Initialize head of linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Insert node in coorect sorted position"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node

            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """Define the print() representation of a Singly linked list."""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return ('\n'.join(values))
