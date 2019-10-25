
print(sorted([10,7,15,4,19],reverse=False))#reverse表示大到小

# 利用key
# key=lambda x:x[1]
print(sorted([10,7,15,4,19],key=lambda x:x,reverse=False))#key的输入是 根据前面的元素来定的


# [('a', 1), ('b', 2), ('c', 3), ('d', 4)]#一个元素是一个元组，用第2位进行排序
print(sorted([('a', 1), ('b', 2), ('c', 3), ('d', 4)],key=lambda x:x[1],reverse=False))

print((1,2,2))
print(set((1,2,2))










