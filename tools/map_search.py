#!/usr/bin/python3 

from sys import argv, exit
import re

try:
    _, mapfile = argv
except ValueError:
    print('''
    Usage : make_search <mapfile>
    ''')
    exit(0)
    
f = open(mapfile,'r',encoding='GB18030')

line = f.readline()

room_count = 0
area_dict = {}

bus_station_list = []

while line:
    matchobj = re.match(r'R {(.*)} {(.*)} {(.*)} {(马车)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)} {(.*)}',line)
    
    if matchobj:
        room_count += 1;
        bus_station_list.append(matchobj.group(1).strip())
        new_name = "{0:{wd}}".format(matchobj.group(4),wd=16-len(matchobj.group(4))*2)
        print("id:{} status:{} name:{} area:{}".format(
            matchobj.group(1),
            matchobj.group(2),
            new_name,
            matchobj.group(7)))
    
    line = f.readline()
    
f.close()

print("matched room count : {}".format(room_count))

connector = ";"
print("#list bus_station_list create {" + connector.join(bus_station_list) + "}")
    
    
    
    
    
    
