i = 0
sum = 0
while i < 99:
    i += 1
    if i == 88:
        continue
    if i % 2 == 1:
        sum += i
    else:
        sum -= i
print(sum)