items = [8, 9, 10, -1, 23, 45, 99, 75]

x = int(input("enter a number: "))

if x in items:
    print("Found")
    found_index = items.index(x)
    print(found_index)
else:
    print("Not found")