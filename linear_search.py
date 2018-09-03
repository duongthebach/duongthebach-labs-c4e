items = [8, 9, 10, -1, 23, 45, 99, 75]

x = int(input("enter a number: "))


for index, items in enumerate(items):
    if x == items:
        print("found it")
        print(index)
        break   
else:
    print("Not found")