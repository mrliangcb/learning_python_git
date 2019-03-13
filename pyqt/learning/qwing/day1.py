#

from PyQt5.Qt import *
import sys

app=QApplication(sys.argv)
window=QWidget()
window.resize(300,300)


red=QWidget(window)#red会放到父对象window里面
red.resize(30,30)
red.setStyleSheet('background-color:red;')
red.move(100,100)

label1=QLabel(window)#绑到window，如果在类里面就绑到self
label1.setText('hello1!')
label1.setObjectName("obname")

#空间坐标系统(向右走，向下走)
#如果没有父控件，则参考电脑屏幕窗口，如果有父控件，则参考父控件。如window参考电脑，red参考window


window.show()
sys.exit(app.exec_())


































