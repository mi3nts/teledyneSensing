from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import struct
import time
from datetime import datetime, timezone
import os
from collections import OrderedDict
import requests
import json 
from mintsXU4 import mintsSensorReader as mSR
import sys 
import re 
import traceback
from pprint import pprint
from t700.t700 import T700

loopInterval = 10 
hostIP       = "192.168.20.109"

def main(loopInterval, hostIP):

    monitor = T700(host=hostIP)
    time.sleep(1)
    monitor.activateStandByMode()
    time.sleep(1)
    monitor.continousRead(loopInterval=loopInterval, duration=60)

if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    main(loopInterval, hostIP)
