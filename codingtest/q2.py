#code to catch an Exception in python?
x= int(input("Enter a number1: "))
y= int(input("Enter a number2: "))

try:
    z= x/y
except Exception as e:
    print("Error occures:", e)
    z= None
print("Division is: ",z)
