#!/bin/bash -eu

FILENAME=$1
found=false
ip=''
I=0
for LN in $(cat $FILENAME)
do
    #echo "Line number $((I++)) -->  $LN"
    if $found ; then
       ip=$LN
       ip="${ip::-1}"
       break
    fi
    if [[ $LN == '"IP":' ]]; then
       #echo "It's there!"
       found=true
    fi
done
echo $ip
