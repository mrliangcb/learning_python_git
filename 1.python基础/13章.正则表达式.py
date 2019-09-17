import re

#正则表达式
#<title>题目<\title>
import re

#基础python匹配
pattern1='dog'
string='cat is run dog r5n run'
print(pattern1 in string)

#正则匹配
print(re.search(pattern1,string))#前面是要找的东西，后面是池   返回一个object
#返回span 0到3 

#匹配多种可能
ptn=r'r[au]n' #本来是run的，但是我想找ran或者run，所以中间[],里面是分别与r n组合成多种匹配方式。所以这里是找ran '或' run
print(re.search(ptn,string))

ptn=r'r[a-z]n'
print('用-匹配',re.search(ptn,string))

#r'r[0-9a-z]n'意思就是 r[0-9]n和r[a-z]n的并 
#数字匹配
#\d表示数字  \D表示非数字  
ptn=r'r[\d]n'#与r'r\dn'相等
print('用\d匹配',re.search(ptn,string))

#空白 空格
#\s为空   \S为非空
ptn=r's\sr'#找到s r
print('用\s匹配',re.search(ptn,string))

#空白字符
#\b  \B

#\w  \W  表示数字，字符和_

#句尾句首

#寻找所有匹配
print('找到所有',re.findall(r'r[au]n','run rn run ran  r5n'))#等价于(ran|run)

#compile
compiled_re=re.compile(r'r[au]n')
print(compiled_re.search('ran run r5n'))#其实跟随上面是一样的



# https://www.cnblogs.com/taostaryu/p/8759550.html
# a="['2,000100,TCL集团,4.04,6.04,43627.28,16.65,36227.73,13.83,7399.56,2.82,-17616.76,-6.72,-26010.52,-9.93,2019-03-22 15:00:00,0.23','1,600352,浙江龙盛,12.56,9.98,34626.14,17.13,45660.37,22.59,-11034.23,-5.46,-23788.51,-11.77,-10837.64,-5.36,2019-03-22 15:00:00,1.14']"
# pat='data:\[(.*?)\]'  #匹配 data:
# data=re.compile(pat,re.S).findall(a)
# print(data)

# datas = data[0].split('","')
# print(datas)


text1='hello egon 123'
print(re.findall('\d',text1))#找出单个数字   \D就是找出单个字母

#\A字符串的开始,   \Z字符串的结束(换行前)
print('字符串的开始',re.findall('\Ahe','hello egon 123')) #比如这里要找开头是he的，而且返回这个开头
print(re.findall('\A(he..)','hello egon 123')) #.指的是任意字符0次或1次  *表示前一个符号出现0次或多次

print(re.findall('bd(ec?)','[abdecbdec]'))#先找bde，再找bdec，有哪个就返回哪个，如果满了bdec就作为一个结果，再去找下一个   ?表示前面一个是0或1次

print(re.findall('\[(.*?)\]','[abdecbdec],[abdecbdeccde]')) #.*代表的是[]里面的内容,    ()表示只返回括号里面的，其他是正常匹配




















