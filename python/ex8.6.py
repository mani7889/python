lst=list()
while True:
    number=0.0
    input_number=input('enter a number:')
    if input_number=="done":
        break
    try:
        number=float(input_number)
    except:
        print('invalid input')
        quit()
    lst.append(input_number)
print(max(lst))
print(min(lst))





#2nd method
lst=list()
while True:
    numbers=input('enter a number')
    if numbers=='done':
        break
    lst.append(numbers)  
print(max(lst))
print(min(lst))