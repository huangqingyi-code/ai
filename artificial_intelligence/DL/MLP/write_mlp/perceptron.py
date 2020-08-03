import numpy as np
import matplotlib.pyplot as plt
class Perceptron:
    def __init__(self,input_num,activor):
        self.activor = activor
        self.weights = [0.0 for _ in range(input_num)]
        self.bias = 0.0
    def __str__(self):
        #打印学习到的权重、偏置项
        return 'weights\t:%s\nbias\t:%f\n' % (self.weights, self.bias)
    def predict(self,input_vec):
        #输入向量，输出感知器的计算结果
        ret1 = [x*w for x,w in zip(input_vec,self.weights)]
        # ret1 = map(lambda x,w:x*w,zip(self.input_vec,self.weights))
        return self.activor.forward(sum(ret1)+self.bias)
    def one_iteration(self,input_vecs,labels,rate):
        for x,label in zip(input_vecs,labels):
            output = self.predict(x)
            self.update_weights(x,output,label,rate)
    def update_weights(self,input_vec,output,label,rate):
        loss = 1/2*(output-label)**2
        print("loss:",loss)
        # print(input_vec,type(input_vec))
        # print(self.activor.backward(output))
        dw = (output-label)*input_vec*self.activor.backward(output)
        db = (output-label)*self.activor.backward(output)
        self.weights -= rate*dw
        print(f"w:{self.weights}")
        self.bias -= rate*db
        print(f"b:{self.bias}")
    def train(self,input_vecs,labels,iteration,rate):
        # 输入训练数据：一组向量、与每个向量对应的label；以及训练轮数、学习率
        for i in range(iteration):
            self.one_iteration(input_vecs,labels,rate)
    def get_traindataset(self):
        input_vecs = np.array([[1,1],[0,0],[1,0],[0,1]])
        labels = [1,0,1,1]
        return input_vecs,labels
    # def train_perceptron(self):
    #     from activators import SigmoidActivator
    #     actavor = SigmoidActivator()
    #     p = Perceptron(2,actavor)
    #     input_vecs,labels = self.get_traindataset()
    #     p.train(input_vecs,labels,10,0.01)
    #     return p
if __name__ == '__main__':
    from activators import SigmoidActivator
    activator = SigmoidActivator()
    p = Perceptron(2, activator)
    input_vecs,labels = p.get_traindataset()
    p.train(input_vecs, labels, 10, 0.1)
    # print(p.weights,p.bias)
    x1 = np.arange(-10,10,0.5)
    x2 = np.arange(-10,10,0.5)
    w1,w2 = p.weights
    # print("w1:",w1,"w2:",w2)
    dataset = []
    for i in x1:
        for j in x2:
            y = activator.forward(w1*i+w2*j)
            dataset.append((i,j,y))
    dataset = np.array(dataset)
    # dataset = dataset.astype(np.float32)
    # print(len(dataset))
    label1 = dataset[dataset[:,1]>=0.5]
    label2 = dataset[dataset[:,1]<0.5]
    # print(len(label1),len(label2))
    # print(label1[:,0])
    # print(label1[:,0])
    plt.scatter(label1[:,0],label1[:,1],c="r")
    plt.scatter(label2[:,0], label2[:,1], c="b")
    plt.show()