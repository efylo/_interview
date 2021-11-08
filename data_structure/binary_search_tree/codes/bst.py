from collections import deque
from typing import Iterable


class Node:
    def __init__(self, key) -> None:
        self.key = key
        self.left = None
        self.right = None

    def isLeaf(self, ) -> bool:
        return not self.left and not self.right

    def __repr__(self) -> str:
        return f'key = {self.key}'


class BST:
    def __init__(self) -> None:
        self.root = None
    
    # insertion to root node
    def insert(self, key):
        self.root = self.__insert(self.root, key)
        return self.root
    
    def insertIter(self, iter_key: Iterable):
        # root node
        root = Node(iter_key[0])
        self.root = root
        i, l = 1, len(iter_key)
        while i < l:
            key = iter_key[i]
            self.__insert(root, key)
            if key > root.key:
                root = root.right
            i += 1
        
    # recursive insertion
    def __insert(self, node, key):
        if not node:
            return Node(key)
        if key == node.key:
            return node
        if key < node.key:
            node.left = self.__insert(node.left, key)
        if key > node.key:
            node.right = self.__insert(node.right, key)
        return node
    
    # returns a node or None(not found)
    def search(self, key):
        return self.__search(self.root, key)

    def __search(self, node, key):
        # found / not found
        if not node or key == node.key:
            return node
        # search for left node
        if key < node.key:
            return self.__search(node.left, key)
        # search for right node
        return self.__search(node.right, key)
    
    # search for minimum node
    def minNode(self, node):
        if not node.left:
            return node
        return self.minNode(node.left)
    
    # search for maximum node
    def maxNode(self, node):
        if not node.right:
            return node
        return self.minNode(self.right)

    def delete(self, key):
        self.root = self.__delete(self.root, key)
    
    def __delete(self, node, key):
        # null node
        if not node:
            return node
        
        # key to delete is lesser than node's key
        # search for left node, 
        # if key searched then left node is naturally modified
        if key < node.key:
            node.left = self.__delete(node.left, key)
            return node
        elif key > node.key:
            node.right = self.__delete(node.right, key)
            return node

        # when the key is found
        else:
            # when left node is none(also includes leaf node)
            # a node is deleted, then right node goes to the node's position
            if not node.left:
                temp = node.right
                del node
                return temp
            # similar, when right node is none
            if not node.right:
                temp = node.left
                del node
                return temp
            # else when both children exists
            # search for successor, deletes the successor
            # and change the deleted node's key to the successor's key
            successor = self.minNode(node.right)
            s_key = successor.key
            self.__delete(node, s_key)
            node.key = s_key
            return node

    def height(self, ):
        return self.__height(self.root)
    
    def __height(self, node):
        if not node:
            return 0
        return 1 + max(self.__height(node.left), self.__height(node.right))


def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root)
    inorder(root.right)

bst = BST()
a = [10, 5, 1, 7, 40, 50]

bst.insertIter(a)

bst.delete(50)

inorder(bst.root)