#!/usr/bin/env python3

import sys
from .common import Tintin



if __name__ == '__main__':
    msg = sys.argv[1]
    
    surname_py = get_fuxing(conn, name[0:2])
    if surname_py:
        name_py = get_pinyin(conn, name[2:len(name)])
    else:
        surname_py = get_xing(conn, name[0:1])
        name_py = get_pinyin(conn, name[1:len(name)])

    tt = Tintin()
    tt.write("result",surname_py+" "+name_py)
