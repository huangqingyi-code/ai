import numpy as np
from sklearn.metrics import confusion_matrix
#多分类
y_ture = [2,1,0,2,1,0,1]
y_pre =  [2,1,1,2,1,1,0]
ret = confusion_matrix(y_ture,y_pre)
print(ret)
# [[0 2 0]
#  [1 2 0]
#  [0 0 2]]