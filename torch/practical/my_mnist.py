#train
import my_get_data
import my_model
from torch import nn
import torch.optim as optim
import torch 
import numpy as np
import copy
import pandas as pd
from torch.autograd import Variable
#use gpu_flag to set gpu

select_cuda=0
server=False
gpu=False
#True

#get_Data
if server:
	path=r'./MNIST_data'
else:
	path = r'./MNIST_data'
trainloader,testloader,minibatchsize=my_get_data.mnist_dataLoader(path)



# net = nn.Sequential(
    # nn.Linear(784, 400),
    # nn.ReLU(),
    # nn.Linear(400, 200),
    # nn.ReLU(),
    # nn.Linear(200, 100),
    # nn.ReLU(),
    # nn.Linear(100, 10)
# )

#build model
#net = my_model.googlenet(1, 10, False)#false表示不显示featuremap
net=my_model.CNN()
if gpu:
	net=net.cuda(select_cuda)
print(net)

#交叉熵代价函数
criterion = nn.CrossEntropyLoss()#输入的是logit，和groundtrue
#MSE代价函数，两个都包含了softmax+求代价，所以输入的都是logit
#criterion = torch.nn.MSELoss(size_average=False)
#loss = loss_fn(y_pred, y)

optimizer = optim.Adam(net.parameters(), lr=0.002)

nb_used_sample=0
running_loss=0
num_epochs=20

#note
global_bath=[]#
global_train_loss=[]
global_train_acc=[]
global_vali_loss=[]
global_vali_acc=[]

for epoch in range(num_epochs):

	for i, data in enumerate(trainloader, 0):
		net.train()
		print('now_batch:{} / |共epoch:{}'.format(i,num_epochs),end="\r")
		inputs, labels = data
		inputs=Variable(inputs)
		labels=Variable(labels)
		train_labels=labels.data.numpy()
		if gpu:inputs, labels=inputs.cuda(select_cuda), labels.cuda(select_cuda)
		
		optimizer.zero_grad()
		outputs = net(inputs)#softmax
		loss = criterion(outputs, labels)#输入的是logit，和groundtrue

		loss.backward()
		optimizer.step()
		nb_used_sample += minibatchsize#第几张图
		running_loss += loss.item()#累计loss
		
		show_result=500
		if nb_used_sample % (show_result * minibatchsize) == 0:  # print every 1000 mini-batches
			train_err = (running_loss / (show_result * minibatchsize))#每个样本的loss
			print('Epoch %d batch %5d ' % (epoch + 1, i + 1))
			print('Train loss : %.3f' % train_err)
			running_loss = 0.0
			if gpu:
				train_pre= torch.max(outputs,1)[1].cpu().data.numpy()
			else:
				train_pre= torch.max(outputs,1)[1].data.numpy()
			
			train_acc=np.sum(np.array(train_pre)==np.array(train_labels))/len(train_labels)
			print('瞬时准确率:',train_acc)

			# evaluation on validation set
			totalValLoss = 0.0
			flag=0
			vali_num=0
			cal_acc=0
			net.eval()
			with torch.no_grad():
				for data in testloader:
					images,labels= data
					inputs=Variable(inputs)
					labels=Variable(labels)
					vali_y=labels.data.numpy()
					flag+=1
					if gpu:
						images, labels=inputs.cuda(select_cuda), labels.cuda(select_cuda)
					outputs = net(images)
					loss = criterion(outputs, labels)
					totalValLoss += loss.item()
					if gpu:
						pre = torch.max(outputs,1)[1].cpu().data.numpy()#torch.max(outputs,1):([0.97,0.1,0.45],[101,1,98])
					else:
						
						pre = torch.max(outputs,1)[1].data.numpy()
					
					vali_accuracy=np.sum(pre==vali_y)/len(vali_y)
					print('how_many right:{}/{}'.format(np.sum(pre==vali_y),len(vali_y)))
					print('{}_test_acc:{:.4%}'.format(flag,vali_accuracy))
					if flag>=10:
						break
						# cal_acc+=vali_accuracy
						# vali_num+=len(vali_y)
				# val_err = (totalValLoss / vali_num)
				# vali_accuracy=cal_acc/flag
				# print('train_ave_acc:{:.3%}  |  vali_ave_acc{:.4%}  |  vali_ave_loss:{}'.format(train_acc,vali_accuracy,val_err))

				
				# print('\n###############################################')
				# #save_learning curve
				# global_bath.append(round(nb_used_sample/minibatchsize,0))
				# global_train_loss.append(train_err)
				# global_vali_loss.append(val_err)
				# global_vali_acc.append(vali_accuracy)
				# global_train_acc.append(round(train_acc,4))
				# # save_global={'batch':global_bath,'train_loss':global_train_loss,'train_acc':global_train_acc,
							# # 'global_vali_loss':global_vali_loss,'global_vali_acc':global_vali_acc}
				# # df=pd.DataFrame(save_global)
				# # if server:
					# # savecsv_path=r'./10111class.csv'
				# # else:
					# # savecsv_path=r'./learning_curve.csv'
				# # df.to_csv(savecsv_path,sep=',',index=0)
				
			# # if nb_used_sample % (1000 * minibatchsize) == 0:
				# if train_acc >= 0.8:
					# state = {'net':net.state_dict(), 'optimizer':optimizer.state_dict()}
				# # if server:
					
					# ckpt_path=r'./my_mnist.clk'
				# # else:
					# #ckpt_path=r'C:\lcb\learning_python_git\extradoc\TP-MLP\101program\checkpoint\net_params{}_{}.pkl'.format(epoch,train_acc)
					# torch.save(state,ckpt_path)

			
			
			
			