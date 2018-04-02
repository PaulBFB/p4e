fname = None

while True:
    fname = input('please enter a file name: ')
    try:
        fpath = open(fname)
        break
    except:
        print('your file could not be found: ',fname)
        again = input('would you like to try again (y/n): ')
        if again == 'n':
            quit()
        else:
            continue

#print('success! your file was read: ',fpath)

nlines = 0
fls = 0

for line in fpath:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    else:
        nlines = nlines + 1
        flpos = line.find('X-DSPAM-Confidence:')
        flpart = line[flpos+20:].strip()
        fls = fls + float(flpart)
        #print(flpart)
        #print(fls)

#print('numer of lines starting with specified string: ',nlines)
#print('sum of floats containted: ',fls)
print('Average spam confidence:', fls/nlines)
