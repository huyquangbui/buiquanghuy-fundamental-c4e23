yob_str = input("your year birth:")
while (not yob_str.isdigit()):
    print("only numbers!")
    yob_str = input("your year birth:")
yob = int(yob_str)
age = 2018 - yob
print("your age:",age)