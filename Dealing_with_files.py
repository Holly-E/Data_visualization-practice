# -*- coding: utf-8 -*-
"""
Spyder Editor

Master Data Visualization with Python Course
"""
#open pre-existing file or create and open new file to write to 
# you can only write strings to txt files- must cast #'s to str( ) 
file = open('MyFile.txt', 'w')

file.write('Hello')
file.close()

# can reuse file variable name after you close it. 'a' appends to file, vs 'w' which overwrites file
file = open('MyFile.txt', 'a')
file.write(' World')

# \n makes a new line
file.write('\n')
file.write(str(123))
file.close()

# open in reading mode
file = open('MyFile.txt', 'r')

# line = first line, if you call twice it will read the second line if there was one
line = file.readline().split()
print(line)

line = file.readline()
print(int(line) + 2)

# .strip() to remove string .split() to make lists
file.close()

#The WITH method allows you to perfomr the same actions but without needing to close the file
#The file is automatically closed outside the indentation
with open('MyFile.txt', 'r') as file:
    line = file.readline()
    print(line)
    
