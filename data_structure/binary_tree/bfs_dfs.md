# Search Algorithms

## Abstract

Search algorithms of a tree

- Breadth First Traversal(Level Order)
- Depth First Traversals
  - Inorder, Preorder, Postorder

Problems of size, height, maximum, minimum, ...

---

## Breadth First Traversal(Search)

Firstly searching for a node in current level, then the next level. 

Typically implemented by queue, dequeue-search the node and enqueue children of the node. 

```python
from collections import deque

# tree - root(Node)
def BFS(tree):
    q = deque([tree.root])
    # while any element is in the queue
    while len(q) > 0:
        node = q.popleft()
        f(node) # any possible functionalities
        if not not node.left:
            q.append(node.left)
        if not not node.right:
            q.append(node.right)
```

---

## Depth First Traversal(Search)

In traversing through current node, then search goes to the child node. 

```python
from collections import deque

# Recursive DFS
def DFS(node):
    # node is None
    if not node:
        return
    # inorder traversal
    DFS(node.left)
    f(node)
    DFS(node.right)

# DFS without function-call(recursive)
def DFS2(node):
    stack = deque([node])
    
    while len(stack) > 0:
        if not not node.left:
            stack.append(node.left)
            node = node.left
            continue
        node = stack.pop()
        if not not node.right:
            stack.append(node.right)
            node = node.right
            continue
```

---

## Differences

### Time Complexity

- O(n) for all traversals

### Extra Space

- assume w is maximum width, BFS need O(w) extra space
  - extra space is in the queue
- assume h is maximum height, DFS need O(h) extra space
  - extra space is in the stack(function-call)
- with balanced tree, generally maximum w > h
- with skewed tree, generally maximum h > w

### Nodes

- BFS start from root node
- DFS start from leaves(except preorder)

---

## Code

- [binary_tree.py](./codes/binary_tree.py)
- [traversal.py](./codes/traversal.py)

---

## Reference

- [BFS vs DFS for Binary Tree](https://www.geeksforgeeks.org/bfs-vs-dfs-binary-tree/)

