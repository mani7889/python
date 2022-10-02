def chop(t):
    del t[0]
    del t[1]
    print(t)
letters=['a','b','c']
x=chop(letters)
print(x)

def middle(m):
    return m[1:2]
letters=['a','b','c']
rest=middle(letters)
print(rest)