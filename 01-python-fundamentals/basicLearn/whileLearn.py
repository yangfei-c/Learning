#打断点调试，帮助查找修复代码错误
#程序到断点处暂停
# step over不会进入子函数内部
# step into会进入以便了解函数内部
#break立即终止循环，且不单独使用只能放在循环内部
#continue立即结束当前循环进入下一次循环
count=5
print("Hello(你只有五次机会)!")
while count>=0:
    num=int(input("输入你猜的数字："))
    if num>66:
        print("大了")
    elif num<66:
        print("小了")
    elif num==66:
        print("恭喜猜对，奖金1000分")
        break
    if  count>0:
        print("你还有" + str(count) + "次机会！")
    else:
        print("很遗憾你没有机会了！")
    count-=1
print("Goodbye!")