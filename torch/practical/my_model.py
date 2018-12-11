#net_model
from torch import nn
import torch.nn.functional as F
def conv3x3(in_channel, out_channel, stride=1):
		return nn.Conv2d(in_channel, out_channel, 3, stride=stride, padding=1, bias=False)

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
		)
		self.conv2 = nn.Sequential(         # input shape (16, 14, 14)
			nn.Conv2d(32, 64, 5, 1, 2),     # output shape (32, 14, 14)
			nn.ReLU(),                      # activation
			nn.MaxPool2d(2),                # output shape (32, 7, 7)
		)
		self.out = nn.Linear(32 * 7 * 7*2, 1024)   # fully connected layer, output 10 classes
		self.out2 = nn.Linear(1024, 10)									#拍扁之后mlp
	def forward(self, x):
		
		x = self.conv1(x)
		
		x = self.conv2(x)
		x = x.view(x.size(0), -1)           # flatten the output of conv2 to (batch_size, 32 * 7 * 7)
		
		output = self.out(x)
		output = self.out2(output)
		output = F.softmax(x, dim=1)
		return output   # return x for visualization

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
		x = self.classifier1(x)
		# x = self.classifier2(x)
		output = F.softmax(x, dim=1)
		return output










