#排队买火车票
user_name=[]
while True:
    name=input("洛阳-上海火车票，购买者姓名（Q/q退出）:")
    if name.upper()=="Q":
        break
    user_name.append(name)
#只有前两名有票
for i in range(2):
    username=user_name.pop(0)
    message="恭喜{},购买成功".format(username)
    print(message)
orthers=",".join(user_name)
data="票已经卖完了，请以下人员选择其它方式：{}".format(orthers)
print(data)