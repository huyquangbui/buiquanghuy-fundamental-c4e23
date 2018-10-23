start_number = int(input("enter start number: "))
stop_number = int(input("enter last number: "))
step_number = int(input("enter step number: "))
sum = 0
for i in range(start_number, stop_number+1, step_number):
    sum = sum + i 
print("the list:", *range(start_number, stop_number+1, step_number))    
print ("sum is:", sum)