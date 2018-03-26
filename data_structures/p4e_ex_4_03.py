sscore = input('please enter score:')

try: # check for numerical conversion, quit and error if fail
    fscore = float(sscore)
except:
    print('please enter a NUMERICAL value, class input error')
    quit()

if (fscore > 1) or (fscore < 0): #check for score out of range, quit if true
    print('score is out of range - please enter a score between 0 and 1.0, inclusive')
    quit()
elif fscore >= 0.9:
    print('A')
elif fscore >= 0.8:
    print('B')
elif fscore >= 0.7:
    print('C')
elif fscore >= 0.6:
    print('D')
elif fscore < 0.6:
    print('F')