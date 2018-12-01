#torch gpu运行

# device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
# print('电脑设备:',device)
#查看

###分成两步：网络放在gpu上，数据放在gpu上


# 建立好模型之后，准备进入epoch训练
net=net.cuda(0)#先把网络放在gpu上

for epoch in range(num_epochs):
	print(r'/n第几张图{} | 当前batch:{:.1f}/{:.1f} | {:.1%}'.format(i,a,b,c),end="\r")
	for img, label in train_loader:
		img = Variable(im)#如果是numpy list 进来要换成variable
		img = im.cuda(0)#把数据放在gpu上
		label = Variable(label)
		label = label.cuda(0)#把数据放在gpu上
		#如果要把gpu数据换成cpu的(才能用numpy)
		label.cpu().data.numpy()