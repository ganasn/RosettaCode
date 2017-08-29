#http://rosettacode.org/wiki/FizzBuzz
#FizzBuzz.py
#Task
#Write a program that prints the integers from   1   to   100   (inclusive).
#But:
#  for multiples of three,   print   Fizz     (instead of the number)
#  for multiples of five,   print   Buzz     (instead of the number)
#  for multiples of both three and five,   print   FizzBuzz     (instead of the number)
#The   FizzBuzz   problem was presented as the lowest level of comprehension required to illustrate adequacy.

for numbers in range(1, 101):
    if numbers % 15 == 0:
        print 'FizzBuzz'
    elif numbers % 5 == 0:
        print 'Buzz'
    elif numbers % 3 == 0:
        print 'Fizz'
    else:
        print numbers