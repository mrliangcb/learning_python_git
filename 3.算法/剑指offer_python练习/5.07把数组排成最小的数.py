

# 例如输入 {3，32，321}
# 输出321323

# 如30和9  309<930，所以30要在9左边
# 感觉可以用快排序的思路

a=[12,3,56,1,4]
b=str(a[0])
c=str(a[1])
print(b,c)
print(b+c)
print(c+b)

x1=int(b+c)
x2=int(c+b)
print(x1<x2)

# 用快排序  小的放左边，大的右边

















