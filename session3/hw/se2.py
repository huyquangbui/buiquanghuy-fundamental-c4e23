print("Hi there, this is a superuse gateway.")
username = input("Username: ")
while username != "c4e":
    print("You are not superuser!")
    username = input("Username: ")
else:
    password = input("Password: ")
    while password != "codeforchange":
        print("Password is incorrect!")
        password = input("Password: ")
    else:
        print("Welcome, c4e!")