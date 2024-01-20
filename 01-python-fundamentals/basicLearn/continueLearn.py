#输出1-10，不输出7
number=1
print("Hello World!")
while number<11:
    if number==7:
        number+=1
        continue
    print(number)
    number+=1
print("Goodbye!")