class Matrix:
    def __init__(self,lst):
        self.lst = lst
    def __add__(self, other):
        a_row = len(self.lst)
        a_col = len(self.lst[0])
        b_row = len(other.lst)
        b_col = len(other.lst[0])
        if a_row == b_row and a_col == b_col:
            for row in range(a_row):
                for col in range(a_col):
                    self.lst[row][col] += other.lst[row][col]
            return self.lst
        else:
            return "形状不同，不能相加"
        def __str__(self):
            return str(self.lst)

a = Matrix([[1,2],[3,4]])
b = Matrix([[5,6],[7,8]])
print(a+b)