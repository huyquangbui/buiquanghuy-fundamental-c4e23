print("nhap he so cua 1 phuong trinh bac 2")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
print("ket qua:")
delta = b**2 - 4*a*c
if delta < 0:
    print("vo nghiem")
elif delta==0:
    print("01 nghiem:",-b/(2*a))
else:
    print("nghiem 1st:",(-b+delta**(1/2))/(2*a))
    print("nghiem 2nd:",(-b-delta**(1/2))/(2*a))
