_testVar = 100
_testVar2 = 500

print(_testVar)
print(_testVar2)

num_1 = int(input("Please enter a first number: "))
num_2 = int(input("Please enter a second number: "))

def add(num1,num2):
    return int(num1) + int(num2) 
def subtract(num1,num2):
    return int(num1) - int(num2)
def multiply(num1,num2):
    return int(num1) * int(num2)
def divide(num1,num2):
    return int(num1) / int(num2)

operator = str(input("select an operation [add, subtract, multiply, divide]"))
if operator == "add":
    result = add(num_1, num_2)
elif operator == "subtract":
    result = subtract(num_1,num_2)
elif operator == "multiply":
    result = multiply(num_1,num_2)
elif operator == "divide":
    result = divide(num_1,num_2)
else:
    result = "invalid operator!"

print("Your result is: " + str(result))
