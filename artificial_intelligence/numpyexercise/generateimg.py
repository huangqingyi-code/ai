#生成验证码
import random
import matplotlib.pyplot as plt
from PIL import Image,ImageDraw,ImageFont

class GenerateCode():
    lst1 = [chr(i) for i in range(65, 91)]
    lst2 = [chr(i) for i in range(97, 123)]
    lst3 = [i for i in range(10)]
    lst = lst1 + lst2 + lst3
    def get_code(self):
        return(str(random.choice(GenerateCode.lst)))
    def bg_color(self):
        return (random.randint(0,160),
                random.randint(0,160),
                random.randint(0,160))
    def fw_color(self):
        return (random.randint(100,255),
                random.randint(100,255),
                random.randint(100,255))
    def generate_pic(self):
        w = 240
        h = 60
        pic = Image.new(mode="RGB",size=(240,60),color=(255,255,255))
        font = ImageFont.truetype(font="image/segoesc.ttf",size=30)
        draw = ImageDraw.Draw(pic)
        for x in range(w):
            for y in range(h):
                draw.point((x,y),fill=self.bg_color())
        for i in range(4):
            draw.text((60*i+15,15),text=self.get_code(),fill=self.fw_color(),font=font)
            # draw.rectangle((30,30,100,10))  #PIL画矩形框
        pic.show()
code = GenerateCode()
code.generate_pic()

# import random
# from PIL import ImageDraw,Image,ImageFont
# import matplotlib.pyplot as plt
# class GenerateCode:
#     def get_alpha(self):
#         return chr(random.randint(65,90))
#     def bg_color(self):
#         return (random.randint(0,155),
#                 random.randint(0,155),
#                 random.randint(0,155))
#     def fg_color(self):
#         return (random.randint(120,255),
#                 random.randint(120,255),
#                 random.randint(120,255))
#     def generate_img(self):
#         w = 240
#         h = 60
#         img = Image.new(mode="RGB",size=(w,h),color=self.bg_color())
#         font = ImageFont.truetype(font="times.ttf",size=30)
#         draw = ImageDraw.Draw(img)
#         for x in range(w):
#             for y in range(h):
#                 num = random.randint(0, 100)
#                 if num>80:
#                     draw.point((x,y),fill=self.bg_color())
#         # for x in range(w):
#         #     for y in range(h):
#         #         draw.point((x,y),fill=self.bg_color())
#         for i in range(4):
#             draw.text((i*60+20,15),text=self.get_alpha(),font=font,fill=self.fg_color())
#         num = random.randint(1,3)
#         for i in range(num):
#             begin = (random.randint(0,w),random.randint(0,h))
#             end = (random.randint(0,w),random.randint(0,h))
#             draw.line((begin,end),fill=self.fg_color())
#         # for x in range(w):
#         #     for y in range(h):
#         #         num = random.randint(0, 100)
#         #         if num>80:
#         #             draw.point((x,y),fill=self.bg_color())
#         draw.rectangle((20,20,80,50))
#
#         plt.imshow(img)
#         plt.show()
# img = GenerateCode()
# img.generate_img()