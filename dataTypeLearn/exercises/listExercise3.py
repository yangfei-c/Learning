goods=[
    ["飞机",3000],
    ["迫击炮",200],
    ["AK47",1000],
    ["m9",200],
]
for i in range(len(goods)):
    messige="{}-{}".format(i,goods[i][0])
    print(messige)
while True:
    select=input("请输入序号，Q/q退出！:")
    if select.upper()=="Q":
        break
    elif select.isdecimal():
        choice = int(select)
        if choice>=0 and choice<=len(goods):
            msg = "您选择的商品是:" + str(goods[choice][0]) + ",价格是:" + str(goods[choice][1])
            print(msg)
        else:
            print("输入序号不对！")
    else:
        print("输入的并非数字！")
