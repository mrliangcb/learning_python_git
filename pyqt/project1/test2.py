#pyqt画图，按钮
import sys
#from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import * #QFileDialog,QApplication,QLineEdit,QWidget,QToolTip,QPushButton,QDesktopWidget,QLabel,QDialog,QHBoxLayout, QVBoxLayout, QMessageBox
from PyQt5.QtCore import * #QCoreApplication,Qt, QEvent, QRegExp, QObject
from PyQt5.QtGui import * #QFont,QKeyEvent, QKeySequence, QRegExpValidator,QPainter,QColor,QPen
import data
import time
import numpy as np
import math


# class Mythread(QThread):
    # # 定义信号,定义参数为str类型
    # breakSignal = pyqtSignal(str,list)

    # def __init__(self, parent=None):
        # super().__init__(parent)
        # # 下面的初始化方法都可以，有的python版本不支持
        # #  super(Mythread, self).__init__()

    # def run(self):
        # for i in range(2000000):
            # # 发出信号
            
            # a=[i,i+1]
            # self.breakSignal.emit(str(i),a)
            # # 让程序休眠
            # time.sleep(0.3)




class Example(QWidget):
	def __init__(self):
		super().__init__()#继承QWidget类，返回example类的父类对象，的初始化
		self.initUI()#一开始就调用自己的函数
		self.flag=1
		# self.center()
	def initUI(self):#只调用一次
		self.lines_data=data.get_data()
		print('拿到的数据',type(self.lines_data))
		print(self.lines_data.shape)
		self.num_img=0
		
		
		# 创建线程
		#thread = Mythread() 
		# # 注册信号处理函数
		#thread.breakSignal.connect(self.chuli)
		#thread.start()
		
		QToolTip.setFont(QFont('SansSerif', 10))#用了两个组件显示

		# qbtn = QPushButton('Quit', self)#创建一个按钮
		# qbtn.clicked.connect(QCoreApplication.instance().quit)
		# qbtn.resize(qbtn.sizeHint())
		# qbtn.move(300, 300)  
		
		
		
		self.lb = QLabel("name：",self)#文本显示
		self.lb.move(400,100)
		self.edit = QLineEdit(self)#输入框
		self.edit.installEventFilter(self)
		self.edit.move(400,130)
		
		
		self.btn = QPushButton('your_name', self)#定义了一个按钮，名字
		self.btn.setToolTip('This is a <b>QPushButton</b> widget')#指着按钮显示字
		self.btn.resize(self.btn.sizeHint())
		self.btn.move(400, 160)
		self.btn.clicked.connect(self.on_click_textbox)
		
		 
		self.bt1 = QPushButton("left is unparallel",self)
		self.bt1.clicked.connect(self.on_click_1)
		self.bt2 = QPushButton("right is unparallel",self)#建立一个按钮
		self.bt2.clicked.connect(self.on_click_2)#点击按钮触发self.on_click这个函数
		self.bt3 = QPushButton("next_image",self)#建立一个按钮
		self.bt3.clicked.connect(self.on_click_3)#点击按钮触发self.on_click这个函数
		
		#布局分为水平和垂直布局
		
		#第一个水平图层
		h_buttons = QHBoxLayout()#从左往右布局顺序
		h_buttons.addStretch(1)#在前面增加了弹性空间，对于水平图层，下面的命令把元素加到这个图层
		h_buttons.addWidget(self.bt1)#放在右下角，因为左边没有任何东西，所以当做一个弹性空间
		h_buttons.addStretch(1)#现在左边有一个bt1了，再放一个弹性空间，跟前面的弹性空间平分水平值
		h_buttons.addWidget(self.bt2)#
		h_buttons.addStretch(1)#这里相当于分了3份，里面的参数表示这里放多少个弹性空间
		h_buttons.addWidget(self.bt3)#
		h_buttons.addStretch(1)#这里相当于分了3份，里面的参数表示这里放多少个弹性空间
		
		# h_lb= QHBoxLayout()
		# h_lb.addStretch(1)
		# h_lb.addWidget(self.lb)#放在水平中间
		# h_lb.addStretch(1)
		
		#第二个水平图层
		h_edit= QHBoxLayout()
		h_edit.addWidget(self.lb)
		h_edit.addWidget(self.edit)#放在水平中间btn
		h_edit.addWidget(self.btn)
		h_edit.addStretch(1)
		
		#然后把刚刚水平图层放进来做垂直规划
		vbox = QVBoxLayout()
		#vbox.addWidget(self.lb)
		#vbox.addWidget(self.edit)#这样就容易设置紧挨着的
		#从上往下布局顺序
		
		vbox.addLayout(h_edit)
		vbox.addStretch(1)
		vbox.addLayout(h_buttons)
		
		self.setLayout(vbox)

		 #这三个都是继承qwidgets类的，
		self.setGeometry(300, 300, 1900, 900)#在屏幕显示，并且设置尺寸，前两个是位置，第三宽度，第四高度
		self.setWindowTitle('choose the image unparallel to the middle one')#左上角窗口名字
		#self.setWindowIcon(QIcon('web.png')) #左上角图标

		self.show()#显示，期待下一行是循环语句
		
		
	def on_click_textbox(self):
		textboxValue = self.edit.text()
		
		print(textboxValue)
	def on_click_1(self):#按这个键之后响应
		print("左边不像")
		name = self.edit.text()
		data.mark_data(name,0,self.lines_data[self.num_img,3],self.lines_data[self.num_img,0],self.lines_data[self.num_img,1],self.lines_data[self.num_img,2])
		self.flag=0
		self.repaint()
	def on_click_2(self):#按这个键之后响应
		print("右边不像")
		name = self.edit.text()
		data.mark_data(name,1,self.lines_data[self.num_img,3],self.lines_data[self.num_img,0],self.lines_data[self.num_img,1],self.lines_data[self.num_img,2])
		self.flag=0
		self.repaint()
	def on_click_3(self):#按这个键之后响应
		self.flag=1
		self.num_img+=1
		print('当前图片:',self.num_img)
		self.repaint()
	def center(self):#居中函数
		qr = self.frameGeometry()
		cp = QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
	def paintEvent(self, e):#自动刷新的，一直循环
		qp = QPainter(self)
		qp.setPen(QPen(Qt.black, 1, Qt.SolidLine))
		sta_x=200
		sta_y=700
		sto_x=500
		sto_y=350
		interal=500
		
		img=self.lines_data[self.num_img]
		print('当前图:',img)
		if self.flag==1:
			if img[1]==1:
				if img[0]!=1:#左边不像
					qp.drawLine(sta_x, sta_y, sto_x+img[0],sto_y)
					qp.drawLine(sta_x+interal, sta_y, (sto_x)+interal,sto_y)
					qp.drawLine(sta_x+2*interal, sta_y, (sto_x)+2*interal,sto_y)
				else:#右边不像
					qp.drawLine(sta_x, sta_y, sto_x,sto_y)
					qp.drawLine(sta_x+interal, sta_y, (sto_x)+interal,sto_y)
					qp.drawLine(sta_x+2*interal, sta_y, (sto_x+img[2])+2*interal,sto_y)
			else:
				if img[0]!=2:#左边不像
					qp.drawLine(sta_x, sta_y, sta_x+img[0]+3,sto_y)
					qp.drawLine(sta_x+interal, sta_y, (sta_x)+interal+3,sto_y)
					qp.drawLine(sta_x+2*interal, sta_y, (sta_x+3)+2*interal,sto_y)
				else:#右边不像
					qp.drawLine(sta_x, sta_y, sta_x+3,sto_y)
					qp.drawLine(sta_x+interal, sta_y, (sta_x+3)+interal,sto_y)
					qp.drawLine(sta_x+2*interal, sta_y, (sta_x+img[2])+3+2*interal,sto_y)
					
		#qp.begin(self)
		#self.drawLines(qp)
		qp.end()

	#def drawLines(self, qp):
		#self.qp=qp
		#pen = QPen(Qt.black, 5, Qt.SolidLine)#宽度为2，solidline画笔风格
		#self.qp.setPen(pen)
		#self.qp.drawLine(300, 300, 1300,300-17.45)
		#qp.setPen(pen)
		#qp.drawLine(20, 70, 500, 40)
		# pen.setStyle(Qt.SolidLine)#Qt.DashLine
		# qp.drawLine(self.abc, 300, 1300,300-17.45)

		# pen.setStyle(Qt.SolidLine)#Qt.DashLine


		# # pen.setStyle(Qt.DashDotLine)

		# # pen.setStyle(Qt.DotLine)
		
		# # pen.setStyle(Qt.DashDotDotLine)


		# #pen.setStyle(Qt.CustomDashLine)#定义画笔风格，
		# #pen.setDashPattern([1, 4, 5, 4])#一定是偶数个数字，奇数代表划线，偶数表示留空

	def chuli(self,a,s):#可以处理初始化定义的参数
	# dlg.setWindowTitle(s)
		#self.btn.setText(a+str(s[0]*10))
		b=1
		#self.qp.drawLine(300+int(a), 300, 1300,300-17.45)
		
app = QApplication(sys.argv)
app.processEvents()
ex = Example()
app.exec_()
sys.exit(app.exec_())

#QPushButton(string text, QWidget parent = None)


