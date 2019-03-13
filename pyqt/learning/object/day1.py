# -*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt, QPoint
from PyQt5.Qt import *

print(sys.argv)

app=QApplication(sys.argv)#创建一个应用  
# print(app.arguments()) #查看application对象传入了什么
# print(qApp.arguments())

window =QWidget()

window.setWindowTitle("标题1")
window.resize(600,400)
window.move(400,200) #移动窗口  (行位移，列)
label=QLabel(window)
label.setText('hello!')
label.move(200,200)


window.show()
# sys.exit(app.exec_())	#进入消息循环，用户手动退出的时候返回0
#没有的话，窗口一闪而过
app.exec_()

#
qobject  qwidget(可视化)是所有类(大多为控件)的基本类


















