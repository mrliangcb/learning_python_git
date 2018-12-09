#opencv
import numpy as np
import cv2 as cv

#读入图片
src = cv.imread(r'*.jpg')
#show
cv.imshow('imput image2',src)
cv.waitKey(0)  #如果《=0，表示一直延迟，返回值为按键的值，检测到按键就延时结束。
cv.destroyAllwindows()#当上面延迟结束之后，到这一条指令，关闭所有窗口



#视频加载，保存
def get_image_info(image):
	#cv.imshow('imput image2',src)
	print(image.shape)  #高度，宽度，通道
	print(image.shape[0])#取到高度
	print(image.size)	#总的像素数据
	print(image.dtype)	#每个像素的每个通道所占用的位数
	print(type(image))	#numpy类型
	pixel_data = np.array(image)
	#print(pixel_data)
	gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)#把原图像变成灰色图像
	cv.imshow('imput image2',gray)
	cv.imwrite(r'*.jpg',gray) #保存图片src以jpg的格式
	#cv.waitKey(0)

def get_image_info(image):
	#cv.imshow('imput image2',src)
	print(image.shape)  #高度，宽度，通道
	print(image.shape[0])#取到高度
	print(image.size)	#总的像素数据
	print(image.dtype)	#每个像素的每个通道所占用的位数
	print(type(image))	#numpy类型
	pixel_data = np.array(image)
	#print(pixel_data)
	gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)#把原图像变成灰色图像
	cv.imshow('imput image2',gray)
	cv.imwrite(r'C:\Users\mrliangcb\Desktop\abc\save\result2.jpg',gray) #保存图片src以jpg的格式
	#cv.waitKey(0)
get_image_info(src)#里面最后一行waitkey一直等待按键，如果没有按键，则一直滞留
video_demo()
#cv.waitKey(0)#等待按键
cv.destroyWindow('video')
#cv.destroyAllWindows()



def access_pixels(image):
	cv.imshow('imput image2',image)
	print(image.shape)
	height = image.shape[0]
	width = image.shape[1]
	channels = image.shape[2]
	print("width : %s height : %s  channels : %s"%(width,height,channels))
	
access_pixels(src)
cv.waitKey(0)
cv.destroyAllWindows()


def fill_color_demo(image):
	copyimage = image.copy()
	h,w = image.shape[:2]#0为行数，1位列数
	mask = np.zeros([h+2,w+2],np.uint8) #泛洪填充，可能是弄个标志位，保证元素都遍历了
	cv.floodFill(copyimage,mask,(30,30),(0,255,255),(100,100,100),(50,50,50),cv.FLOODFILL_FIXED_RANGE)
	cv.imshow('范洪:',copyimage)
	cv.waitKey(0)
	

def access_pixels(image):
	print(image.shape)
	height = image.shape[0]
	width = image.shape[1]
	channels = image.shape[2]
	print("width : %s height : %s  channels : %s"%(width,height,channels))
	
	image2 = image[100:300,100:300,:]#选择区域，3通道的图像
	print('image2_shape',image.shape) #1028*1024*3
	gray = cv.cvtColor(image2 , cv.COLOR_BGR2GRAY) #变灰色
	print('gray_shape:',gray.shape)#200*200
	backface=cv.cvtColor(gray ,cv.COLOR_GRAY2BGR)#把灰色大小的这个填充给彩色全图，但先要变回3通道
	image[100:300,100:300]=backface
	cv.imshow('imput image2',image)
	cv.waitKey(0) #等待按键
fill_color_demo(src)


#直方图
# from matplotlib import pyplot as plt
# src=cv2.imread(r'C:\Users\mrliangcb\Desktop\ljy.jpg')

# def plot_demo(image):
	# plt.hist(image.ravel(), 256, [0,256])
	# plt.show('直方图') 
# plot_demo(src)
# cv.waitKey(300)
# cv.destroyAllWindows()

# def hist2d_demo(image):
	# hsv = cv.cvtColor(image,cv.COLOR_BGR2HSV)
	# hist = cv.calcHist([image],[0,1],None,[180,256],[0,180,0,256])
	# cv.imshow('image')


#常用属性:
#(1)















