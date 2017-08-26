#100 Doors
#http://rosettacode.org/wiki/100_doors#Python

#There are 100 doors in a row that are all initially closed.
#You make 100 passes by the doors.
#The first time through, visit every door and  toggle  the door  (if the door is closed,  open it;   if it is open,  close it).
#The second time, only visit every 2nd door   (door #2, #4, #6, ...),   and toggle it.
#The third time, visit every 3rd door   (door #3, #6, #9, ...), etc,   until you only visit the 100th door.
#SELF: You keep doing Nth door until you reach N = 100

#Task
#Answer the question:   what state are the doors in after the last pass?   Which are open, which are closed?
#Alternate: As noted in this page's   discussion page,   the only doors that remain open are those whose numbers are perfect squares.
#Opening only those doors is an   optimization   that may also be expressed; however, as should be obvious, this defeats the intent of comparing implementations across programming languages.

#Create a dict with data:

import math

doors = dict()
count = 0

try:
    number_of_doors = int(raw_input('Enter number of doors>'))
except:
    print 'Enter an integer'
    quit() 

for count in range (1,number_of_doors+1):
    doors[count]  = False
    
#print doors

j = i  = 0
i = int(math.sqrt(number_of_doors))

for j in range(1, i+1):
    doors[j*j] = True

print doors