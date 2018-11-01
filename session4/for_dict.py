person ={
    "name": "Z",
    "age": 29,
    "city": "hcm",
}

# for k in person.keys(): # tuple ~ list
#     print(k, person[k],sep=":")

# for v in person.values():
#     print(v)

for k, v in person.items():
    print(k, v,sep=":")