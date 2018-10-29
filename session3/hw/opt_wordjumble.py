import random 

word_list = ["Chelsea", "Poker", "Finance", "Electricity", "Lamp", "Excessive"]
#print("Here is my pretty awesome word list: ")
#print(*word_list, sep=", ")

loop = 2
while loop == 2:
    word = random.choice(word_list)
    shuffled = list(word)
    random.shuffle(shuffled)
    shuffled = ''.join(shuffled)
    print(*shuffled, sep=" ")

    guess = input("your guess: ")
    loop = 1
    while loop == 1:
        if guess != word:
            print("Try again!")
            guess = input("your guess: ")
        else: 
            print("IMPRESSIVE")
            choice = input("Continue? (Y/N) ").upper()
            if (choice == "Y"):
                loop = 2
            elif  (choice == "N"):
                loop = 0
                        
                

    
