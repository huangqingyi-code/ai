from sklearn import datasets,linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,explained_variance_score
import numpy as np
import matplotlib.pyplot as plt

# np.random.RandomState(0)
x,y =datasets.make_regression(n_samples=100,n_features=1,n_targets=1,noise=10,random_state=0)
# print(x,y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3)

reg =linear_model.LinearRegression()
# reg =linear_model.Ridge(0.5)
# reg = linear_model.Lasso(0.5)
# reg = linear_model.ElasticNet(0.5,0.5)
# reg = linear_model.BayesianRidge()

reg.fit(x_train,y_train)
print(reg.coef_,reg.intercept_)

y_pred =reg.predict(x_test)

print(mean_squared_error(y_test,y_pred))
print(mean_squared_error(y_test,y_pred))
print(r2_score(y_test,y_pred))
print(explained_variance_score(y_test,y_pred))

_x = np.array([[-2.5],[2.5]])
_y = reg.predict(_x)
# _x = np.array([-2.5, 2.5])
# _y = reg.predict(_x[:,None])   #升维

plt.scatter(x_test,y_test)
plt.plot(_x,_y,color="r")
plt.show()

