#第9章.plt画图
#本文分为 (1)plt基础  (2)动态画线  (3)画学习曲线
import numpy as np
import matplotlib.pyplot as plt
import pdb



#################   (1)plt基础     ###################
x = np.linspace(0, 10, 1000)
y=x**2
z=np.sin(x)

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 这两条可以使得标题和图例显示中文

#用figure创建主图，用subplot创建子图
fig=plt.figure(num='第一个对象',figsize=(8,4))

ax1=plt.subplot(1,2,1)#ax1指针指向当前这个窗口显示4个子图，最后一个参数表示第一个子图
ax1.plot(x,y,'r-',label="x^2",linewidth=1,markerfacecolor='blue',markersize='5')
plt.text(1,1,(1,1),ha='center', va='bottom', fontsize=10)
plt.title('R channel')
plt.xlabel(u"Time(s)")#显示横轴名字
plt.ylabel(u"Volt")

plt.ylim(-2,2)
plt.xlim(-3,15)
#plt.text(5,1,'three') 在5,1上显示这个文字
plt.yticks([-2,-1.8,-1,1.22],[r'same',r'mike',r'blue',r'hhaa'])#在特定坐标轴位置标记
plt.legend()#图例生效


#操作第二个子图
ax2=plt.subplot(1,2,2)
ax2.plot(x,z,'b-',label="sin(x)",linewidth=1,markerfacecolor='blue',markersize='5')
plt.title(u"PyPlot First Example")
plt.legend()#图例生效
plt.grid(True)#网格模式

#保存
#plt.savefig(r'C:\Users\mrliangcb\Desktop\笔记整理\python\画图\tessstttyyy.png')#保存图片，正确运行






# plt.pause(2)#但如果重复画图的话，不会重置图像需要ax1.cla()  clf()来清除  close（）只是关掉窗口  或者重新设置窗口也是可以的
plt.show() #
# plt.pause(15)#
# plt.close()#这个是关闭窗口
#plt.clf()#清空画布上所有内容

# 颜色（color 简写为 c）：
# 蓝色： 'b' (blue)
# 绿色： 'g' (green)
# 红色： 'r' (red)
# 蓝绿色(墨绿色)： 'c' (cyan)
# 红紫色(洋红)： 'm' (magenta)
# 黄色： 'y' (yellow)
# 黑色： 'k' (black)
# 白色： 'w' (white)

# 线型（linestyle 简写为 ls）：
# 实线： '-'
# 虚线： '--'
# 虚点线： '-.'
# 点线： ':'
# 点： '.' 

# 点型（标记marker）：
# 像素： ','
# 圆形： 'o'
# 上三角： '^'
# 下三角： 'v'
# 左三角： '<'
# 右三角： '>'
# 方形： 's'
# 加号： '+' 
# 叉形： 'x'
# 棱形： 'D'
# 细棱形： 'd'
# 三脚架朝下： '1'（像'丫'）
# 三脚架朝上： '2'
# 三脚架朝左： '3'
# 三脚架朝右： '4'
# 六角形： 'h'
# 旋转六角形： 'H'
# 五角形： 'p'
# 垂直线： '|'
# 水平线： '_'

#plt.imshow(im.astype('uint8'), cmap='gray')通常这样可视化图像
#edge1 = edge1.data.squeeze().numpy()# 将输出转换为图片的格式
#plt.imshow(edge1, cmap='gray')

#scatter
#plt.scatter(x.data.numpy()[:, 0], x.data.numpy()[:, 1], c=pred_y, s=4, lw=0.1, cmap='RdYlGn')



#https://blog.csdn.net/u013468614/article/details/58689735 动态显示！


#################    二、动态划线     ###################
# from matplotlib.animation import FuncAnimation
# fig=plt.figure(num='第一个对象')
# ax=plt.subplot(2,2,1)


# xdata, ydata = [], []
# ln, = ax.plot([], [], 'r-', animated=False)

# def init():
    # ax.set_xlim(0, 2*np.pi)
    # ax.set_ylim(-1, 1)
    # return ln,

# def update(frame):
    # xdata.append(frame)
    # ydata.append(np.sin(frame))
    # ln.set_data(xdata, ydata)
    # return ln,

# ani = FuncAnimation(fig=fig,func=update, frames=np.linspace(0, 2*np.pi, 128),
                    # init_func=init,interval=20,blit=True)
# plt.show()

########################################################


################### (3)画学习曲线  #####################
# global_bath=df2.values
# global_train=df3.values
# global_loss=df4.values

# fig=plt.figure(num='learning curve')
# ax1=plt.subplot(1,2,1)
# ax1.cla()
# ax1.plot(global_bath,global_train,'b-',label="train_acc",linewidth=1)
# # plt.title('acc')
# plt.xlabel(u"epoch")#显示横轴名字
# plt.ylabel(u"acc")
# plt.legend()
# plt.grid(True)
# ax2=plt.subplot(1,2,2)
# ax2.cla()
# ax2.plot(global_bath,global_loss,'r-',label="train_loss",linewidth=1)
# # plt.title('loss')
# plt.xlabel(u"epoch")#显示横轴名字
# plt.ylabel(u"loss")
# plt.legend()
# plt.grid(True)
# plt.show()

# #保存
# png_path=r'./result/plt/{}.png'.format(epoch)
########################################################################






