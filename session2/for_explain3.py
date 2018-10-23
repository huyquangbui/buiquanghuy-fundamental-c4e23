from turtle import *
speed(0)
shape("turtle")
n=int(input("enter number:"))
for i in range(n):
    forward(10*i)
    left(90)
mainloop()