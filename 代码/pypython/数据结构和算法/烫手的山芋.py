# class Queue():
#     def __init__(self):
#         self.items = []
#     def enqueue(self,item):
#         self.items.insert(0,item)
#     def dequeue (self):
#         self.items.pop()
#     def isEmpty(self):
#         return self.items == []
#     def size(self):
#         return len(self.items)
# q = Queue()
kids = ['A','B','C','D','E','F']
new_kids = []
for i in kids:
    new_kids.insert(0,i)
while len(new_kids)>1:
    for i in range(6):
        kid = new_kids.pop()
        new_kids.insert(0,kid)
    new_kids.pop()
print(new_kids)

