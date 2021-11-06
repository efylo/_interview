from binary_tree import Node, BinTree
from collections import deque


def printNode(node: Node):
    print(node.val, end=" ")


def BFS(tree: BinTree):
    q = deque([tree.root])

    while len(q) > 0:
        node = q.popleft()
        # any function possible, here I just used function to print node
        printNode(node)
        # next-level nodes are always behind prev-level nodes
        if not not node.left:
            q.append(node.left)
        if not not node.right:
            q.append(node.right)


# inorder = left - root - right
def inorder(tree: BinTree):
    __inorder(tree.root)


def __inorder(node: Node):
    # node is None
    if not node:
        return
    __inorder(node.left)
    printNode(node)         # like before, any function possible
    __inorder(node.right)


# preorder = root - left - right
def preorder(tree: BinTree):
    __preorder(tree.root)


def __preorder(node: Node):
    if not node:
        return
    printNode(node)
    __preorder(node.left)
    __preorder(node.right)


# postorder = left - right - root
def postorder(tree: BinTree):
    __postorder(tree.root)


def __postorder(node: Node):
    if not node:
        return
    __postorder(node.left)
    __postorder(node.right)
    printNode(node)


def DFS2(node):
    stack = deque([node])
    
    while len(stack) > 0:
        if not not node.left:
            stack.append(node.left)
            node = node.left
            continue
        node = stack.pop()
        printNode(node)
        if not not node.right:
            stack.append(node.right)
            node = node.right
            continue


def main():
    cnt = int(input("enter num. of elements: "))
    bin_tree = BinTree()
    while cnt > 0:
        x = input()
        bin_tree.insert(x)
        cnt -= 1
    
    DFS2(bin_tree.root)

    print("BFS: ", end="")
    BFS(bin_tree)

    print("\ninorder: ", end="")
    inorder(bin_tree)

    print("\npreorder: ", end="")
    preorder(bin_tree)

    print("\npostorder: ", end="")
    postorder(bin_tree)


if __name__ == "__main__":
    main()