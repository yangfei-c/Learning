import random
#随机抽奖小案例
user_list=[]
for i in range(1,11):
    name="员工-{}".format(i)
    user_list.append(name)
selecct=random.choice(user_list)#随机抽取一个员工
print("三等奖获得者：",selecct)
user_list.remove(selecct)
selecct=random.choice(user_list)
print("二等奖获得者：",selecct)
user_list.remove(selecct)
selecct=random.choice(user_list)
print("一等奖获得者：",selecct)