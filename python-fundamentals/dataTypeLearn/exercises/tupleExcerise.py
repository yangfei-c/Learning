colors = ['red', 'green', 'blue']
numbers = [1, 2, 3, 4, 5]
res=[]
for color in colors:
    print(color)
    for number in numbers:
        item=(color, number)
        res.append(item)
print(res)