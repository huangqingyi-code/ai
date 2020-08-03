class Node:
    def __init__(self,item):
        self.item = item
        self.next = None
class Link:
    def __init__(self):
        self._head = None
    def head_add(self,item):
        node = Node(item)
        if self._head == None:
            self._head = node
            return
        else:
            node.next = self._head
            self._head = node
    def last_add(self,item):
        node = Node(item)
        if self._head == None:
            self._head = node
            return
        else:
            cur = self._head
            while True:
                if cur.next == None:
                    break
                else:cur = cur.next
            cur.next = node
        # while cur.next:
        #     cur = cur.next
        # cur.next = node
    def travel(self):
        if self._head == None:
            print('the link is empty')
        else:
            cur = self._head
            while cur:
                print(cur.item)
                cur = cur.next
    def get_size(self):
        if self._head == None:
            return 0
        else:
            cur = self._head
            num = 0
            while cur:
                num +=1
                cur = cur.next
        print(num)
    def insert(self,position,item):
        node = Node(item)
        cur = self._head
        nxt = cur.next
        num = 1
        while num < position:
            num += 1
            cur = cur.next
            nxt = cur.next
        cur.next = node
        node.next = nxt
    def remove(self,num):
        cur = self._head
        pre = 0
        if cur.item == num:
            self._head = cur.next
        else:
            while True:
                pre = cur
                cur = cur.next
                if cur.item == num:
                    pre.next = cur.next
                    return


link = Link()
# link.head_add(1)
# link.head_add(2)
# link.head_add(3)
# link.head_add(4)
# link.head_add(5)
link.last_add(1)
link.last_add(2)
link.last_add(3)
link.last_add(4)
link.insert(2,5)
link.remove(1)
link.travel()
# link.get_size()