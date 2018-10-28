pw = input("password: ")
while (pw.isalpha()) \
        or (pw.isdigit()) \
        or (pw.isupper()) \
        or (pw.islower()) \
        or (len(pw)<=8):
    if pw.isalpha():
        print("should contain numbers")
    if pw.isdigit():
        print("should contain char also")  
    if pw.isupper() or pw.islower():
        print("should contain both upper- and lower-case")  
    if len(pw)<=8:
        print("should have length of more than 8")
    pw = input("password: ")
print("accepted")