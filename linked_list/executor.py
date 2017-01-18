__author__ = 'jonathanm'
from linked_list import Node, LinkedList


class Executor(object):
    """Executes the program."""

    def linked_list_intro_play(self):
        """ Linked List | Set 1 (Introduction)"""
        # Steps are:
        # 1. Create an empty list
        # 2. Create nodes
        # 3. Link the nodes.

        # Start with the empty list
        llist = LinkedList()

        llist.head = Node(1)
        second = Node(2)
        third = Node(3)

        '''
        Three nodes have been created.
        We have references to these three blocks as first,
        second and third

        llist.head        second              third
             |                |                  |
             |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  | None |     | 2  | None |     |  3 | None |
        +----+------+     +----+------+     +----+------+
        '''

        llist.head.next = second  # Link first node with second

        '''
        Now next of first Node refers to second.  So they
        both are linked.

        llist.head        second              third
             |                |                  |
             |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  | null |     |  3 | null |
        +----+------+     +----+------+     +----+------+
        '''

        second.next = third  # Link second node with the third node

        '''
        Now next of second Node refers to third.  So all three
        nodes are linked.

        llist.head        second              third
             |                |                  |
             |                |                  |
        +----+------+     +----+------+     +----+------+
        | 1  |  o-------->| 2  |  o-------->|  3 | null |
        +----+------+     +----+------+     +----+------+
        '''

        # traversing the entire linked list and printing
        llist.print_list()


# Code execution starts here
if __name__ == '__main__':
    obj = Executor()
    obj.linked_list_intro_play()