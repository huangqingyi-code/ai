import numpy as np
from activators import SigmoidActivator

def sigmoid(x):
    sig = 1 / (1 + np.exp(-x))     # Define sigmoid function
    sig = np.minimum(sig, 0.9999)  # Set upper bound
    sig = np.maximum(sig, 0.0001)  # Set lower bound
    return sig

class FullConnectedLayer(object):

    def __init__(self, input_size, output_size,activator):
        self.w = np.random.uniform(-0.1, 0.1, (input_size, output_size))
        # self.w = np.ones((output_size, input_size))
        self.b = np.zeros((1,output_size))
        self.activator = activator

        self.w_grad_total = np.zeros((input_size, output_size))
        self.b_grad_total = np.zeros((1,output_size))

    def forward(self, input_data):
        self.input_data = input_data
        self.output_data =  self.activator.forward(np.matmul(self.input_data,self.w)+self.b)

    def backward(self, input_delta):
        # input_delta_为后一层传入的误差
        # output_delta为传入前一层的误差
        self.sen = input_delta * self.activator.backward(self.output_data)  #1*2

        # print(self.sen.shape)

        output_delta = np.dot(self.sen,self.w.T)   #1*3

        # print(self.input_data.shape)

        self.w_grad = np.matmul(self.input_data.T,self.sen)
        self.b_grad = self.sen

        # self.w_grad_total += self.w_grad
        # self.b_grad_total += self.b_grad
        return output_delta

    def update(self, lr, MBGD_mode=0):
    # 梯度下降法进行权值更新,有几种更新权值的算法。
    # MBGD_mod==0指SGD模式，即随机梯度下降
    # MBGD_mod==1指mnni_batch模式，即批量梯度下降, 当选取batch为整个训练集时，为BGD模式，即批量梯度下降
        if MBGD_mode == 0:
            self.w -= lr * self.w_grad
            self.b -= lr * self.b_grad

        elif MBGD_mode == 1:
            self.w -= lr * self.w_grad_add
            self.b -= lr * self.b_grad_add
            self.w_grad_add = np.zeros((self.input_size, self.output_size))
            self.b_grad_add = np.zeros((1,self.output_size))

class Network():
    def __init__(self, params_array, activator):
        #params_array为层维度信息超参数数组
#       #layers为网络的层集合
       self.layers = []
       for i in range(len(params_array)):
            self.layers.append(FullConnectedLayer(params_array[i][0], params_array[i][1], activator))
        #网络前向迭代
    def predict(self, sample):
        #下面一行的output可以理解为输入层输出
        output = sample
        for layer in self.layers:
            # ret = layer.forward(output)
            # output = ret
            layer.forward(output)
            output = layer.output_data
        return output

    #网络反向迭代
    def calc_gradient(self, label):
        delta = (self.layers[-1].output_data - label)
        # print("delta:",delta.shape)
        for layer in self.layers[::-1]:
            delta = layer.backward(delta)
        return delta

    # 一次训练一个样本 ，然后更新权值          
    def train_one_sample(self, sample, label, lr,epoch):
        for i in range(epoch):
            for num in range(len(sample)):

                self.predict(sample[num].reshape(1,2))
                print(sample[num])
                Loss = self.loss(self.layers[-1].output_data, label[num].reshape(1,2))

                # print(Loss)
                self.calc_gradient(label[num].reshape(1,2))
                self.update(lr)
                # return Loss

    #一次训练一批样本 ，然后更新权值  
    def train_batch_sample(self, sample_set, label_set, lr, batch):
        Loss = 0.0
        for i in range(batch):
            self.predict(sample_set[i])
            Loss += self.loss(self.layers[-1].output_data, label_set[i])
            self.calc_gradient(label_set[i])
            self.update(lr, 1)
            return Loss

    def update(self, lr, MBGD_mode=0):
        for layer in self.layers:
            layer.update(lr, MBGD_mode)

    def loss(self, pred, label):
        return 0.5 * ((pred - label) * (pred - label)).sum()

    def gradient_check(self, sample, label):
        self.predict(sample)
        self.calc_gradient(label)
        incre = 10e-4
        for layer in self.layers:
            for i in range(layer.w.shape[0]):
                for j in range(layer.w.shape[1]):
                    layer.w[i][j] += incre
                    pred = self.predict(sample)
                    err1 = self.loss(pred, label)
                    layer.w[i][j] -= 2 * incre
                    pred = self.predict(sample)
                    err2 = self.loss(pred, label)
                    layer.w[i][j] += incre
                    pred_grad = (err1 - err2) / (2 * incre)
                    calc_grad = layer.w_grad[i][j]
                    print('weights(%d,%d): expected - actural %.4e - %.4e' % (i, j, pred_grad, calc_grad))


if __name__ == '__main__':
    params = np.array([[2,5],[5,3],[3,2]])
    activator = SigmoidActivator()
    net = Network(params, activator)
    data = np.array([[1.9,2],[0.9,1],[1.1,1],[2.1,2]])
    label = np.array([[0,1],[0,1],[1,0],[1,0]])
    # ret = net.train_batch_sample(data,label,lr=0.01,batch=2)
    ret = net.train_one_sample(data,label,lr=0.1,epoch=10)
    # print(ret)

