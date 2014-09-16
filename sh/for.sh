#!/bin/bash

for i in 1 2 3 4 5
do
    echo 'Welcome '$i' times.'
done

for c in {1..5}
do
    echo 'Welcome '$c' times.'
done

for ((c=1;c<=5;c++))
do
    echo 'wow '$c'.'
done
c=0
echo $c
while [ $c -le 10 ];
do
    echo "wow "$c
    c=$(($c + 1))
    if [ $c -eq 5 ]; then
	break; 
    fi
done

echo $@
echo $#
echo $!
echo $%

echo $2 "case argue"

case $2 in 
    a) echo "wow in a";;
    b) echo "not so wow in b";;
esac
