# Build a simple calculator
import re
run = True
previous = 0
def my_cal():
    global run
    global previous
    # Calculator = input(str(previous))
    if previous == 0:
        Calculator = input('Enter input: ')
    else:
        Calculator = input(str(previous))
        # print('New expression is', Calculator)
    if  Calculator == 'quit':
        print('Terminated')
        run = False
    else:
        if previous == 0:
            Calculator = re.sub('[a-zA-Z,.?():;!@]','',Calculator)
            previous = eval(Calculator)
        else:
            previous = eval(str(previous) + Calculator)
            print('Ans: ', previous)        
    
while run:
    my_cal()