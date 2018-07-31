#!/bin/bash

current_dir=$(cd `dirname $0`;pwd)

a=$(python3 $current_dir/getCaptcha.py $1 $2)

if [ ! -z $a ];then

    if [ -e $a ];then
        echo $a;
        mv $a $current_dir/../tmp/;
    fi;
fi


