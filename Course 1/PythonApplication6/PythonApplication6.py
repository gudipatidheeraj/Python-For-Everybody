
largest = None
smallest = None
while True:
    try:
        num = input("Enter a number: ")
        if num == "done" : break
        number = int(num)
        if largest is None:
            largest = number
        if smallest is None:
            smallest = number
        if number > largest:
            largest = number
        if number < smallest:
            smallest = number
    except:
        print('Invalid input')

print("Maximum is", largest)
print("Minimum is", smallest)