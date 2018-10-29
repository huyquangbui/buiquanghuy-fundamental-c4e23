shop_list = ["sweater", "T-shirt"]

option = input("What do you wanna do? [C, R, U, D]").upper()

loop = 1
while loop == 1:
    
    if (option=="C") or \
    (option=="R") or  \
    (option=="U") or  \
    (option=="D") :

        if (option=="C") :
            new_item = input("Enter new item: ")
            shop_list.append(new_item)
            print("Our items: ", end="")
            print(*shop_list, sep=", ")

        elif (option=="R") :
            print("Our items: ", end="")
            print(*shop_list, sep=", ")
        
        elif (option=="U") :
            pos = int(input("Update position: "))
            change = input("Enter new item: ")
            shop_list[pos-1] = change
            print("Our items: ", end="")
            print(*shop_list, sep=", ")
            
        elif (option=="D") :
            pos = int(input("Delete position: "))
            shop_list.pop(pos-1)
            print("Our items: ", end="")
            print(*shop_list, sep=", ")
        option = input("What do you wanna do? [C, R, U, D]")
    elif option=="stop":
        loop = 0
    else:
        print("option not understandable!")
        option = input("What do you wanna do? [C, R, U, D]")

    






