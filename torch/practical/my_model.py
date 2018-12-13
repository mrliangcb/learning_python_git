#net_model
from torch import nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch

def conv3x3(in_channel, out_channel, stride=1):
		return nn.Conv2d(in_channel, out_channel, 3, stride=stride, padding=1, bias=False)

		
class CNN2(nn.Module):
    def __init__(self):
        super(CNN2, self).__init__()
        self.conv1 = nn.Sequential(
                nn.Conv2d(
                        in_channels=1,
                        out_channels=16,
                        kernel_size=5,
                        stride=1,
                        padding=2
                        ),
                nn.ReLU(),
                nn.MaxPool2d(kernel_size=2))
        self.conv2 = nn.Sequential(
                nn.Conv2d(16, 32, 5, 1, 2), 
                nn.ReLU(), 
                nn.MaxPool2d(2))
        self.out = nn.Linear(32*7*7, 10)
    
    def forward(self, x):
        x = self.conv1(x)
        x = self.conv2(x)
        x = x.view(x.size(0), -1)
        output = self.out(x)#logit输出，如果loss函数为mse，则还要进行softmax
        return output#, x
		

		
class CNN(nn.Module):#这是mnist专用28*28
	def __init__(self):
		super(CNN, self).__init__()
		self.conv1 = nn.Sequential(         # input shape (1, 28, 28)
			nn.Conv2d(
				in_channels=1,              # input height
				out_channels=32,            # n_filters
				kernel_size=5,              # filter size
				stride=1,                   # filter movement/step
				padding=2,                  # if want same width and length of this image after Conv2d, padding=(kernel_size-1)/2 if stride=1
			),                              # output shape (16, 28, 28)
			nn.ReLU(),                      # activation
			nn.MaxPool2d(kernel_size=2),    # choose max value in 2x2 area, output shape (16, 14, 14)
			nn.BatchNorm2d(32),
		)
		self.conv2 = nn.Sequential(         # input shape (16, 14, 14)
			nn.Conv2d(32, 64, 5, 1, 2),     # output shape (32, 14, 14)
			nn.ReLU(),                      # activation
			nn.MaxPool2d(2),                # output shape (32, 7, 7)
			nn.BatchNorm2d(64),			#这里有1d和2d的
		)
		self.fc1 = nn.Linear(32 * 7 * 7*2, 10)   # fully connected layer, output 10 classes
		#self.bn1 = nn.BatchNorm1d(1024, momentum=0.5)
		#self.fc2 = nn.Linear(1024, 10)									#拍扁之后mlp
		#self.bn2 = nn.BatchNorm1d(10, momentum=0.5)
		self.dropout=nn.Dropout(0.5)
	def forward(self, x):
		
		x = self.conv1(x)
		x = self.conv2(x)
		x = x.view(x.size(0), -1)           # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
		x = self.dropout(x)
		output = self.fc1(x)
		# output=self.bn1(output)
		# output = self.dropout(output)
		# output = self.fc2(output)
		# output=self.bn2(output)
		
		#torch里面的代价函数自带求softmax所以输出直接logit就好了，mse和crossentropy都是
		#output = F.softmax(x, dim=1)
		return output   # return x for visualization

class residual_block(nn.Module):
	def __init__(self, in_channel, out_channel, same_shape=True):
		super(residual_block, self).__init__()
		self.same_shape = same_shape
		stride=1 if self.same_shape else 2
		
		self.conv1 = conv3x3(in_channel, out_channel, stride=stride)
		self.bn1 = nn.BatchNorm2d(out_channel)#outchannel或者是输出特征数（mlp）
		
		self.conv2 = conv3x3(out_channel, out_channel)
		self.bn2 = nn.BatchNorm2d(out_channel)
		if not self.same_shape:
			self.conv3 = nn.Conv2d(in_channel, out_channel, 1, stride=stride)
			#通过步长来减少一半长宽，增加一倍的channel
		
	def forward(self, x):
		#经过一次3*3卷积，直接到达输出channel，长宽不变
		#如果输出比输入channel大了一倍，则步长设为2，长宽减少一半
		out = self.conv1(x)
		out = F.relu(self.bn1(out), True)
		##第一第二层间输入输出channel大小不变，则长宽不变
		out = self.conv2(out)
		out = F.relu(self.bn2(out), True)
		
		#如果下一个块channel比这层大，如64到128
		#如果汇合的时候channel不同(输入和输出channel不同的时候进入)
		if not self.same_shape:
			x = self.conv3(x)
		return F.relu(x+out, True)#输入加上输出
		
class resnet(nn.Module):
	def __init__(self, in_channel, num_classes, verbose=False):
		super(resnet, self).__init__()
		self.verbose = verbose
		
		self.block1 = nn.Conv2d(in_channel, 64, 7, 2)#先进行卷积
		
		self.block2 = nn.Sequential(
			nn.MaxPool2d(3, 2),
			residual_block2(64, 64),
			residual_block2(64, 64),
			
		)
		self.block3 = nn.Sequential(
			residual_block2(64, 128, False),#前后块形状不同了
			residual_block2(128, 128)
		)
		self.block4 = nn.Sequential(
			residual_block2(128, 256, False),
			residual_block2(256, 256)
		)
		
		self.block5 = nn.Sequential(
			residual_block2(256, 512, False),
			residual_block2(512, 512),
			nn.AvgPool2d(3)
		)
		
		self.classifier1 = nn.Linear(512, num_classes)
		# self.classifier2 = nn.Linear(512,num_classes)
		# self.classifier3 = nn.Linear(16, num_classes)
	def forward(self, x):
		x = self.block1(x)
		
		# if self.verbose:
			# print('block 1 output: {}'.format(x.shape))
		x = self.block2(x)
		
		# if self.verbose:
			# print('block 2 output: {}'.format(x.shape))#32,2,2
		x = self.block3(x)
		
		# if self.verbose:
			# print('block 3 output: {}'.format(x.shape))
		
		x = self.block4(x)
		# if self.verbose:
		# print('block 4 output: {}'.format(x.shape))#128,256,6,6
		x = self.block5(x)
		
		# if self.verbose:
		#print('block 5 output: {}'.format(x.shape))
		x = x.view(x.shape[0], -1)#改变一下形状
		#print('这个x的大小；',x.shape)#128*2340
		last_layer = self.classifier1(x)
		# x = self.classifier2(x)
		#output = F.softmax(last_layer, dim=1)
		return last_layer

		
		
def conv_relu(in_channel, out_channel, kernel, stride=1, padding=0):
	layer = nn.Sequential(
		nn.Conv2d(in_channel, out_channel, kernel, stride, padding),
		nn.BatchNorm2d(out_channel, eps=1e-3),
		nn.ReLU(True)
	)
	return layer
	
class inception(nn.Module):
	def __init__(self, in_channel, out1_1, out2_1, out2_3, out3_1, out3_5, out4_1):
		super(inception, self).__init__()
		# 第一条线路
		self.branch1x1 = conv_relu(in_channel, out1_1, 1)
		
		# 第二条线路
		self.branch3x3 = nn.Sequential( 
			conv_relu(in_channel, out2_1, 1),
			conv_relu(out2_1, out2_3, 3, padding=1)
		)
		
		# 第三条线路
		self.branch5x5 = nn.Sequential(
			conv_relu(in_channel, out3_1, 1),
			conv_relu(out3_1, out3_5, 5, padding=2)
		)
		
		# 第四条线路
		self.branch_pool = nn.Sequential(
			nn.MaxPool2d(3, stride=1, padding=1),
			conv_relu(in_channel, out4_1, 1)
		)
		
	def forward(self, x):
		f1 = self.branch1x1(x)
		f2 = self.branch3x3(x)
		f3 = self.branch5x5(x)
		f4 = self.branch_pool(x)
		output = torch.cat((f1, f2, f3, f4), dim=1)
		return output

class googlenet(nn.Module):
	def __init__(self, in_channel, num_classes, verbose=False):
		super(googlenet, self).__init__()
		self.verbose = verbose
		
		self.block1 = nn.Sequential(
			conv_relu(in_channel, out_channel=64, kernel=7, stride=2, padding=3),
			nn.MaxPool2d(3, 2)
		)
		
		self.block2 = nn.Sequential(
			conv_relu(64, 64, kernel=1),
			conv_relu(64, 192, kernel=3, padding=1),
			nn.MaxPool2d(3, 2)
		)
		
		self.block3 = nn.Sequential(
			inception(192, 64, 96, 128, 16, 32, 32),
			inception(256, 128, 128, 192, 32, 96, 64),
			nn.MaxPool2d(3, 2)
		)
		
		self.block4 = nn.Sequential(
			inception(480, 192, 96, 208, 16, 48, 64),
			inception(512, 160, 112, 224, 24, 64, 64),
			inception(512, 128, 128, 256, 24, 64, 64),
			inception(512, 112, 144, 288, 32, 64, 64),
			inception(528, 256, 160, 320, 32, 128, 128),
			nn.MaxPool2d(3, 2)
		)
		
		self.block5 = nn.Sequential(
			inception(832, 256, 160, 320, 32, 128, 128),
			inception(832, 384, 182, 384, 48, 128, 128),
			nn.AvgPool2d(2)
		)
		
		self.classifier = nn.Linear(1024, num_classes)
		
	def forward(self, x):
		x = self.block1(x)
		if self.verbose:
			print('block 1 output: {}'.format(x.shape))
		x = self.block2(x)
		if self.verbose:
			print('block 2 output: {}'.format(x.shape))
		x = self.block3(x)
		if self.verbose:
			print('block 3 output: {}'.format(x.shape))
		x = self.block4(x)
		if self.verbose:
			print('block 4 output: {}'.format(x.shape))
		x = self.block5(x)
		if self.verbose:
			print('block 5 output: {}'.format(x.shape))
		x = x.view(x.shape[0], -1)
		x = self.classifier(x)
		return x
#看一下网络输入输出参数
# test_net = inception(3, 64, 48, 64, 64, 96, 32)
# test_x = Variable(torch.zeros(1, 3, 96, 96))
# print('input shape: {} x {} x {}'.format(test_x.shape[1], test_x.shape[2], test_x.shape[3]))
# test_y = test_net(test_x)
# print('output shape: {} x {} x {}'.format(test_y.shape[1], test_y.shape[2], test_y.shape[3]))







