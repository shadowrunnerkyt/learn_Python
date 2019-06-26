
def print_list(mylist):
    for element in mylist:
        if element == 4:
            continue
        print(element)

def sum_list(mylist):
    list_sum=0
    for number in mylist:
        list_sum = list_sum + number
    return list_sum

def list_contains(mylist,element):
    for el in mylist:
        if el == element:
            print("Yes!")
            break

print(sum_list([5,6,7,8]))

list_contains([2,4,6,8,2],2)

print_list([2,4,6,8])
