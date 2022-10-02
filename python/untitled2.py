
fhand=open('mbox-short.txt')
for line in fhand:
    if line.startswith('From:'):
        print(line)
        
 fhand=open('mbox-short.txt')
 len(fhand.read())
 len(fhand.read()) 


def cat_twice(part1,part2):
    cat=part1+part2
    print_twice(cat)
    
line1='bing'
line2='bang'
cat_twice(line1,line2) 

import turtle
bob=turtle.Turtle()

cheese=['chedddar','jkl','bnm']
cheese[0]

t=['a','b','c','d','e']
t[2:5]=['x','y','z']
t

t=['a','b','c','d','e']
t=t+[x]
t

t1=[1,2]
t2=t1.append(2.0)
t1

fhand=open('mbox-short.txt')
count=0
for line in fhand:
    words=line.split()
    if len(words)==0 or words[0] != 'From': continue
    print(words[2])
    
    print(line.rstrip())
    
fh = open('romeo.txt')
lst = list()
for line in fh:
    words=line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()        
print(lst)
    

fh = open('romeo.txt')
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)

 
