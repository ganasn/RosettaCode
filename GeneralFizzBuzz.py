#http://rosettacode.org/wiki/General_FizzBuzz
#GeneralFizzBuzz.py
#Task: 
#Write a generalized version of FizzBuzz that works for any list of factors, along with their words.
#This is basically a "fizzbuzz" implementation where the user supplies the parameters.
#The user will enter the max number, then they will enter the factors to be calculated along with the corresponding word to be printed.

#For simplicity's sake, assume the user will input an integer as the max number and 3 factors, each with a word associated with them.

#For example, given:
#>20      #This is the maximum number, supplied by the user
#>3 Fizz  #The user now enters the starting factor (3) and the word they want associated with it (Fizz)
#>5 Buzz  #The user now enters the next factor (5) and the word they want associated with it (Buzz)
#>7 Baxx  #The user now enters the next factor (7) and the word they want associated with it (Baxx)
#In other words: For this example, print the numbers 1 through 20, replacing every multiple of 3 with "Fizz", every multiple of 5 with "Buzz", and every multiple of 7 with "Baxx".
#In the case where a number is a multiple of at least two factors, print each of the words associated with those factors in the order of least to greatest factor.
#For instance, the number 15 is a multiple of both 3 and 5; print "FizzBuzz".
#If the max number was 105 instead of 20, you would print "FizzBuzzBaxx" because it's a multiple of 3, 5, and 7.

from sys import *

commands = dict()

script, max_number = argv 

#while True:
#    command = raw_input('Enter integer & codeword>')
#    if command == 'do':
##Do General Fizz Buzz
##unpack commands list as individual combinations of integer and codeword
#        for number in range(1, int(max_number)+1):
#            print number
#        print commands
#        break
#    else:
#        commands[int(command.split()[0])] = command.split()[1]
#        continue

combo1 = raw_input('Enter first combination>')
number1 = int(combo1.split()[0])
code1 = combo1.split()[1]

combo2 = raw_input('Enter second combination>')
number2 = int(combo2.split()[0])
code2 = combo2.split()[1]

combo3 = raw_input('Enter third combination>')
number3 = int(combo3.split()[0])
code3 = combo3.split()[1]

#print combo1, combo2, combo3, code1, code2, code3, number1, number2, number3

for number in range(1, int(max_number)+1):
    if number % (number1 * number2 * number3) == 0:
        print code1 + code2 + code3
    elif number % (number2 * number3) == 0:
        print code2 + code3
    elif number % (number1 * number2) == 0:
        print code1 + code2
    elif number % (number1 * number3) == 0:
        print code1 + code3
    else:
        print number