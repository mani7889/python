num=0
tot=0.0
while True:
    sval=input("enter a number")
    if sval=='done':
        break
    try:
        fval=float(sval)
    except:
        print("invalid data")
        continue
    print(fval)
    tot=tot+fval
    num=num+1
print('all done')
print(num,tot,tot/num)
    