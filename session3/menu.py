items = ["ghe","so huyet","chao"] 
print(items[-3])

i = int(input("index: "))
new_value = input("new value: ")
items[i] = new_value
print(*items, sep=", ")

items.pop(1)
print(*items, sep=", ")

items.remove("chao")
print(*items, sep=", ")