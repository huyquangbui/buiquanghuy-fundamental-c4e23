sheep1 = [5,7,300,90,24,50,75]
print ("Hello here is my flock ")
print(sheep1)
#
# writing a program is very misleading when it is (just) a function
#
# sheep = sorted(set(sheep1))
# for r in sheep:
#     count = 0
#     for t in sheep:
#         if r >= t:
#             count += 1  #if there were 2 sheep with same sizes, doesnt work!
#             if count == len(sheep):
#                 print("now my biggest sheep has size", r, "let's shear it")
#                 sheep1[sheep1.index(r)]= 8
#
big = max(sheep1)
sheep1[sheep1.index(big)] = 8
print("after shearing, here is my flock")
print(sheep1)
print()
loop = 1
month = 1
while loop == 1:
    print("MONTH: ",month)
    print("one month has passed, now here is my flock")
    for i in sheep1:
        num = sheep1.index(i)
        i += 50
        sheep1[num] = i
    print(sheep1)
    big = max(sheep1)
    
    # sheep = sorted(set(sheep1))
    # for i in sheep:
    #     count = 0
    #     for j in sheep:
    #         if i >= j:
    #             count += 1  #if there were 2 sheep with same sizes, doesnt work!
    #             if count == len(sheep):
    #                 print("now my biggest sheep has size", i, "let's shear it")
    #                 sheep1[sheep1.index(i)]= 8
    
    choice = input("wanna Shear or Sell? ").lower()
    if choice == "shear":
        sheep1[sheep1.index(big)] = 8
        print("after shearing, here is my flock")
        print(sheep1)
        loop = 1
        month += 1
    elif choice == "sell":
        sum = 0
        for i in sheep1:
            sum += i
        print("my flock has total size of: ",sum)
        print("i would get",sum,"* 2$ =", sum*2,"$")
        loop = 0
    print()

