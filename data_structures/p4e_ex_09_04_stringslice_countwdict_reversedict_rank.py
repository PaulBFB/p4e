fname = 'mbox-short.txt'
fpath = open(fname)
counts = {}
emails = []
bigcount = None
bigemail = None

for line in fpath:
    if not line.startswith('From '):
        continue
    else:
        words = line.split()
        emails.append(words[1].strip())
# print(emails)

for email in emails:
    counts[email] = counts.get(email, 0) + 1

# print(counts)

for k, v in counts.items():
    if bigcount is None or v > bigcount:
        bigcount = v
        bigemail = k

print(bigemail, bigcount)
