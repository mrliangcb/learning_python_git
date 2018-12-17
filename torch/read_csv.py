#torch read csv
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
txt_path=r'C:\lcb\learning_python_git\learning_python_git\torch\test.csv'



with open(txt_path, mode='rt') as f:
			lines = f.readlines()
print(lines)#['第一行','第二行']
img_list = [i.split(',') for i in lines]#可以在(',')后面[]取出每行的哪个元素
print('########### 逗号分隔 #############')
print(img_list)#[['第一行元素1','第一行元素2'],[第二行]]


print('##### 取出特定特征 #####')
#假如我们只想要第0列和第3列元素
fea0=[]
fea3=[]
for i in img_list:
	fea0.append(i[0])
print(fea0)
for i in img_list:
	fea3.append(i[3])
print(fea3)


###########################################
print('##########  下面是dataloader实验   ###################')
class custom_dataset(Dataset):
	def __init__(self, txt_path, transform=None):
		self.transform = transform # 传入数据预处理
		with open(txt_path, mode='rt') as f:
			lines = f.readlines()
			print(lines)#得到一个数组，每个元素是一个str，是一行数据
			#for i in lines:
				#print('输出',len(i.split()))#放在数组
		self.img_list = [i.split(',')[0] for i in lines] # 遍历每一行，取出每行的第0特征
		self.label_list = [i.split(',')[3] for i in lines] # 遍历每一行，取出每行的第3特征
	#上面执行完就进入下面
	def __getitem__(self, idx): # 提供用法 实例名[下标]
		
		img = self.img_list[idx]
		label = self.label_list[idx]
		#这里包装了两个输出值
		
		if self.transform is not None:
			img = self.transform(img)
		return img, label
	#上面return之后就不运行下面了
	def __len__(self): # 提供用法 len(实例名)
		print('进入2')
		return len(self.label_list)

txt_dataset = custom_dataset(txt_path)
train_data2 = DataLoader(txt_dataset, batch_size=2, shuffle=False)

for i in train_data2:#dataloader都是要放到for里面循环
	print(i)

print('### 所以可以用两个变量分别取dataloader返回的两个元素 ###')	
for i in train_data2:#dataloader都是要放到for里面循环
	a,b=i
	print('a:',a)
	print('b:',b)

	
	
	
	
	