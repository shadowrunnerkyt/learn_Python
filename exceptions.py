
myarray = {1,2,3}
for item in [0,1,2,3,4,5]:
    try:
        print(myarray[item])
    except IndexError:
        print("Failed at index " + str(item))

print("The program continues to run!")
