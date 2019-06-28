
def add(num1, num2):
    return int(num1) + int(num2)

def subtract(num1, num2):
    return int(num1) - int(num2)

def multiply(num1, num2):
    return int(num1) * int(num2)

def divide(num1, num2):
    return int(num1)/int(num2)

num_1 = input("Please enter a first number: ")
num_2 = input("Please enter a second number: ")

operator = input("Select an operation: [add, subtract, multiply, divide]")
results_list = open('result_list','r').read().splitlines()

if operator == "add":
    result = add(num_1,num_2)
elif operator == "subtract":
    result = subtract(num_1,num_2)
elif operator == "multiply":
    result = multiply(num_1,num_2)
elif operator == "divide":
    result = divide(num_1,num_2)
else:
    result = "invalid operator!"

print("Your result was " + str(result))

results_list.append(result)
print(results_list)

result_file = open('result_list','w')
for result in results_list:
    result_file.write(str(result)+"\n")
result_file.close()

