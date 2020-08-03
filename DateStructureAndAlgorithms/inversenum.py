def inversenum(x):
    num = 0
    # pop = x % 10
    while x:
        pop = x % 10
        num = num*10+pop
        x = x//10
    return num

ret=inversenum(52461)
print(ret)