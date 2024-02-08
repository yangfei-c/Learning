data=("京A9919","豫S1113","京A3122")
list=[]
num=0
for i in data:
    list.append(i)
    if i[0]=="京":#i.startswith("京")
        num+=1
for item in list:
    print(item)
msg="北京的车牌一共"+str(num)+"个"
print(msg)