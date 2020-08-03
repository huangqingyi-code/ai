import os, shutil

path = r"D:\dataset\cat_dog\img"
train = r"D:\dataset\cat_dog\train"
test = r"D:\dataset\cat_dog\test"

def move_img():
    if not os.path.exists(train):
        os.makedirs(train)
    if not os.path.exists(test):
        os.makedirs(test)
    name_list = os.listdir(path)
    num = len(name_list)
    num1 = 0
    num2 = 0
    for name in name_list:
        if name[0] == "0":
            if num1 < 0.1 * num:
                src = os.path.join(path, name)
                dst = os.path.join(test, name)
                shutil.copy2(src, dst)
                num1 += 1
            else:
                src = os.path.join(path, name)
                dst = os.path.join(train, name)
                shutil.copy2(src, dst)
        if name[0] == "1":
            if num2 < 0.1 * num:
                src = os.path.join(path, name)
                dst = os.path.join(test, name)
                shutil.copy2(src, dst)
                num2 += 1
            else:
                src = os.path.join(path, name)
                dst = os.path.join(train, name)
                shutil.copy2(src, dst)


if __name__ == '__main__':
    move_img()
