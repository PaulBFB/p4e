shrs = input("enter your hours")
srte = input("enter your hourly pay")
try:
    fhrs = float(shrs)
except:
    print("please enter a numerical value for hours")
    quit()
try:
    frte = float(srte)
except:
    print("please enter a numerical value for hourly pay")
    quit()
def pay(hours,rate):
    if hours <= 40:
        return hours * rate
    else:
        return (40 * rate) + ((hours - 40) * rate * 1.5)
print(pay(fhrs,frte))