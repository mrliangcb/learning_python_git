#mnist深层神经网络
#此文档可用于测网络是否基本ok
#sharedeep
import numpy as np
import torch
from torchvision.datasets import mnist # 导入 pytorch 内置的 mnist 数据
import my_model
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

from torch import nn
from torch.autograd import Variable
# 使用内置函数下载 mnist 数据集
train_set = mnist.MNIST('./MNIST_data', train=True, download=False)
test_set = mnist.MNIST('./MNIST_data', train=False, download=False)


# a_data, a_label = train_set[0]
# a_data
#plt转成numpy
# a_data = np.array(a_data, dtype='float32')
# print(a_data.shape)



transform = transforms.Compose(
			[transforms.Grayscale(),  # CROHME png are RGB, but already 32x32
			transforms.Resize(28),#Scale
			transforms.ToTensor(),
			transforms.Normalize((0.5,), (0.5,))])
			
#先拍扁
def data_tf(x):
    x = np.array(x, dtype='float32') / 255
    x = (x - 0.5) / 0.5 # 标准化，这个技巧之后会讲到
    x = x.reshape((-1,)) # 拉平
    x = torch.from_numpy(x)
    return x

train_set = mnist.MNIST('./data', train=True, transform=transform, download=True) # 重新载入数据集，申明定义的数据变换
test_set = mnist.MNIST('./data', train=False, transform=transform, download=True)

a, a_label = train_set[0]
print(a.shape)
print(a_label)

from torch.utils.data import DataLoader
# 使用 pytorch 自带的 DataLoader 定义一个数据迭代器
train_data = DataLoader(train_set, batch_size=64, shuffle=True)
test_data = DataLoader(test_set, batch_size=64, shuffle=False)


net=my_model.CNN()

# 定义 loss 函数
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), 0.01) # 使用随机梯度下降，学习率 0.1


losses = []
acces = []
eval_losses = []
eval_acces = []
do_train=0

for e in range(0,20,1):
	train_loss = 0
	train_acc = 0
	net.train()
	
	for im, label in train_data:#在一个epoch里面循环
		
		#im = Variable(im)
		#label = Variable(label)
		# 前向传播
		out = net(im)
		loss = criterion(out, label)
		# 反向传播
		optimizer.zero_grad()
		loss.backward()
		optimizer.step()
		# 记录误差
		train_loss += loss.item()
		# 计算分类的准确率
		
		test_pred = torch.max(out, 1)[1].data.numpy()
		ground_true=label.data.numpy()
		acc=sum(test_pred==ground_true)/len(ground_true)
		
		#acc = num_correct / im.shape[0]
		train_acc += acc
		
	losses.append(train_loss / len(train_data))
	acces.append(train_acc / len(train_data))
	# 在测试集上检验效果
	eval_loss = 0
	eval_acc = 0
	net.eval() # 将模型改为预测模式
	for im, label in test_data:
		
		#im = Variable(im)
		#label = Variable(label)
		out = net(im)#输出是variable型
		loss = criterion(out, label)
		# 记录误差
		eval_loss += loss.item()
		# 记录准确率
		
		test_pred = torch.max(out, 1)[1].data.numpy()
		ground_true=label.data.numpy()
		acc=sum(test_pred==ground_true)/len(ground_true)
		eval_acc += acc
	eval_losses.append(eval_loss / len(test_data))
	eval_acces.append(eval_acc / len(test_data))
	#保存 
	# torch.save(net,'net.pkl')#整个模型保存
	state = {'net':net.state_dict(), 'optimizer':optimizer.state_dict(), 'epoch':e}
	# torch.save(state,r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\sharedeep\mnist_canshu.pkl')
	# print('保存')
	
	print('epoch: {}, Train Loss: {:.6f}, Train Acc: {:.6f}, Eval Loss: {:.6f}, Eval Acc: {:.6f}'.format(e, train_loss / len(train_data), train_acc / len(train_data), eval_loss / len(test_data), eval_acc / len(test_data)))

# import matplotlib.pyplot as plt
# plt.title('train loss')
# plt.plot(np.arange(len(losses)),losses)
# plt.show()

# plt.plot(np.arange(len(acces)), acces)
# plt.title('train acc')
# plt.show()


# plt.plot(np.arange(len(eval_losses)), eval_losses)
# plt.title('test loss')
# plt.show()

# plt.plot(np.arange(len(eval_acces)), eval_acces)
# plt.title('test acc')
# plt.show()


















