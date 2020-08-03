import urllib.request
import requests
import urllib.parse
import re
import os

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# res = response.read().decode("utf-8")

#获取一个post请求（还要cookie）：需要登陆的爬取
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data)
# res = response.read().decode("utf-8")

#网络超时：timeout默认60s

# try:
#     respose = urllib.request.urlopen("http://httpbin.org/get",timeout=0.1)
#     res = response.read().decode("utf-8")
# except:
#     print("time out")

#封装header
# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# header = \
#     {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
#         "referer": "https://image.baidu.com"
#     }
# req = urllib.request.Request(url=url,data=data,headers=header,method="POST")
# response = urllib.request.urlopen(req)
# res = response.read().decode("utf-8")
# print(res)


def crath_img():
    keyword = "北京夜景"
    path = f"D:\dataset\yellow_minion\{keyword}"
    if not os.path.exists(path):
        os.makedirs(path)
    keyword = urllib.parse.quote(keyword, "utf-8")
    url = f"https://image.baidu.com/search/flip?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result" \
          "&fr=&sf=1&fmq=1595660989390_R&pv=&ic=0&nc=1&z=&hd=&latest=&copyright=&se=1&showtab=0&fb=0&width=0&" \
          "height=0&face=0&istype=2&ie=utf-8&ctd=1595660989391%5E00_1903X937&sid=&word="+keyword
    header=\
    {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
         "referer":"https://image.baidu.com"
        }
    num = 1
    while True:
        #方法一：用urllib
        req = urllib.request.Request(url=url,headers=header)

        response = urllib.request.urlopen(req,timeout=10)

        html = response.read().decode("utf-8")

        # 方法二：用requests,要加urllib.parse.quote(keyword, "utf-8")
        # response =requests.get(url,headers=header)
        # html = response.text

        pucture_url = re.findall('"thumbURL":"(.*?)","middleURL"',html)
        url_next_page = re.findall(r'<a href="(.*?)" class="n">下一页', html)

        for i in pucture_url:
            type = i.split(".")[-1]
            img_name = path+"/"+str(num)+".jpg"
            try:
                picture = requests.get(i,timeout=10)
                with open(img_name,mode="wb") as f:
                    f.write(picture.content)
                print(num)
                num += 1
            except :
                continue

        if len(url_next_page):
            next_page = 'http://image.baidu.com' + url_next_page[0]
            url = next_page
        else:
            print("已到达最后一页")
            break
if __name__ == '__main__':
    ret = crath_img()
    # print(ret)






