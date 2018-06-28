host=pkuxkx.net
#host=223.202.85.195

a=`curl http://${host}/antirobot/robot.php?filename=$1 2>/dev/null | sed 's/[^"]*="\([^"]*\)"[^"]*/\1/g;s/"/\n/g;' | sed -n 1p | sed s/\.// `
echo $a

fname=${2}_$(date +%Y%m%d%H%M%S).jpg

if [ -n "$a" ]; then
	echo wget http://${host}/antirobot$a -o /home/caoliangcheng/mud/xkx/data/tmp/$fname 2> /dev/null &
	
	if [ $? -eq 0 ]; then
	    echo $fname
	fi
fi
