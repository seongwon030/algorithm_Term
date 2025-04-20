RED = True
BLACK = False

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'

class RedBlackTree:
    def __init__(self,data):
        self.nil = Node(None)
        self.nil.color = BLACK
        self.root = self.nil


    def left_rotate(self, x):
        y = x.right # x의 오른쪽 자식이 y
        if y == self.nil:
            return

        x.right = y.left # y의 왼쪽 자식을 x의 오른쪽 자식으로 만듦
        if y.left != self.nil:
            y.left.parent = x # y의 왼쪽 자식의 부모를 x로 설정

        y.parent = x.parent # y의 부모를 x의 부모로 설정

        if x.parent == self.nil:
            self.root = y # x가 루트였다면 y가 루트가 됨
        elif x == x.parent.left: # x가 자신의 부모의 왼쪽 자식인 경우
            x.parent.left = y
        else:
            x.parent.right = y # x가 자신의 부모의 오른쪽 자식인 경우

        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left # x의 왼쪽 자식이 y
        if y == self.nil:
            return

        # x의 오른쪽 자식을 y의 왼쪽 자식으로 만듦
        y.left = x.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent

        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.right = x
        x.parent = y




