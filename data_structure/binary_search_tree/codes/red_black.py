from collections import deque


class Node:
    def __init__(self, val, parent=None, color='r') -> None:
        self.val = val
        self.left = NIL(self)
        self.right = NIL(self)
        self.color = color
        self.parent = parent
    
    def isLeaf(self, ):
        return not self.left.val and not self.right.val

    def changeColor(self, ):
        self.color = 'b' if self.color == 'r' else 'r'
        return self

    def __repr__(self) -> str:
        return f'key = {self.val}, color = {self.color}'


# NIL(Null in leaf)
class NIL(Node):
    def __init__(self, parent=None) -> None:
        self.val = None
        self.color = 'b'
        self.parent = parent
    
    def isNIL(self, ):
        return True


class RedBlackTree:
    def __init__(self) -> None:
        self.root = None

    # a search algorithm for given val
    def search(self, val):
        return self.__search(self.root, val)

    def __search(self, root: Node, val):
        if not root or not root.val or root.val == val:
            return root
        if root.val > val:
            return self.__search(root.left, val)
        return self.__search(root.right, val)

    # method for searching the node of min/max value
    def searchMin(self, root: Node):
        if not root.left.val:
            return root
        return self.searchMin(root.left)
    
        
    
    def delete(self, val):
        _, bb = self.__std_delete(self.root, val)
        # print(bb, bb.parent)
        # _ is always self.root

    def __std_delete(self, root: Node, val):
        # if not root:
        #     return root, root
        if not root.val:
            return root, root
        if root.val == val:
            # when left node is NIL
            if not root.left.val:
                temp = root.right
                p = root.parent
                if root.color == 'b':
                    if temp.color == 'r':
                        temp.color = 'b'
                    else:
                        temp.color = 'bb'
                del root
                temp.parent = p
                return temp, temp

            if not root.right.val:
                temp = root.left
                p = root.parent
                if root.color == 'b':
                    if temp.color == 'r':
                        temp.color = 'b'
                    else:
                        temp.color = 'bb'
                del root
                temp.parent = p
                return temp, temp
            
            successor = self.searchMin(root.right)
            s_key = successor.val
            root.right, bb = self.__std_delete(root.right, s_key)
            root.val = s_key
            return root, bb

        if root.val > val:
            root.left, bb = self.__std_delete(root.left, val)
            return root, bb
        if root.val < val:
            root.right, bb = self.__std_delete(root.right, val)
            return root, bb
        





    # a insertion algorithm for given val
    def insert(self, val):
        self.root = self.__std_insert(self.root, val)
        x = self.search(val)
        
        self.__red_black_insert(x)

    def __std_insert(self, root: Node, val):
        if not root or not root.val:
            x = Node(val)
            return x
        if root.val > val:
            root.left = self.__std_insert(root.left, val)
            root.left.parent = root
        if root.val < val:
            root.right = self.__std_insert(root.right, val)
            root.right.parent = root
        return root
    
    def __red_black_insert(self, x: Node):
        # got no parent == root node
        if not x.parent:
            x.color = 'b'
            self.root = x
            return self.root
        # got no grand parent == parent is root node
        if not x.parent.parent:
            return x
        # x.parent.color == 'r' ensures x have grandparent?
        if x.parent.color == 'r':
            gp = x.parent.parent
            # since grandparent node can change
            # need to keep previous grandparent's value
            prev_val = gp.val
            uncle = gp.left if gp.right and gp.right.val == x.parent.val else gp.right
            # only when parent & uncle's color is both red
            # need consideration upon grandparent's color
            # if grandparent is root node, need to change
            if uncle and uncle.color == 'r':
                x.parent.color = 'b'
                uncle.color = 'b'
                gp.color ='r'
                gp = self.__red_black_insert(gp)
            # when parent is red, uncle is black
            # rotation of a tree w.r.t grandparent and parent node
            else:
                case1 = 'L' if gp.left and gp.left.val == x.parent.val else 'R'
                case2 = 'L' if x.parent.left and x.parent.left.val == x.val else 'R'
                if case1 == 'L':
                    if case2 == 'R':
                        gp.left = self.__L_rotate(x.parent, x)
                    gp = self.__R_rotate(gp.left, gp)
                    gp.color = 'b'
                    gp.right.color = 'r'
                if case1 == 'R':
                    if case2 == 'L':
                        gp.right = self.__R_rotate(x, x.parent)
                    gp = self.__L_rotate(gp, gp.right)
                    gp.color = 'b'
                    gp.left.color = 'r'
            # if grandparent is root node
            if not gp.parent:
                self.root = gp
                return gp
            # else when grandparent has grand-grand parent
            if gp.parent.left and gp.parent.left.val == prev_val:
                gp.parent.left = gp
            else:
                gp.parent.right = gp
            return gp
    
    # y.left == x, x.parent == y
    def __R_rotate(self, x: Node, y: Node) -> Node:
        xR = x.right
        yP = y.parent
        if not not xR:
            xR.parent = y
        y.left = xR
        y.parent = x
        x.parent = yP
        x.right = y
        return x
    
    # x.right == y, y.parent == x
    def __L_rotate(self, x:Node, y: Node) -> Node:
        yL = y.left
        xP = x.parent
        if not not yL:
            yL.parent = x
        x.right = yL
        x.parent = y
        y.parent = xP
        y.left = x
        return y
        
    
def printNode(root: Node):
    q = deque([root])
    while len(q) > 0:
        node = q.popleft()
        if not not node:
            print(node)
            if not not node.left.val:
                q.append(node.left)
            if not not node.right.val:
                q.append(node.right)


rbt = RedBlackTree()

rbt.insert(3)
rbt.insert(21)
rbt.insert(32)
rbt.insert(17)
rbt.insert(8)
rbt.insert(1)

rbt.delete(21)

print(rbt.search(32).right)

printNode(rbt.root)