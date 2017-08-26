#http://rosettacode.org/wiki/15_Puzzle_Game
#15 Puzzle Game
#Implement the 15 Puzzle Game

import random

#Function to identify where 0 is located within the matrix - returns position of 0
def check_zero(array):
    pass

#Function to identify empty spot and returns position of that empty spot
def get_location(array, number):
    pass

#Function to swap number with 0
def swap(array, number):
    get_location(array, number)
    check_zero(array)
#    If check_zero & get_location return positions in proximity, swap()
    pass

def check_complete(b):
    if(b[0][0] == 1 and b[0][1] == 2 and b[0][2] == 3 and b[0][3] == 4 and b[1][0] == 5 and b[1][1] == 6 and b[1][2] == 7 and b[1][3] == 8 and b[2][0] == 9 and b[2][1] == 10 and b[2][2] == 11 and b[2][3] == 12 and b[3][0] == 13 and b[3][1] == 14 and b[3][2] == 15):
        print 'You\'ve completed the game'
        quit() 

#Main
a = list()
b = list()
for i in range(0, 16):
    a.append(i) 

random.shuffle(a)

b = [[a[0], a[1], a[2], a[3]], [a[4], a[5], a[6], a[7]], [a[8], a[9], a[10], a[11]], [a[12], a[13], a[14], a[15]]]

print b[0]
print b[1]
print b[2]
print b[3]
print 'game setup complete'

count = 0
while True:
    count += 1
    print 'round %d' % count
    user_input = raw_input('Enter number to move>')
    try:
        if user_input == 'quit':
            break
        else:
            number = int(user_input)
    except:
        print 'Input has to be an integer'
        count -= 1
        continue
    if not(1 <= number <= 15):
        print 'Input has to be an integer between 1 & 15'
        count -= 1
        continue
    swap(b, number)
    print b[0]
    print b[1]
    print b[2]
    print b[3]
    check_complete(b)
    