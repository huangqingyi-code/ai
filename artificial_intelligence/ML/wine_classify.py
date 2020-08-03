from sklearn import neighbors,datasets,preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split,cross_val_score
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVC

datas = np.loadtxt("data/wine.data",delimiter=",")
x = datas[:,1:]
y = datas[:,0]

x_train,x_test,y_train,y_test = train_test_split(x,y)
# print(len(x_train),len(x_test))

scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

# KNN
# best_score = 0
# for i in range(1,20):
#     knn = neighbors.KNeighborsClassifier(n_neighbors=i)
#     knn.fit(x_train,y_train)
#     scores = cross_val_score(knn,x_train,y_train,cv=10,scoring="accuracy")
#     score = scores.mean()
#     # print(score)
#     if score>best_score:
#         best_score = score
#         parameter = i
# print(parameter)
# knn = neighbors.KNeighborsClassifier(n_neighbors=parameter)
# knn.fit(x_train,y_train)
#
# y_pre = knn.predict(x_test)
# print(accuracy_score(y_pre,y_test))

#SVM
best_score = 0
for gamma in [0.001, 0.01, 1, 10, 100]:
    for c in [0.001, 0.01, 1, 10, 100]:
        svm = SVC(gamma=gamma, C=c)
        svm.fit(x_train, y_train)
        scores = cross_val_score(svm,x_train,y_train,cv=5)
        score = scores.mean()
        if score > best_score:
            best_score = score
            best_parameters = {'gamma': gamma, "C": c}

svm = SVC(**best_parameters)

svm.fit(x_train,y_train)

test_score = svm.score(x_test, y_test)

print('Best socre:{:.2f}'.format(best_score))
print('Best parameters:{}'.format(best_parameters))
print('Best score on test set:{:.2f}'.format(test_score))
# print(**a)