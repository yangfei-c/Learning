#感觉像是某些评论发不出来的处理
text=input("Enter a string:")
if "日本" in text:
    print("不要包含日本！")
print(0 and 1)
print(1 and 0)
print(2 and 1)
print("" and 3)#第一个是False整体是False
print("chen" and "ch")#第一个True结果取决于后面True还是False
#逻辑运算结果取决于那个值，结果等于那个值，值与值的逻辑比较
print("chen" and 1 or 3 and 2 or 0 and 1 or 3 and 2 or 2)
#先分析and再or，1 or 2 or 0 or 2 or 2
#1 or 0 or 2 or 2
# 1 or 2 or 2
#1 or 2
name="YC"
if True:
    v1=name
else:
    v1=66
print(v1)
#直接可以写成v1=name or 66