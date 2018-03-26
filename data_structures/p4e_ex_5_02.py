#assignment for week 5 autograder - python 4 everybody

hrs = input('Enter Hours:')
rt = input('Enter the hourly rate:')
try: #check for float conversion - if unable to convert, give error and quit
    h = float(hrs)
    r = float(rt)
except:
    print('please enter numeric values!')
    quit()

basepay = h * r

if h <= 40: #check for overtime
    pay = basepay
else: #if there was overtime, set pay to be 40 hours regularly plus any overtime with rate * 1.5
    pay = (40 * r) + (r * (h - 40) * 1.5)

print(pay)