import numpy as np
import matplotlib.pyplot as plt
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import GridSearchCV

x = 5*np.random.RandomState(0).rand(100,1)
y = np.sin(x).ravel()
# print(y)

y[::5] +=3*(0.5-np.random.rand(x.shape[0]//5))

# kr = KernelRidge(kernel="rbf",gamma=0.1)

#网格搜索和交叉验证GridSearchCV
#当超参数的数量增长时，网格搜索的计算复杂度会呈现指数增长，这时候则使用随机搜索（RandomizedSearchCV）
kr = GridSearchCV(KernelRidge(),param_grid={"kernel":["rbf","laplacian","polynomial","sigmoid"],
                                            "alpha":[1e0,0.1,1e-2,1e-3],
                                            "gamma":np.logspace(-2,2,5)})
                #np.logspace(-2,2,5) 构造5个10的-2次方到10的2次方的等比数列，不想10的次方可以改变基数np.logspace(-2,2,base=2)


kr.fit(x,y)
print(kr.best_score_,kr.best_params_)

x_plot = np.linspace(0, 5, 100)   #构建等差数列（start,end,num）
y_kr = kr.predict(x_plot[:, None])    #x升维

plt.scatter(x,y)
plt.plot(x_plot,y_kr,color="r")
plt.show()