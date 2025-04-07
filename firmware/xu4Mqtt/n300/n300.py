
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

# Future Corrections Initially Read Everyting then keep it down 

def decode_float(regs, index):
    raw = (regs[index] << 16) + regs[index + 1]
    return struct.unpack('>f', raw.to_bytes(4, byteorder='big'))[0]


class N300:
    def __init__(self, host: str, port: int = 502, api_port: int = 8180 ,unit_id=1):
        
        self.client = ModbusTcpClient(host, port=port)
        if not self.client.connect():
            print(f"Unable to connect to Modbus server at {host}:{port}")
            sys.exit(1)  # Exit the script with a non-zero exit code        
        
        self.unit_id = unit_id
        self.sensorIDPreModbus = "N300MB001"
        self.sensorIDPreAPI    = "N300API001"
        self.apiURL            = "http://" + host +":"+ str(api_port) + "/api/taglist"  

        self.discrete_fields = {
            0:  "Source Warning",
            2:  "Bench Temperature Warning",
            3:  "Wheel Temperature Warning",
            7:  "CPU Rebooted Warning",
            8:  "Supervisor Communication Warning",
            9:  "GFC Communication Warning",
            10: "Pump Control Communication Warning",
            11: "Analog Output Communication Warning",
            12: "Digital I/O Communication Warning",
            13: "Low Memory Warning",
            14: "Invalid Concentration Warning",
            18: "System OK Status Warning",
            19: "Analog Output 1 Requires Calibration Warning",
            20: "Analog Output 2 Requires Calibration Warning",
            21: "Analog Output 3 Requires Calibration Warning",
            22: "Analog Output 4 Requires Calibration Warning",
            23: "Analog Output 5 Requires Calibration Warning",
            24: "Analog Output 6 Requires Calibration Warning",
            25: "Analog Output 7 Requires Calibration Warning",
            26: "Time Not Synced with Network  Warning"
        }

        self.coil_labels = {
            20: "Zero Calibration - Range 1 Enabled",
            21: "Span Calibration - Range 1 Enabled",
            22: "Zero Calibration - Range 2 Enabled",
            23: "Span Calibration - Range 2 Enabled"
        }

        self.input_float_fields = {
            0:  "Photometer - Measure Reading (mV)",
            2:  "Photometer - Reference Reading (mV)",
            4:  "Measure over Reference Ratio",
            6:  "CO Slope - Range 1",
            8:  "CO Slope - Range 2",
            10: "CO Offset - Range 1",
            12: "CO Offset - Range 2",
            18: "CO Concentration - Range 1",
            20: "CO Concentration - Range 2",
            22: "CO Concentration Stability",
            24: "Bench Temperature (°C)",
            26: "Bench Temperature Control Duty Cycle (%)",
            28: "Wheel Temperature (°C)",
            30: "Wheel Temperature Control Duty Cycle (%)",
            32: "Sample Temperature (°C)",
            34: "Sample Pressure (PSIA)",
            36: "Box Temperature (°C)",
            38: "Photometer Temperature Drive (mV)",
            40: "Pump Flow (CCM)",
            42: "Atmospheric Pressure (Pa)"
        }

        self.holding_register_fields = {
            0:  "CO Target Span Concentration 1",
            2:  "CO Target Span Concentration 2",
        }

    def read_discrete_inputs(self):
        dateTime  = datetime.now(timezone.utc)
        try:
            start_address = min(self.discrete_fields.keys())
            count = max(self.discrete_fields.keys()) - start_address + 1
            result = self.client.read_discrete_inputs(start_address, count, unit=self.unit_id)
            # print(result.bits)
            if not result.isError():
                (   self.sourceWarning,
                    self.benchTemperatureWarning,
                    self.wheelTemperatureWarning,
                    self.cpuRebootedWarning,
                    self.supervisorComWarning,
                    self.gfcComWarning,
                    self.pumpControlComWarning,
                    self.analogOutputComWarning,
                    self.digitalIOComWarning,
                    self.lowMemoryWarning,
                    self.invalidConcentrationWarning,
                    self.systemOKStatusWarning,
                    self.analogOutput1CalibWarning,
                    self.analogOutput2CalibWarning,
                    self.analogOutput3CalibWarning,
                    self.analogOutput4CalibWarning,
                    self.analogOutput5CalibWarning,
                    self.analogOutput6CalibWarning,
                    self.analogOutput7CalibWarning,
                    self.timeNotSyncedWarning
                ) = [
                    result.bits[address - start_address] if (address - start_address) < len(result.bits) else None
                    for address in sorted(self.discrete_fields.keys())
                ]
                # print(result.bits)
                sensorDictionary = OrderedDict([
                    ("dateTime", str(dateTime.strftime('%Y-%m-%d %H:%M:%S.%f'))),
                    ("sourceWarning",                     int(self.sourceWarning)),
                    ("benchTemperatureWarning",           int(self.benchTemperatureWarning)),
                    ("wheelTemperatureWarning",           int(self.wheelTemperatureWarning)),
                    ("cpuRebootedWarning",                int(self.cpuRebootedWarning)),
                    ("supervisorComWarning",              int(self.supervisorComWarning)),
                    ("gfcComWarning",                     int(self.gfcComWarning)),
                    ("pumpControlComWarning",             int(self.pumpControlComWarning)),
                    ("analogOutputComWarning",            int(self.analogOutputComWarning)),
                    ("digitalIOComWarning",               int(self.digitalIOComWarning)),
                    ("lowMemoryWarning",                  int(self.lowMemoryWarning)),
                    ("invalidConcentrationWarning",       int(self.invalidConcentrationWarning)),
                    ("systemOKStatusWarning",             int(self.systemOKStatusWarning)),
                    ("analogOutput1CalibWarning",         int(self.analogOutput1CalibWarning)),
                    ("analogOutput2CalibWarning",         int(self.analogOutput2CalibWarning)),
                    ("analogOutput3CalibWarning",         int(self.analogOutput3CalibWarning)),
                    ("analogOutput4CalibWarning",         int(self.analogOutput4CalibWarning)),
                    ("analogOutput5CalibWarning",         int(self.analogOutput5CalibWarning)),
                    ("analogOutput6CalibWarning",         int(self.analogOutput6CalibWarning)),
                    ("analogOutput7CalibWarning",         int(self.analogOutput7CalibWarning)),
                    ("timeNotSyncedWarning",              int(self.timeNotSyncedWarning)),
                ])
                mSR.sensorFinisher(dateTime,self.sensorIDPreModbus+"WRNS",sensorDictionary)

            return True, {
                self.discrete_fields[address]: result.bits[address - start_address]
                for address in self.discrete_fields
                if (address - start_address) < len(result.bits)
            }
        except ModbusException as e:
            print("[Error] Discrete Inputs:", e)
            traceback.print_exc()
        return False, None
    
    def read_coils(self):
        dateTime = datetime.now(timezone.utc)
        try:
            # Read coil states for the calibration control (coils 20–23)
            start_address = 20
            coil_count = 4

            result = self.client.read_coils(start_address, coil_count, unit=self.unit_id)

            # Print raw bit results for debugging
            # print(result.bits)

            # Proceed if there is no error
            if not result.isError():
                (
                    self.zeroCalRange1,
                    self.spanCalRange1,
                    self.zeroCalRange2,
                    self.spanCalRange2
                ) = result.bits[:coil_count]

            # Create an ordered dictionary with the coil values
            sensor_data = OrderedDict([
                ("dateTime"       , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("zeroCalRange1"  , int(self.zeroCalRange1)),
                ("spanCalRange1"  , int(self.spanCalRange1)),
                ("zeroCalRange2"  , int(self.zeroCalRange2)),
                ("spanCalRange2"  , int(self.spanCalRange2)),
            ])

            # Finalize and log the sensor data
            mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "COIL", sensor_data)

            return True, dict(zip(self.coil_labels, result.bits))

        except ModbusException as e:
            print("[Error] Coils:", e)
            traceback.print_exc()
        return False, None


    def read_input_registers(self):
        dateTime = datetime.now(timezone.utc)
        try:
           # Read input registers for CO analyzer values (total 44 bytes = 22 floats = 0 to 42)
            result = self.client.read_input_registers(0, 44, unit=self.unit_id)

            if not result.isError():
                regs = result.registers

                # Decode float values from register pairs
                self.irMeasure              = decode_float(regs, 0)
                self.irReference            = decode_float(regs, 2)
                self.measureRefRatio        = decode_float(regs, 4)
                self.coSlope1               = decode_float(regs, 6)
                self.coSlope2               = decode_float(regs, 8)
                self.coOffset1              = decode_float(regs, 10)
                self.coOffset2              = decode_float(regs, 12)
                self.coConcRange1           = decode_float(regs, 18)
                self.coConcRange2           = decode_float(regs, 20)
                self.coStability            = decode_float(regs, 22)
                self.benchTemp              = decode_float(regs, 24)
                self.benchDutyCycle         = decode_float(regs, 26)
                self.wheelTemp              = decode_float(regs, 28)
                self.wheelDutyCycle         = decode_float(regs, 30)
                self.sampleTemp             = decode_float(regs, 32)
                self.samplePressure         = decode_float(regs, 34)
                self.boxTemp                = decode_float(regs, 36)
                self.photoTempRaw           = decode_float(regs, 38)
                self.sampleFlow             = decode_float(regs, 40)
                self.atmosphericPressure    = decode_float(regs, 42)

                # Create a dictionary for core sensor values you might want to log
                coAnalyzerData = OrderedDict([
                    ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("irMeasure"             , self.irMeasure),
                    ("irReference"           , self.irReference),
                    ("measureRefRatio"       , self.measureRefRatio),
                    ("coSlope1"              , self.coSlope1),
                    ("coSlope2"              , self.coSlope2),
                    ("coOffset1"             , self.coOffset1),
                    ("coOffset2"             , self.coOffset2),
                    ("coConcRange1"          , self.coConcRange1),
                    ("coConcRange2"          , self.coConcRange2),
                    ("coStability"           , self.coStability),
                ])
                # Finalize or log the sensor reading
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "CO", coAnalyzerData)

                coClimateData = OrderedDict([
                    ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("benchTemp"             , self.benchTemp),
                    ("benchDutyCycle"        , self.benchDutyCycle),
                    ("wheelTemp"             , self.wheelTemp),
                    ("wheelDutyCycle"        , self.wheelDutyCycle),
                    ("sampleTemp"            , self.sampleTemp),
                    ("samplePressure"        , self.samplePressure),
                    ("boxTemp"               , self.boxTemp),
                    ("photoTempRaw"          , self.photoTempRaw),
                    ("sampleFlow"            , self.sampleFlow),
                    ("atmosphericPressure"   , self.atmosphericPressure),
                ])

                # Finalize or log the sensor reading
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "CLMT", coClimateData)

                
                return True, {
                    self.input_float_fields[i]: decode_float(regs, i)
                    for i in sorted(self.input_float_fields.keys())
                }
        except ModbusException as e:
            print("[Error] Input Registers:", e)
            traceback.print_exc()
        return False, None            
    
    def read_holding_registers(self):
        dateTime = datetime.now(timezone.utc)
        try:
            # Read holding registers for CO target span concentrations (2 floats = 4 registers)
            result = self.client.read_holding_registers(0, 4, unit=self.unit_id)

            if not result.isError():
                regs = result.registers

                # Decode float values from register pairs
                self.coTargetSpanConc1 = decode_float(regs, 0)
                self.coTargetSpanConc2 = decode_float(regs, 2)

                # Create dictionary for logging or transmission
                coSpanCalibrationDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("coTargetSpanConc1" , self.coTargetSpanConc1),
                    ("coTargetSpanConc2" , self.coTargetSpanConc2)
                ])

                # Finalize or log the span calibration data
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "SPAN", coSpanCalibrationDict)

                time.sleep(.1)                

                return True, {
                    self.holding_register_fields[i]: decode_float(regs, i)
                    for i in sorted(self.holding_register_fields.keys())
                }
            
        except ModbusException as e:
            print("[Error] Input Registers:", e)
            traceback.print_exc()
        return False, None                
    
    def _to_camel_case(self, s):
        """Convert tag name from UPPER_SNAKE_CASE to camelCase."""
        s = s.replace('.', '_') 
        parts = s.lower().split('_')
        return parts[0] + ''.join(word.capitalize() for word in parts[1:])

    def _normalize_value(self, value):
        if isinstance(value, bool):
            return int(value)
        elif isinstance(value, (int, float)):
            return value
        elif isinstance(value, str):
            val = value.strip().lower()
            if val == "true":
                return 1
            elif val == "false":
                return 0
        try:
            # Try converting to float or int if it's a numeric string
            if '.' in str(value):
                return float(value)
            return int(value)
        except (ValueError, TypeError):
            return value


    def read_api(self, startUp = False):

        response = requests.get(self.apiURL)
        if response.status_code == 200:
            data = response.json()
            for tag in data.get("tags", []):
                name = tag.get("name", "")
                raw_value = tag.get("value", "")
                camel_name = self._to_camel_case(name)
                # print(camel_name + ":" + raw_value)

            
                # Skip tags that start with digits (e.g., '1MIN-DATA')
                if name and name[0].isdigit():
                    continue

                # Special case for opcDustHistogram
                if camel_name == "hires":
                    if isinstance(raw_value, str):
                        try:
                            match_id = re.search(r"#(\d+):", raw_value)
                            prefix_value = int(match_id.group(1)) if match_id else None

                            # Extract values inside brackets
                            matches = re.findall(r"\[(.*?)\]", raw_value)

                            if prefix_value is not None and matches:
                                float_values = [float(x.strip()) for x in matches[0].split(',')]
                                values = [prefix_value] + float_values
                            else:
                                continue

                            for i, val in enumerate(values):
                                bin_name = f"hires{i:02d}"
                                setattr(self, bin_name, val)
                                # print(f"self.{bin_name} = {val}")

                        except Exception as e:
                            print("Error:", str(e))
                            traceback.print_exc()
                    continue  # Skip setting opcDustHistogram as a string
                            
                # Normalize the value (convert strings "True"/"False" to 1/0, etc.)
                normalized_value = self._normalize_value(raw_value)

                # Save to camelCase class attribute
                try:
                    setattr(self, camel_name, normalized_value)
                    # print(f"self.{camel_name} = {repr(normalized_value)}")
                except Exception as e:
                    print(f"[Warning] Failed to set attribute '{camel_name}': {e}")
                    traceback.print_exc()
            
        #     # At this point, the data is attached to sensors 
            dateTime  = datetime.now(timezone.utc)
            
            if startUp:
                print(" ON STARTUP")
                # STRING VARS: instrumentTime, packageVersion, osPlatform, osVersion, cfnetVersion
                systemInfoDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("instrumentTime", self.instrumentTime),
                    ("svSerialNumber", self.svSerialNumber),
                    ("packageVersion", self.packageVersion),
                    ("osPlatform",     self.osPlatform),
                    ("osVersion",      self.osVersion),
                    ("cfnetVersion",   self.cfnetVersion)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "INFO", systemInfoDict )
                time.sleep(.1)    


                memoryDiskDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("systemTotalRam", self.systemTotalRam),
                    ("systemFreeRam", self.systemFreeRam),
                    ("systemUsedRam", self.systemUsedRam),
                    ("systemTotalDiskSize", self.systemTotalDiskSize),
                    ("systemAvailableDiskSpace", self.systemAvailableDiskSpace),
                    ("systemUsedDiskSpace", self.systemUsedDiskSpace)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "RAM", memoryDiskDict  )
                time.sleep(.1)    

                # STRING VARS: networkAddressType, networkIpAddress, networkSubnetMask, networkDefaultGateway, networkDns1, networkDns2
                networkInfoDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("networkAddressType", self.networkAddressType),
                    ("networkIpAddress", self.networkIpAddress),
                    ("networkSubnetMask", self.networkSubnetMask),
                    ("networkDefaultGateway", self.networkDefaultGateway),
                    ("networkDns1", self.networkDns1),
                    ("networkDns2", self.networkDns2)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "NTWRK",networkInfoDict )
                time.sleep(.1)    

                # STRING VARS: remoteUpdateControl, remoteUpdateState, remoteUpdateVersion, lastInstrumentUpdateCheck, packageVersionNeedingUpdate
                remoteUpdateDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("remoteUpdateControl", self.remoteUpdateControl),
                    ("remoteUpdateState", self.remoteUpdateState),
                    ("remoteUpdateDownloadPercent", self.remoteUpdateDownloadPercent),
                    ("remoteUpdateVersion", self.remoteUpdateVersion),
                    ("remoteUpdateRequiredDiskSpace", self.remoteUpdateRequiredDiskSpace),
                    ("periodicUpdateCheck", self.periodicUpdateCheck),
                    ("lastInstrumentUpdateCheck", self.lastInstrumentUpdateCheck),
                    ("packageVersionNeedingUpdate", self.packageVersionNeedingUpdate),
                    ("periodicUpdateFlag", self.periodicUpdateFlag),
                    ("sysInfoUpdateAvail", self.sysInfoUpdateAvail),
                    ("configResetFlag", self.configResetFlag),
                    ("sysWarnConfigReset", self.sysWarnConfigReset),
                    ("lowMemoryRestart", self.lowMemoryRestart),
                    ("lowMemoryWarning", self.lowMemoryWarning)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "RMT",remoteUpdateDict)
                time.sleep(.1)    

                # STRING VARS: manualTimeServer, lastInstrumentTimeSynced, nextInstrumentTimeSync
                timeSyncDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("timeSync", self.timeSync),
                    ("timeSyncUseManual", self.timeSyncUseManual),
                    ("manualTimeServer", self.manualTimeServer),
                    ("timeSyncInterval", self.timeSyncInterval),
                    ("lastInstrumentTimeSynced", self.lastInstrumentTimeSynced),
                    ("nextInstrumentTimeSync", self.nextInstrumentTimeSync)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYNC",  timeSyncDict)
                time.sleep(.1)    

                memoryProcessDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("memoryTotal", self.memoryTotal),
                    ("memoryTee", self.memoryTee),
                    ("memoryHmi", self.memoryHmi),
                    ("memoryDl", self.memoryDl),
                    ("memoryAc", self.memoryAc),
                    ("memoryEv", self.memoryEv),
                    ("memoryMb", self.memoryMb),
                    ("memoryDo", self.memoryDo),
                    ("memoryAo", self.memoryAo),
                    ("memoryWeb", self.memoryWeb),
                    ("memoryRu", self.memoryRu),
                    ("memoryCg", self.memoryCg),
                    ("memoryHsn", self.memoryHsn)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MMRY", memoryProcessDict  )
                time.sleep(.1)    

                # STRING VARS: svCom2Protocol, svCom2ModemInitString, svCom2Parity, svCom2HandshakingMode
                comConfigDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("svMachineId", self.svMachineId),
                    ("svCom2Protocol", self.svCom2Protocol),
                    ("svCom2ModemInitString", self.svCom2ModemInitString),
                    ("svCom2Baudrate", self.svCom2Baudrate),
                    ("svCom2Parity", self.svCom2Parity),
                    ("svCom2Databits", self.svCom2Databits),
                    ("svCom2Stopbits", self.svCom2Stopbits),
                    ("svCom2ModemConnection", self.svCom2ModemConnection),
                    ("svCom2EnableQuietMode", self.svCom2EnableQuietMode),
                    ("svCom2EnableSecurity", self.svCom2EnableSecurity),
                    ("svCom2EnableRs485", self.svCom2EnableRs485),
                    ("svCom2HandshakingMode", self.svCom2HandshakingMode),
                    ("svCom2EnableCommandPromptDisplay", self.svCom2EnableCommandPromptDisplay),
                    ("svCom2DisableEchoLineEditing", self.svCom2DisableEchoLineEditing),
                    ("svCom2DisableHardwareErrorChecking", self.svCom2DisableHardwareErrorChecking),
                    ("svCom2EnableHardwareFifo", self.svCom2EnableHardwareFifo),
                    ("svCom2Initialize", self.svCom2Initialize)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "COM",comConfigDict )
                time.sleep(.1)    

                # STRING VARS: hessenVariation, hessenResponseMode, hessenGasName
                hessenConfigDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("hessenVariation", self.hessenVariation),
                    ("hessenResponseMode", self.hessenResponseMode),
                    ("hessenFixedTag", self.hessenFixedTag),
                    ("hessenGasName", self.hessenGasName),
                    ("hessenGasSelect", self.hessenGasSelect)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "HSSN", hessenConfigDict)
                time.sleep(.1)    

                gfcFirmwareDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("gfcFirmwarePartnumber", self.gfcFirmwarePartnumber),
                    ("gfcFirmwareRev", self.gfcFirmwareRev),
                    ("gfcFirmwareBuildNumber", self.gfcFirmwareBuildNumber),
                    ("gfcHardwareRev", self.gfcHardwareRev),
                    ("gfcHardwarePartnumber", self.gfcHardwarePartnumber),
                    ("gfcModuleSerialNumber", self.gfcModuleSerialNumber),
                    ("gfcModuleRuntimeHours", self.gfcModuleRuntimeHours),
                    ("gfcFirmwareVersionMismatch", self.gfcFirmwareVersionMismatch),
                    ("sysWarnGfcFirmwareVersionMismatch", self.sysWarnGfcFirmwareVersionMismatch)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "GFC",gfcFirmwareDict)
                time.sleep(.1)    

                # STRING VARS: homeMeter1, homeMeter2, homeMeter3, boardFamily, boardMeasureLevel, instMode, svUserUnits
                instrumentInfoDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("homeMeter1", self.homeMeter1),
                    ("homeMeter2", self.homeMeter2),
                    ("homeMeter3", self.homeMeter3),
                    ("boardFamily", self.boardFamily),
                    ("boardMeasureLevel", self.boardMeasureLevel),
                    ("instMode", self.instMode),
                    ("sfDiagnosticMode", self.sfDiagnosticMode),
                    ("svUserUnits", self.svUserUnits),
                    ("asfSystemResetWarning", self.asfSystemResetWarning),
                    ("warmUpComplete", self.warmUpComplete)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ININFO", instrumentInfoDict)
                time.sleep(.1)                
                

                calibrationDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("svDarkCalDuration", self.svDarkCalDuration),
                    ("svDarkMeasMv", self.svDarkMeasMv),
                    ("svDarkRefMv", self.svDarkRefMv),
                    ("svNormSpan1", self.svNormSpan1),
                    ("svNormSpan2", self.svNormSpan2),
                    ("svSpanRatio1", self.svSpanRatio1),
                    ("svSpanRatio2", self.svSpanRatio2)
                ]) 
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CLB",calibrationDict)
                time.sleep(.1)    

                analogOutputDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("analogOutputFirmwarePartnumber", self.analogOutputFirmwarePartnumber),
                    ("analogOutputFirmwareRev", self.analogOutputFirmwareRev),
                    ("analogOutputFirmwareBuildNumber", self.analogOutputFirmwareBuildNumber),
                    ("analogOutputHardwareRev", self.analogOutputHardwareRev),
                    ("analogOutputHardwarePartnumber", self.analogOutputHardwarePartnumber),
                    ("analogOutputModuleSerialNumber", self.analogOutputModuleSerialNumber),
                    ("analogOutputModuleRuntimeHours", self.analogOutputModuleRuntimeHours),
                    ("analogOutputFirmwareVersionMismatch", self.analogOutputFirmwareVersionMismatch)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "OAFRM",analogOutputDict)
                time.sleep(.1)    

                warningsDict = OrderedDict([
                    ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("sysOkWarn", self.sysOkWarn),
                    ("wheelTempWarn", self.wheelTempWarn),
                    ("benchTempWarn", self.benchTempWarn),
                    ("sysInvalidConcWarning", self.sysInvalidConcWarning),
                    ("sysWarnSourceWarning", self.sysWarnSourceWarning),
                    ("sysWarnReset", self.sysWarnReset),
                    ("sysWarnSampleFlow", self.sysWarnSampleFlow),
                    ("sysWarnSampleTemp", self.sysWarnSampleTemp),
                    ("sysWarnSamplePressure", self.sysWarnSamplePressure)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "WRN",warningsDict)
                time.sleep(.1)    




            coMeasurementDict = OrderedDict([
                ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                ("coConc", self.coConc),
                ("coStability", self.coStability),
                ("coAdaptiveFilterActive", self.coAdaptiveFilterActive),
                ("coSlope1", self.coSlope1),
                ("coOffset1", self.coOffset1),
                ("coZeroConc1", self.coZeroConc1),
                ("coSpanConc1", self.coSpanConc1),
                ("coPreCalConc1", self.coPreCalConc1),
                ("coTargetZeroConc1", self.coTargetZeroConc1),
                ("coTargetSpanConc1", self.coTargetSpanConc1),
                ("coConc2", self.coConc2),
                ("coSlope2", self.coSlope2),
                ("coOffset2", self.coOffset2),
                ("coZeroConc2", self.coZeroConc2),
                ("coSpanConc2", self.coSpanConc2),
                ("coPreCalConc2", self.coPreCalConc2),
                ("coTargetZeroConc2", self.coTargetZeroConc2),
                ("coTargetSpanConc2", self.coTargetSpanConc2)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CO",coMeasurementDict)
            time.sleep(.1)    

            hiresDict = OrderedDict([
                ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                ("hires00", self.hires00),
                ("hires01", self.hires01),
                ("hires02", self.hires02),
                ("hires03", self.hires03),
                ("hires04", self.hires04),
                ("hires05", self.hires05),
                ("hires06", self.hires06),
                ("hires07", self.hires07),
                ("hires08", self.hires08),
                ("hires09", self.hires09),
                ("hires10", self.hires10),
                ("hires11", self.hires11),
                ("hires12", self.hires12),
                ("hires13", self.hires13),
                ("hires14", self.hires14)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "HIRES",hiresDict)
            time.sleep(.1)    

            boxPressureDict = OrderedDict([
                ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                ("aiBoxTemp", self.aiBoxTemp),
                ("aiAtmosphericPressure", self.aiAtmosphericPressure),
                ("aiSamplePressureShared", self.aiSamplePressureShared),
                ("prigasPrec", self.prigasPrec)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PRSR",boxPressureDict )
            time.sleep(.1)    
            
            maintenanceTempDict = OrderedDict([
                ("dateTime"          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                ("asfMaintenanceModeSoftware", self.asfMaintenanceModeSoftware),
                ("svMaintenanceModeTimeout", self.svMaintenanceModeTimeout),
                ("sysWarnMaintenanceMode", self.sysWarnMaintenanceMode),
                ("aiDetectorTemp", self.aiDetectorTemp),
                ("aiDetectorTempRaw", self.aiDetectorTempRaw),
                ("aiSampleTemp", self.aiSampleTemp),
                ("aiSampleTempRaw", self.aiSampleTempRaw),
                ("aiPhotoTempRaw", self.aiPhotoTempRaw),
                ("aiIrMeasure", self.aiIrMeasure),
                ("aiIrReference", self.aiIrReference),
                ("aiSamplePressure", self.aiSamplePressure),
                ("aiSamplePressureRaw", self.aiSamplePressureRaw)
            ])

            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MNTMP",  maintenanceTempDict  )
            time.sleep(.1)    

        return True