largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
       break
    try:
        no=int(num)
    except:
        print("Invalid input")
        continue
    if largest is None or no > largest:
        largest=no
    if smallest is None or no < smallest:
        smallest=no

print("Maximum is", largest)
print("Minimum is",smallest)