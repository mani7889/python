fname=input('Enter the file name:')
try:
    fhandle=open(fname)
except:
    print('file cannot be opened:',fname)
    exit()
count=0
for line in fhandle:
    count=count+1
print('there wer  e',count,'subject lines in',fname)    