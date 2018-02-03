#!/bin/bash

script_path=$(cd `dirname $0`;pwd)
file_full_path=$script_path/../modules/$1.tin
tpl_full_path=$script_path/../modules/module_tpl

LANG=zh_CN.gbk cat $tpl_full_path | sed "s/<module_name>/$1/" > $file_full_path

if [ -f $file_full_path ]; then
    gedit $file_full_path & > /dev/null &
else
    echo "$1:module creation faied"
fi

