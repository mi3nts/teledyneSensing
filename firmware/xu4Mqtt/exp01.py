from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import struct
import time
from datetime import datetime, timezone
import os
from collections import OrderedDict
import requests
import json 

import sys 
import re 
import traceback
from pprint import pprint
import yaml

from t700.t700 import T700

loopInterval = 10 
hostIP       = "192.168.20.109"

cylinder     = "cylinder01.yaml"

# Exp 1 = 

# API ALSO AVAILABLE AT: http://hostIP:8180/api/taglist - Have 1031 parametors 



def main(hostIP):

    time.sleep(1)
    print("Starting T700 Monitor on ", hostIP)
    device = T700(host=hostIP)  # Or your device IP

    time.sleep(1)

    device.runSequence( conc=25000, flowRate=0.01, time=600, cylinder="cylinder01")

    device.activateStandByMode(device)
    device.continousRead(device)



if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    main(loopInterval,hostIP)
        

