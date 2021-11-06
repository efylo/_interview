# Binary Tree

## Abstract

A binary tree is a tree which its elements have at most 2 children. Typically these children are named 'left' and 'right'. 

Prior data structures are linear(stack, queue, array, linked lists). Though trees are not linear, they are hierarchical. 

vocabs.: *root* = the topmost node, *leaves* = with no children

---

## Features

- hierarchical structure, e.g) the file system
- moderate access, search - if tree is in its order
- moderate insertion, deletion
- dynamic - no limitation on size

---

## Applications

- manipulate hierarchical data
- make information ease in search(traversal)
- manipulate sorted lists of data
- workflow for compositing digital images for visual effects
- router algorithms(network is kind of tree)
- form of a multi-stage decision-making

---

## Properties

1. The maximum number at level *l* is *2^l*
   - level 0 can have 1 node, level 1 can have 2 nodes, ...
2. The maximum number of height *h* is *2^h-1*
   - height 1 can have 1 node, height 2 can have 3 nodes, ...
3. within *N* nodes, minimum possible height is *Log_2(N+1)*
   - for binary tree with 7 nodes, minimum height is 3
4. within *L* leaves, minimum *Log_2(L)+1* levels possible
5. every node with 0 or 2 children, the number of leaf nodes is one more than nodes with two children

---

## Types

- Full Binary Tree - every node has 0 or 2 children
- Complete Binary Tree - all the levels are maximally filled
- Perfect Binary Tree - all the levels are perfectly filled, *2^l* nodes at level *l*
- Balanced Binary Tree - height of the tree is O(Log n)
  - AVL tree, Red-Black tree
  - shows good-performance
- A Degenerate(or pathological) Tree - every node has one child

---

## Code

```python
# a simple node for binary tree
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
```

---

## Reference

- [Binary Tree Data Structure](https://www.geeksforgeeks.org/binary-tree-data-structure/)
- [Binary Tree | Set 1 (Introduction)](https://www.geeksforgeeks.org/binary-tree-set-1-introduction/)
- [Binary Tree | Set 2 (Properties)](https://www.geeksforgeeks.org/binary-tree-set-2-properties/)
- [Binary Tree | Set 3 (Types of Binary Tree)](https://www.geeksforgeeks.org/binary-tree-set-3-types-of-binary-tree/)