# 链表：是一种常见的数据结构，是一种线性表，不想顺序表一样连续存储数据。
# 每一个节点存储数据和下一个节点的地址
class Node():
    def __init__(self,item):
        self.item = item
        self.next = None
class Link():
    def __init__(self):
        #构造出一个空链表
        #_head存储的只能是空或者是第一节点的地址
        self._head = None
    def add(self,item):
        #创建一个新的节点
        node = Node(item)
        node.next = self._head
        self._head = node
    def travel(self):#遍历
        cur = self._head
        while cur:
            print(cur.item)
            cur = cur.next
    def size(self):#有几个节点
        cur = self._head
        count = 0
        while cur:
            count +=1
            cur = cur.next
        return count
    def isEpmty(self):#是否为空
        return self._head == None
    def append(self,item):#尾部增加
        node = Node(item)
        if self._head == None:
            self._head = node
            return
        else:
            cur = self._head
            while cur.next:
                cur = cur.next
            cur.next = node
    def search(self,item):#查找
        cur = self._head
        while cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False
    def insert(self,pos,item):
        node = Node(item)
        cur = self._head
        pre = None
        for i in range(pos):
            pre = cur
            cur = cur.next
        pre.next = node
        node.next = cur
    def remove(self,item):
        cur = self._head
        pre = None
        if cur.item == item:
            self._head = cur.next
            return
        while cur:
            pre =cur
            cur = cur.next
            if cur.item ==item:
                pre.next = cur.next
                break
link = Link()
link.add(3)
link.add(4)
link.append(5)
link.append(6)
# link.insert(2,1.1)
link.remove(4)
link.travel()
# print(link.search(75))
# print(link.size())
# print(link.isEpmty())