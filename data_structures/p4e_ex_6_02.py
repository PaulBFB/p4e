from random import randint
from time import sleep


print('I will find the largest number in this (random) list!\n')

sleep(1)

print('tell me how many items there should be in the list! (use numbers)\n')

sleep(2)

size = input('so how many elements should there be? \n')

try:
    intsize = int(size)
except:
    print('I told you to use numbers :facepalm:')
    quit()

rndlist = []

n = 0
while n<intsize:
    rndlist.append(randint(1,100))
    n=n+1

print('I made your list:\n')
sleep(1)
print(rndlist)

biggest=-1

for number in rndlist:
    if number > biggest:
        biggest = number

print('I found it! The largest number in your random list is\n',biggest)
