#learning_curve


#一个batch对应一个acc和loss
global_bath=df2.values
global_train=df3.values
global_loss=df4.values

fig=plt.figure(num='learning curve')
ax1=plt.subplot(1,2,1)
ax1.cla()
ax1.plot(global_bath,global_train,'b-',label="train_acc",linewidth=1)
# plt.title('acc')
plt.xlabel(u"epoch")#显示横轴名字
plt.ylabel(u"acc")
plt.legend()
plt.grid(True)
ax2=plt.subplot(1,2,2)
ax2.cla()
ax2.plot(global_bath,global_loss,'r-',label="train_loss",linewidth=1)
# plt.title('loss')
plt.xlabel(u"epoch")#显示横轴名字
plt.ylabel(u"loss")
plt.legend()
plt.grid(True)
plt.show()

#保存
png_path=r'./result/plt/{}.png'.format(epoch)
# plt.savefig(png_path)#保存图片