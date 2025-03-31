from t640.t640 import T640
import time 




if __name__ == "__main__":
    monitor = T640(host="192.168.31.9")  # Or your device IP
    time.sleep(1)
    print(monitor.read_discrete_inputs())
    time.sleep(1)
    print(monitor.read_coils())
    time.sleep(1)
    print(monitor.read_input_registers())
    time.sleep(1)
    print(monitor.read_holding_registers())    