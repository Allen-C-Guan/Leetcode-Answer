class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root):
        self.root = root

    def inOrder(self, root):
        if root is not None:
            self.inOrder(root.left)
            # 这个递归不能加return， 递归中return只有两种情况下才有，1 递归出口， 当前括号的结果，这个题中，很明显，不需要每个括号要有结果，括号内已经完成了内容
            # 如果有了return，则意味着括号结束！！！
            print(root.val)
            self.inOrder(root.right)
        return  # 这才是括号的结尾

    def preOrder(self, root):
        if root is not None:
            print(root.val)
            self.preOrder(root.left)
            self.preOrder(root.right)


t1 = Node(1)
t2 = Node(2)
t3 = Node(3)

t1.left = t2
t1.right = t3

tree = Tree(t1)

tree.preOrder(t1)

tree.inOrder(t1)
