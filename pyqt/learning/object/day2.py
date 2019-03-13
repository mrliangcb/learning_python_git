#day2   自己创建一个QWindget窗口类

from PyQt5.Qt import *

class Window(QWidget):#继承QWidget
	def __init__(self):
		super().__init__()#运行父类的初始化 
		self.setWindowTitle("标题一")
		self.resize(500,500)
		self.setup_ui()
		# self.father()
		self.test2()
	def setup_ui(self):
		print("进入设置ui")
	
	def father(self):
		# QObject.__subclasses__()
		mros=QObject.mro() #谁继承了他
		for mro in mros:
			print(mro)
	
	def test(self):#做一个object类的实验
		obj=QObject()#建立一个object对象
		obj.setObjectName("测试1")#设置object的名字
		print(obj.objectName())
		obj.setProperty('abc',"def")
		obj.setProperty("aa",'bb')
		print("显示特性",obj.property('aa'))#好像创建了字典一样
		print(obj.dynamicPropertyNames())#显示了两个属性('abc')  ('aa')
		
		
	def test2(self):#设置风格练习，object名字的作用
		label1=QLabel(self)#传入一个object，self就是未来创建的ob
		label1.setText('hello1!')
		label1.setObjectName("obname")
		
		# label.move(200,200)
		with open('C:\lcb\learning_python_git\learning_python_git\pyqt\learning\QObject.qss','r') as f:
			qApp.setStyleSheet(f.read())#这里面写好了样式
		#找整个test2中，不论前后，test的风格都采用这个
		#也可以设置特定objectname的才听从这个风格 
		
		
		# label.setStyleSheet("font-size:20px;color:red;")#
		label2=QLabel(self)#传入一个object，self就是未来创建的ob
		label2.setText('hello2!')
		label2.move(100,100)
		# label2.setObjectName("obname")#QLabel类型的，object名字为 obname的，才会引用qss的第一个样式
		label2.setObjectName("alert")
		label2.setProperty("notice_level","warning")#匹配这个QLabel#alert[notice_level="warning"]  类，名，属性 分别匹配
		
		
		btn=QPushButton(self)
		btn.setText('按键')#这里的样式就没有按照上面那个了，因为没有匹配
		btn.move(130,130)
		btn.setObjectName("obname")#QPushButton#obname    类和名字都对上的才可以匹配第二个样式
		
		
		
		
import sys
app=QApplication(sys.argv)

window=Window()#创建一个对象
window.show()
window.test2()
window.setObjectName("chuangkou")#window本身就是一个object，因为object是所有的基类
sys.exit(app.exec_())



















