#torch模型保存


#读取权重，在进入epoch之前
# checkpoint = torch.load(r'C:\Users\mrliangcb\Desktop\笔记整理\pytorch\sharedeep\restnet4fc\net_params0.9.pkl')
# net.load_state_dict(checkpoint['net'])
# optimizer.load_state_dict(checkpoint['optimizer'])
# # start_epoch = checkpoint['epoch'] + 1


for i in range(epoch):
	……
	state = {'net':net.state_dict(), 'optimizer':optimizer.state_dict(),'epoch':epoch}
	path_checkpoint=r'./{}_{}.clk'.format(epoch,i)
	torch.save(state,path)
			