#!/usr/bin/python3 

import os
import re
from sys import argv, exit

basedir = os.path.split(os.path.realpath(__file__))[0]

mapfile = basedir + '/../data/pku.map'

print("map db :{}".format(mapfile))

try:
    _, roomname, area = argv

    print("search for:{} {}".format(roomname,area))
except ValueError:
    print('''
    Usage : mapList <roomname> <area>
    ''')
    exit(0)
    
f = open(mapfile,'r',encoding='GB18030')

line = f.readline()

room_count = 0
area_dict = {}

map_list = []

while line:
    matchobj = re.match(r'R {(.*)} {(.*)} {(.*)} {(' + roomname + ')} {(.*)} {(.*)} {(' + area + ')} {(.*)} {(.*)} {(.*)} {(.*)}',line)
    
    if matchobj:
        room_count += 1;
        map_list.append(matchobj.group(1).strip())
        new_name = "{0:{wd}}".format(matchobj.group(4),wd=16-len(matchobj.group(4))*2)
        print("vnum:{} name:{} area:{}".format(
            matchobj.group(1),
            new_name,
            matchobj.group(7)))
    
    line = f.readline()
    
f.close()

print("matched room count : {}".format(room_count))

connector = ";"
print("#list map_list create {" + connector.join(map_list) + "}")
    
