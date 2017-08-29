#http://rosettacode.org/wiki/99_Bottles_of_Beer
#99Bottles.py
#Task
#Display the complete lyrics for the song:     99 bottles of beer on the wall.
#    Until reaching 0

for number in range(99, 1, -1):
    print '%d bottles of beer on the wall\n%d bottles of beer\nTake one down, pass it around\n%d bottles of beer on the wall' % (number, number, number-1)