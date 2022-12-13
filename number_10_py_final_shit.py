arr = [0] * 10
average = 0
try:
    for num in range(0,len(arr)):
        new_val = float(input("Please enter a value: "))
        arr[num] = new_val
        average+=new_val
    print(format(average/len(arr),'.4f'))
except:
    print("Something went wrong restart the program")
