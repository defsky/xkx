#!/bin/bash

current_dir=$(cd `dirname $0`;pwd)

msg=$1
echo -e ${msg//\\\;/\;}>> $current_dir/../data/$2
