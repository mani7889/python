fname = input("Enter file name: ")
fh = open(fname)
count=0
total=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    count=count+1
    x=line[21:27]
    y=float(x)
    total=total+y
z=total/count
print('Average spam confidence:',z)
