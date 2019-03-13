#QObject 之间建立父子关系
#子对象 父对象
from PyQt5.Qt import *

class Window(QWidget):#继承QWidget
	def __init__(self):
		super().__init__()#运行父类的初始化 
		self.setWindowTitle("标题一")
		self.resize(500,500)
		self.setup_ui()
		self.father_son()
		
	def setup_ui(self):
		print("进入设置ui")
		
	def father_son(self):
		obj1=QObject()
		obj2=QObject()
		print("对象1:",obj1)
		print("对象2:",obj2)
		
		obj1.setParent(obj2)#2是爸爸  找爸爸api
		print(obj1.parent())
		print('儿子是谁',obj2.children())
		print('找一个儿子',obj2.findChild(QObject))
		
		
		
import sys
app=QApplication(sys.argv)

window=Window()#创建一个对象
window.show()
sys.exit(app.exec_())





























