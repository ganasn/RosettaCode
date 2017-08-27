#A+B
#a classic problem in programming contests, it's given so contestants can gain familiarity with the online judging system being used.
#Task
#Given two integer,   A and B, their sum needs to be calculated.
#Input data
#Two integers are written in the input stream, separated by space(s):
#Output data
#The required output is one integer:   the sum of A and B.

from sys import *

script, i, j = argv

try:
    num1 = int(i)
    num2 = int(j)
    print num1 + num2
except:
    print 'one or both aren\'t integers'