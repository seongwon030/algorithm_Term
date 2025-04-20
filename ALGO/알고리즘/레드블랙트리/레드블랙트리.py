RED = True
BLACK = False

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = RED

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

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.parent = self.nil

        y = self.nil # x의 부모후보
        x = self.root # 트리의 루트부터 탐색

        # 삽입할 위치 찾기 위해 루트부터 내려가면서
        # 삽입값이 작으면 왼쪽, 크면 오른쪽이로 이동
        #  x가 self.nil이 되면 위치찾기 종료
        while x != self.nil:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right

        new_node.parent = y # 삽입 위치 정해졌으므로, 새 노드의 부모를 y로 설정

        if y == self.nil:
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        new_node.color = RED
        self.insert_fixup(new_node)

    def insert_fixup(self, z):
        while z.parent.color == RED: # 삽입할 노드 z의 부모가 Red가 아닐 때까지 반복
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right  # 삼촌 노드
                if y.color == RED:
                    # Case 1
                    z.parent.color = BLACK # 부모를 Black으로
                    y.color = BLACK # 삼촌 노드를 Black으로
                    z.parent.parent.color = RED # 조부모 노드를 red로
                    z = z.parent.parent # z를 조부모로 갱신
                else:
                    if z == z.parent.right:
                        # Case 2
                        z = z.parent
                        self.left_rotate(z)
                    # Case 3
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    # Case 1 (대칭)
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        # Case 2 (대칭)
                        z = z.parent
                        self.right_rotate(z)
                    # Case 3 (대칭)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)

        self.root.color = BLACK

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

    def minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node

    def delete(self, z):
        y = z
        y_original_color = y.color # 삭제될 노드의 원래 색깔 기억
        # case1: 왼쪽 자식이 nil
        if z.left == self.nil:
            x = z.right # x는 삭제 후 fixup 대상 노드
            self.transplant(z, z.right) # z의 오른쪽 자식을 올려 붙임
        # case2: 오른쪽 자식이 nil
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left) # z의 왼쪽 자식을 올려 붙임

        # case3: 자식이 둘 다 있음
        else:
            y = self.minimum(z.right) # z의 오른쪽 서브 트리에서 가장 작은 값
            y_original_color = y.color
            x = y.right # x는 후계자 y의 오른쪽 자식 (fixup 대상)
            if y.parent == z:
                x.parent = y
            else:
                # 후계자 y가 z의 자식이 아닌 경우
                self.transplant(y, y.right) # y에 y.right를 옮기고
                y.right = z.right # y를 z 자리로 옮길 준비
                y.right.parent = y
            self.transplant(z, y) # z를 y로 대체
            y.left = z.left # z의 왼쪽 자식도 연결
            y.left.parent = y
            y.color = z.color # y의 색깔은 z의 색을 유지

        if y_original_color == BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK
