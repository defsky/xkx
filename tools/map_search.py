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

bus_station_list = []

while line:
    #words = line.split(' ')
    
    #if words[0] == 'R':
    #    room_count += 1;
    matchobj = re.match(r'R {(.*)} {(.*)} {(.*)} {(.*马车\S+)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)}',line)
    
    if matchobj:
        room_count += 1;
        bus_station_list.append(matchobj.group(1).strip())
        print("id:{} status:{} name:{} area:{}".format(matchobj.group(1),matchobj.group(2),matchobj.group(4),matchobj.group(7)))
    
    line = f.readline()
    
f.close()

print("matched room count : {}".format(room_count))

connector = ";"
print("#list bus_station_list create {" + connector.join(bus_station_list) + "}")
    
    
    
    
    
    
