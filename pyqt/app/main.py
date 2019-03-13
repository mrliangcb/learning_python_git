#

from PyQt5.Qt import *


class Window(QWidget):#继承QWidget
	def __init__(self):
		super().__init__()#运行父类的初始化 
		self.setWindowTitle("事件")
		self.resize(800,500)
		self.setup_ui()
	def setup_ui(self):
		print('设置ui')
		
		#label区
		self.lb1 = QLabel("两融非沪深：",self)#文本显示
		self.lb2 = QLabel("沪深非两融：",self)#文本显示
		
		#
		
		#文本框区
		self.edit1 = QLineEdit(self)#输入框
		self.edit2 = QLineEdit(self)
		self.edit3 = QLineEdit(self)
		
		# self.edit1.installEventFilter(self)
		
		#按钮区
		self.bt1 = QPushButton("next_image",self)#建立一个按钮
		self.bt1.clicked.connect(self.on_click_1)
		self.bt1.setStyleSheet("QPushButton{color:black}"
			"QPushButton:hover{color:red}"
			"QPushButton{background-color:rgb(78,255,255)}"
			"QPushButton{border:2px}"
			"QPushButton{border-radius:10px}"
			"QPushButton{padding:2px 4px}")

		
		#第一个图层的垂直定义
		vbox1 = QVBoxLayout()
		vbox1.addStretch(1)
		vbox1.addWidget(self.lb1)#加控件就widget，加水平/垂直布局就layout
		vbox1.addStretch(1)
		vbox1.addWidget(self.lb2)
		vbox1.addStretch(1)
		vbox1.addStretch(1)
		
		
		#第二垂直
		vbox2 = QVBoxLayout()
		vbox2.addStretch(1)
		vbox2.addWidget(self.edit1)#加控件就widget，加水平/垂直布局就layout
		vbox2.addStretch(1)
		vbox2.addWidget(self.edit2)
		vbox2.addStretch(1)
		vbox2.addWidget(self.edit3)
		vbox2.addStretch(1)
		
		#第一个图层的水平定义QH
		h_box1 = QHBoxLayout()#从左往右布局顺序
		# h_box1.addStretch(1)
		h_box1.addLayout(vbox1)
		h_box1.addLayout(vbox2)
		h_box1.addStretch(1)
		h_box1.addStretch(1)
		h_box1.addStretch(1)
		
		self.setLayout(h_box1)
		
	def on_click_1(self):#按这个键之后响应
		print('按钮1')
		self.edit2.setText('按钮按下!')
		self.lb1.setText("按下啦！")
		
		
if __name__=='__main__':
	import sys
	app=QApplication(sys.argv)
	window=Window()#创建一个对象
	window.show()
	sys.exit(app.exec_())
		
		
		
		
		
		
		