from random import randint

print("The guessing game begins!")

loop = 2
while loop == 2:
    x = randint(0,100)
    guess = int(input("guess my number between 0-100: "))
    loop = 1
    while loop==1:
        if guess<x:
            print("try bigger!")
            guess = int(input("guess my number between 0-100: "))
        elif guess > x:
            print("try smaller!")
            guess = int(input("guess my number between 0-100: "))
        else:
            print("Bingo!")
            choice = input("Continue? (Y/N) ")
            if (choice == "y") or (choice == "Y"):
                loop = 2
            elif (choice == "n") or (choice == "N"):
                loop = 0