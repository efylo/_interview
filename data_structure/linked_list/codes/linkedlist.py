from typing import Any
from copy import *
# from dataclasses import dataclass


# class of Node
class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.next = None
    
    def __repr__(self) -> str:
        return f'Node(key={self.key}, next={self.next})'


# class of LinkedList - specific methods will be defined
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # print out all data in linked list, example for traversal
    def printList(self) -> None:
        node = self.head
        s = f'no nodes in the list' if not node else f'Keys in the list:  '
        print(s, end="")
        while not not node:
            print(f'{node.key}', end=", ")
            node = node.next
        print('')

    # add new node to the front of a linked list
    def push(self, key) -> None:
        node = Node(key)
        node.next = self.head
        self.head = node

    # add new node to the rear of a linked list
    def append(self, key) -> None:
        node = self.head
        while not not node.next:
            node = node.next
        node.next = Node(key)
    
    # add new node right after the given key
    def addAfter(self, prev_node, next_key) -> None:
        if not prev_node:
            return
        new_node = Node(next_key)
        next_node = prev_node.next
        new_node.next = next_node
        prev_node.next = new_node

    # iterative way of deletion - recursive not possible in python for singly linked list
    def delete(self, key) -> None:
        node = self.head

        # if head is to be deleted, and it's not none
        if not not node and node.key == key:
            to_del = node
            self.head = node.next
            del to_del
        else:
            # while next node exists
            while not not node.next:
                # next node is to deleted
                if node.next.key == key:
                    next_node = node.next.next
                    to_del = node.next
                    node.next = next_node
                    del to_del
                    break
                node = node.next

    # for representation
    def __repr__(self) -> str:
        return f'LinkedList(head={self.head})'


def main():
    # a linked list
    llist = LinkedList()

    # three nodes, any data type is possible
    head = Node('head')
    first = Node(1987)
    second = Node(3.14)

    # connect - without methods
    llist.head = head
    llist.head.next = first
    first.next = second

    # add new node to the front
    newHead = 'new captain'
    llist.push(newHead)

    # add new node at the end
    newTail = 'tail of a dragon'
    llist.append(newTail)

    # add new node after the given node
    newYear = 1988
    llist.addAfter(first, newYear)

    # delete node of 'head'(head) - 1988(between) - 'tail of a dragon'(tail)
    llist.delete('head')
    llist.delete(1988)
    llist.delete('tail of a dragon')

    # using a python class __repr__ can make automatic traversal through linked list
    # , though defining a function may be desirable
    llist.printList()


if __name__ == "__main__":
    main()