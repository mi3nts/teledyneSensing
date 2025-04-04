
from n300.n300 import N300
import time 
from mintsXU4 import mintsSensorReader as mSR

loopInterval = 10 
hostIP       = "192.168.31.150"

def main(loopInterval,hostIP):

    monitor = N300(host=hostIP)  # Or your device IP
    time.sleep(1)
    startTime = time.time()

    while True:
        try:
            print("======= N300 ========")
            monitor.read_discrete_inputs()
            time.sleep(0.1)
            # monitor.read_coils()
            # time.sleep(0.1)
            # monitor.read_input_registers()
            # time.sleep(0.1)
            # monitor.read_holding_registers()
            # time.sleep(0.1)
            # monitor.read_api()        
            # print("=====================")
            startTime = mSR.delayMints(time.time() - startTime,loopInterval)
        
        except Exception as e:
            print(e)
            time.sleep(loopInterval)
        
        
if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    main(loopInterval,hostIP)
        