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


# API ALSO AVAILABLE AT: http://hostIP:8180/api/taglist - Have 1031 parametors 

def decode_float(regs, index):
    raw = (regs[index] << 16) + regs[index + 1]
    return struct.unpack('>f', raw.to_bytes(4, byteorder='big'))[0]

def getSequenceIndex(*,conc, flowRate, time, cylinder):
    cylinderFile = os.path.join("gasCylinders", cylinder+".yaml")
    cylinderSequences = yaml.load(open(cylinderFile ),Loader=yaml.FullLoader)
    # print(cylinderSequences)

    for entry in cylinderSequences['cylinder']:
        # print(entry)
        if (entry["ch4_ppm"] == conc and
            entry["flow_SLPM"] == flowRate and
            entry["time_seconds"] == time):
            print("Found Match: ", entry)
            return entry["index"], entry


def runSequence(monitor, sequenceIndex, sequenceEntry):

    print("Running: ",sequenceEntry)
    monitor.write_coil(sequenceEntry, True)


def main(loopInterval,hostIP):

    lk = getSequenceIndex(conc=25000, flowRate=0.01, time=600, cylinder="cylinder01")
    print(lk)
    monitor = T700(host=hostIP)  # Or your device IP
    time.sleep(1)
    startTime = time.time()
    time.sleep(1)
    monitor.read_api(True)  
    time.sleep(0.1)     
     
    # initialRead = True
    # while True:
    #     try:
    #         print("======= T700 ========")
    #         # read, data = monitor.read_discrete_inputs()
    #         # if read:
    #         #     print("Discrete Inputs:", data)
    #         # time.sleep(0.25)
            
    #         read, data = monitor.read_input_registers()
    #         if read:
    #             print("Discrete Inputs:", data)   
    #         time.sleep(0.25)         
            
    #         read, data = monitor.read_coils()
    #         if read:
    #             print("Discrete Inputs:", data)   
    #         time.sleep(0.25)      
    
    #         if initialRead:
    #             print("Initial Read Complete - Write Coil 0 - Sequence 0")
    #             monitor.write_coil(0, True)
    #             initialRead = False

    #         print("=====================")
    #         startTime = mSR.delayMints(time.time() - startTime,loopInterval)

    #     except Exception as e:
    #         print(e)
    #         time.sleep(loopInterval)
    
    #     return False, None
    


if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    main(loopInterval,hostIP)
        

