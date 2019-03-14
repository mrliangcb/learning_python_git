#计时器
import time
a=time.strftime('%Y.%m.%d.%I.%M.%S',time.localtime(time.time()))
print(a)
print(a[0:4])
print(a[5:7])
print(a[8:10])
time_start=time.time()

time_end=time.time()
print('用时:',time_end-time_start)