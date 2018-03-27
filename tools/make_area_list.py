#!/usr/bin/python3 

from sys import argv, exit

try:
    _, mapfile = argv
except ValueError:
    print('''
    Usage : make_area_list.py <mapfile>
    ''')
    exit(0)
    
f = open(mapfile,'r',encoding='GBK')
f.read(1)

