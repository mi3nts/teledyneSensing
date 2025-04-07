
from t640.t640 import T640
import time 
from mintsXU4 import mintsSensorReader as mSR

loopInterval = 10 
hostIP       = "192.168.20.125"

def main(loopInterval,hostIP):

    monitor = T640(host=hostIP)  # Or your device IP
    time.sleep(1)
    startTime = time.time()
    time.sleep(1)
    monitor.read_api(True)  
    time.sleep(0.1)      

    while True:
        try:
            print("======= T640 ========")
            monitor.read_discrete_inputs()
            time.sleep(0.25)
            monitor.read_coils()
            time.sleep(0.25)
            monitor.read_input_registers()
            time.sleep(0.25)
            monitor.read_holding_registers()
            time.sleep(0.25)
            monitor.read_api()  
            time.sleep(0.25)    
            print("=====================")
            startTime = mSR.delayMints(time.time() - startTime,loopInterval)
        
        except Exception as e:
            print(e)
            time.sleep(loopInterval)
        
        
if __name__ == "__main__":
    print("=============")
    print("    MINTS    ")
    print("=============")
    main(loopInterval,hostIP)
        