#http://rosettacode.org/wiki/Loops/Break
#
#Show a loop which prints random numbers (each number newly generated each loop) from 0 to 19 (inclusive). If a number is 10, stop the loop after printing it, and do not generate any further numbers. Otherwise, generate and print a second random number before restarting the loop. If the number 10 is never generated as the first number in a loop, loop forever

import random

def break_loop():
    counter = 0
    while True:
        counter += 1
        value = random.randrange(0, 19)
        if counter != 1 and value == 10:
            print counter, value
            break
        elif counter == 1 and value == 10:
            print 'first value generated was 10'
            continue
        else:
            print value
            continue
            
            
            
break_loop()