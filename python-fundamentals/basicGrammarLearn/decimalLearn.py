print("Hello!")
while True:
    print("1.十进制转二进制，2，十进制转八进制，3.20_testImage.十进制转十六进制!")
    print("4.二进制转十进制，5.八进制转十进制，6.十六进制转十进制!")
    print("0.退出!")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Goodbye!")
        break
    else:
        data = input("Enter a number to convert: ")
        if choice==1:
            print(data + "的二进制为" + bin(int(data)))
        elif choice==2:
            print(data+"的八进制为"+oct(int(data)))
        elif choice==3:
            print(data+"的十六进制为"+hex(int(data)))
        elif choice==4:
            print(data+"的十进制为"+str(int(data,base=2)))
        elif choice==5:
            print(data+"的十进制为"+str(int(data,base=8)))
        elif choice==6:
            print(data+"的十进制为"+str(int(data,base=16)))



