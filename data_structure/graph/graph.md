# Graph

## Abstract

a graph consists of a finite set of vertices(or nodes) and set of edges which connect a pair of nodes. 

edge is in the form (u, v) where u, v are vertices. 

if directed graph, (u, v) != (u, v)

in weighted graph, the edge (u, v) contains weight(value, cost, etc)

---

## Representation

### 1. Adjacency Matrix

- the number of vertices *V*, adjacency matrix is a matrix of size *V* x *V*
- matrix[a] [b] represents an edge from vertex a to b. 
- if matrix[a] [b] == 1, then there is (a, b) edge. 
- if undirected graph, matrix[a] [b] == matrix[b] [a] (symmetric)
- if weighted, matrix[a] [b] = w
- search, insert, delete are fast, O(1)
- use more space, O(V^2)

### 2. Adjacency List

- an array of lists, the size of array = *V*
- array[a] refers the list of vertices adjacent to vertex a
- if weighted, array[a] = (b, w_ab), edge from a to b with weigh w_ab
- use less space, O(|V| + |E|)
- search queries are slow, O(V)

---

## Implementation

### in Python

Implementation of adjacency list is quite simple. Using defaultdict class of collections module is one of the implementations. Since later nodes can be added to the graph first, use of defaultdict class is recommended. 

You may add some attributes inside the class. Some possible attributes are *directed*, *weighted*, etc. 

### Codes

- [graph.py](./codes/graph.py)

---

## Traversal

Different from other non-linear data structures, graph may contain cycles. the solution is using an array of bools (visited or not). both breadth-first-search(BFS) and depth-first-search(DFS) is possible. 

Similar to tree-traversals, BFS uses queue and DFS uses stack(recursive call) in implementation. 

Inside a graph, there may exist isolated nodes that cannot be reached if starting from some nodes. So, for BFS or DFS to traverse all nodes inside the graph, integrated visited array should be supervised so that all nodes are visited. 

---

## Reference

- [Graph Data Structure And Algorithms](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/)
- [Graph and its representations](https://www.geeksforgeeks.org/graph-and-its-representations/)
- [Breadth First Search or BFS for a Graph](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
- [Depth First Search or DFS for a Graph](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)

