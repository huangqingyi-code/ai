#方法一：
# class Solution:
#     def spiralOrder(self, matrix):
#         top = 0
#         bottom = len(matrix)
#         left = 0
#         right = len(matrix[0])
#         lst = []
#         while left+1<=right and top+1<=bottom:
#             for i in range(left,right):
#                 lst.append(matrix[top][i])
#             if top+1<bottom:
#                 for i in range(top+1,bottom):
#                     lst.append(matrix[i][right-1])
#             else:break
#             if left+1<right:
#                 for i in range(right-2,left-1,-1):
#                     lst.append(matrix[bottom-1][i])
#             else:break
#             for i in range(bottom-2,top,-1):
#                 lst.append(matrix[i][left])
#             top +=1
#             bottom -= 1
#             left +=1
#             right -=1
#         return lst
#
# ret = Solution()
# res = ret.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
# print(res)

# method two：
def spiralorder(matrix):
    lst = []
    while matrix:
        lst += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return lst
ret = spiralorder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(ret)