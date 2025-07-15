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


def main(loopInterval,hostIP):

    monitor = T700(host=hostIP)  # Or your device IP
    time.sleep(1)
    startTime = time.time()
    time.sleep(1)
    # monitor.read_api(True)  
    # time.sleep(0.1)      
    initialRead = True
    while True:
        try:
            print("======= T700 ========")
            
            read, data = monitor.read_input_registers()
            if read:
                print("Discrete Inputs:", data)   
            time.sleep(0.25)         
            
            read, data = monitor.read_coils()
            if read:
                print("Discrete Inputs:", data)   
            time.sleep(0.25)      
    
            # if initialRead:
            #     print("Initial Read Complete - Write Coil 0 - Sequence 0")
            #     monitor.write_coil(0, True)
            #     initialRead = False

            print("=====================")
            startTime = mSR.delayMints(time.time() - startTime,loopInterval)

        except Exception as e:
            print(e)
            time.sleep(loopInterval)
    
        return False, None
    


if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    main(loopInterval,hostIP)
        

