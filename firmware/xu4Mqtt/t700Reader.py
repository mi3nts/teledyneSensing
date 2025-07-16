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
    startTime = time.time()
    time.sleep(1)

    try:
        while True:
            try:
                print("======= T700 ========")

                read, data = monitor.read_discrete_inputs()
                # if read:
                #     print("Discrete Inputs:", data)
                time.sleep(2)

                read, data = monitor.read_input_registers()
                # if read:
                #     print("Input Registers:", data)
                time.sleep(2)

                read, data = monitor.read_coils()
                # if read:
                #     print("Coils :", data)
                time.sleep(2)

                print("=====================")
                startTime = mSR.delayMints(time.time() - startTime, loopInterval)

            except Exception as e:
                print("Exception during polling:")
                traceback.print_exc()
                time.sleep(loopInterval)

    except KeyboardInterrupt:
        print("\n[INFO] KeyboardInterrupt received. Exiting gracefully.")
        # Add cleanup code here if necessary
        return False, None

if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    main(loopInterval, hostIP)
