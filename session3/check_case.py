S=input("enter a text:")

if (not S.isdigit()) and (not S.isupper()) and (not S.islower()):
    print("both uppercase and lowercase")
elif S.isupper():
    print("all uppercase")
else:
    print("all lowercase")

if len(S)>8:
    print("more than 8 char")
else:
    print("equal or less")

# not finished