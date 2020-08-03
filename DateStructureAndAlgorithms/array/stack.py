def calPoints(ops):
    lst = []
    for i in ops:
        if i.isdigit() or str(i.split("-")[-1]).isdigit():
            lst.append(int(i))
        elif i == "C":
            lst.pop()
        elif i == "D":
            num = lst.pop()
            lst.append(num)
            lst.append(2 * num)
        elif i == "+":
            num1 = lst.pop()
            num2 = lst.pop()
            num = num1 + num2
            lst.extend((num2, num1, num))
    return sum(lst)

ret = calPoints(["5","-2","4","C","D","9","+","+"])
print(ret)

a = "-2"
# print(a.isdigit())   #False