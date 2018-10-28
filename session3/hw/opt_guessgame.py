from random import randint

x = randint(0,100)

print("The guessing game begins!")

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
        loop = 0