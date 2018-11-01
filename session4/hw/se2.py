inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}
print()

# CREATE
inventory["pocket"] = ["seashell","strange berry","lint"]
for k, v in inventory.items():
    print(k,v, sep=": ")
print("---")

# DELETE/REMOVE
(inventory["backpack"]).remove("dagger")
for k, v in inventory.items():
    print(k,v, sep=": ")
print("---")

# ADD VALUE TO EXISTING KEY/ UPDATE
inventory["gold"]=500,50
for k, v in inventory.items():
    print(k,v, sep=": ")
print("---")