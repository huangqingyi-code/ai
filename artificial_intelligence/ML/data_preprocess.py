from sklearn import preprocessing
from sklearn.impute import SimpleImputer
import numpy as np

x = np.arange(12).reshape(4,3)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
# scaler = preprocessing.StandardScaler().fit(x)
# x = scaler.transform(x)
# print(x)

# scaler = preprocessing.MinMaxScaler()
# x = scaler.fit_transform(x)
# print(x)

# scaler = preprocessing.MaxAbsScaler()
# x = scaler.fit_transform(x)
# print(x)

# scaler = preprocessing.Normalizer(norm="l2")
# x = scaler.fit_transform(x)
# print(x)

# scaler = preprocessing.RobustScaler()
# x = scaler.fit_transform(x)
# print(x)

#弥补缺失数据
# data = [[1,2],[np.nan,5],[6,np.nan]]
# imp = SimpleImputer(missing_values=np.nan,strategy="mean")
# data = imp.fit_transform(data)
# print(data)
data = []
with open("data\datas",mode="r",encoding="utf-8")as f:
    for line in f:
        data.append(line.strip().split(","))
print(data)
datas = []
for i in data:
    lst = []
    for j in i:
        if j:
            j = int(j)
            lst.append(j)
        else:
            j = np.nan
            lst.append(j)
    datas.append(lst)
print(datas)