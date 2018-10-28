fav_list = ["a", "b", "z"]

print ("here is your list", *fav_list, sep="\n")
new = input("wanna add one more? ")

while new != "no":
    fav_list.append(new)
    print ("your new list", *fav_list, sep="| ")
    break
q = input("wanna change any? ")
while q != "no":
    i = int(input("position: "))
    change = input("into?")
    fav_list[i-1]=change
    print("new list", *fav_list, sep=", ")
    break

o = input("wanna delete any? ")
while o != "no":
    j = int(input("position: "))
    fav_list.pop(j-1)
    print("new list", *fav_list, sep=", ")
    break