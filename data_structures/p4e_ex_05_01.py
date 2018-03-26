p4e_ex_5_01 = 'words.txt'
fpath = open(p4e_ex_5_01)
counts = {}
for line in fpath:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#for key in counts:
#    print(key,counts[key])
bigcount = None
bigword = None
for a,b in counts.items():
    if bigcount is None or b > bigcount:
        bigcount = b
        bigword = a

print(bigcount,bigword)

