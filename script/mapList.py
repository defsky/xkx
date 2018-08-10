#!/usr/bin/python3 

import os
import re
import time
from sys import argv, exit

basedir = os.path.split(os.path.realpath(__file__))[0]

mapfile = basedir + '/../data/pku.map'

#print("map db :{}".format(mapfile))

try:
    _, roomname, area = argv
    
    #roomname = roomname.encode()
    #area = area.encode()
    
    #print("search for:{} {}".format(roomname,area))
except ValueError as ve:
    #print(ve)
    print('''
    Usage : mapList <roomname> <area>
    ''')
    exit(0)

try:
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
            #print("vnum:{} name:{} area:{}".format(
            #    matchobj.group(1),
            #    new_name,
            #    matchobj.group(7)))
        
        line = f.readline()

    #print("matched room count : {}".format(room_count))

    
    #print("#list map_list create {" + connector.join(map_list) + "}")
    #print("{" + connector.join(map_list) + "}")
except:
    print("exception detected")
else:
    outFileName = time.strftime("%Y%m%d%H%M%S",time.localtime()) + '.tmp'
    outFilePath = basedir + '/../data/' + outFileName
    connector = ";"
    
    of = open(outFilePath,'w',encoding='GB18030')
    of.write("#list map_list create {" + connector.join(map_list) + "}".encode().decode("gbk"))
    print(outFileName)
finally:
    of.close()
    f.close()
