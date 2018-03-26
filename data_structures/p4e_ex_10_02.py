fname = 'mbox-short.txt'
file = open(fname)

hour_count = {}

for line in file:
    if not line.startswith('From '):
        continue
    else:
        for word in line.rstrip().split():
            if len(word) < 3 or word[2] != ':':
                continue
            else:
                hour_count[word[:2]] = hour_count.get(word[:2], 0) + 1


hour_rank = sorted([(v, k) for v, k in hour_count.items()])

for k,v in hour_rank:
    print(k, v)
