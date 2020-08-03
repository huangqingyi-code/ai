from sklearn import neighbors,datasets,preprocessing
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score,f1_score,classification_report

#数据加载
iris = datasets.load_iris()   #数据集加载时shuffle=True，默认打乱
# print(iris["data"].shape)
# print(iris.data.shape)   #内置的api和上面一样

#划分训练集和测试集`

x,y = iris.data,iris.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.3,random_state=1)   #random_state随机数种子相同,shuffle是否打乱
# 划分的训练集和测试集相同，random_state不同划分的数据集也不同，默认不给每次划分的数据集都不同；设置好随机数种子别人运行你的代码
# 可以复现你的结果；当你用sklearn分割完测试集和训练集，确定模型和初始参数以后，你会发现程序每运行一次，都会得到不同的准确率，无法调参。
# 这个时候就是因为没有加random_state。加上以后就可以调参了。
# print(x_train.shape,y_train.shape,x_test.shape,y_test.shape)

#数据预处理
scaler = preprocessing.StandardScaler().fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

#创建模型
knn = neighbors.KNeighborsClassifier(n_neighbors=4)

#模型拟合
knn.fit(x_train,y_train)

#交叉验证
# score = cross_val_score(knn,x_train,y_train,cv=5,scoring="accuracy")
# print(score)
# print(score.mean())

#测试
y_pred = knn.predict(x_test)

#评估
print(accuracy_score(y_pred,y_test))
#f1-score
print(f1_score(y_pred,y_test,average="micro"))   #'micro':通过先计算总体的TP，FN和FP的数量，再计算F1
                                                 #'macro':分布计算每个类别的F1，然后做平均
#分类报告                                         #默认二分类，binary
print(classification_report(y_pred,y_test))