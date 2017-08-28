#LoopContinue.py
#http://rosettacode.org/wiki/Loops/Continue
#
#Show the following output using one loop.
#1, 2, 3, 4, 5
#6, 7, 8, 9, 10

for i in xrange(1,11):
    if i % 5 == 0:
        print i
        continue
    print i, ",", 