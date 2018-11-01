p1 = {
    "name": "p1",
    "age": 2,
    "city": "ldn",
}

p2 = {
    "name": "p2",
    "age": 5,
    "city": "man",
}

p_list = [
    {
    "name": "p1",
    "age": 2,
    "city": "ldn",
    },
    {
    "name": "p2",
    "age": 5,
    "city": "man",
    }
]

# p_list.append(p1)
# p_list.append(p2)
# print(p_list)

for p in p_list:
    print(p["age"])
    print("-----")
