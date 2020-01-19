#!/usr/bin/env python3

import sys
import time
import re
import sqlite3

from .common import Tintin

from urllib import request

#http://pkuxkx.com/antirobot/robot.php?filename=1533298957741196

def get_captcha(captcha_id, user_id):
    baseurl = 'http://pkuxkx.com/antirobot/'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebkit/537.36 (KHTML,like Gecko) Chrome/55.0.2883.75 Safari/537.36'
    header = {'User-Agent':user_agent}

    try:
        pageurl = baseurl + 'robot.php?filename=' + captcha_id
        
        req = request.Request(pageurl,headers=header)

        page = request.urlopen(req,timeout=10)

        html = page.read().decode('UTF-8')

        #html = '<html><img src="./b2evo_captcha_tmp/b2evo_captcha_28E1DDAD1C0E0BA3F9087B4CAD052F80.jpg" alt="This is a captcha-picture. It is used to prevent robots." title=""><br> <H3>If you can not read the image, please refresh the page to genenrate new.<H3><br></html>'


        searchObj = re.search(r'<html><img src="(.*)" alt=.*',html,re.M|re.I)

        if searchObj:
            imgurl = baseurl + searchObj.group(1)
            
            #print(searchObj.group(1))
            #print(imgurl)
            
            filename = 'tmp/{}_{}.jpg'.format(user_id,time.strftime("%Y%m%d%H%M%S",time.localtime()))
            
            opener = request.build_opener()
            opener.addheaders = [('User-Agent',user_agent)]
            request.install_opener(opener)
            
            request.urlretrieve(imgurl,filename)
            return filename
        else:
            return "0"
            
    #except ConnectionResetError:
    except:
        #print(sys.exc_info())
        return "0"
    
if __name__ == '__main__':
    _,imgID, uid = sys.argv
    
    image_file_path = get_captcha(imgID, uid)
    
    if image_file_path == None:
        image_file_path = "0"

    tt = Tintin()
    tt.write("result",image_file_path)
