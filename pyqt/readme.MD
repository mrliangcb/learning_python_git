# pyqt笔记


### 1.常用包和格式  
'''python  
from PyQt5.Qt import *
import sys

class Window(QWidget):#继承QWidget  进行重写  
	def __init__(self):
		super().__init__() #运行父类的初始化 
		self.setWindowTitle("事件") #self就是一个QWidget类建立的对象
		self.resize(800,500)
		self.setup_ui()
	def setup_ui(self):
		print('设置ui')
		

def work():  
	app=QApplication(sys.argv) #先创建环境
	window = Window()  
	window.show() #弹出窗口
	sys.exit(app.exec_())  #环境循环
'''


### 2.object  
最底层的基类是object，其次是widget  
object属性:   
> obj=QObject()					#建立  
> obj.setObjectName("测试1") 	#设置名字  
> obj.objectName()				#获取名字  
> obj.setProperty('abc',"def")  
> obj.setProperty("aa",'bb')	#设置两个属性，类似字典abc:def   aa:bb  
> obj.property('aa')			#根据属性名查找属性值  
> obj.dynamicPropertyNames()	#显示全部属性  
> obj1.setParent(obj2)			#ob1找ob2为爸爸  
> obj1.parent()  
> obj2.children()
> obj2.findChild(QObject)		#查找QObject类型的儿子

### 3.widget(控件通用)  
> .move(200,200)#先往右走，再往下走，绑定了谁就以谁为参考，最外层窗口以屏幕为参考  s
> .setText('hello!')	#显示文字


### 4.窗口整体  
> .setWindowTitle("窗口名")
> 

### 5.label控件
> label=QLabel(window) 		#里面是要绑定的窗口控件



### 6.风格设置 qss   
- 新建一个name.qss文件 
 
'''python
QLabel#obname[a="b"]{font-size:20px;color:blue;}  #风格1 
#(1)'QLabel(self)'生成的对象 (2)'.setObjectName("obname")'名字为obname (3)'.setProperty('a',"b")'属性对的上的

QLabel#alert[notice_level="warning"]{color:red; border-color: blue;} #风格2
QPushButton#obname{font-size:20px;color:blue;} #风格3
'''

- 然后在窗口类内调用。不用管前后顺序，因为是窗口是循环监听的，所以只要类别，名字，属性匹配上了，就会采用这个风格  
'''python
with open('.\name.qss','r') as f:
		qApp.setStyleSheet(f.read())
'''
这样就不用逐个去设置，也不用逐个setsytle调用，只要查到有这样的物体存在，就给它上色  


### 7.按键  
> bt1=QPushButton(self) #创建对象
> self.bt1.clicked.connect(self.on_click_1)		#给按钮挂上一个子函数，按键按下的时候进入这个函数def on_click_1()
> 

### 8.布局
> vbox1 = QVBoxLayout() #建立一个列,layout类型
> vbox1.addStretch(1)	#列的最高放一个弹性空间
> vbox1.addWidget(self.lb1) #放一个控件/按钮，button都行
> 

> h_box1 = QHBoxLayout()	#建立一个行布局
> h_box1.addLayout(vbox1)	#把一列绑进来第一个位置，也可以绑控件/弹性空间

### 9.文本框txt  
> self.edit.text() #获得文本框的文字
> 







