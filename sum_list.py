
numbers_file = open("numbers.list",'r')
number_list = numbers_file.read().splitlines()

sum = 0

for number in number_list:
    sum = sum + int(number)

print('The sum of the numbers is:')

print(sum)
