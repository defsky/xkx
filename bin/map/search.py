#!/usr/bin/python3 

import os
import re
from sys import argv, exit

from ..common import logger
from ..common import Tintin

basedir = os.path.split(os.path.realpath(__file__))[0]

mapfile = basedir + '/../../data/pku.map'

#print("map db :{}".format(mapfile))

try:
    _, roomname, area, playerid = argv
    
except ValueError as ve:
    logger.error(ve)
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
        
        line = f.readline()

except:
    logger.error("exception occurred when search room")
else:
    connector = ";"
    tt = Tintin()
    
    tt.write("result", "{{{}}}".format(connector.join(map_list)))

finally:
    if f:
        f.close()
