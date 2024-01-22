'''
文本输入判断文本是否以”中国”开头是中国人，不是外国人
text=input("Enter a paragraph:")
if text.startswith("中国"):
    print("中国人")
else:
    print("外国人")
'''

'''
文本输入，将文本中的上替换成下
text = input("Enter a paragraph:")
new_text = text.replace("上","下")
print("源文本："+text)
print("新文本："+new_text)
'''

'''
文本输入两个数字相加 2+1，输出结果
如果都是数字相加，如果有不是数字的输入错误
text = input("Enter a paragraph:")
new_text = text.split("+")
if new_text[0].isdecimal() and new_text[1].isdecimal():
    res=int(new_text[0])+int(new_text[1])
    print("输入文字:"+text)
    print("相加结果:"+str(res))
else:
    print("Invalid string")
'''

'''
循环输入姓名，q或Q终止，然后将已输入的姓名通过逗号连接并输出
user_list=[]
print("开始！")
while True:
    name = input("Enter a name:")
    if name.upper() == "Q":
        break
    user_list.append(name)
res=",".join(user_list)
print("输入的姓名："+res)
print("结束！")
'''


