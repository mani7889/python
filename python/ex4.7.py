def computegrade(score):
    if score>=0.9 and score<=1.0:
        print('grade A')
    elif score>=0.8 and score<0.9:
        print('grade B')
    elif score>=0.7 and score<0.8:
        print('grade C')
    elif score>=0.6 and score<0.7:
        print('grade D')
    elif score>=0.1 and score<0.6:
        print('grade F')
    else:
        print('Bad score')
x=input("enter score:")
try:
    y=float(x)
    computegrade(y)
except:
    print("bad score")