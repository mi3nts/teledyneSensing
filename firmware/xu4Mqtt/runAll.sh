#!/bin/bash
#
sleep 60

kill $(pgrep -f 't640Reader.py')
sleep 5
python3 t640Reader.py &
sleep 5


kill $(pgrep -f 'n300Reader.py')
sleep 5
python3 n300Reader.py &
sleep 5


python3 ipReader.py
sleep 5