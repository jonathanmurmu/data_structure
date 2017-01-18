__author__ = 'jonathanm'


class Node(object):
    """Node class."""

    def __init__(self, data):
        """Function to initialize the node object"""
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


class LinkedList(object):
    """Linked List class."""
    def __init__(self):
        """Function to initialize the Linked List object"""
        self.head = None

    def print_list(self):
        """Traverse the list and print the linked list."""
        node_data = self.head
        while node_data:
            print node_data.data, '->',
            node_data = node_data.next

    def push(self, new_data):
        """Add a node in the beginning of the linked list."""
        # Allocate the Node & Put in the data
        new_node = Node(new_data)

        # Make next of new Node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_data