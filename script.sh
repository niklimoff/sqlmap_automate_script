#!/bin/bash

if [ -n "$1" ]

then

for VARIABLE in $(python script.py -s "$1")

do

echo "Testing url $VARIABLE..."

sqlmap --url="$VARIABLE"

done

else

echo "No URL parameter."

fi
