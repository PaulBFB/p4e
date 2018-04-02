fname = 'romeo.txt'
fpath = open(fname)
lst = []
for line in fpath:
    words = line.split()
    for word in words:
        if word.strip() not in lst:
            lst.append(word)
lst.sort()
print(lst)
