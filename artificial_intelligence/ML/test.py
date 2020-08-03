import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import GridSearchCV,train_test_split,cross_val_score
from sklearn.metrics import accuracy_score,r2_score,explained_variance_score
from sklearn.kernel_ridge import KernelRidge
from sklearn import svm,linear_model,neighbors,preprocessing

# x = np.arange(-10,10,0.2).reshape(100,1)
x = 5*np.random.RandomState(0).rand(100,1)
y = np.sin(x).ravel()
y[::5] += (0.5-np.random.rand(x.shape[0]//5))

x_train,x_test,y_train,y_test = train_test_split(x,y)
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
best_core = 0
for gamma in [0.001, 0.01, 1, 10, 100]:
    for c in [0.001, 0.01, 1, 10, 100]:
        module = svm.SVR(gamma=gamma,C=c)
        module.fit(x_train,y_train)
        scores = cross_val_score(module,x_train,y_train,cv=10,scoring="r2")
        score = scores.mean()
        if score>best_core:
            best_core = score
            gamma = gamma
            C = c
# print(best_core)
print(gamma)
print(C)
module = svm.SVR()
module.fit(x,y)

# scores = cross_val_score(module,x_train,y_train,cv=10,scoring="r2")
# score = scores.mean()
# print(score)

_x = np.linspace(0,5,100)
_y = module.predict(_x[:,np.newaxis])

plt.plot(_x,_y,color="r")
plt.scatter(x,y)
plt.show()