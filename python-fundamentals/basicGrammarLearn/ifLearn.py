# else可以省略，处理比较数值时int()把输入字符串型转成整型
# if嵌套时满足条件往里执行执行完再出来
print("欢迎致电10086，我们提供以下服务：1.话费流量查询（11花费，12流量）；2.宽带办理；3.20_testImage.人工服务；")
choice=input("请输入序号！")
data=int(choice)
if data==1:
    print("话费流量查询专区")
    a=int(input("请输入具体序号"))
    if a==11:
        print("话费余额为x元")
    elif a==12:
        print("流量余额为y元")
elif data==2:
    print("宽带办理专区")
elif data==3:
    print("人工服务专区")
print("感谢您的致电，祝您生活愉快!")
