sal_list = [
    {
        "no":1,
        "name":"Huy",
        "hours":30,
        "rates":50,
    },
    {
        "no":2,
        "name":"Quan",
        "hours":20,
        "rates":40,
    },
    {
        "no":3,
        "name":"Duc",
        "hours":15,
        "rates":35,
    }
]

sum = 0
print("Hours worked by each:")

for i in range(len(sal_list)):
    print(sal_list[i]["hours"],sep=", ")
    sal = (sal_list[i]["hours"])*(sal_list[i]["rates"])
    print(sal_list[i]["name"], "salary: ", sal)
    sum += sal
print("Sal sum: ", sum)