# 列表
# 增/删/改/查
# a = [1,[2,3,4],2,3,'wusir']
# a.append('taibai')
# a.extend([6,6])
# a.insert(1,'alex')
# print(a)
# a = [1, 'alex', [2, 3, 4], 2, 3, 'wusir', 'taibai', 6, 6]
#
# a.pop()
# del a[1]
# a.remove('wusir')
# print(a)
# a = [1, [2, 3, 4], 2, 3, 'taibai', 6]
# a[5] = 8
# a[1][0] = 66
# print(a)
# a = [1, [2, 3, 4], 2, 3, 'taibai', 6,6]
# print(a.count(6))
# 深浅copy
# import copy
# lst1 = [1,2,3,[1,2,3]]
# lst2 = lst1.copy()
# lst3 = lst1[::]
# lst4 = copy.deepcopy(lst1)
# lst1[-1].append(6)
# print(lst1,lst2,lst3,lst4)
# 列表再循环中更改,去除列表中的偶数
# lst = [0,1,2,3,4]
# new_lst = lst[1::2]
# new_lst = []
# for i in lst:
#     if i%2==0:
#         new_lst.append(i)
# print(new_lst)
# new_lst.sort(reverse=True)
# new_lst.reverse()
# print(new_lst)
lst = ['a','b','c']
for x,y in enumerate(lst,1):
    print(f'{x}:{y}')