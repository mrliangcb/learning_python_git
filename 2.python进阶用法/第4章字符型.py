#

a = 'café'
b = 'cafe\u0301'
print(a, b)                       # café café
print(ascii(a), ascii(b))         # 'caf\xe9' 'cafe\u0301'
print(len(a), len(b), a == b)     # 4 5 False

a='123'
print(chardet(a))