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

b='20.15.40'
c='20.15.43'

b2='20.15.50'
c2='20.15.53'

while 1:
	a=time.strftime('%H.%M.%S',time.localtime(time.time()))
	if b<a<c or b2<a<c2:
		print('超过了')
	if a>c2:
		break
print('完成')