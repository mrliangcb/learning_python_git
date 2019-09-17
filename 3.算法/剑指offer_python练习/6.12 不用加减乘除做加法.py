# 不用加减乘除做加法
# 可以用二进制，二进制的异或相当于不进位的异或 ^
# 二进制的 左移 相当于 乘以2
print(0b001 ^ 0b001)
# 进位就需要 与&，然后移位，  又重复做 异或，进位移位，直到不产生进位
print(0b10<<1)#2左移一位=4  

a=10
b=41
print(a,b)
c=a^b
print('无进位加法',c)#无进位加法35
d=a&b
d=d<<1
print('第一次进位:',d)#
e=d^c
print('加上第一次进位',e)
f=d&c

print('第二次进位:',f==0,not f)

nums='1 2 3'
a=list(map(int,nums.split(" ")))






















