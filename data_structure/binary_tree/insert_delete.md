# Insertion & Deletion

## Abstract

insertion and deletion in a level order can guarantee that a binary tree is balanced enough. balanced enough means that the height of the tree is minimum among possible heights. 

to ensure the minimum height of a binary tree, need to manipulate thoroughly. implementation using queue that saves nodes of the same level may be probable. 

---

## Insertion(key)

1. BFS the binary tree, search a node with null child
2. Assert a node of given key into the position of null child
3. After assertion, **return**

---

## Deletion(key)

1. if tree is empty, **return**
2. BFS for a node to delete and the last node
3. if a node to delete is not found, **return**
4. assert value of the last node into value of a node to delete
5. delete the last node
   - use of a pointer to parent node makes it easier

---

## BFS(Breadth-First Search)

- an algorithm to search for something in a tree
- breadth-first meaning keys within same height is searched consequently
- queue implementation - **dequeue** an item, then enqueue the item's children **while** queue has item(s)

---

## Reference

- [Insertion in a Binary Tree in level order](https://www.geeksforgeeks.org/insertion-in-a-binary-tree-in-level-order/)
- [Deletion in a Binary Tree](https://www.geeksforgeeks.org/deletion-binary-tree/)

