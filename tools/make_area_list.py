#!/usr/bin/python3 

from sys import argv, exit

try:
    _, mapfile = argv
except ValueError:
    print('''
    Usage : make_area_list.py <mapfile>
    ''')
    exit(0)
    
f = open(mapfile,'r',encoding='GB18030')

line = f.readline()

room_count = 0

while line:
    words = line.split(' ')
    
    if words[0] == 'R':
        room_count += 1;
    
    line = f.readline()
    
f.close()

print("room count : {}".format(room_count))
