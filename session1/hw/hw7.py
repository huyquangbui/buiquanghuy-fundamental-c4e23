from turtle import *
speed (0)
shape("turtle")
color("green")
n = int(input("How many circles do you want to draw?"))
for i in range(n):
    circle(100)
    left(360/n)    
mainloop()