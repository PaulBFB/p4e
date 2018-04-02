fname = 'mbox-short.txt'
fpath = open(fname)
count = 0
for line in fpath:
    if not line.startswith('From '):
        continue
    else: # increase count by 1, slice into words and print the email (second word)
        count = count + 1
        words = line.split()
        print(words[1].strip())
print('There were', count, 'lines in the file with From as the first word')
