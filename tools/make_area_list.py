#!/usr/bin/python3 

from sys import argv, exit
import re

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
area_dict = {}

while line:
    #words = line.split(' ')
    
    #if words[0] == 'R':
    #    room_count += 1;
    matchobj = re.match(r'R {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)}',line)
    
    if matchobj:
        room_count += 1;
        #print("id:{} area:{} name:{} desc:{}".format(matchobj.group(1),matchobj.group(7),matchobj.group(4),matchobj.group(6)))
        if matchobj.group(7) in area_dict:
            area_dict[matchobj.group(7)] += 1
        else:
            area_dict[matchobj.group(7)] = 1
    
    line = f.readline()
    
    if line:
        print("Room count processed : {5d}".format(room_count),end = "\r")
    else:
        print("Room count processed : {}".format(room_count))
    
f.close()

#print("room count : {}".format(room_count))

for i in area_dict:
    print("{} {}".format(i,area_dict[i]))
