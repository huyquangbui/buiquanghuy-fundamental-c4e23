sen = input("Enter a string: ").lower()
count = 1
sort = sorted(set(sen)) 
#sorted = alphabetical order
#set = distinct character
for i in range(len(sort)):
    char1 = sort[i]
    print(char1, sen.count(char1), sep="  ")
