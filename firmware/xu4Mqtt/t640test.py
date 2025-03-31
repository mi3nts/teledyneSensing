from pymodbus.client import ModbusTcpClient
from pymodbus.exceptions import ModbusException
import struct
import time
from datetime import datetime
import os

def decode_float(regs, index):
    """Decode 2 registers (32-bit IEEE 754 float)"""
    raw = (regs[index] << 16) + regs[index + 1]
    return struct.unpack('>f', raw.to_bytes(4, byteorder='big'))[0]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_section(title):
    print("=" * 60)
    print(f"{title}".center(60))
    print("=" * 60)

# Setup
client = ModbusTcpClient("192.168.31.9", port=502)  # Change IP as needed
unit_id = 1

discrete_labels = [
    "BOX_TEMP_WARNING", "SAMPLE_FLOW_WARNING", "INTERNAL_SERIAL_TIMEOUT",
    "SYSTEM_RESET_WARNING", "SYS_OK_WARN", "SAMPLE_TEMPERATURE_WARNING",
    "BYPASS_FLOW_WARNING", "SYSTEM_FAULT_WARNING"
]

coil_labels = [
    "Control Relay 36", "Control Relay 37", "Control Relay 38",
    "Control Relay 39", "Maintenance Mode"
]

input_float_fields = {
    6:  "PM10 Real-time", 8: "PM2.5 Real-time", 10: "PM10-2.5 Real-time",
    12: "PM10 Std", 14: "PM10 1Hr Avg", 16: "PM2.5 1Hr Avg",
    18: "PM10-2.5 1Hr Avg", 20: "PM10 12Hr Avg", 22: "PM2.5 12Hr Avg",
    24: "PM10-2.5 12Hr Avg", 26: "PM10 24Hr Avg", 28: "PM2.5 24Hr Avg",
    30: "PM10-2.5 24Hr Avg", 32: "LED Temp", 34: "Ambient Pressure",
    36: "Humidity", 38: "Box Temp", 40: "Ambient Temp",
    42: "ASC Tube Temp", 44: "RH Sensor Temp", 46: "Sample Flow (5lpm)",
    48: "Bypass Flow (11.67lpm)", 50: "Total Flow", 52: "Signal Length",
    54: "P3 Value", 56: "Pump Duty Cycle", 58: "Valve Duty Cycle",
    60: "ASC Heater Duty", 62: "PM2.5 Std", 64: "PM1", 66: "PM1 Std",
    68: "PM1 1Hr Std", 70: "PM2.5 1Hr Std", 72: "PM10 1Hr Std",
    74: "PM1 12Hr Std", 76: "PM2.5 12Hr Std", 78: "PM10 12Hr Std",
    80: "PM1 24Hr Std", 82: "PM2.5 24Hr Std", 84: "PM10 24Hr Std",
    86: "Span Deviation", 88: "Span Dev Track", 90: "PM1 1Hr Avg",
    92: "PM1 12Hr Avg", 94: "PM1 24Hr Avg", 96: "PMtot", 98: "PMtot Std",
    100: "PMtot 1Hr", 102: "PMtot 1Hr Std", 104: "PMtot 12Hr",
    106: "PMtot 12Hr Std", 108: "PMtot 24Hr", 110: "PMtot 24Hr Std",
    112: "Sample Flow CV", 114: "Bypass Flow CV", 116: "Total Flow CV",
    118: "Total Particle Count"
}

holding_float_fields = {
    0: "PMT Voltage", 2: "PMT Offset", 4: "PMT HVPS",
    6: "5LPM Flow Cal", 8: "Bypass Flow Cal", 10: "Pressure Cal",
    12: "RH Setpoint", 14: "Sample Flow Setpoint",
    16: "Bypass Flow Setpoint", 18: "RH Sensor Slope",
    20: "KS10 PM10 Slope", 22: "KS2.5 PM2.5 Slope", 24: "KS1 PM1 Slope",
    26: "KO10 PM10 Offset", 28: "KO2.5 PM2.5 Offset", 30: "KO1 PM1 Offset"
}

# Main Loop
try:
    while True:
        clear_terminal()
        print_section(f"Teledyne API T640 Status @ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Discrete Inputs
        try:
            result = client.read_discrete_inputs(0, len(discrete_labels), unit=unit_id)
            if not result.isError():
                print_section("Discrete Warnings")
                for i, label in enumerate(discrete_labels):
                    print(f"{label:<40} {'ON' if result.bits[i] else 'OFF'}")
        except ModbusException as e:
            print("[Error] Discrete Inputs:", e)

        # Input Registers
        try:
            result = client.read_input_registers(0, 120, unit=unit_id)
            if not result.isError():
                regs = result.registers
                print_section("Environmental and PM Measurements")
                for i in sorted(input_float_fields):
                    try:
                        val = decode_float(regs, i)
                        print(f"{input_float_fields[i]:<40} {val:>10.3f}")
                    except:
                        print(f"{input_float_fields[i]:<40} [Decode Error]")
        except ModbusException as e:
            print("[Error] Input Registers:", e)

        # Holding Registers
        try:
            result = client.read_holding_registers(0, 32, unit=unit_id)
            if not result.isError():
                regs = result.registers
                print_section("Calibration and Configuration")
                for i in sorted(holding_float_fields):
                    try:
                        val = decode_float(regs, i)
                        print(f"{holding_float_fields[i]:<40} {val:>10.3f}")
                    except:
                        print(f"{holding_float_fields[i]:<40} [Decode Error]")
        except ModbusException as e:
            print("[Error] Holding Registers:", e)

        # Coil Registers
        try:
            result = client.read_coils(0, len(coil_labels), unit=unit_id)
            print(result.bits)
            if not result.isError():
                print_section("Control Coils")
                for i, label in enumerate(coil_labels):
                    print(f"{label:<40} {'ON' if result.bits[i] else 'OFF'}")
        except ModbusException as e:
            print("[Error] Coils:", e)

        # Wait 10 seconds before the next read
        print("\nRefreshing in 10 second...\n")
        time.sleep(10)

except KeyboardInterrupt:
    print("\nExiting gracefully...")

client.close()
