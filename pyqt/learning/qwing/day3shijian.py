#事件消息行为

from PyQt5.Qt import *


class Window(QWidget):#继承QWidget
	def __init__(self):
		super().__init__()#运行父类的初始化 
		self.setWindowTitle("事件")
		self.resize(500,500)
		self.setup_ui()
	def setup_ui(self):
		print('设置ui')
		
	def showEvent(self,QSshowEvent):
		print('展示窗口')
		
	def closeEvent(self,QCloseEvent):
		print('关闭窗口')#当我关闭窗口时候，cmd会输出这个
		
	def moveEvent(self,QMoveEvent):#窗口移动
		print('移动窗口')
#QResizeEvent
#enterEvent(QEvent) 鼠标进来
#leaveEvent(QEvent)
#mousePressEvent(self,QMouseEvent):鼠标按下
		
		
		
if __name__=='__main__':
	import sys
	app=QApplication(sys.argv)

	window=Window()#创建一个对象
	window.show()

	window.setObjectName("chuangkou")#window本身就是一个object，因为object是所有的基类
	sys.exit(app.exec_())




















