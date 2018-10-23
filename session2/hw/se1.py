h = int(input("your height in cm: "))
h1 = h/100
print("which is",h1,"in m")
w = int(input("your weight in kg: "))

BMI = w/h1**2

if BMI < 16:
    print("severly underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI < 25:
    print("normal")
elif BMI < 30:
    print("overweight")
else:
    print("obese")

print("bye")