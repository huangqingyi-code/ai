import cv2
from mtcnn import MTCNN
import os
import time
import json
import warnings
import tensorflow as tf


warnings.filterwarnings("ignore")

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"  # 设置日志级别
root_path = r'C:\Users\71915\Desktop/17'  # 需要处理的图片路径 注意最后有斜杠
out_put_file = r'C:\Users\71915\Desktop/1.txt'  # 输出标注内容的文件
error_point = 0  # 异常点，如果程序发生异常，从异常文件的名称序号开始重新执行
detector = MTCNN()

if __name__ == '__main__':
    begin = time.time()
    err_files = []
    dic_arr = []
    x = 0
    try:
        for file in os.listdir(root_path):
            try:
                image = cv2.cvtColor(cv2.imread(root_path + file), cv2.COLOR_BGR2RGB)
                res = detector.detect_faces(image)
                bounding_box = res[0]['box']
                bounding_box = res[0]['box']
                keypoints = res[0]['keypoints']
                confidence = res[0]['confidence']
                dic = {'name': file, 'box': bounding_box, 'confidence': confidence, 'keypoints': keypoints, }
                dic_arr.append(dic)
            except Exception as ex:
                x += 1
                err_files.append(file)
                print(f"=================>>>>: 【{file}】 发生异常.............", ex)
                continue
            print(f"=================>>>>正在处理第: 【{x}】 张图片")
            if x % 100 == 0:  # 每100次打印到控制台，防止丢失
                cache_json = json.dumps(dic_arr)
                print(f'x: {x}  cache:    ', cache_json)
            if x != 0 and x % 1000 == 0:  # 每1000次清空一次数组 并将内容追加到文件中 防止OOM
                cache_json = json.dumps(dic_arr)
                fh = open(out_put_file, 'a', encoding='utf-8')
                fh.write(cache_json)
                fh.close()
                del dic_arr[:]  # 清空数组 防止OOM
            x += 1
    except Exception as ex:
        print('==============>>>>>>>>Exception Info ', ex)

    res_json = json.dumps(dic_arr)
    if len(dic_arr) > 0:  # 最后还有数据的情况再存储一次
        fh = open(out_put_file, 'a', encoding='utf-8')
        fh.write(res_json)
        fh.close()

    cost = time.time() - begin
    print(f'=================>>>>Error Files：{err_files}')
    print('=================>>>>End total cost:{cost}<<<<=================>>>>')
