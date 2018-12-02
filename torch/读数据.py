#torch读数据
#https://github.com/L1aoXingyu/code-of-learn-deep-learning-with-pytorch/blob/master/chapter8_PyTorch-Advances/data-io.ipynb

from torchvision.datasets import ImageFolder
# folder_set = ImageFolder(r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\example_data\image\\')
# print(folder_set.class_to_idx)
# #得到一个字典{'0':0,'3':1,'4':2} 这个文件夹搜到三种文件名0,3,4分别称为0,1,2类
# print(folder_set.imgs)#获得一个字典，每个元是图片和label的结合turble，
# print(folder_set.imgs[0][0])#获得第一位不是第一类，的组合，然后再把路径取出来
# im, label = folder_set[0]#取出第0个数据
# print(im)#PIL类型
#上面只是取一个作为例子


from torchvision import transforms as tfs
transform = tfs.Compose(#建立一个方法一
	[#tfs.Pad(2),
	 tfs.ToTensor(),
	 #transforms.Grayscale(),
	 tfs.Normalize((0.5,), (0.5,))])

data_tf = tfs.ToTensor()#建立一个方法二

folder_set = ImageFolder(root=r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\example_data\image\\', transform=transform)
im, label = folder_set[0]
print('把什么文件夹归为哪个类',folder_set.class_to_idx)#关键字为文件夹名字
print('所有图片的路径和对应的label',folder_set.imgs)#list里面包着tuple
print('图片大小',folder_set[0][0].size())
print('有多少张图:',len(folder_set))#如果要把该文件夹下的图片全部预测，则batch=这个长度




print(im)#是一个tensor 

from torch.utils.data import Dataset


#自定义的数据，读txt
# 定义一个子类叫 custom_dataset，继承与 Dataset
class custom_dataset(Dataset):
	def __init__(self, txt_path, transform=None):
		self.transform = transform # 传入数据预处理
		with open(txt_path, mode='rt') as f:
			lines = f.readlines()
			print(lines)#得到一个数组，每个元素是一个str，是一行数据
			#for i in lines:
				#print('输出',len(i.split()))#放在数组
		self.img_list = [i.split(',')[0] for i in lines] # split是设置分隔的得到所有的图像名字，用i遍历行
		self.label_list = [i.split(',')[1] for i in lines] # 得到所有的 label 
	#上面执行完就进入下面
	def __getitem__(self, idx): # 根据 idx 取出其中一个
		print('进入1')
		img = self.img_list[idx]
		label = self.label_list[idx]
		if self.transform is not None:
			img = self.transform(img)
		return img, label
	#上面return之后就不运行下面了
	def __len__(self): # 总数据的多少
		print('进入2')
		return len(self.label_list)

txt_dataset = custom_dataset(r'C:\Users\mrliangcb\Desktop\note\extra_feature\test.csv') # 读入 txt 文件
#print('得到的',txt_dataset)
# 取得其中一个数据
data, label = txt_dataset[0]#拿第几行
print(data)
print(label)


#其实可以用pandas读
#txt_dataset是一个二维np或者list，行每个ID的记录，列为每个属性
train_data2 = DataLoader(txt_dataset, 8, True) # batch size 设置为 8
print(train_data2)
# im, label = next(iter(train_data2)) # 使用这种方式访问迭代器中第一个 batch 的数据

# def collate_fn(batch):
    # batch.sort(key=lambda x: len(x[1]), reverse=True) # 将数据集按照 label 的长度从大到小排序
    # img, label = zip(*batch) # 将数据和 label 配对取出
    # # 填充
    # pad_label = []
    # lens = []
    # max_len = len(label[0])
    # for i in range(len(label)):
        # temp_label = label[i]
        # temp_label += '0' * (max_len - len(label[i]))
        # pad_label.append(temp_label)
        # lens.append(len(label[i]))
    # pad_label 
    # return img, pad_label, lens # 输出 label 的真实长度
# train_data3 = DataLoader(txt_dataset, 8, True, collate_fn=collate_fn) # batch size 设置为 8
# im, label, lens = next(iter(train_data3))


#dataloader
from torch.utils.data import DataLoader
train_data1 = DataLoader(folder_set, batch_size=2, shuffle=True) #迭代器只是只做了目录，虚拟tensor
#2个数据作为一个batch
for img,label in train_data1 :
	print('类型是:',img.shape)
#注意这里，每个图的size要相同
#for循环读dataloader之前，batch器只是拿到目录，虚拟tensor，当for的时候才是真正读
# dataiter = iter(train_data1)#的到loader类型，还不是tensor

# images, labels = dataiter.next()#转为tensor了
# print(images.shape)


#https://www.cnblogs.com/qinduanyinghua/p/9311410.html





