list = [1,2,3,4,5,6,8,9]
def search(item):
    global list
    while len(list)>1:
        mid_index = len(list) // 2
        if list[mid_index] == item:
            return item
        elif list[mid_index] > item:
            list = list[:mid_index]
        else:
            list = list[mid_index+1:]
    return list[0]
print(search(99))