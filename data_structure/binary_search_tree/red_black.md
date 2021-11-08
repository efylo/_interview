# Red-Black Tree

## Abstract

Algorithm for building quite a balanced binary search tree. But not as balanced as AVL tree. Though, Red-Black tree can perform better if there are much more insertions and deletions than searches. 

Red-Black came from the feature that nodes of red-black tree has either red or black color. 

Due to self-balancing features, it is hard to implement on your own. Programming languages like Java, C++ STL supports binary search tree using Red-Black tree. 

---

## Rules

1. Every node has a colour either red or black
2. The root node is always black
3. There are no two adjacent red nodes
4. Every path from a node to its descendants Null node has same number of black nodes

---

## Insert Algorithm

1. insert a red node via standard insert algorithm of binary search tree
2. if the node is root, then make node's color black
3. if the node's parent has red color, find the color of uncle's. 
   - the uncle is sibling of the parent, (if parent = right node of grandparent, then uncle = left node. and vice versa)
4. if the color of uncle is red, change the color of parent and uncle node to black. and change the color of grandparent to the red. 
   - go back to 2'nd route, making the node to the node's grandparent. 
5. if not, rotate the tree via grandparent and parent node. 
   - this rotation algorithm is really complicated, and have 4 different rotations via parent & child's position. 

### Assumptions

- when the node's parent is red, it assures that the node has grandparent
- Null node is considered black
- due to constraint in direct memory access in python, I used a pointer to the parent node in implementation
- use of a pointer to the parent node makes more considerations upon inserting a node

---

## Codes

- [red-black.py](./codes/red-black.py)

---

## Reference

- [Red-Black Tree | Set 1 (Introduction)](https://www.geeksforgeeks.org/red-black-tree-set-1-introduction-2/)
- [Red-Black Tree | Set 2 (Insert)](https://www.geeksforgeeks.org/red-black-tree-set-2-insert/)