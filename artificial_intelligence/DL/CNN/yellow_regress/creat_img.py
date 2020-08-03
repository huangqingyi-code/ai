from PIL import Image,ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import os
def creat_img():
    number = 1
    lst = ["北京夜景","佐助","周杰伦","雨滴","鱼","游艇","薰衣草","雪","星空","新年","夏","天空","树木","山脉","秋","清晨","枪",
           "跑车","玫瑰","猫","马","露水","路灯","刘德华","林依晨","花","公园","房子","大象","大海","春","草原","别墅",
           "scenery","food","dog","清华","北大","华中科技","西安交大","上海交大","厦大","哈佛","香港","重庆","厦门","成都","福州"]
    for i in lst:
        bg_path = f"D:\dataset\yellow_minion\{i}"
        for file_name in os.listdir(bg_path):
            bgimg_path = os.path.join(bg_path,file_name)
            bgimg = Image.open(bgimg_path)
            bgimg_mode = bgimg.mode
            # print(bgimg_mode)
            if number==75001:
                return
            if bgimg_mode=="RGB":
                bgimg = bgimg.resize((300,300))
                yellow_number = np.random.randint(1,21)
                yellow_img = Image.open(fr"yellow/{yellow_number}.png")
                yellow_width = np.random.randint(50,181)
                yellow_img = yellow_img.resize((yellow_width,yellow_width))
                paste_x = np.random.randint(0,300-yellow_width)
                paste_y = np.random.randint(0,300-yellow_width)

                r,g,b,a = yellow_img.split()
                bgimg.paste(yellow_img,(paste_x,paste_y),mask=a)

                x = paste_x+yellow_width
                y = paste_y+yellow_width

                draw = ImageDraw.Draw(bgimg)
                draw.rectangle((paste_x,paste_y,x,y),outline=(255,0,0),width=2)

                bgimg.save(f"D:\dataset\yellow_minion\img_rectangle\{number}.{paste_x}.{paste_y}.{x}.{y}.jpg")
                number += 1

                # plt.imshow(bgimg)
                # plt.show()
            else:
                continue
creat_img()
