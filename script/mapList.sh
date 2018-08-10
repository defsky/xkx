#!/bin/bash

current_dir=$(cd `dirname $0`;pwd)

a=$(python3 $current_dir/mapList.py $1 $2)

#if [ ! -z $a ];then
    echo $a
#fi
