
class queue(object):
    def __init__(self,quesize):
        self.maxsize =quesize+1
        self.data = [0] * self.maxsize
        self.front = 0
        self.rear = 0
    #入队
    def enQueue(self,data):
        #判满
        if self.isFull():
            #队列满
            print("队列满，长度",self.qlen)
            return
        self.data[self.rear] = data
        self.rear += 1
        self.rear %= self.maxsize
    #出队
    def deQueue(self):
        if self.isEmpty():
            # 队列空
            print("队列空")
            return
        data = self.data[self.front]
        self.front+=1
        self.front%=self.maxsize
        return data
    #判满
    def isFull(self):
        self.qlen = (self.rear-self.front+self.maxsize)%self.maxsize
        if self.qlen == self.maxsize-1:
            return True
        else:
            return False
    #判空
    def isEmpty(self):
        return self.rear == self.front

    #显示所有元素
    def show(self):
        self.isFull()
        for i in range(self.qlen):
            print(self.data[(i+self.front)%self.maxsize],end=' ')
        print("\n队列长度",self.qlen)


if __name__ == '__main__':
    myqueue = queue(5)

    while(True):
        print('----------------')
        print("请选择操作:")
        print("1.入队")
        print("2.出队")
        print("3.显示所有元素")

        sel = input()
        print('----------------')

        if sel=='1':
            print('入队操作')
            while True:
                print("请输入数字(输入q退出):", end=' ')
                data = input()
                if data == 'q' or data == 'Q':
                    break
                myqueue.enQueue(data)
        elif sel=='2':
            print('出队',end='')
            print(myqueue.deQueue())
        elif sel=='3':
            print('显示所有元素')
            myqueue.show()
        else:
            print("wrong input")







