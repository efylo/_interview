from collections import deque


# a simple class for binary tree's node
class Node:
    def __init__(self, key, parent=None):
        self.val = key
        self.left = None
        self.right = None
        self.parent = parent

    def __repr__(self) -> str:
        return f'node[{self.val}]'
        pass


# a simple class for binary tree
class BinTree:
    def __init__(self):
        self.root = None
        pass

    def inorder(self):
        self.__inorder(self.root)

    def __inorder(self, root):
        if not root:
            return
        self.__inorder(root.left)
        print(root.val, end=" ")
        self.__inorder(root.right)

    # level-order insertion
    def insert(self, key):
        # tree empty
        if not self.root:
            self.root = Node(key)
            return
        # level queue
        q_level = deque([self.root])
        # FIFO ensures lower-level is always before higher-level
        while len(q_level) > 0:
            node = q_level.popleft()
            if not node.left:
                node.left = Node(key, node)
                break
            if not node.right:
                node.right = Node(key, node)
                break
            q_level.append(node.left)
            q_level.append(node.right)

    # level-order deletion
    def delete(self, key):
        # tree empty
        if not self.root:
            return
        # node to delete, node to move
        to_del, to_mov = None, None
        # queue for bfs along the tree
        q_level = deque([self.root])
        # find node to delete
        while len(q_level) > 0:
            node = q_level.popleft()
            if node.val == key:
                to_del = node
            if not not node.left:
                q_level.append(node.left)
            if not not node.right:
                q_level.append(node.right)
        to_mov = node
        # key not found
        if not to_del:
            return
        # make value of a node to delete to value of the deepest node
        to_del.val = to_mov.val
        # delete deepest node
        if not to_mov.parent.right:
            to_mov.parent.left = None
            return
        to_mov.parent.right = None
        return


    # returns height: int of the binary tree
    def height(self):
        return self.__h(self.root)

    def __h(self, root):
        if not root:
            return 0
        return 1+max(self.__h(root.left), self.__h(root.right))


def main():
    # binary tree object
    bt = BinTree()

    # insert 8 keys, which makes height = 4
    bt.insert(1)
    bt.insert(3)
    bt.insert(4)
    bt.insert(5)
    bt.insert(6)
    bt.insert(7)
    bt.insert(8)
    bt.insert(9)

    # delete a node, should make height = 3
    bt.delete(1)

    print(bt.height())

    # check if deletion successful
    bt.inorder()


if __name__ == "__main__":
    main()