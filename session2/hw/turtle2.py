from turtle import *
speed(0)

n = int(input("nhap so canh ban muon co o da giac deu lon nhat:"))

for i in range(3,n+1):
    if i%2==1:
        color("green")
    else:
        color("red")
    for j in range(i):
        forward(100)
        left(180-(i-2)*180/i)

mainloop()