#!/bin/bash
#
# sleep 1
# echo "IPS7100"
# echo $(pgrep -f 'ips7100ReaderV1.py')
# sleep 2

sleep 1
echo "T640"
echo $(pgrep -f 't640Reader.py')
sleep 1

python3 ipReader.py
sleep 1