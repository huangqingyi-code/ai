import numpy as np
from sklearn import neighbors,datasets,preprocessing
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,explained_variance_score

datas = []
with open("data/housing.data",mode="r",encoding="utf-8") as f:
    for line in f:
        line = line.strip().split()
        # print(line)
        datas.append(line)
# datas = np.loadtxt("data/housing.data")
# print(datas)

datas = np.array(datas)
datas = datas.astype(np.float32)
print(datas)
x = datas[:,:-1]
y = datas[:,-1]
# print(x)
x_train,x_test,y_train,y_test = train_test_split(x,y)
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

kr = GridSearchCV(KernelRidge(),param_grid={"kernel":["rbf","laplacian","polynomial","sigmoid"],
                                            "alpha":np.arange(0,1,0.05),
                                            "gamma":np.logspace(-10,10,10)})

kr.fit(x_train,y_train)
print(kr.best_score_,kr.best_params_)

y_pred =kr.predict(x_test)
print(mean_squared_error(y_test,y_pred))
print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred))
print(explained_variance_score(y_test,y_pred))
