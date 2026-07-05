user_list=[]
while True:
    user=input("your username(Q/q退出)-(P/p打印):")
    if user.upper()=="Q":
        break
    elif user.upper()=="P":
        print(user_list)
    pwd=input("your passward:")
    item=[user,pwd]
    user_list.append(item)

