# import sys
# import os
# def get_size(path):
#     size = 0
#     name_list = os.listdir(path)
#     # print(name_list)
#     for name in name_list:
#         abs_path = os.path.join(path,name)
#         if os.path.isfile(abs_path):
#             size += os.path.getsize(abs_path)
#         else:
#             ret = get_size(abs_path)
#             size += ret
#     return size
#
# ret = get_size(r"D:\pycharm\pycharm project")
# print(ret)
a = 10
def func(d):
    print(d)
    print(type(d))
    d = 6
    print(d)
    return
func(10)