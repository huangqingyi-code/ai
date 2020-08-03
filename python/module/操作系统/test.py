import hashlib
path = r"C:\Users\Administrator\Desktop\资料\数字图像处理_第三版_中_冈萨雷斯.pdf"
with open(path,mode="rb")as f:
    content = f.read()
    ret = hashlib.md5("hqy".encode("utf-8"))
    ret.update(content)
    print(ret.hexdigest())

path = r"C:\Users\Administrator\Desktop\资料\数字图像处理_第三版_中_冈萨雷斯.pdf"
with open(path,mode="rb")as f1:
    ret = hashlib.md5("hqy".encode("utf-8"))
    while True:
        content = f1.read(1024)
        if not content:break
        ret.update(content)
    print(ret.hexdigest())


