smallest = None
biggest = None
while True:
    snum = input('please enter a number: ')
    if snum == 'done':
        break
    try:
        num = int(snum)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest = num
    elif smallest < num:
        smallest = num
    if biggest is None:
        biggest = num
    elif biggest > num:
        biggest = num


print('Minimum is', smallest)
print('Maximum is', biggest)
