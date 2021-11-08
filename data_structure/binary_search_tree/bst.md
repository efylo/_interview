# Binary Search Tree

## Abstract

A binary tree with some constraints(properties)

- The left subtree of a node has keys lesser than the node's
- The right subtree of a node has keys greater than the node's
- Left and right subtree are a binary search tree, and no duplicate nodes possible

---

## Insertion

a function to insert a given key, not violates above properites

- input: a node, a key
- goes left if given key is lesser, right if greater
- upon finding a null node, insert a key to the node

---

## Search

a function to find a given key, O(log n)

- input: a key
- goes left if given key is lesser, right if greater
- upon finding a corresponding node, returns

---

## Delete

a function to delete a given key, have 3 situations

1. a leaf node: just delete
2. has a child: delete - move a child to the parent's position
3. has both children - use of key's successor, predecessor

### Successor

a key slightly greater than the key to delete

1. successor doesn't have a left node
2. delete a successor - can delete since it has only child
3. move a successor's key to a node of the key to delete

---

## Reference

- [Binary Search Tree](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)
- [Binary Search Tree | Set 1 (Search and Insertion)](https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/)
- [Binary Search Tree | Set 2 (Delete)](https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/)

