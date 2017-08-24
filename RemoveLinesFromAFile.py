#RemoveLinesFromAFile.py
#Remove lines from a file
#http://rosettacode.org/wiki/Remove_lines_from_a_file

#Task
#Remove a specific line or a number of lines from a file.
#
#This should be implemented as a routine that takes three parameters (filename, starting line, and the number of lines to be removed).
#
#For the purpose of this task, line numbers and the number of lines start at one, so to remove the first two lines from the file foobar.txt, the parameters should be: foobar.txt, 1, 2
#
#Empty lines are considered and should still be counted, and if the specified line is empty, it should still be removed.
#
#An appropriate message should appear if an attempt is made to remove lines beyond the end of the file. 

def remove_lines(file_name, start_line, number_of_lines):
    try:
        in_handler = open(file_name,'r')
    except:
        print 'Unable to open file. Aborting program!'
        exit
    
    if start_line < 0 or number_of_lines < 1:
        print 'Can\'t remove specified number of lines. Aborting program!'
        exit
        
    line_count = 0
    for lines in in_handler.read():
        line_count += 1
    
    if line_count < (start_line + number_of_lines - 1):
        print 'Fewer number of lines in file than that expected to remove. Aborting program!'
        exit
    
    in_handler.seek(0)
    
    line_count = 0 
    out_handler = open('temp.txt', 'w')
    for lines in in_handler.read():
        line_count += 1
        if not(start_line < line_count and line_count < (start_line + number_of_lines - 1)):
            out_handler.write(lines)
    out_handler.close()        
    print 'Lines removed and wrote into temp.txt. Quitting program!'
    return 0


        
file_name = None
start_line, number_of_lines = 0, 0

while True:
    try:
        start_line = int(raw_input('Enter starting line to be removed>'))
        number_of_lines = int(raw_input('Enter number of lines to be removed>'))
        break
    except:
        print 'Incorrect format entered. Please enter integers'
        continue

file_name = raw_input('Enter file name>')
remove_lines(file_name, start_line, number_of_lines)