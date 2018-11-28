import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib
import pandas as pd
# x=np.linspace(-1,1,50)#将——1和1之间分成51份，生成50个点
# print(x)
# y=x**2
# plt.plot(x,y)
# plt.close()

#动态
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig=plt.figure(num='第一个对象')
ax=plt.subplot(2,2,1)


xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', animated=False)

def init():
    ax.set_xlim(0, 2*np.pi)
    ax.set_ylim(-1, 1)
    return ln,

def update(frame):
    xdata.append(frame)
    ydata.append(np.sin(frame))
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig=fig,func=update, frames=np.linspace(0, 2*np.pi, 128),
                    init_func=init,interval=20,blit=True)
plt.show()



