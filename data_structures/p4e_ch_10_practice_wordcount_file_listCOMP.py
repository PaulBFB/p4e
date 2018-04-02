while True:
    fname = input('enter a filename: ')
    if len(fname) < 1:
        fname = 'words.txt'
    try:
        file = open(fname)
        break
    except:
        print('file not found:', fname)
        goon = input('do you want to continue? (y/n): ')
        if goon == 'y':
            continue
        else:
            quit()

counts = {}

for line in file:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#alternate solution - list comprehension:
ranking = sorted([(v, k) for k, v in counts.items()], reverse=True)

#unsorted = []
#for k,v in counts.items():
#    unsorted.append((v,k))

#ranking = sorted(unsorted, reverse=True)

itop = input('words have been ranked - print out top X (enter an integer): ')
top = int(itop)

for val, key in ranking[:top]:
    print(val, key)
