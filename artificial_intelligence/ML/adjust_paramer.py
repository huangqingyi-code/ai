# from sklearn import neighbors,datasets,preprocessing
# from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split,cross_val_score
# import matplotlib.pyplot as plt
#
# iris = datasets.load_iris()
#
# x,y = iris.data,iris.target
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=0)
#
# scaler = preprocessing.StandardScaler().fit(x_train)
# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)
#
# k_range = range(1,31)
# k_score = []
# for i in k_range:
#     knn = neighbors.KNeighborsClassifier(n_neighbors=i)
#     score = cross_val_score(knn,x_train,y_train,cv=5,scoring="accuracy")
#     k_score.append(score.mean())
# plt.plot(k_range,k_score)
# plt.show()


from sklearn.datasets import load_iris
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split

iris_data = load_iris()
# X_train,X_test,y_train,y_test = train_test_split(iris_data.data,iris_data.target,random_state=0)
X_trainval, X_test, y_trainval, y_test = train_test_split(iris_data.data, iris_data.target, random_state=0)
X_train, X_val, y_train, y_val = train_test_split(X_trainval, y_trainval, random_state=1)
#原始数据集划分成训练集和测试集以后，其中测试集除了用作调整参数，也用来测量模型的好坏；这样做导致最终的评分结果比实际效果好。
#将数据集分为：训练集，验证集和测试集；但是最终的表现好坏与初始数据的划分结果有很大的关系，为了处理这种情况，我们采用交叉验证的方式来减少偶然性。
# grid search start
best_score = 0
for gamma in [0.001, 0.01, 1, 10, 100]:
    for c in [0.001, 0.01, 1, 10, 100]:
        # 对于每种参数可能的组合，进行一次训练
        svm = SVC(gamma=gamma, C=c)
        svm.fit(X_train, y_train)
# 验证模型用的数据不能是测试集的数据，最终的表现好坏与初始数据的划分结果有很大的关系，为了处理这种情况，我们采用交叉验证的方式来减少偶然性
        # score = svm.score(X_val, y_val)
        scores = cross_val_score(svm,X_trainval,y_trainval,cv=5)
        score = scores.mean()
        # 找到表现最好的参数
        if score > best_score:
            best_score = score
            best_parameters = {'gamma': gamma, "C": c}

# 使用最佳参数，构建新的模型
svm = SVC(**best_parameters)

# 使用训练集和验证集进行训练 more data always resultd in good performance
svm.fit(X_trainval, y_trainval)

# evalyation 模型评估
test_score = svm.score(X_test, y_test)

print('Best socre:{:.2f}'.format(best_score))
print('Best parameters:{}'.format(best_parameters))
print('Best score on test set:{:.2f}'.format(test_score))