names = { }
while True:
    name = input('to continue, please enter a name - to quit enter "q": ')
    if name == 'q':
        break
    else:
        names[name] = names.get(name, 0) + 1
print('name frequency:', names)