n = int(input("enter number of symbols:"))
for i in range(n):
    if i%2==0:
        print("x ",end='')
    else:
        print("O ",end='')
print()