# -*- coding: utf-8 -*-
"""
Training a classifier
=====================

sourced from https://pytorch.org/tutorials/beginner/blitz/neural_networks_tutorial.html

Modified by : Harold Mouchère / University of Nantes

2018

"""
import time
import copy
import torch
import torchvision
import torchvision.transforms as transforms
import pdb
import matplotlib.pyplot as plt
import pandas as pd
def duandian():
	pdb.set_trace()

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

#返回cpu或者gpu
print(device)#cpu

########################################################################
# We transform them to Tensors of normalized range [-1, 1].
transform = transforms.Compose(
		[#transforms.Pad(2),#每条边都补两个0
		transforms.Grayscale(),
		transforms.ToTensor(),
		transforms.Normalize((0.5,), (0.5,))])

minibatchsize = 128
test_batch=500
from torchvision.datasets import ImageFolder   
from torch.utils.data import DataLoader  

#1.训练数据                                   # download=True, transform=transform)
folder_set = ImageFolder(r'C:\lcb\learning_python_git\extradoc\task2-trainSymb2014\jungleornot\trainingdata\\', 
							transform=transform)
train_data = DataLoader(folder_set, batch_size=minibatchsize, shuffle=True) #迭代器只是只做了目录，虚拟tensor,loader型

# dataiter = iter(train_data)
# images, labels = dataiter.next()

#2.测试数据
test_data1 = ImageFolder(r'C:\lcb\learning_python_git\extradoc\task2-trainSymb2014\jungleornot\testdata', transform=transform)
test_data = DataLoader(test_data1,batch_size=test_batch, shuffle=True) #迭代器只是只做了目录，虚拟tensor,loader型

print('有哪些类',test_data1.class_to_idx)#{'trainingJunk_png': 0, 'trainingSymbols_png': 1}


classes = range(0,1)#这些类设为0到1
nb_classes = len(classes)#多少个类2


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

# functions to show an image
# def imshow(img, name='output.png'):
    # img = img / 2 + 0.5     # unnormalize
    # npimg = img.numpy()
    # plt.imshow(np.transpose(npimg, (1, 2, 0)))
    # plt.savefig(name)



# show images
# imshow(torchvision.utils.make_grid(images))
# print labels
#print(' '.join('%5s' % classes[labels[j]] for j in range(4)))


########################################################################
# 2. Define a Convolution Neural Network
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


import torch.nn as nn
import torch.nn.functional as F


class NetMLP(nn.Module):#继承了nn.Module
    def __init__(self, hiddencells = 100):
        super(NetMLP, self).__init__()#继承自己
        self.fc1 = nn.Linear(32 * 32 , hiddencells)#mpl写法
        self.fc2 = nn.Linear(hiddencells, 10)

    def forward(self, x):#前向过程，输入x才开始
        x = x.view(-1, 32 * 32)
        x = F.relu(self.fc1(x))
        x = F.softmax(self.fc2(x), dim=1)
        return x#模型输出
class CNN(nn.Module):#建立网络
	def __init__(self):
		super(CNN, self).__init__()
		self.conv1 = nn.Sequential(         # input shape (1, 28, 28)
			nn.Conv2d(
				in_channels=1,              # input height
				out_channels=16,            # n_filters
				kernel_size=5,              # filter size
				stride=1,                   # filter movement/step
				padding=2,                  # if want same width and length of this image after Conv2d, padding=(kernel_size-1)/2 if stride=1
			),                              # output shape (16, 28, 28)
			nn.ReLU(),                      # activation
			nn.MaxPool2d(kernel_size=2),    # choose max value in 2x2 area, output shape (16, 14, 14)
		)
		self.conv2 = nn.Sequential(         # input shape (16, 14, 14)
			nn.Conv2d(16, 32, 5, 1, 2),     # output shape (32, 14, 14)
			nn.ReLU(),                      # activation
			nn.MaxPool2d(2),                # output shape (32, 7, 7)
		)
		
		self.conv3 = nn.Sequential(         # input shape (16, 14, 14)
			nn.Conv2d(32, 64, 5, 1, 2),     # output shape (32, 14, 14)
			nn.ReLU(),                      # activation
			nn.MaxPool2d(2),                # output shape (32, 7, 7)
		)
		
		   # fully connected layer, output 10 classes
											#拍扁之后mlp
	def forward(self, x):
		x = self.conv1(x)
		x = self.conv2(x)
		
		x = x.view(x.size(0), -1)           # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
		self.fc = nn.Linear(x.shape[1], 512)
		self.out = nn.Linear(512, 2)
		x = self.fc(x)
		x = self.out(x)
		output = F.softmax(x, dim=1)#softmax把输出转换成概率
		return output, x#输出是一个tuple

		
from torch import nn
def conv3x3(in_channel, out_channel, stride=1):
    return nn.Conv2d(in_channel, out_channel, 3, stride=stride, padding=1, bias=False)
class residual_block(nn.Module):
    def __init__(self, in_channel, out_channel, same_shape=True):
        super(residual_block, self).__init__()
        self.same_shape = same_shape
        stride=1 if self.same_shape else 2
        
        self.conv1 = conv3x3(in_channel, out_channel, stride=stride)
        self.bn1 = nn.BatchNorm2d(out_channel)
        
        self.conv2 = conv3x3(out_channel, out_channel)
        self.bn2 = nn.BatchNorm2d(out_channel)
        if not self.same_shape:
            self.conv3 = nn.Conv2d(in_channel, out_channel, 1, stride=stride)
        
    def forward(self, x):
        out = self.conv1(x)
        out = F.relu(self.bn1(out), True)
        out = self.conv2(out)
        out = F.relu(self.bn2(out), True)
        
        if not self.same_shape:
            x = self.conv3(x)
        return F.relu(x+out, True)
		
class resnet(nn.Module):
	def __init__(self, in_channel, num_classes, verbose=False):
		super(resnet, self).__init__()
		self.verbose = verbose
		
		self.block1 = nn.Conv2d(in_channel, 32, 7, 2)
		
		self.block2 = nn.Sequential(
			nn.MaxPool2d(3, 2),
			residual_block(32, 32),
			residual_block(32, 32),
			nn.AvgPool2d(3)
		)
		self.block3 = nn.Sequential(
			residual_block(32, 64, False),
			residual_block(64, 64)
		)
		self.block4 = nn.Sequential(
			residual_block(64, 256, False),
			residual_block(256, 256)
		)
		
		self.block5 = nn.Sequential(
			residual_block(256, 512, False),
			residual_block(512, 512),
			nn.AvgPool2d(3)
		)
		
		self.classifier1 = nn.Linear(32*2*2, 64)
		self.classifier2 = nn.Linear(64,16)
		self.classifier3 = nn.Linear(16, num_classes)
		self.classifier4 = nn.Linear(2, 2)
	def forward(self, x):
		x = self.block1(x)
		
		# if self.verbose:
			# print('block 1 output: {}'.format(x.shape))
		x = self.block2(x)
		
		# if self.verbose:
			# print('block 2 output: {}'.format(x.shape))#32,2,2
		# x = self.block3(x)
		
		# if self.verbose:
			# print('block 3 output: {}'.format(x.shape))
		
		# x = self.block4(x)
		# if self.verbose:
			# print('block 4 output: {}'.format(x.shape))#128,256,2,2
		# x = self.block5(x)
		
		# if self.verbose:
			# print('block 5 output: {}'.format(x.shape))
		x = x.view(x.shape[0], -1)
		#print('这个x的大小；',x.shape)#128*2340
		x = self.classifier1(x)
		x = self.classifier2(x)
		x = self.classifier3(x)
		x = self.classifier4(x)
		output = F.softmax(x, dim=1)
		return output,x
		
		
		
		

########################################################################
# Define the network to use :
# net = NetMLP(100)
net =resnet(1,2,True)
net.to(device) # move it to GPU or CPU
# show the structure :
print(net)
########################################################################
# Define a Loss function and optimizer
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# Let's use a Classification Cross-Entropy loss and SGD with momentum.

import torch.optim as optim

# criterion = nn.CrossEntropyLoss()#softmax
# optimizer = optim.SGD(net.parameters(), lr=0.001, momentum=0.9)
 
LR = 0.002
optimizer = torch.optim.Adam(net.parameters(), lr=LR)   # optimize all cnn parameters
criterion = nn.CrossEntropyLoss()                       # the target label is not one-hotted
#loss function做回归的时候用nn.MSELoss()



##评价网络
def show_train_result(epoch,i,running_loss,show_batch):#后面两个都是variables
	#最近一次的而预测
	# pred_y = torch.max(outputs[0], 1)[1].data.numpy()#根据最大softmax预测类别,若list就是argmax(list[])
	# ground_true=labels.data.numpy()
	train_err = (running_loss / show_batch)#多少个batch的loss平均值*
	print('\nEpoch %d batch %5d' % (epoch + 1, i + 1))
	print('\n{}个batch的训练平均 loss : {:.3%}'.format(show_batch,train_err))
	

def show_test_result(net):
	totalValLoss = 0.0#进入先置0
	batch=1
	test_loss=0
	test_acc=0
	#进入测试，算平均损失
	with torch.no_grad():
		for data in test_data:#(一次取得一个test_batch，取四次)
			test_x, test_y = data
			test_x, test_y = test_x.to(device), test_y.to(device)
			softmax_outputs = net(test_x)[0]#输出softmax
			normal_out=net(test_x)[1]#softmax前一层
			
			loss = criterion(softmax_outputs, test_y)#计算一个batch的loss
			totalValLoss += loss.item()#四个batch的loss叠加
			test_pred = torch.max(softmax_outputs, 1)[1].data.numpy()
			ground_true=test_y.data.numpy()#叠加loss，长度为500
			print('\ntest_batch  {},预测有{}/{}个对'.format(batch,sum(test_pred==ground_true),len(test_y)))
			batch+=1
			accuracy=sum(test_pred==ground_true)/len(ground_true)
			print('\n瞬时准确率:{:.3%}'.format(accuracy))
			test_acc+=accuracy
			test_loss+=loss
			#保存
			# if accuracy>0.85:
				# state = {'net':net.state_dict(), 'optimizer':optimizer.state_dict()}
				# torch.save(state,r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\sharedeep\net_params0.85.pkl')
			# if accuracy>0.88:
				# state = {'net':net.state_dict(), 'optimizer':optimizer.state_dict()}
				# torch.save(state,r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\sharedeep\net_params0.88.pkl')
			# if accuracy>0.9:
				# state = {'net':net.state_dict(), 'optimizer':optimizer.state_dict()}
				# torch.save(state,r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\sharedeep\net_params0.9.pkl')
			# if accuracy>0.92:
				# state = {'net':net.state_dict(), 'optimizer':optimizer.state_dict()}
				# torch.save(state,r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\sharedeep\net_params0.92.pkl')
		#plt_result(normal_out,ground_true)
		softmax_positive=softmax_outputs[:,1]
		draw_roc(ground_true,test_pred,softmax_positive)
		print('\n所以平均准确率为: {:.3%} | 平均loss {:.3} :'.format(test_acc/4,test_loss/4))
		print('\n\n\n\n')

def plt_result(pre_argmax,ground_true):
	type1x=[]
	type1y=[]
	type0x=[]
	type0y=[]
	fig=plt.figure(num='第一个对象')
	ax1=plt.subplot(1,2,1)
	ax2=plt.subplot(1,2,2)
	ax1.cla()
	ax2.cla()
	for i in range(len(ground_true)):
		if ground_true[i]==0: 
			type0x.append(pre_argmax[:,0].data.numpy()[i])
			type0y.append(pre_argmax[:,1].data.numpy()[i])
		else :
			type1x.append(pre_argmax[:,0].data.numpy()[i])
			type1y.append(pre_argmax[:,1].data.numpy()[i])
	ax1.scatter(type0x,type0y,c='b',label=r'jungle_type')
	x1=np.linspace(min(type0x),max(type0y),40)
	y1=x1
	ax1.plot(x1,y1,'r--')
	ax1.legend()
	ax2.scatter(type1x,type1y,c='r',label=r"symbol_type")
	x2=np.linspace(min(type1x),max(type1y),40)
	y2=x2
	ax2.plot(x2,y2,'r--')
	ax2.legend()
	plt.pause(0.5)
	
from sklearn import metrics
from sklearn.metrics import roc_auc_score
def draw_roc(y_true,pre,pre_pro):#传入三个数组，真实类，预测类，positive的概率
	# pro=[]
	
	# for i in range(len(pre)):
		# pro.append(proba[i,pre[i]])
	dict={'label':y_true,'pre':pre_pro}#'pro':pro
	df1=pd.DataFrame(dict)
	
	fpr,tpr,thresholds=metrics.roc_curve(df1['label'],df1['pre'],pos_label=1)
	plt.plot(fpr,tpr)
	plt.show()
	auc_score=roc_auc_score(df1['label'],df1['pre'])
	print('面积是',auc_score)






########################################################################
# 训练网络
# ^^^^^^^^^^^^^^^^^^^^


# 定义矩阵存结果，然后显示
val_err_array = np.array([])
train_err_array = np.array([])
nb_sample_array = np.array([])

# best system results
best_val_loss = 1000000
best_epoch = 0
best_model =  copy.deepcopy(net)
nb_used_sample = 0
running_loss = 0.0
num_epochs = 10
print('总数据长度:',len(folder_set))
print('验证长度:',len(test_data1))#2000
one_epoch_length=len(folder_set)

#读取权重
checkpoint = torch.load(r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\sharedeep\restnet4fc\net_params0.9.pkl')
net.load_state_dict(checkpoint['net'])
optimizer.load_state_dict(checkpoint['optimizer'])
# # start_epoch = checkpoint['epoch'] + 1

	
for epoch in range(num_epochs):  # loop over the dataset multiple times
	start_time = time.time()
	for i, data in enumerate(train_data, 0):
		if i%50==0:
			a=nb_used_sample/minibatchsize
			b=len(folder_set)/minibatchsize
			c=a/b
			print(r'当前batch:{}/{},{:.2%}'.format(a,b,c), end="\r")
			
		inputs, labels = data#一个batch
		inputs, labels = inputs.to(device), labels.to(device) # if possible, move them to GPU
		#inputs:[2,3,32,32]
		# zero the parameter gradients
		optimizer.zero_grad()
		# forward + backward + optimize
		outputs = net(inputs)[0]#输出为variable类型,(softmax,x)
		loss = criterion(outputs, labels)#计算lossfunction，输入输出和label
		loss.backward()
		optimizer.step()#梯度施加到网络参数中
		nb_used_sample += minibatchsize#现在到第几个符号
		running_loss += loss.item()#loss叠加，一个batch加一次
		
		#设置多少个batch显示一次训练结果
		show_batch=4
		if nb_used_sample % (show_batch * minibatchsize) == 0:    #每{}个batch就操作一次
			show_train_result(epoch,i,running_loss,show_batch)#传入总lost,show_batch(积累loss次数,单位batch)
			running_loss=0#重置loss
			show_test_result(net)
			
			# if nb_used_sample % (2000 * minibatchsize) == 0:
			
			
			# val_err = (totalValLoss / (len(test_data1)/test_batch))#得到平均的测试集loss
			# print('测试集平均 loss  : {:.3f}'.format(val_err))
			# print('\n','\n')
			# train_err_array = np.append(train_err_array, train_err)
			# val_err_array = np.append(val_err_array, val_err)#把平均测试拼在里面
			# nb_sample_array = np.append(nb_sample_array, nb_used_sample)
			
			# # save the model only when loss is better
			# best_model =  copy.deepcopy(net)
	# print("Epoch {} of {} took {:.3f}s".format(epoch + 1, num_epochs, time.time() - start_time))

print('Finished Training')











### save the best model :
# torch.save(best_model.state_dict(), "./best_model.nn")

##############################################################################
# Prepare and draw the training curves

# plt.clf()
# plt.xlabel('epoch')
# plt.ylabel('val / train LOSS')
# plt.title('Digit classifier')
# plt.plot(nb_sample_array.tolist(), val_err_array.tolist(), 'b',nb_sample_array.tolist(), train_err_array.tolist(), 'r', [best_epoch], [best_val_loss],         'go')
# plt.savefig('resultMLP.png')

########################################################################
# Test the network on the test data#选出最好的model
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# first on few sample, just to see real results
# dataiter = iter(testloader)
# images, labels = dataiter.next()
# plt.clf()
# imshow(torchvision.utils.make_grid(images))
# print('GroundTruth: ', ' '.join('%5s' % classes[labels[j]] for j in range(minibatchsize)))
# # activate the net with these examples
# outputs = best_model(images)

# # get the maximum class number for each sample, but print the corresponding class name
# _, predicted = torch.max(outputs, 1)
# print('Predicted: ', ' '.join('%5s' % classes[predicted[j]]
                              # for j in range(minibatchsize)))

# # Test now  on the whole test dataset.

# correct = 0
# total = 0
# with torch.no_grad():
    # for data in testloader:
        # images, labels = data
        # outputs = best_model(images)
        # _, predicted = torch.max(outputs.data, 1)
        # total += labels.size(0)
        # correct += (predicted == labels).sum().item()

# print('Accuracy of the network on the test images: %d %%' % (
    # 100 * correct / total))

# # Check the results for each class
# class_correct = list(0. for i in range(nb_classes))
# class_total = list(0. for i in range(nb_classes))
# with torch.no_grad():
    # for data in testloader:
        # images, labels = data
        # outputs = best_model(images)
        # _, predicted = torch.max(outputs, 1)
        # c = (predicted == labels).squeeze()
        # for i in range(minibatchsize):
            # label = labels[i]
            # class_correct[label] += c[i].item()
            # class_total[label] += 1


# for i in range(nb_classes):
    # if class_total[i] > 0 :
        # print('Accuracy of %5s : %2d %% (%d/%d)' % (
            # classes[i], 100 * class_correct[i] / class_total[i], class_correct[i] , class_total[i]))
    # else:
        # print('No %5s sample' % (classes[i]))




