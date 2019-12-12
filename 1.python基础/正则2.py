
import re

ret=re.match('he','hello')
print(ret.group())


a=123
b=a
print(id(a),id(b))
a=1234
print(b)
print(id(a),id(b))
c=1234
print(id(a),id(b),id(c))

m=re.findall("\((.*?)\)","(1234)") #没有括号会抓取所有内容，有括号会抓取括号里的内容，有多个括号会抓取多个括号里的内容
print(m)


















