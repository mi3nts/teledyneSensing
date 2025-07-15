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

loopInterval = 10 
hostIP       = "192.168.20.109"

# API ALSO AVAILABLE AT: http://hostIP:8180/api/taglist - Have 1031 parametors 


def decode_float(regs, index):
    raw = (regs[index] << 16) + regs[index + 1]
    return struct.unpack('>f', raw.to_bytes(4, byteorder='big'))[0]


class T700:
    def __init__(self, host: str, port: int = 502, api_port: int = 8180 ,unit_id=1):
        
        self.client = ModbusTcpClient(host, port=port)
        
        if not self.client.connect():
            print(f"Unable to connect to Modbus server at {host}:{port}")
            sys.exit(1)  # Exit the script with a non-zero exit code        
        
        self.unit_id = unit_id
        self.sensorIDPreModbus = "T700MB001"
        
        self.sensorIDPreAPI    = "T700API001"
        self.apiURL            = "http://" + host +":"+ str(api_port) + "/api/taglist"  

        # 0 System reset warning 
        # 1 Box temperature warning 
        # 2 Photometer lamp temperature warning 
        # 3 O3 generator lamp temperature warning 
        # 4 Permeation tube #1 temperature warning 3
        # 5 Photometer reference warning 
        # 6 Photometer lamp stability warning 
        # 7 N/A 
        # 8 Regulator pressure warning 
        # 9 Any MFC pressure outside of warning limits 
        # 10 Any MFC drive less than 10% of full scale or greater than full scale 
        # 11 Any MFC sensor offset greater than allowable limit 
        # 12 Rear board communication warning 
        # 13 Relay board communication warning 
        # 14 Valve board communication warning 
        # 15 O3 generator or photometer lamp I2C driver chip communication warning
        # 16 Front panel communication warning 
        # 17 Firmware is unable to communicate with any MFC 
        # 18 Analog calibration warning 
        # 19 System is OK (same meaning as SYSTEM_OK I/O signal) 
        # 20 O3 generator not yet stabilized 
        # 21 Permeation tube #2 temperature warning 1

        self.discrete_labels = [
            "System Reset Warning",                                  # 0
            "Box Temperature Warning",                               # 1
            "Photometer Lamp Temperature Warning",                   # 2
            "Ozone Generator Lamp Temperature Warning",              # 3
            "Permeation Tube #1 Temperature Warning",                # 4
            "Photometer Reference Warning",                          # 5
            "Photometer Lamp Stability Warning",                     # 6
            "N/A",                                                   # 7
            "Regulator Pressure Warning",                            # 8
            "Any MFC Pressure Outside Warning Limits",               # 9
            "Any MFC Drive Below 10% or Above Full Scale",           #10
            "Any MFC Sensor Offset Exceeds Limit",                   #11
            "Rear Board Communication Warning",                      #12
            "Relay Board Communication Warning",                     #13
            "Valve Board Communication Warning",                     #14
            "O3 Generator or Photometer I2C Driver Communication",   #15
            "Front Panel Communication Warning",                     #16
            "No Communication with Any MFC",                         #17
            "Analog Calibration Warning",                            #18
            "System OK",                                             #19
            "Ozone Generator Not Yet Stabilized",                    #20
            "Permeation Tube #2 Temperature Warning"                 #21
        ]


        self.input_float_fields = {
            0:  "Actual Cal. Gas Flow Rate (LPM)",
            2:  "Actual Diluent Flow Rate (LPM)",
            4:  "Photometer Measured Ozone Concentration (PPB)",
            6:  "N/A",
            8:  "Ozone Generator Flow Rate (LPM)",
            10: "Ozone Generator Lamp Drive (mV)",
            12: "Ozone Generator Lamp Temperature (°C)",
            14: "Cal. Gas Pressure (PSIG)",
            16: "Diluent Pressure (PSIG)",
            18: "Regulator Pressure (PSIG)",
            20: "Internal Box Temperature (°C)",
            22: "Permeation Tube #1 Temperature (°C)",
            24: "Permeation Tube Flow Rate (LPM)",
            26: "Photometer Detector Measure Reading (mV)",
            28: "Photometer Detector Reference Reading (mV)",
            30: "Photometer Sample Flow Rate (LPM)",
            32: "Photometer Lamp Temperature (°C)",
            34: "Photometer Sample Pressure (inHg)",
            36: "Photometer Sample Temperature (°C)",
            38: "Photometer Slope (Zero/Span Calibration)",
            40: "Photometer Offset (Zero/Span Calibration, PPB)",
            42: "Ground Reference (mV)",
            44: "Precision 4.096 mV Reference (mV)",
            46: "Permeation Tube #2 Temperature (°C)",
            48: "Ozone Generator Fraction"
        }

    def read_discrete_inputs(self):
        dateTime = datetime.now(timezone.utc)

        try:
            result   = self.client.read_discrete_inputs(address=0, count=len(self.discrete_labels))  # Read 22 bits total (0–21)
            if not result.isError():
                (
                    self.systemResetWarning,                            # 0
                    self.boxTemperatureWarning,                         # 1
                    self.photometerLampTemperatureWarning,              # 2
                    self.o3GeneratorLampTemperatureWarning,             # 3
                    self.permeationTube1TemperatureWarning,             # 4
                    self.photometerReferenceWarning,                    # 5
                    self.photometerLampStabilityWarning,                # 6
                    _,                                                  # 7 (N/A)
                    self.regulatorPressureWarning,                      # 8
                    self.mfcPressureOutOfLimitWarning,                  # 9
                    self.mfcDriveOutOfRangeWarning,                     # 10
                    self.mfcSensorOffsetWarning,                        # 11
                    self.rearBoardCommWarning,                          # 12
                    self.relayBoardCommWarning,                         # 13
                    self.valveBoardCommWarning,                         # 14
                    self.i2cDriverCommWarning,                          # 15
                    self.frontPanelCommWarning,                         # 16
                    self.noMfcCommWarning,                              # 17
                    self.analogCalibrationWarning,                      # 18
                    self.systemOK,                                      # 19
                    self.o3GeneratorNotStabilizedWarning,               # 20
                    self.permeationTube2TemperatureWarning              # 21
                ) = result.bits[:len(self.discrete_labels)]  # Unpack the bits into variables

                sensorDictionary = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("systemResetWarning", int(self.systemResetWarning)),
                    ("boxTemperatureWarning", int(self.boxTemperatureWarning)),
                    ("photometerLampTemperatureWarning", int(self.photometerLampTemperatureWarning)),
                    ("o3GeneratorLampTemperatureWarning", int(self.o3GeneratorLampTemperatureWarning)),
                    ("permeationTube1TemperatureWarning", int(self.permeationTube1TemperatureWarning)),
                    ("photometerReferenceWarning", int(self.photometerReferenceWarning)),
                    ("photometerLampStabilityWarning", int(self.photometerLampStabilityWarning)),
                    ("regulatorPressureWarning", int(self.regulatorPressureWarning)),
                    ("mfcPressureOutOfLimitWarning", int(self.mfcPressureOutOfLimitWarning)),
                    ("mfcDriveOutOfRangeWarning", int(self.mfcDriveOutOfRangeWarning)),
                    ("mfcSensorOffsetWarning", int(self.mfcSensorOffsetWarning)),
                    ("rearBoardCommWarning", int(self.rearBoardCommWarning)),
                    ("relayBoardCommWarning", int(self.relayBoardCommWarning)),
                    ("valveBoardCommWarning", int(self.valveBoardCommWarning)),
                    ("i2cDriverCommWarning", int(self.i2cDriverCommWarning)),
                    ("frontPanelCommWarning", int(self.frontPanelCommWarning)),
                    ("noMfcCommWarning", int(self.noMfcCommWarning)),
                    ("analogCalibrationWarning", int(self.analogCalibrationWarning)),
                    ("systemOK", int(self.systemOK)),
                    ("o3GeneratorNotStabilizedWarning", int(self.o3GeneratorNotStabilizedWarning)),
                    ("permeationTube2TemperatureWarning", int(self.permeationTube2TemperatureWarning)),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "WRNS", sensorDictionary)
                return True, dict(zip(self.discrete_labels, result.bits))
            
        except Exception as e:
            print(f"Error reading discrete inputs: {e}")
        
        return False, None
    
    def read_input_registers(self):
        dateTime = datetime.now(timezone.utc)
        try:
            result = self.client.read_input_registers(address=0, count=50)
            print(result)
            print(result.registers)
            time.sleep(3)

            if not result.isError():
                regs = result.registers

                self.cal_gas_flow_rate         = decode_float(regs, 0)
                self.diluent_flow_rate         = decode_float(regs, 2)
                self.ozone_concentration       = decode_float(regs, 4)
                # 6 is marked N/A – skipping
                self.ozone_gen_flow_rate       = decode_float(regs, 8)
                self.ozone_gen_lamp_drive_mv   = decode_float(regs, 10)
                self.ozone_gen_lamp_temp_c     = decode_float(regs, 12)
                self.cal_gas_pressure_psig     = decode_float(regs, 14)
                self.diluent_pressure_psig     = decode_float(regs, 16)
                self.regulator_pressure_psig   = decode_float(regs, 18)
                self.internal_box_temp_c       = decode_float(regs, 20)
                self.perm_tube1_temp_c         = decode_float(regs, 22)
                self.perm_tube_flow_rate_lpm   = decode_float(regs, 24)
                self.detector_measure_mv       = decode_float(regs, 26)
                self.detector_reference_mv     = decode_float(regs, 28)
                self.sample_flow_rate_lpm      = decode_float(regs, 30)
                self.lamp_temp_c               = decode_float(regs, 32)
                self.sample_pressure_inHg      = decode_float(regs, 34)
                self.sample_temp_c             = decode_float(regs, 36)
                self.photometer_slope          = decode_float(regs, 38)
                self.photometer_offset_ppb     = decode_float(regs, 40)
                self.ground_reference_mv       = decode_float(regs, 42)
                self.precision_ref_mv          = decode_float(regs, 44)
                self.perm_tube2_temp_c         = decode_float(regs, 46)
                self.ozone_gen_fraction        = decode_float(regs, 48)

                
                ozone_data = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("ozoneConcPPB"        , self.ozone_concentration),
                    ("ozoneGenFlowLPM"     , self.ozone_gen_flow_rate),
                    ("ozoneGenLampDriveMV" , self.ozone_gen_lamp_drive_mv),
                    ("ozoneGenLampTempC"   , self.ozone_gen_lamp_temp_c),
                    ("ozoneGenFraction"    , self.ozone_gen_fraction),
                ])
                
                
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "O3",ozone_data)
                time.sleep(0.1)
                
                
                flow_data = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("calGasFlowLPM"       , self.cal_gas_flow_rate),
                    ("diluentFlowLPM"      , self.diluent_flow_rate),
                    ("permTubeFlowRateLPM" , self.perm_tube_flow_rate_lpm),
                    ("sampleFlowRateLPM"   , self.sample_flow_rate_lpm),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "FLOW", flow_data)
                time.sleep(0.1)

                pressure_data = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("calGasPressurePSIG"    , self.cal_gas_pressure_psig),
                    ("diluentPressurePSIG"   , self.diluent_pressure_psig),
                    ("regulatorPressurePSIG" , self.regulator_pressure_psig),
                    ("samplePressureInHg"    , self.sample_pressure_inHg),
                ])


                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "PRES", pressure_data)
                time.sleep(0.1)

                temperature_data = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("internalBoxTempC"  , self.internal_box_temp_c),
                    ("permTube1TempC"    , self.perm_tube1_temp_c),
                    ("permTube2TempC"    , self.perm_tube2_temp_c),
                    ("lampTempC"         , self.lamp_temp_c),
                    ("sampleTempC"       , self.sample_temp_c),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "TEMP", temperature_data)
                time.sleep(0.1)




                photometer_data = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("detectorMeasureMV"   , self.detector_measure_mv),
                    ("detectorReferenceMV" , self.detector_reference_mv),
                    ("photometerSlope"     , self.photometer_slope),
                    ("photometerOffsetPPB" , self.photometer_offset_ppb),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "PHOT", photometer_data)
                time.sleep(0.1)


                electrical_data = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("groundRefMV"    , self.ground_reference_mv),
                    ("precisionRefMV" , self.precision_ref_mv),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "ELEC", electrical_data)
                time.sleep(0.1)



                return True, {
                    self.input_float_fields[i]: decode_float(regs, i)
                    for i in sorted(self.input_float_fields.keys())
                }


        except ModbusException as e:
            print("[Error] Input Registers:", e)

        return False, None

    def get_true_indices_padded(self,bool_list):
        true_indices = [i for i, val in enumerate(bool_list) if val]
        return true_indices[:5] + [-1] * (5 - len(true_indices))

    def read_coils(self):
        dateTime = datetime.now(timezone.utc)
        try:
            resultStatus   = self.client.read_coils(address=0, count=102)
            resultControls = self.client.read_coils(address=200, count=12)

            if not resultStatus.isError():
                # Unpack up to 102 coils
                # print(resultStatus.bits)
                print(resultControls.bits)
                sequences       = resultStatus.bits[:100]
                purgeStatus     = resultStatus.bits[100]
                standByStatus   = resultStatus.bits[101]
                sequenceIndices = self.get_true_indices_padded(sequences)
                # print("Sequences:", sequences)
                # print("Purge Status:", purgeStatus)       
                # print("Standby Status:", standByStatus)
                # print("Sequence Indices:", sequenceIndices)
      
                status_info = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("sequence00", int(sequenceIndices[0])),
                    ("sequence01", int(sequenceIndices[1])),
                    ("sequence02", int(sequenceIndices[2])),           
                    ("sequence03", int(sequenceIndices[3])),
                    ("sequence04", int(sequenceIndices[4])),
                    ("purgeStatus", int(purgeStatus)),
                    ("standByStatus", int(standByStatus)),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "STATUS", status_info)
                time.sleep(0.1)


                control_info = OrderedDict([    
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("controlOut01", int(resultControls.bits[0])),
                    ("controlOut02", int(resultControls.bits[1])),
                    ("controlOut03", int(resultControls.bits[2])),
                    ("controlOut04", int(resultControls.bits[3])),
                    ("controlOut05", int(resultControls.bits[4])),
                    ("controlOut06", int(resultControls.bits[5])),
                    ("controlOut07", int(resultControls.bits[6])),
                    ("controlOut08", int(resultControls.bits[7])),
                    ("controlOut09", int(resultControls.bits[8])),
                    ("controlOut10", int(resultControls.bits[9])),
                    ("controlOut11", int(resultControls.bits[10])),
                    ("controlOut12", int(resultControls.bits[11])),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "CONTROL", control_info)  
                time.sleep(0.1)
                
                return True, [resultStatus,resultControls]
            
        except ModbusException as e:
            print("[Error] Coils:", e)
        except Exception as e:
            print("[Error] Coils (General):", e)
        return False, None
    
    def write_coil(self, address, value):
        """
        Write a single coil (boolean) value to the given address.
        address: int - coil address
        value: bool - True (set) or False (reset)
        Returns the result object from pymodbus.
        """
        try:
            result = self.client.write_coil(address= address, value=value)
            if result.isError():
                print(f"Failed to write coil at address {address}")
                return False
            return True
        except Exception as e:
            print(f"Error writing coil at address {address}: {e}")
            return False

    # def run_sequence(self, cylinder, gas, concentration_ppm, duration_sec):
    #     """
    #     Write a single coil (boolean) value to the given address.
    #     address: int - coil address
    #     value: bool - True (set) or False (reset)
    #     Returns the result object from pymodbus.
    #     """
    #     findIndex = f"C{cylinder}G{gas}C{concentration_ppm}"


 
    #     try:
    #         result = self.client.write_coil(address= address, value=True)
    #         if result.isError():
    #             print(f"Failed to write coil at address {address}")

    #             return False
    #         return True
    #     except Exception as e:
    #         print(f"Error writing coil at address {address}: {e}")
    #         return False

