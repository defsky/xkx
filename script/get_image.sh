#!/bin/bash

host=pkuxkx.net
img_dir=/home/caoliangcheng/mud/xkx/data/tmp/

a=`curl http://${host}/antirobot/robot.php?filename=$1 2>/dev/null | sed 's/[^"]*="\([^"]*\)"[^"]*/\1/g;s/"/\n/g;' | sed -n 1p | sed s/\.// `
echo $a

fname=${2}_$(date +%Y%m%d%H%M%S).jpg
filefullpath=$img_dir$fname

if [ -n "$a" ]; then
	wget -c http://${host}/antirobot$a -o $filefullpath 2> /dev/null &
	
	if [ $? -eq 0 ]; then
	    echo $fname
	fi
fi

display $filefullpath
