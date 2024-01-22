'''
字符串独有功能：大小写，是否是数字，替换，去除空白，切割
'''

#切割,字符串从指定地方切割
text="陈某-19-root-大四-洛阳"
new_text=text.split("-")
print(new_text)#切割得到一个列表

#拼接,把列表里面的字符串用某种符号拼接
new_text1="=".join(new_text)
print(new_text1)

#字符串转成字节类型
new_text2=text.encode("utf-8")
print(new_text2)
print(type(new_text2))
new_text3=new_text2.decode("utf-8")
print(new_text3)
print(type(new_text3))

#长度补足
text1="欢迎登录！"
print(text1.center(13,"*"))
print(text1.ljust(13,"*"))
print(text1.rjust(13,"*"))
data="1010"
new=data.zfill(8)
print(new)

#长度,循环输出一段文本所有字符
data2="fjfisdj能否地方急急急"
index=0
while index<len(data2):
    print(data2[index])
    index=index+1

#切片,前取后不取
data3=data2[0:7]
print(data3)

#for in 来遍历输出
for item in data2:
    print(item)
