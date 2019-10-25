
# int 有两种形式 10进制(一般用10进制)  和  2进制
# bin b'' 是 str形式  都可以通过int(,2)转int


a=bin(4)  #十进制转二进制
#oct是十进制转八进制   hex转16
print(a) #显示二进制缩写，这是str字符串
print(type(a))


b=b'0100' 
print(b) #显示完全二进制
print('b的类型',type(b)) #bytes类型   字符集

#二进制转10进制
print('0100的十进制',int(b,2)) #要记得表明这个原来是几进制
print(bin(4))# bin 就是把Int转化为 str
print(bin(1))
print(bin(4 ^ 1)) #做异或，不同为1
print('二进制数字运算，输出是整形',0b0100 + 0b1011)#为15整形
print('把整形变回二进制0b',bin(0b0100 + 0b1011))
print(type(b'0100'))#bytes型，但不能计算，用作计算的时候把这个当成字符串型的

# and or 是判断是否为0，十进制
# &  |  基于bit的判断
# ~ 二进制+1 然后符号取- 比如~132   就为-133   经常先异或 全1(求反) 然后再~  来求负数的反码
# ^异或

#这里用的最多
x = b'10101010'#bytes 离散的 int可以把他们组合起来
print('把bytes解析成int',int(x,2))#按照二进制解析
x2=int(x,2)
print('bytes转化为int:',x2,"也可以bin(int)",bin(x2))

y2=0b0111 #这种最直接是int  b''要用int(,2)转为int   
y=0b0101
print('求异或和与',y2^y,y2&y)#^是异或， &是与
#x是bytes型，y是int型
# int型可以右移，可以bin(),可以求与^
print('抗一下两个长度x,x2:',len(x))#,len(x2)  #第一个代表8个bytes，第二个是int没有len，所以报错



#平时int('123')是默认10进制

# a>>2 右移符号，不是循环

# bytearray(bytes)用法
# 

#python二进制加减法 遇到负数的时候

a=int(b'11111000',2)
print(a)
print(a>0x7f) #False，
t=0xff
#检测到是负数 两种处理办法
# (1)
print(bin(t))
print(bin(~(a^t)))
print(~(a^t))#求反然后~ 就是加一 加符号

#(2)
print(-(0b100000000-a))#8位系统，那用第九位1 减去自己=反码+1










