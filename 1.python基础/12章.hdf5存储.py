#

import h5py
import numpy as np
# import torch
# a=3
# print(torch.Tensor([a]))

readmode=1
# readmode=0

if readmode==1:
	f = h5py.File(r"C:\lcb\learning_python_git\python_basic\1.python基础\mytestfile.hdf5", 'r')  #打开.h5
	
	print(list(f.keys())) #看数据集列表，所有主键
	dset = f['init']
	print(dset)
	print(dset.shape)
	print(dset.dtype)
	print(np.array(dset))
	f.close()
	# print(dset.value)
	
#.shape .dtype

if readmode==0:
#保存操作
	f = h5py.File(r"C:\lcb\learning_python_git\python_basic\1.python基础\mytestfile.hdf5", "w") #建立一个h5文件
	#dset = f.create_dataset(u"mydataset", (100,), dtype='i') #建立一个数据集
	# X = f.create_dataset(shape=(0,args.patch_size,args.patch_size),　            #数据集的维度
							# maxshape = (None,args.patch_size,args.patch_size),                #数据集的允许最大维度　
							# dtype=float,compression='gzip',name='train',                      #数据类型、是否压缩，以及数据集的名字
							# chunks=(args.chunk_size,args.patch_size,args.patch_size))         #分块存储，每一分块的大小
	arr = np.zeros((30,3,128,256),dtype=np.float32)
	dset = f.create_dataset("init", data=arr)#init主键
	dset = f.create_dataset("label", data=3)#init主键
	# f.create_group("subgroup") #建立group
	f.close()
	



