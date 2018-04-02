#ask for file name until a valid file is called

fname = None

while True:
    fname = input('please enter a filename ')
    try:
        fpath = open(fname)
        break
    except:
        print('your input filename could not be found: ',fname)
        goon = input('do you want to continue? y/n ')
        if goon == 'n':
            quit()
        else:
            continue

print('you have entered the filename: ', fname)
print('the path to your file is: ', fpath, '\n your file will be printed below \n')
for line in fpath:
    line_upper = line.upper()
    print(line_upper.rstrip())
