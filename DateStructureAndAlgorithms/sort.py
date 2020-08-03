# 1.冒泡排序：两两比较最大值在最后  稳定/慢
# 2.选择排序：将乱序中的最大值找出跟最后一个数交换  不稳定
# 3.插入排序： 稳定/快
# 4.希尔排序  不稳定
#5.快速排序:1.指定一个基数（一般是第一个） 1.排序算法的效率在序列越乱的时候，效率越高。在数据有序时，会退化成冒泡排序,大量数据时先快排再插入2.不稳定
          # 2.将比基数小的数放在基数左边，比基数大的放在基数右边
# 6.二叉树排序，稳定
def BubbleSort(alist):
     for x in range(len(alist)-1):
         for y in range(x+1,len(alist)):
             if alist[x]>alist[y]:
                 alist[x],alist[y] = alist[y],alist[x]
     return alist
# ret = BubbleSort([5,6,1,3,8,9,10,0])
# print(ret)

# def SelectSort(alist):
#     maxnum = alist[0]
#     for i in range(len(alist)-1,-1,-1):
#         for x in range(1,i+1):
#             maxnum = max(maxnum,alist[x])
#         alist[alist.index(maxnum)],alist[i] = alist[i],alist[alist.index(maxnum)]
#         maxnum = alist[0]
#     return alist
def SelectSort(alist):
    maxnum = alist[0]
    for x in range(len(alist)-1,-1,-1):
        maxnum = alist[0]
        for i in range(1,x+1):
            if alist[i]>maxnum:
                maxnum = alist[i]
        alist[alist.index(maxnum)],alist[x] = alist[x],alist[alist.index(maxnum)]
    return alist
# ret = SelectSort([5,6,1,3,8,9,10,0])
# print(ret)

def InsertSort(alist):
    for i in range(1,len(alist)):
        while i:
            if alist[i-1] > alist[i]:
                alist[i-1],alist[i] = alist[i],alist[i-1]
                i -= 1
            else:break
    return alist
# ret = InsertSort([5,6,1,3,8,9,10,0])
# print(ret)

def ShellSort(alist):
    gap = len(alist)//2
    while gap >= 1:
        for i in range(gap,len(alist)):
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i],alist[i-gap] = alist[i-gap],alist[i]
                    i -= gap
                else:break
        gap = gap//2
    return alist
# ret = ShellSort([5,6,1,3,8,9,10,0])
# print(ret)

def QuickSort(alist,start,end):
    x = end
    y = start
    if y > x:return
    middle = alist[y]

    while x >y:
        while True:
            if alist[x] > middle:
                x -= 1
            else:
                alist[x],alist[y] = alist[y],alist[x]
                # y += 1
                break
        while True:
            if alist[y] < middle:
                y += 1
            else:
                alist[x],alist[y] = alist[y],alist[x]
                # x -= 1
                break
        if x == y:
            alist[x] = middle
    QuickSort(alist,start,y-1)
    QuickSort(alist,y+1,end)
    return alist
ret = QuickSort([5,6,100,3,8,90,10,0,11,12,13,14,20,16,17,50,19,30],0,17)
print(ret)
def sort(alist, start, end):
    low = start
    high = end
    # 递归结束的条件
    if low > high:
        return
    # 基准：最左侧的数值
    mid = alist[low]
    # low和high的关系只能是小于，当等于的时候就要填充mid了
    while low < high:
        while low < high:
            if alist[high] > mid:
                high -= 1
            else:
                alist[low] = alist[high]
                break
        while low < high:
            if alist[low] < mid:
                low += 1
            else:
                alist[high] = alist[low]
                break

        # 当low和high重复的时候，将mid填充
        if low == high:
            alist[low] = mid  # or alist[high] = mid
            break
    # 执行左侧序列
    sort(alist, start, high - 1)
    # 执行右侧序列
    sort(alist, low + 1, end)

    return alist
ret = sort([5,6,1,3,8,9,10,0,11,12,13,14,15,16,17,18,19,20],0,17)
print(ret)