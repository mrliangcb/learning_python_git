#my_get_data
import time
import copy
import os
import torch
import torchvision
import torchvision.transforms as transforms
import torch.optim as optim
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import torch.nn as nn
import torch.nn.functional as F
import pandas as pd
from torchvision.datasets import ImageFolder   
from torch.utils.data import DataLoader  

def get_dataLoader(path):
	minibatchsize = 64
	testsize = 200
	
	transform = transforms.Compose(
		[transforms.Grayscale(),  # CROHME png are RGB, but already 32x32
		#transforms.Scale(96),
		transforms.ToTensor(),
		transforms.Normalize((0.5,), (0.5,))])
	fulltrainset = torchvision.datasets.ImageFolder(root=path, transform=transform)
	a_part = int(len(fulltrainset) / 10)
	trainset, validationset, testset = torch.utils.data.random_split(fulltrainset, [8 * a_part, a_part,len(fulltrainset) - 9 * a_part])
	print('training_all:',len(trainset))#51480
	print('vali_all',len(validationset))#17160
	print('test_all',len(testset))
	
	trainloader = torch.utils.data.DataLoader(trainset, batch_size=minibatchsize,
											shuffle=True, drop_last=True)#, num_workers=1
	validationloader = torch.utils.data.DataLoader(validationset, batch_size=minibatchsize,
												shuffle=False, drop_last=True)#, num_workers=1
	testloader = torch.utils.data.DataLoader(testset, batch_size=testsize,
											shuffle=False, drop_last=True)#, num_workers=1
	classes = [x[0].replace(path, '') for x in os.walk(path)][1:]  
	print('Name of classes:',classes)
	nb_classes = len(classes)
	print("Number of classes :%d , training size:%d, validation size:%d, test size:%d" % (
		nb_classes, 3 * a_part, a_part, len(fulltrainset) - 4 * a_part))
	return trainloader,validationloader,testloader,classes,nb_classes,minibatchsize,testsize
	
from torchvision.datasets import mnist
def mnist_dataLoader(path):
	#train_set = mnist.MNIST(path, train=True, download=False)
	#test_set = mnist.MNIST(path, train=False, download=False)
	
	transform = transforms.Compose(
			[transforms.Grayscale(),  # CROHME png are RGB, but already 32x32
			transforms.Resize(28),#Scale
			transforms.ToTensor(),
			transforms.Normalize((0.5,), (0.5,))])
			
	train_set = mnist.MNIST(path, train=True, transform=transform, download=False) # 重新载入数据集，申明定义的数据变换
	test_set = mnist.MNIST(path, train=False, transform=transform, download=False)
	
	print('训练集长度',len(train_set))#60000
	print('测试集长度',len(test_set))#10000
	a, a_label = train_set[0]
	print(a.shape)
	print(a_label)
	batch=64
	trainloader = DataLoader(train_set, batch_size=batch, shuffle=True)
	testloader = DataLoader(test_set, batch_size=batch, shuffle=False)
	return trainloader,testloader,batch
			
			
			
			
			
			
			