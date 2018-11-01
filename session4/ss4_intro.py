# person = ["Jerry","US","Tom",4,3.5,2000, False]

# person = {}
# print(person)
# print(type(person))

# person = {
#     "name": "Jerry"
# }
# print(person)

person = {
     "name": "Jerry",
    "location": "US",
    "rival": "Tom"
}

person["rival"] = "Thomas"  #Update
print(person)

del person["name"]  #Delete
print(person)

# print(person)
# person["random"] = 4    #Create
# print(person)

# key = "name"
# print(person[key])   #Read