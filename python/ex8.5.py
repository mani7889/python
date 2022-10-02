fh = open('mbox-short.txt')
count = 0
for line in fh:
    if not line.startswith('From'): continue
    if line.startswith('From:'): continue
    words = line.split()
    count = count + 1
    print(words[1])
print("There were", count, "lines in the file with From as the first word")