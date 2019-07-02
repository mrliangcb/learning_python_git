
a=bin(4)  #十进制转二进制
#oct是十进制转八进制   hex转16
print(a) #显示二进制缩写，这是str字符串
print(type(a))


b=b'0100' 
print(b) #显示完全二进制
print(type(b))

#二进制转10进制
print('0100的十进制',int(b,2)) #要记得表明这个原来是几进制

print(bin(4))
print(bin(1))
print(bin(4 ^ 1)) #做异或，不同为1
print('二进制数字运算，输出是整形',0b0100 + 0b1011)#为15整形
print('把整形变回二进制0b',bin(0b0100 + 0b1011))
print(type(b'0100'))#bytes型，但不能计算，用作计算的时候把这个当成字符串型的

# and or 是判断是否为0，十进制
# &  |  基于bit的判断
