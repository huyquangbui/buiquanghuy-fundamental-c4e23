che = {
    "8": "Lampard",
    "10": "Hazard",
    "11": "Drogba",
    "3": "Cole",
    "1": "Cech",
    "26": "Terry"
}

print(che)
loop = 1
while loop == 1:
    key = input("choose a jersey number: ")

    if key in che:
        print("player:",che[key])
    else:
        print("sorry we dont have that player yet")
        choice = input("do wanna add new player? (Y/N)").upper()
        if choice == "Y":
            value = input("name of new player: ")
            che[key] = value
            print(che)
        elif choice == "N":
            print()

print()