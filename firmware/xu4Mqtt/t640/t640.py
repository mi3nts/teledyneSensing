
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


def decode_float(regs, index):
    raw = (regs[index] << 16) + regs[index + 1]
    return struct.unpack('>f', raw.to_bytes(4, byteorder='big'))[0]


class T640:
    def __init__(self, host: str, port: int = 502, api_port: int = 8180 ,unit_id=1):
        
        
        self.client = ModbusTcpClient(host, port=port)
        if not self.client.connect():
            print(f"Unable to connect to Modbus server at {host}:{port}")
            sys.exit(1)  # Exit the script with a non-zero exit code        
        
        self.unit_id = unit_id
        self.sensorIDPreModbus = "T640MB001"
        
        self.sensorIDPreAPI    = "T640API001"
        self.apiURL            = "http://" + host +":"+ str(api_port) + "/api/taglist"  

        self.discrete_labels = [
            "Box Temperature Warning",
            "Sample Flow Warning",
            "Internal Serial Timeout",
            "System Reset Warning",
            "System OK Warning",
            "Sample Temperature Warning",
            "Bypass Flow Warning",
            "System Fault Warning"
        ]

        self.coil_labels = [
            "Control Relay 36 (Fan or Heater)",
            "Control Relay 37",
            "Control Relay 38",
            "Control Relay 39",
            "Maintenance Mode Enabled"
        ]


        self.input_float_fields = {
            0:  "Pump Tachometer Reading",
            2:  "Total Amplitude Histogram Particle Count",
            4:  "Total Length Distribution Particle Count",
            6:  "PM10 Real-time Concentration",
            8:  "PM2.5 Real-time Concentration",
            10: "PM10-2.5 Real-time Concentration",
            12: "PM10 Standardized Real-time Concentration",
            14: "PM10 1Hr Rolling Avg",
            16: "PM2.5 1Hr Rolling Avg",
            18: "PM10-2.5 1Hr Rolling Avg",
            20: "PM10 12Hr Rolling Avg",
            22: "PM2.5 12Hr Rolling Avg",
            24: "PM10-2.5 12Hr Rolling Avg",
            26: "PM10 24Hr Rolling Avg",
            28: "PM2.5 24Hr Rolling Avg",
            30: "PM10-2.5 24Hr Rolling Avg",
            32: "LED Temperature",
            34: "Ambient Pressure",
            36: "Humidity Sensor Reading",
            38: "Box Temperature",
            40: "Ambient Temperature Probe",
            42: "ASC Tube Jacket Temperature",
            44: "RH Sensor Temperature",
            46: "Sample Flow (5lpm)",
            48: "Bypass Flow (11.67lpm)",
            50: "Total Flow (Sample + Bypass)",
            52: "Signal Length",
            54: "P3 Value",
            56: "Pump Duty Cycle",
            58: "Valve Duty Cycle",
            60: "ASC Heater Duty Cycle",
            62: "PM2.5 Standardized Real-time Concentration",
            64: "PM1 Real-time Concentration",
            66: "PM1 Standardized Real-time Concentration",
            68: "PM1 1Hr Standardized Avg",
            70: "PM2.5 1Hr Standardized Avg",
            72: "PM10 1Hr Standardized Avg",
            74: "PM1 12Hr Standardized Avg",
            76: "PM2.5 12Hr Standardized Avg",
            78: "PM10 12Hr Standardized Avg",
            80: "PM1 24Hr Standardized Avg",
            82: "PM2.5 24Hr Standardized Avg",
            84: "PM10 24Hr Standardized Avg",
            86: "Span Deviation",
            88: "Span Dev Track (48Hr Rolling Avg)",
            90: "PM1 1Hr Rolling Avg",
            92: "PM1 12Hr Rolling Avg",
            94: "PM1 24Hr Rolling Avg",
            96: "PMtot Real-time Concentration",
            98: "PMtot Standardized Real-time Concentration",
            100: "PMtot 1Hr Avg",
            102: "PMtot 1Hr Standardized Avg",
            104: "PMtot 12Hr Avg",
            106: "PMtot 12Hr Standardized Avg",
            108: "PMtot 24Hr Avg",
            110: "PMtot 24Hr Standardized Avg",
            112: "Sample Flow CV (24Hr Avg)",
            114: "Bypass Flow CV (24Hr Avg)",
            116: "Total Flow CV (24Hr Avg)",
            118: "Total Particle Number Concentration"
        }


        self.holding_float_fields = {
            0:  "PMT Output Voltage",
            2:  "PMT Offset Voltage",
            4:  "PMT High Voltage Power Supply (HVPS)",
            6:  "Sample Flow Calibration (5LPM)",
            8:  "Bypass Flow Calibration",
            10: "Pressure Sensor Calibration",
            12: "Relative Humidity (RH) Setpoint",
            14: "Sample Flow Setpoint",
            16: "Bypass Flow Setpoint",
            18: "RH Sensor Calibration Slope",
            20: "PM10 Calibration Slope (KS10)",
            22: "PM2.5 Calibration Slope (KS2.5)",
            24: "PM1 Calibration Slope (KS1)",
            26: "PM10 Calibration Offset (KO10)",
            28: "PM2.5 Calibration Offset (KO2.5)",
            30: "PM1 Calibration Offset (KO1)"
        }


    def read_discrete_inputs(self):
        dateTime  = datetime.now(timezone.utc)
        try:
            result                     = self.client.read_discrete_inputs(0, len(self.discrete_labels), unit=self.unit_id)
            if not result.isError():
                (   self.boxTempWarning,
                    self.sampleFlowWarning,
                    self.internalSerialTimeout,
                    self.systemResetWarning,
                    self.sysOkWarning,
                    self.sampleTemperatureWarning,
                    self.bypassFlowWarning,
                    self.systemFaultWarning
                ) = result.bits
                
                sensorDictionary = OrderedDict([
                    ("dateTime"                , str(dateTime.strftime('%Y-%m-%d %H:%M:%S.%f'))),
                    ("boxTempWarning"           , int(self.boxTempWarning)) ,
                    ("sampleFlowWarning"        , int(self.sampleFlowWarning)),
                    ("internalSerialTimeout"    , int(self.internalSerialTimeout)),
                    ("systemResetWarning"       , int(self.systemResetWarning)),
                    ("sysOkWarning"             , int(self.sysOkWarning)),
                    ("sampleTemperatureWarning" , int(self.sampleTemperatureWarning)),
                    ("bypassFlowWarning"        , int(self.bypassFlowWarning)),
                    ("systemFaultWarning"       , int(self.systemFaultWarning)),
                    ])       
      
                mSR.sensorFinisher(dateTime,self.sensorIDPreModbus+"WRNS",sensorDictionary)
      
                return True, dict(zip(self.discrete_labels, result.bits))
        except ModbusException as e:
            print("[Error] Discrete Inputs:", e)
        return False, None
    
    def read_coils(self):
        dateTime = datetime.now(timezone.utc)
        try:
            result = self.client.read_coils(0, len(self.coil_labels), unit=self.unit_id)
            print(result.bits)
            if not result.isError():
                (
                    self.controlRelay36,
                    self.controlRelay37,
                    self.controlRelay38,
                    self.controlRelay39,
                    self.maintenanceMode
                ) = result.bits[:len(self.coil_labels)] 

                sensorDictionary = OrderedDict([
                    ("dateTime"       , str(dateTime.strftime('%Y-%m-%d %H:%M:%S.%f'))),
                    ("controlRelay36" , int(self.controlRelay36)),
                    ("controlRelay37" , int(self.controlRelay37)),
                    ("controlRelay38" , int(self.controlRelay38)),
                    ("controlRelay39" , int(self.controlRelay39)),
                    ("maintenanceMode", int(self.maintenanceMode)),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "COIL", sensorDictionary)

                return True, dict(zip(self.coil_labels, result.bits))

        except ModbusException as e:
            print("[Error] Coils:", e)

        return False, None


    def read_input_registers(self):
        dateTime = datetime.now(timezone.utc)
        try:
            result = self.client.read_input_registers(0, 120, unit=self.unit_id)
            if not result.isError():
                regs = result.registers
                self.pumpTachometer                 = decode_float(regs, 0)
                self.totalAmpHistParticles          = decode_float(regs, 2)
                self.totalLenDistParticles          = decode_float(regs, 4)
                self.pm10Realtime                   = decode_float(regs, 6)
                self.pm2_5Realtime                  = decode_float(regs, 8)
                self.pm10_2_5Realtime               = decode_float(regs, 10)
                self.pm10StdRealtime                = decode_float(regs, 12)
                self.pm10_1hrRollingAvg             = decode_float(regs, 14)
                self.pm2_5_1hrRollingAvg            = decode_float(regs, 16)
                self.pm10_2_5_1hrRollingAvg         = decode_float(regs, 18)
                self.pm10_12hrRollingAvg            = decode_float(regs, 20)
                self.pm2_5_12hrRollingAvg           = decode_float(regs, 22)
                self.pm10_2_5_12hrRollingAvg        = decode_float(regs, 24)
                self.pm10_24hrRollingAvg            = decode_float(regs, 26)
                self.pm2_5_24hrRollingAvg           = decode_float(regs, 28)
                self.pm10_2_5_24hrRollingAvg        = decode_float(regs, 30)
                self.ledTemp                        = decode_float(regs, 32)
                self.ambientPressure                = decode_float(regs, 34)
                self.humidity                       = decode_float(regs, 36)
                self.boxTemp                        = decode_float(regs, 38)
                self.ambientTemp                    = decode_float(regs, 40)
                self.ascTubeTemp                    = decode_float(regs, 42)
                self.rhSensorTemp                   = decode_float(regs, 44)
                self.sampleFlowMB                   = decode_float(regs, 46)
                self.bypassFlowMB                   = decode_float(regs, 48)
                self.totalFlowMB                    = decode_float(regs, 50)
                self.signalLength                   = decode_float(regs, 52)
                self.p3Value                        = decode_float(regs, 54)
                self.pumpDuty                       = decode_float(regs, 56)
                self.valveDuty                      = decode_float(regs, 58)
                self.ascHeaterDuty                  = decode_float(regs, 60)
                self.pm2_5StdRealtime               = decode_float(regs, 62)
                self.pm1Realtime                    = decode_float(regs, 64)
                self.pm1StdRealtime                 = decode_float(regs, 66)
                self.pm1_1hrStandardizedAvg         = decode_float(regs, 68)
                self.pm2_5_1hrStandardizedAvg       = decode_float(regs, 70)
                self.pm10_1hrStandardizedAvg        = decode_float(regs, 72)
                self.pm1_12hrStandardizedAvg        = decode_float(regs, 74)
                self.pm2_5_12hrStandardizedAvg      = decode_float(regs, 76)
                self.pm10_12hrStandardizedAvg       = decode_float(regs, 78)
                self.pm1_24hrStandardizedAvg        = decode_float(regs, 80)
                self.pm2_5_24hrStandardizedAvg      = decode_float(regs, 82)
                self.pm10_24hrStandardizedAvg       = decode_float(regs, 84)
                self.spanDeviation                  = decode_float(regs, 86)
                self.spanDevTrack                   = decode_float(regs, 88)
                self.pm1_1hrRollingAvg              = decode_float(regs, 90)
                self.pm1_12hrRollingAvg             = decode_float(regs, 92)
                self.pm1_24hrRollingAvg             = decode_float(regs, 94)
                self.pmtotRealtime                  = decode_float(regs, 96)
                self.pmtotStdRealtime               = decode_float(regs, 98)
                self.pmtot_1hrRollingAvg            = decode_float(regs, 100)
                self.pmtot_1hrStandardizedAvg       = decode_float(regs, 102)
                self.pmtot_12hrRollingAvg           = decode_float(regs, 104)
                self.pmtot_12hrStandardizedAvg      = decode_float(regs, 106)
                self.pmtot_24hrRollingAvg           = decode_float(regs, 108)
                self.pmtot_24hrStandardizedAvg      = decode_float(regs, 110)
                self.sampleFlowCV                   = decode_float(regs, 112)
                self.bypassFlowCV                   = decode_float(regs, 114)
                self.totalFlowCV                    = decode_float(regs, 116)
                self.totalParticleConc              = decode_float(regs, 118)

                realtimePmDict                      = OrderedDict([
                    ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1Realtime),
                    ("pm2_5"    , self.pm2_5Realtime),
                    ("pm2_5to10", self.pm10_2_5Realtime),
                    ("pm10"     , self.pm10Realtime),
                    ("pmTotal"  , self.pmtotRealtime)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "RTPM", realtimePmDict )
                time.sleep(.1)

                stdRealtimePmDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1StdRealtime),
                    ("pm2_5"   , self.pm2_5StdRealtime),
                    ("pm10"    , self.pm10StdRealtime),
                    ("pmTotal" , self.pmtotStdRealtime)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "STDRTPM", stdRealtimePmDict  )
                time.sleep(.1)

                pm1hrRollingDict                    = OrderedDict([
                    ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1_1hrRollingAvg),
                    ("pm2_5"    , self.pm2_5_1hrRollingAvg),
                    ("pm2_5to10", self.pm10_2_5_1hrRollingAvg),
                    ("pm10"     , self.pm10_1hrRollingAvg),
                    ("pmTotal"  , self.pmtot_1hrRollingAvg),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R1HPM",  pm1hrRollingDict )
                time.sleep(.1)

                pm12hrRollingDict = OrderedDict([
                    ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1_12hrRollingAvg),
                    ("pm2_5"    , self.pm2_5_12hrRollingAvg),
                    ("pm2_5to10", self.pm10_2_5_12hrRollingAvg),
                    ("pm10"     , self.pm10_12hrRollingAvg),
                    ("pmTotal"  , self.pmtot_12hrRollingAvg),                
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R12HPM",  pm12hrRollingDict )
                time.sleep(.1)

                pm24hrRollingDict = OrderedDict([
                    ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1_24hrRollingAvg),
                    ("pm2_5"    , self.pm2_5_24hrRollingAvg),
                    ("pm2_5to10", self.pm10_2_5_24hrRollingAvg),
                    ("pm10"     , self.pm10_24hrRollingAvg),
                    ("pmTotal"  , self.pmtot_24hrRollingAvg),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R24HPM",  pm24hrRollingDict )
                time.sleep(.1)

                pm1hrStandardizedDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1_1hrStandardizedAvg),
                    ("pm2_5"   , self.pm2_5_1hrStandardizedAvg),
                    ("pm10"    , self.pm10_1hrStandardizedAvg),
                    ("pmTotal" , self.pmtot_1hrStandardizedAvg)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S1HPM",  pm1hrStandardizedDict )
                time.sleep(.1)

                pm12hrStandardizedDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1_12hrStandardizedAvg),
                    ("pm2_5"   , self.pm2_5_12hrStandardizedAvg),
                    ("pm10"    , self.pm10_12hrStandardizedAvg),
                    ("pmTotal" , self.pmtot_12hrStandardizedAvg)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S12HPM",  pm12hrStandardizedDict )
                time.sleep(.1)

                pm24hrStandardizedDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1_24hrStandardizedAvg),
                    ("pm2_5"   , self.pm2_5_24hrStandardizedAvg),
                    ("pm10"    , self.pm10_24hrStandardizedAvg),
                    ("pmTotal" , self.pmtot_24hrStandardizedAvg)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S24HPM",  pm24hrStandardizedDict )
                time.sleep(.1)

                particleHistogramCounts    = OrderedDict([
                    ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("totalAmpHistParticles" , self.totalAmpHistParticles),
                    ("totalLenDistParticles" , self.totalLenDistParticles),
                    ("totalParticleConc"     , self.totalParticleConc)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "PHC",  particleHistogramCounts )
                time.sleep(.1)

                climateDict                          = OrderedDict([
                    ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("ledTemp"            , self.ledTemp),
                    ("pressure"           , self.ambientPressure),
                    ("humidity"           , self.humidity),
                    ("boxTemp"            , self.boxTemp),
                    ("temperature"        , self.ambientTemp),
                    ("ascTubeTemp"        , self.ascTubeTemp),
                    ("rhSensorTemp"       , self.rhSensorTemp)
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "CLM",  climateDict )
                time.sleep(.1)

                pumpAndFlowDict = OrderedDict([
                    ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pumpTachometer"     , self.pumpTachometer),
                    ("sampleFlow"         , self.sampleFlowMB),
                    ("bypassFlow"         , self.bypassFlowMB),
                    ("totalFlow"          , self.totalFlowMB),
                    ("signalLength"       , self.signalLength),
                    ("p3Value"            , self.p3Value),
                    ("pumpDuty"           , self.pumpDuty),
                    ("valveDuty"          , self.valveDuty),
                    ("ascHeaterDuty"      , self.ascHeaterDuty),
                    ("sampleFlowCV"       , self.sampleFlowCV),
                    ("bypassFlowCV"       , self.bypassFlowCV),
                    ("totalFlowCV"        , self.totalFlowCV),
                ])

                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "PV",  pumpAndFlowDict )
                time.sleep(.1)
                
                return True, {
                    self.input_float_fields[i]: decode_float(regs, i)
                    for i in sorted(self.input_float_fields.keys())
                }
        except ModbusException as e:
            print("[Error] Input Registers:", e)

        return False, None            
    
    def read_holding_registers(self):
        dateTime = datetime.now(timezone.utc)
        try:
            result = self.client.read_holding_registers(0, 32, unit=self.unit_id)
            # PMT Voltage                                   0.000
            # PMT Offset                                    0.000
            # PMT HVPS                                      0.000
            # 5LPM Flow Cal                                 0.992
            # Bypass Flow Cal                               1.000
            # Pressure Cal                                  1.008
            # RH Setpoint                                  35.000
            # Sample Flow Setpoint                          5.000
            # Bypass Flow Setpoint                         11.670
            # RH Sensor Slope                               1.000
            # KS10 PM10 Slope                               1.000
            # KS2.5 PM2.5 Slope                             1.000
            # KS1 PM1 Slope                                 1.000
            # KO10 PM10 Offset                              0.000
            # KO2.5 PM2.5 Offset                            0.000
            # KO1 PM1 Offset                                0.000


            if not result.isError():
                regs = result.registers
                self.pmtVoltage                     = decode_float(regs, 0)
                self.pmtOffset                      = decode_float(regs, 2)
                self.pmtHVPS                        = decode_float(regs, 4)
                self.fiveLPMFlowCal                 = decode_float(regs, 6)
                self.bypassFlowCal                  = decode_float(regs, 8)
                self.pressureCal                    = decode_float(regs, 10)
                self.rhSetpoint                     = decode_float(regs, 12)
                self.sampleFlowSetpoint             = decode_float(regs, 14)
                self.bypassFlowSetpoint             = decode_float(regs, 16)
                self.rhSensorSlope                  = decode_float(regs, 18)
                self.ks10PM10Slope                  = decode_float(regs, 20)
                self.ks2_5PM2_5Slope                = decode_float(regs, 22)
                self.ks1PM1Slope                    = decode_float(regs, 24)
                self.ko10PM10Offset                 = decode_float(regs, 26)
                self.ko2_5PM2_5Offset               = decode_float(regs, 28)
                self.ko1PM1Offset                   = decode_float(regs, 30)
                
                calibrationDict              = OrderedDict([
                    ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pmtVoltage"            , self.pmtVoltage),
                    ("pmtOffset"             , self.pmtOffset),
                    ("pmtHVPS"               , self.pmtHVPS),
                    ("fiveLPMFlowCal"        , self.fiveLPMFlowCal),
                    ("bypassFlowCal"         , self.bypassFlowCal),
                    ("pressureCal"           , self.pressureCal),
                    ("rhSetpoint"            , self.rhSetpoint),
                    ("sampleFlowSetpoint"    , self.sampleFlowSetpoint),
                    ("bypassFlowSetpoint"    , self.bypassFlowSetpoint),
                    ("rhSensorSlope"         , self.rhSensorSlope),
                    ("ks10PM10Slope"         , self.ks10PM10Slope),
                    ("ks2_5PM2_5Slope"       , self.ks2_5PM2_5Slope),
                    ("ks1PM1Slope"           , self.ks1PM1Slope),
                    ("ko10PM10Offset"        , self.ko10PM10Offset),
                    ("ko2_5PM2_5Offset"      , self.ko2_5PM2_5Offset),
                    ("ko1PM1Offset"          , self.ko1PM1Offset)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "CALV", calibrationDict )
                time.sleep(.1)                

                return True, {
                    self.holding_float_fields[i]: decode_float(regs, i)
                    for i in sorted(self.holding_float_fields.keys())
                }
        except ModbusException as e:
            print("[Error] Input Registers:", e)

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


    def read_api(self):

        response = requests.get(self.apiURL)
        if response.status_code == 200:
            data = response.json()
            for tag in data.get("tags", []):
                name = tag.get("name", "")
                raw_value = tag.get("value", "")
                camel_name = self._to_camel_case(name)

                # Skip tags that start with digits (e.g., '1MIN-DATA')
                if name and name[0].isdigit():
                    continue

                # Special case for opcDustHistogram
                if camel_name == "opcDustHistogram":
                    if isinstance(raw_value, str):
                        try:
                            values = [int(float(v.strip())) for v in raw_value.split(',')]
                            for i, val in enumerate(values):
                                bin_name = f"bin{i:03d}"
                                setattr(self, bin_name, val)
                                # print(f"self.{bin_name} = {val}")
                        except Exception as e:
                            print(f"Failed to parse histogram: {e}")
                    continue  # Skip setting opcDustHistogram as a string
                            
                # Normalize the value (convert strings "True"/"False" to 1/0, etc.)
                normalized_value = self._normalize_value(raw_value)

                # Save to camelCase class attribute
                try:
                    setattr(self, camel_name, normalized_value)
                    # print(f"self.{camel_name} = {repr(normalized_value)}")
                except Exception as e:
                    print(f"[Warning] Failed to set attribute '{camel_name}': {e}")
            
            
            # At this point, the data is attached to sensors 
            dateTime  = datetime.now(timezone.utc)

            realtimePmDict                      = OrderedDict([
                ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"      , self.pm1Conc),
                ("pm2_5"    , self.pm25Conc),
                ("pm2_5to10", self.pmcConc),
                ("pm10"     , self.pm10Conc),
                ("pmTotal"  , self.pmtotConc)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "RTPM", realtimePmDict )
            time.sleep(.1)    

            stdRealtimePmDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stpConc),
                ("pm2_5"   , self.pm25stpConc),
                ("pm10"    , self.pm10stpConc),
                ("pmTotal" , self.pmtotstpConc)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "STDRTPM", stdRealtimePmDict  )
            time.sleep(.1)    

            pm1hrRollingDict                    = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"      , self.pm11hrAvg),
                ("pm2_5"    , self.pm251hrAvg),
                ("pm2_5to10", self.pmc1hrAvg ),
                ("pm10"     , self.pm101hrAvg),
                ("pmTotal"  , self.pmtot1hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "R1HPM",  pm1hrRollingDict )
            time.sleep(.1)    

            pm12hrRollingDict = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"      , self.pm112hrAvg),
                ("pm2_5"    , self.pm2512hrAvg),
                ("pm2_5to10", self.pmc12hrAvg ),
                ("pm10"     , self.pm1012hrAvg),
                ("pmTotal"  , self.pmtot12hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "R12HPM",  pm12hrRollingDict )
            time.sleep(.1)    

            pm24hrRollingDict = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"      , self.pm124hrAvg),
                ("pm2_5"    , self.pm2524hrAvg),
                ("pm2_5to10", self.pmc24hrAvg ),
                ("pm10"     , self.pm1024hrAvg),
                ("pmTotal"  , self.pmtot24hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "R24HPM",  pm24hrRollingDict )
            time.sleep(.1)    


            pm1hrStandardizedDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stp1hrAvg),
                ("pm2_5"   , self.pm25stp1hrAvg),
                ("pm10"    , self.pm10stp1hrAvg),
                ("pmTotal" , self.pmtotstp1hrAvg)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "S1HPM",  pm1hrStandardizedDict )
            time.sleep(.1)    

            pm12hrStandardizedDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stp12hrAvg),
                ("pm2_5"   , self.pm25stp12hrAvg),
                ("pm10"    , self.pm10stp12hrAvg),
                ("pmTotal" , self.pmtotstp12hrAvg)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "S12HPM",  pm12hrStandardizedDict )
            time.sleep(.1)    

            pm24hrStandardizedDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stp24hrAvg),
                ("pm2_5"   , self.pm25stp24hrAvg),
                ("pm10"    , self.pm10stp24hrAvg),
                ("pmTotal" , self.pmtotstp24hrAvg)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "S24HPM",  pm24hrStandardizedDict )
            time.sleep(.1)    

            particleHistogramCounts    = OrderedDict([
                ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("totalAmpHistParticles" , self.opcRtAmplitudeCounts),
                ("totalLenDistParticles" , self.opcRtLengthCounts),
                ("totalParticleConc"     , self.numConc)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PHC",  particleHistogramCounts )
            time.sleep(.1)    


            climateDict                          = OrderedDict([
                ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("ledTemp"            , self.opcRtLedTemp),
                ("pressure"           , self.aiSamplePressureUnits),
                ("humidity"           , self.opcRtHumidity),
                ("boxTemp"            , self.opcRtBoxTemp),
                ("temperature"        , self.opcRtOutsideTemp),
                ("rhSensorTemp"       , self.opcRtSampTemp)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CLMA",  climateDict )
            time.sleep(.1)                
            
            # ASC Temperature is not given on the API 

            pumpAndFlowDict = OrderedDict([
                ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pumpTachometer"     , self.opcRtPumpSpeed),
                ("sampleFlow5"        , self.aiSampleFlow5),             
                ("bypassFlow"         , self.aiSampleFlow11),  
                ("totalFlow"          , self.totalFlow),
                ("signalLength"       , self.opcRtSlValue),
                ("p3Value"            , self.opcSvP3Value),
                ("pumpDuty"           , self.opcRtPwmPump),
                ("valveDuty"          , self.opcRtPwmValve),
                ("ascHeaterDuty"      , self.opcRtHeaterDuty),
                ("sampleFlowCV"       , self.flow5Cv24hrAvg),
                ("bypassFlowCV"       , self.flow11Cv24hrAvg),
                ("totalFlowCV"        , self.flowtotCv24hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PV",  pumpAndFlowDict )
            time.sleep(.1)                

            binDict = OrderedDict([
                ("bin000", self.bin000), ("bin001", self.bin001), ("bin002", self.bin002), ("bin003", self.bin003), ("bin004", self.bin004),
                ("bin005", self.bin005), ("bin006", self.bin006), ("bin007", self.bin007), ("bin008", self.bin008), ("bin009", self.bin009),
                ("bin010", self.bin010), ("bin011", self.bin011), ("bin012", self.bin012), ("bin013", self.bin013), ("bin014", self.bin014),
                ("bin015", self.bin015), ("bin016", self.bin016), ("bin017", self.bin017), ("bin018", self.bin018), ("bin019", self.bin019),
                ("bin020", self.bin020), ("bin021", self.bin021), ("bin022", self.bin022), ("bin023", self.bin023), ("bin024", self.bin024),
                ("bin025", self.bin025), ("bin026", self.bin026), ("bin027", self.bin027), ("bin028", self.bin028), ("bin029", self.bin029),
                ("bin030", self.bin030), ("bin031", self.bin031), ("bin032", self.bin032), ("bin033", self.bin033), ("bin034", self.bin034),
                ("bin035", self.bin035), ("bin036", self.bin036), ("bin037", self.bin037), ("bin038", self.bin038), ("bin039", self.bin039),
                ("bin040", self.bin040), ("bin041", self.bin041), ("bin042", self.bin042), ("bin043", self.bin043), ("bin044", self.bin044),
                ("bin045", self.bin045), ("bin046", self.bin046), ("bin047", self.bin047), ("bin048", self.bin048), ("bin049", self.bin049),
                ("bin050", self.bin050), ("bin051", self.bin051), ("bin052", self.bin052), ("bin053", self.bin053), ("bin054", self.bin054),
                ("bin055", self.bin055), ("bin056", self.bin056), ("bin057", self.bin057), ("bin058", self.bin058), ("bin059", self.bin059),
                ("bin060", self.bin060), ("bin061", self.bin061), ("bin062", self.bin062), ("bin063", self.bin063), ("bin064", self.bin064),
                ("bin065", self.bin065), ("bin066", self.bin066), ("bin067", self.bin067), ("bin068", self.bin068), ("bin069", self.bin069),
                ("bin070", self.bin070), ("bin071", self.bin071), ("bin072", self.bin072), ("bin073", self.bin073), ("bin074", self.bin074),
                ("bin075", self.bin075), ("bin076", self.bin076), ("bin077", self.bin077), ("bin078", self.bin078), ("bin079", self.bin079),
                ("bin080", self.bin080), ("bin081", self.bin081), ("bin082", self.bin082), ("bin083", self.bin083), ("bin084", self.bin084),
                ("bin085", self.bin085), ("bin086", self.bin086), ("bin087", self.bin087), ("bin088", self.bin088), ("bin089", self.bin089),
                ("bin090", self.bin090), ("bin091", self.bin091), ("bin092", self.bin092), ("bin093", self.bin093), ("bin094", self.bin094),
                ("bin095", self.bin095), ("bin096", self.bin096), ("bin097", self.bin097), ("bin098", self.bin098), ("bin099", self.bin099),
                ("bin100", self.bin100), ("bin101", self.bin101), ("bin102", self.bin102), ("bin103", self.bin103), ("bin104", self.bin104),
                ("bin105", self.bin105), ("bin106", self.bin106), ("bin107", self.bin107), ("bin108", self.bin108), ("bin109", self.bin109),
                ("bin110", self.bin110), ("bin111", self.bin111), ("bin112", self.bin112), ("bin113", self.bin113), ("bin114", self.bin114),
                ("bin115", self.bin115), ("bin116", self.bin116), ("bin117", self.bin117), ("bin118", self.bin118), ("bin119", self.bin119),
                ("bin120", self.bin120), ("bin121", self.bin121), ("bin122", self.bin122), ("bin123", self.bin123), ("bin124", self.bin124),
                ("bin125", self.bin125), ("bin126", self.bin126), ("bin127", self.bin127), ("bin128", self.bin128), ("bin129", self.bin129),
                ("bin130", self.bin130), ("bin131", self.bin131), ("bin132", self.bin132), ("bin133", self.bin133), ("bin134", self.bin134),
                ("bin135", self.bin135), ("bin136", self.bin136), ("bin137", self.bin137), ("bin138", self.bin138), ("bin139", self.bin139),
                ("bin140", self.bin140), ("bin141", self.bin141), ("bin142", self.bin142), ("bin143", self.bin143), ("bin144", self.bin144),
                ("bin145", self.bin145), ("bin146", self.bin146), ("bin147", self.bin147), ("bin148", self.bin148), ("bin149", self.bin149),
                ("bin150", self.bin150), ("bin151", self.bin151), ("bin152", self.bin152), ("bin153", self.bin153), ("bin154", self.bin154),
                ("bin155", self.bin155), ("bin156", self.bin156), ("bin157", self.bin157), ("bin158", self.bin158), ("bin159", self.bin159),
                ("bin160", self.bin160), ("bin161", self.bin161), ("bin162", self.bin162), ("bin163", self.bin163), ("bin164", self.bin164),
                ("bin165", self.bin165), ("bin166", self.bin166), ("bin167", self.bin167), ("bin168", self.bin168), ("bin169", self.bin169),
                ("bin170", self.bin170), ("bin171", self.bin171), ("bin172", self.bin172), ("bin173", self.bin173), ("bin174", self.bin174),
                ("bin175", self.bin175), ("bin176", self.bin176), ("bin177", self.bin177), ("bin178", self.bin178), ("bin179", self.bin179),
                ("bin180", self.bin180), ("bin181", self.bin181), ("bin182", self.bin182), ("bin183", self.bin183), ("bin184", self.bin184),
                ("bin185", self.bin185), ("bin186", self.bin186), ("bin187", self.bin187), ("bin188", self.bin188), ("bin189", self.bin189),
                ("bin190", self.bin190), ("bin191", self.bin191), ("bin192", self.bin192), ("bin193", self.bin193), ("bin194", self.bin194),
                ("bin195", self.bin195), ("bin196", self.bin196), ("bin197", self.bin197), ("bin198", self.bin198), ("bin199", self.bin199),
                ("bin200", self.bin200), ("bin201", self.bin201), ("bin202", self.bin202), ("bin203", self.bin203), ("bin204", self.bin204),
                ("bin205", self.bin205), ("bin206", self.bin206), ("bin207", self.bin207), ("bin208", self.bin208), ("bin209", self.bin209),
                ("bin210", self.bin210), ("bin211", self.bin211), ("bin212", self.bin212), ("bin213", self.bin213), ("bin214", self.bin214),
                ("bin215", self.bin215), ("bin216", self.bin216), ("bin217", self.bin217), ("bin218", self.bin218), ("bin219", self.bin219),
                ("bin220", self.bin220), ("bin221", self.bin221), ("bin222", self.bin222), ("bin223", self.bin223), ("bin224", self.bin224),
                ("bin225", self.bin225), ("bin226", self.bin226), ("bin227", self.bin227), ("bin228", self.bin228), ("bin229", self.bin229),
                ("bin230", self.bin230), ("bin231", self.bin231), ("bin232", self.bin232), ("bin233", self.bin233), ("bin234", self.bin234),
                ("bin235", self.bin235), ("bin236", self.bin236), ("bin237", self.bin237), ("bin238", self.bin238), ("bin239", self.bin239),
                ("bin240", self.bin240), ("bin241", self.bin241), ("bin242", self.bin242), ("bin243", self.bin243), ("bin244", self.bin244),
                ("bin245", self.bin245), ("bin246", self.bin246), ("bin247", self.bin247), ("bin248", self.bin248), ("bin249", self.bin249),
                ("bin250", self.bin250), ("bin251", self.bin251), ("bin252", self.bin252), ("bin253", self.bin253), ("bin254", self.bin254),
                ("bin255", self.bin255),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "HIST",binDict)
            time.sleep(.1)    
            ## Pick out the strings 
            # 'svCom1Protocol',
            # 'svCom1ModemInitString',
            # 'svCom1Parity',
            svcom1Config = OrderedDict([
                ("dateTime"               , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("svCom1Protocol"         , self.svCom1Protocol),
                ("svCom1ModemInitString"  , self.svCom1ModemInitString),
                ("svCom1Baudrate"         , self.svCom1Baudrate),
                ("svCom1Parity"           , self.svCom1Parity),
                ("svCom1Databits"         , self.svCom1Databits),
                ("svCom1Stopbits"         , self.svCom1Stopbits),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVCOM1",svcom1Config )
            time.sleep(.1)    

            ## Pick out the strings 
            # 'svCom2Protocol',
            # 'svCom2ModemInitString',
            # 'svCom2Parity',
            # 'svCom2HandshakingMode',
            svcom2Config = OrderedDict([
            ("dateTime"                                , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
            ("svCom2Protocol"                          , self.svCom2Protocol),
            ("svCom2ModemInitString"                   , self.svCom2ModemInitString),
            ("svCom2Baudrate"                          , self.svCom2Baudrate),
            ("svCom2Parity"                            , self.svCom2Parity),
            ("svCom2Databits"                          , self.svCom2Databits),
            ("svCom2Stopbits"                          , self.svCom2Stopbits),
            ("svCom2ModemConnection"                   , self.svCom2ModemConnection),
            ("svCom2EnableQuietMode"                   , self.svCom2EnableQuietMode),
            ("svCom2EnableSecurity"                    , self.svCom2EnableSecurity),
            ("svCom2EnableMultidrop"                   , self.svCom2EnableMultidrop),
            ("svCom2EnableRs485"                       , self.svCom2EnableRs485),
            ("svCom2HandshakingMode"                   , self.svCom2HandshakingMode),
            ("svCom2EnableCommandPromptDisplay"        , self.svCom2EnableCommandPromptDisplay),
            ("svCom2DisableEchoLineEditing"            , self.svCom2DisableEchoLineEditing),
            ("svCom2DisableHardwareErrorChecking"      , self.svCom2DisableHardwareErrorChecking),
            ("svCom2EnableHardwareFifo"                , self.svCom2EnableHardwareFifo),
            ("svCom2Initialize"                        , self.svCom2Initialize),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVCOM2",svcom2Config )
            time.sleep(.1)    

            svtcpConfig = OrderedDict([
                ("dateTime"                           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("svTcp1Initialize"                   , self.svTcp1Initialize),
                ("svTcp1Portnum"                      , self.svTcp1Portnum),
                ("svTcp1EnableSecurity"               , self.svTcp1EnableSecurity),
                ("svTcp1EnableCommandPromptDisplay"   , self.svTcp1EnableCommandPromptDisplay),
                ("svTcp2Initialize"                   , self.svTcp2Initialize),
                ("svTcp2Portnum"                      , self.svTcp2Portnum),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVTCP",svtcpConfig )


            svpmConfig = OrderedDict([
                ("dateTime"         , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("svPm10Disp"       , self.svPm10Disp),
                ("svPmcDisp"        , self.svPmcDisp),
                ("svPm10stpDisp"    , self.svPm10stpDisp),
                ("svPm25stpDisp"    , self.svPm25stpDisp),
                ("svPm1stpDisp"     , self.svPm1stpDisp),
                ("svPmtotstpDisp"   , self.svPmtotstpDisp),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVPM",svpmConfig)
            time.sleep(.1)    

            # # SVINFO
            # 'svLanguageSelect',
            # 'svClockFormat',
            # 'svUserPressureUnits',
            svinfoConfig = OrderedDict([
                ("dateTime"                          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("svClockSpeedAdjust"                , self.svClockSpeedAdjust),
                ("svLanguageSelect"                  , self.svLanguageSelect),
                ("asfMaintenanceModeSoftware"        , self.asfMaintenanceModeSoftware),
                ("sysWarnMaintenanceMode"            , self.sysWarnMaintenanceMode),
                ("svLatchWarning"                    , self.svLatchWarning),
                ("svSerialNumber"                    , self.svSerialNumber),
                ("svClockFormat"                     , self.svClockFormat),
                ("svSystemServiceInterval"           , self.svSystemServiceInterval),
                ("svSystemTotalHours"                , self.svSystemTotalHours),
                ("svSystemTimeSinceLastInterval"     , self.svSystemTimeSinceLastInterval),
                ("svSystemServicePeriodClear"        , self.svSystemServicePeriodClear),
                ("svDaylightSavingsEnable"           , self.svDaylightSavingsEnable),
                ("svMachineId"                       , self.svMachineId),
                ("svDasHoldOff"                      , self.svDasHoldOff),
                ("svUserPressureUnits"               , self.svUserPressureUnits),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVINFO",svinfoConfig)
            time.sleep(.1)    

            ramConfig = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("systemTotalRam"             , self.systemTotalRam),
                ("systemFreeRam"              , self.systemFreeRam),
                ("systemUsedRam"              , self.systemUsedRam),
                ("systemTotalDiskSize"        , self.systemTotalDiskSize),
                ("systemAvailableDiskSpace"   , self.systemAvailableDiskSpace),
                ("systemUsedDiskSpace"        , self.systemUsedDiskSpace),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "RAM",ramConfig)
            time.sleep(.1)    
            # # NET
            # 'networkAddressType',
            # 'networkIpAddress',
            # 'networkSubnetMask',
            # 'networkDefaultGateway',
            # 'networkDns1',
            # 'networkDns2',
            netConfig = OrderedDict([
                ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("networkAddressType"    , self.networkAddressType),
                ("networkIpAddress"      , self.networkIpAddress),
                ("networkSubnetMask"     , self.networkSubnetMask),
                ("networkDefaultGateway" , self.networkDefaultGateway),
                ("networkDns1"           , self.networkDns1),
                ("networkDns2"           , self.networkDns2),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "NET",netConfig)
            time.sleep(.1)    
            # # FRM
            # 'firmwareUpdateState',
            # 'firmwareUpdateResult',
            # 'firmwareUpdateErrorDetails',
            # 'configDownloadUploadState',
            # 'configDownloadUploadResult',
            # 'configDownloadUploadErrorDetails',
            firmwareConfig = OrderedDict([
                ("dateTime"                            , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("refreshInstrumentSettings"           , self.refreshInstrumentSettings),
                ("firmwareUpdateState"                 , self.firmwareUpdateState),
                ("firmwareUpdateResult"                , self.firmwareUpdateResult),
                ("firmwareUpdateProgressPercent"       , self.firmwareUpdateProgressPercent),
                ("firmwareUpdateErrorDetails"          , self.firmwareUpdateErrorDetails),
                ("configDownloadUploadState"           , self.configDownloadUploadState),
                ("configDownloadUploadResult"          , self.configDownloadUploadResult),
                ("configDownloadUploadProgressPercent" , self.configDownloadUploadProgressPercent),
                ("configDownloadUploadErrorDetails"    , self.configDownloadUploadErrorDetails),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "FRM",firmwareConfig)
            time.sleep(.1)    
            # # RMT
            # 'remoteUpdateControl',
            # 'remoteUpdateState',
            # 'remoteUpdateVersion',
            rmtConfig = OrderedDict([
                ("dateTime"                     , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("remoteUpdateControl"          , self.remoteUpdateControl),
                ("remoteUpdateState"            , self.remoteUpdateState),
                ("remoteUpdateDownloadPercent"  , self.remoteUpdateDownloadPercent),
                ("remoteUpdateVersion"          , self.remoteUpdateVersion),
                ("remoteUpdateRequiredDiskSpace", self.remoteUpdateRequiredDiskSpace),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "RMT",rmtConfig)
            time.sleep(.1)    
            # # DNH
            # 'dustCalControl',
            # 'dustCalState',
            # 'homeMeter1',
            # 'homeMeter2',
            # 'homeMeter3',
            dustCalConfig = OrderedDict([
                ("dateTime"        , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("dustCalControl"  , self.dustCalControl),
                ("dustCalState"    , self.dustCalState),
                ("homeMeter1"      , self.homeMeter1),
                ("homeMeter2"      , self.homeMeter2),
                ("homeMeter3"      , self.homeMeter3),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DNH",dustCalConfig)
            time.sleep(.1)    
            # # SLK
            # 'leakCheckControl',
            # 'leakCheckState',
            leakCheckConfig = OrderedDict([
                ("dateTime"            , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("spanDev48hrAvg"      , self.spanDev48hrAvg),
                ("leakcheckpm10Conc"   , self.leakcheckpm10Conc),
                ("leakcheckpm25Conc"   , self.leakcheckpm25Conc),
                ("leakCheckControl"    , self.leakCheckControl),
                ("leakCheckState"      , self.leakCheckState),
                ("ks10"                , self.ks10),
                ("ks25"                , self.ks25),
                ("ks1"                 , self.ks1),
                ("kstot"               , self.kstot),
                ("ko10"                , self.ko10),
                ("ko25"                , self.ko25),
                ("ko1"                 , self.ko1),
                ("kotot"               , self.kotot),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SLK",leakCheckConfig)
            time.sleep(.1)    

            opcSettingsConfig = OrderedDict([
                ("dateTime"                    , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("opcSvOffsetAdjDelay"         , self.opcSvOffsetAdjDelay),
                ("opcSvPmtHvSetting"           , self.opcSvPmtHvSetting),
                ("opcSvPmtHvOffsetAdj"         , self.opcSvPmtHvOffsetAdj),
                ("opcSvBcFiltSize"             , self.opcSvBcFiltSize),
                ("opcSvAcquisitionDuration"    , self.opcSvAcquisitionDuration),
                ("opcSvFlow5lpmOffset"         , self.opcSvFlow5lpmOffset),
                ("opcSvFlow5lpmSlope"          , self.opcSvFlow5lpmSlope),
                ("opcSvFlow1167lpmOffset"      , self.opcSvFlow1167lpmOffset),
                ("opcSvFlow1167lpmSlope"       , self.opcSvFlow1167lpmSlope),
                ("opcSvAmbPressSlope"          , self.opcSvAmbPressSlope),
                ("opcSvRhControlSetpoint"      , self.opcSvRhControlSetpoint),
                ("opcSv5lFlowSetpoint"         , self.opcSv5lFlowSetpoint),
                ("opcSv11lFlowSetpoint"        , self.opcSv11lFlowSetpoint),
                ("opcSvAmbPressOffset"         , self.opcSvAmbPressOffset),
                ("opcSvRhSlope"                , self.opcSvRhSlope),
                ("opcSvRhOffset"               , self.opcSvRhOffset),
                ("opcSvFanSetpoint"            , self.opcSvFanSetpoint),
                ("opcSvInstrumentSlope"        , self.opcSvInstrumentSlope),
                ("opcSvOffsetCounts"           , self.opcSvOffsetCounts),
                ("opcSvAutoAdjustEnable"       , self.opcSvAutoAdjustEnable),
                ("opcSvPmtCalSetting"          , self.opcSvPmtCalSetting),
                ("opcSvLogInterval"            , self.opcSvLogInterval),
                ("opcSvTempCompSlope"          , self.opcSvTempCompSlope),
                ("opcSvDustCalFiltSize"        , self.opcSvDustCalFiltSize),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "OPCSV",opcSettingsConfig)
            time.sleep(.1)    
            #    # OPC
            #     'opcSensorStatus',
            #     'opcSensorMode',
            #     'opcHeaterStatus',
            #     'opcPumpControl',
            #     'opcValveControl',
            #     'opcUsbStorageState',
            #     'opcSensorState',
            #     'opcSensorFirmwareRev',
            #     'opcSyslogFilesize',
            #     'opcInstWarnMessage',
            #     'opcInstErrorMessage',
            opcStatusConfig = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("opcSpanDeviation"          , self.opcSpanDeviation),
                ("opcPm10stpTemp"            , self.opcPm10stpTemp),
                ("opcPm10stpPressure"        , self.opcPm10stpPressure),
                ("opcRtP3Calc"               , self.opcRtP3Calc),
                ("opcSensorStatus"           , self.opcSensorStatus),
                ("opcSensorMode"             , self.opcSensorMode),
                ("opcAmbientTempOverride"    , self.opcAmbientTempOverride),
                ("opcHeaterStatus"           , self.opcHeaterStatus),
                ("opcBoardFirmwareRev"       , self.opcBoardFirmwareRev),
                ("opcHeaterControlEnable"    , self.opcHeaterControlEnable),
                ("opcPumpControl"            , self.opcPumpControl),
                ("opcValveControl"           , self.opcValveControl),
                ("opcRtHeaterDuty"           , self.opcRtHeaterDuty),
                ("opcRtPumpSpeed"            , self.opcRtPumpSpeed),
                ("opcUsbStorageState"        , self.opcUsbStorageState),
                ("opcSensorState"            , self.opcSensorState),
                ("opcZeroChannel"            , self.opcZeroChannel),
                ("opcFastHistUpdate"         , self.opcFastHistUpdate),
                ("opcSensorFirmwareRev"      , self.opcSensorFirmwareRev),
                ("opcSyslogFilesize"         , self.opcSyslogFilesize),
                ("opcDeleteSyslog"           , self.opcDeleteSyslog),
                ("opcLengthPeakChannel"      , self.opcLengthPeakChannel),
                ("opcInstrumentWarning"      , self.opcInstrumentWarning),
                ("opcInstrumentError"        , self.opcInstrumentError),
                ("opcInstWarnMessage"        , self.opcInstWarnMessage),
                ("opcInstErrorMessage"       , self.opcInstErrorMessage),
                ("opcCalPeakChannel"         , self.opcCalPeakChannel),
                ("opcSystemFault"            , self.opcSystemFault),
                ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "OPC",opcStatusConfig)
            time.sleep(.1)    

            # # FLOW
            # 'flow5CalControl',
            # 'flow5CalState',
            # 'flow11CalControl',
            # 'flow11CalState',
            flowDiagnosticsConfig = OrderedDict([
                ("dateTime"                    , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("aiSampleFlow5"              , self.aiSampleFlow5),
                ("flow5CalActualFlowValue"    , self.flow5CalActualFlowValue),
                ("aiSampleFlow11"             , self.aiSampleFlow11),
                ("flow11CalActualFlowValue"   , self.flow11CalActualFlowValue),
                ("flow5CalControl"            , self.flow5CalControl),
                ("flow5CalState"              , self.flow5CalState),
                ("flow11CalControl"           , self.flow11CalControl),
                ("flow11CalState"             , self.flow11CalState),
                ("sensorCheckChannelCounts"   , self.sensorCheckChannelCounts),
                ("sampleFlowWarn"             , self.sampleFlowWarn),
                ("bypassFlowWarn"             , self.bypassFlowWarn),
                ("sampFlowSlopeOor"           , self.sampFlowSlopeOor),
                ("bypsFlowSlopeOor"           , self.bypsFlowSlopeOor),
                ("flow5Cv24hrAvg"             , self.flow5Cv24hrAvg),
                ("flow11Cv24hrAvg"            , self.flow11Cv24hrAvg),
                ("flowtotCv24hrAvg"           , self.flowtotCv24hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "FLOW",flowDiagnosticsConfig)
            time.sleep(.1)    
            # # DUST
            # 'dustCalStartTime',
            # 'dustCalEndTime',
            # 'dustCalActiveTime',
            dustCalConfigEnhanced = OrderedDict([
                ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("dustCalEnhancedLog"    , self.dustCalEnhancedLog),
                ("dustCalOverride"       , self.dustCalOverride),
                ("dustCalStartTime"      , self.dustCalStartTime),
                ("dustCalEndTime"        , self.dustCalEndTime),
                ("dustCalActiveTime"     , self.dustCalActiveTime),
                ("dustCalActiveIndex"    , self.dustCalActiveIndex),
                ("dustCalDwellTime"      , self.dustCalDwellTime),
                ("dustCalMinPeakCounts"  , self.dustCalMinPeakCounts),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DUST", dustCalConfigEnhanced)
            time.sleep(.1)    

            # # DL
            # 'dlTimeFormat',
            # 'dlLastDownloadTime',
            # 'dlDasDownloadFrom',
            # 'dlDasDownloadT1',
            # 'dlDasDownloadT2',
            # 'dlFlush',
            # 'dlLastFlushed',
            downloadConfig = OrderedDict([
                ("dateTime"               , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("dlIncludeUniversalTime" , self.dlIncludeUniversalTime),
                ("dlTimeFormat"           , self.dlTimeFormat),
                ("dlRepoChanged"          , self.dlRepoChanged),
                ("dlLastDownloadTime"     , self.dlLastDownloadTime),
                ("dlDasDownloadFrom"      , self.dlDasDownloadFrom),
                ("dlDasDownloadT1"        , self.dlDasDownloadT1),
                ("dlDasDownloadT2"        , self.dlDasDownloadT2),
                ("dlFlush"                , self.dlFlush),
                ("dlLastFlushed"          , self.dlLastFlushed),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DL", downloadConfig)
            time.sleep(.1)    

            memoryConfig = OrderedDict([
                ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("lowMemoryRestart"   , self.lowMemoryRestart),
                ("lowMemoryWarning"   , self.lowMemoryWarning),
                ("memoryTotal"        , self.memoryTotal),
                ("memoryTee"          , self.memoryTee),
                ("memoryHmi"          , self.memoryHmi),
                ("memoryDl"           , self.memoryDl),
                ("memoryAc"           , self.memoryAc),
                ("memoryEv"           , self.memoryEv),
                ("memoryMb"           , self.memoryMb),
                ("memoryWeb"          , self.memoryWeb),
                ("memoryRu"           , self.memoryRu),
                ("memoryOpc"          , self.memoryOpc),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MMRY", memoryConfig)
            time.sleep(.1)    
            # # TAG
            # 'tagsFlushControl',
            # 'tagsFlushState',
            # 'tagsFlushTimestamp',
            tagConfig = OrderedDict([
                ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("tagEventSystem"     , self.tagEventSystem),
                ("tagEventTee"        , self.tagEventTee),
                ("tagEventHmi"        , self.tagEventHmi),
                ("tagEventDl"         , self.tagEventDl),
                ("tagEventEv"         , self.tagEventEv),
                ("tagEventMb"         , self.tagEventMb),
                ("tagEventWeb"        , self.tagEventWeb),
                ("tagEventRu"         , self.tagEventRu),
                ("tagEventOpc"        , self.tagEventOpc),
                ("tagsFlushControl"   , self.tagsFlushControl),
                ("tagsFlushState"     , self.tagsFlushState),
                ("tagsFlushTimestamp" , self.tagsFlushTimestamp),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "TAG", tagConfig)
            time.sleep(.1)    

            checkConfig = OrderedDict([
                ("dateTime"       , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("checkLed"       , self.checkLed),
                ("checkPmt"       , self.checkPmt),
                ("checkIntPump"   , self.checkIntPump),
                ("checkExtPump"   , self.checkExtPump),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CHCK", checkConfig)
            time.sleep(.1)    

            # # LINF
            # 'instMode',
            linfConfig = OrderedDict([
                ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("instMode"           , self.instMode),
                ("sampleTempWarn"     , self.sampleTempWarn),
                ("boxTempWarn"        , self.boxTempWarn),
                ("sampleRhHigh"       , self.sampleRhHigh),
                ("sampPresSlopeOor"   , self.sampPresSlopeOor),
                ("spanDevOor"         , self.spanDevOor),
                ("placeholderTagBoolean", self.placeholderTagBoolean),
                ("placeholderTagDouble", self.placeholderTagDouble),
                ("warmUpComplete"     , self.warmUpComplete),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "LINF", linfConfig)
            time.sleep(.1)    

            syswConfig = OrderedDict([
                ("dateTime"                       , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("sysWarnSystemFault"             , self.sysWarnSystemFault),
                ("sysWarnInternalSerialTimeout"   , self.sysWarnInternalSerialTimeout),
                ("sysWarnReset"                   , self.sysWarnReset),
                ("sysWarnTimeNotSynced"           , self.sysWarnTimeNotSynced),
                ("sysWarnMaintenanceMode"         , self.sysWarnMaintenanceMode),
                ("sysWarnConfigReset"             , self.sysWarnConfigReset),
                ("asfSystemResetWarning"          , self.asfSystemResetWarning),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSW", syswConfig)
            time.sleep(.1)    

            fosdConfig = OrderedDict([
                ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("fo640x"             , self.fo640x),
                ("foPm1"              , self.foPm1),
                ("foPmtot"            , self.foPmtot),
                ("foNonUsEpaFemMode"  , self.foNonUsEpaFemMode),
                ("concValidFlag"      , self.concValidFlag),
                ("hourAvgPctValid"    , self.hourAvgPctValid),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "FOSD", fosdConfig)
            time.sleep(.1)    

            # # TIME
            # 'manualTimeServer',
            # 'lastInstrumentTimeSynced',
            # 'nextInstrumentTimeSync',
            # 'timeSyncControl',
            # 'timeSyncState',
            # 'dateTimeTargetValue',
            timeConfig = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("timeSync"                   , self.timeSync),
                ("timeSyncUseManual"          , self.timeSyncUseManual),
                ("manualTimeServer"           , self.manualTimeServer),
                ("timeSyncInterval"           , self.timeSyncInterval),
                ("lastInstrumentTimeSynced"   , self.lastInstrumentTimeSynced),
                ("nextInstrumentTimeSync"     , self.nextInstrumentTimeSync),
                ("timeSyncControl"            , self.timeSyncControl),
                ("timeSyncState"              , self.timeSyncState),
                ("timeSyncPassing"            , self.timeSyncPassing),
                ("dateTimeTargetValue"        , self.dateTimeTargetValue),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "TIME", timeConfig)
            time.sleep(.1)    

            # # COMM
            # 'udpBroadcastIp',
            commConfig = OrderedDict([
                ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("udpBroadcastEnable" , self.udpBroadcastEnable),
                ("udpBroadcastIp"     , self.udpBroadcastIp),
                ("modbusUseUserUnits" , self.modbusUseUserUnits),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "COMM", commConfig)
            time.sleep(.1)    

            # # INFO
            # 'driverVersion',
            # 'packageVersion',
            # 'osPlatform',
            # 'osVersion',
            # 'cfnetVersion',
            # 'nativeAppState',
            # 'instrumentMode',
            # 'instrumentTime',
            # 'systemTimeFormat',
            # 'generalTimeFormat',
            # 'alertsTimeFormat',
            # 'datalogTimeFormat',
            # 'instrumentShutdown',
            # 'instrumentReset',
            # 'reportGenerationUploadControl',
            # 'reportGenerationUploadState',
            infoConfig = OrderedDict([
                ("dateTime"                        , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("driverVersion"                   , self.driverVersion),
                ("packageVersion"                  , self.packageVersion),
                ("osPlatform"                      , self.osPlatform),
                ("osVersion"                       , self.osVersion),
                ("cfnetVersion"                    , self.cfnetVersion),
                ("nativeAppState"                  , self.nativeAppState),
                ("instrumentMode"                  , self.instrumentMode),
                ("instrumentTime"                  , self.instrumentTime),
                ("systemTimeFormat"                , self.systemTimeFormat),
                ("generalTimeFormat"               , self.generalTimeFormat),
                ("alertsTimeFormat"                , self.alertsTimeFormat),
                ("datalogTimeFormat"               , self.datalogTimeFormat),
                ("instrumentShutdown"              , self.instrumentShutdown),
                ("instrumentReset"                 , self.instrumentReset),
                ("reportGenerationUploadControl"   , self.reportGenerationUploadControl),
                ("reportGenerationUploadState"     , self.reportGenerationUploadState),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "INFO", infoConfig)
            time.sleep(.1)    

            # # DAP
            # 'dasUploadControl',
            # 'dasUploadState',
            # 'actionProgressTitle',
            # 'pressureCalControl',
            # 'pressureCalState',
            dapConfig = OrderedDict([
                ("dateTime"                        , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("dasUploadControl"                , self.dasUploadControl),
                ("dasUploadState"                  , self.dasUploadState),
                ("actionProgressTitle"             , self.actionProgressTitle),
                ("actionProgressPercent"           , self.actionProgressPercent),
                ("actionProgressCancel"            , self.actionProgressCancel),
                ("actionProgressCancelEnable"      , self.actionProgressCancelEnable),
                ("pressureCalControl"              , self.pressureCalControl),
                ("pressureCalState"                , self.pressureCalState),
                ("pressureCalActualPressureValue"  , self.pressureCalActualPressureValue),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DAP", dapConfig)
            time.sleep(.1)    

            # # ISC
            # 'lastInstrumentUpdateCheck',
            # 'packageVersionNeedingUpdate',
            iscConfig = OrderedDict([
                ("dateTime"                          , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("sensorConfigBypass"                , self.sensorConfigBypass),
                ("prigasPrec"                        , self.prigasPrec),
                ("secgasPrec"                        , self.secgasPrec),
                ("periodicUpdateCheck"               , self.periodicUpdateCheck),
                ("lastInstrumentUpdateCheck"         , self.lastInstrumentUpdateCheck),
                ("packageVersionNeedingUpdate"       , self.packageVersionNeedingUpdate),
                ("periodicUpdateFlag"                , self.periodicUpdateFlag),
                ("sysInfoUpdateAvail"                , self.sysInfoUpdateAvail),
                ("backgroundPeriodicReportUpload"    , self.backgroundPeriodicReportUpload),
                ("reportUploadInterval"              , self.reportUploadInterval),
                ("uploadReportToCloud"               , self.uploadReportToCloud),
                ("configResetFlag"                   , self.configResetFlag),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ISC", iscConfig)
            time.sleep(.1)    

            daalConfig = OrderedDict([
                ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("daOffset1"             , self.daOffset1),
                ("daOffset2"             , self.daOffset2),
                ("daSlope"               , self.daSlope),
                ("foT640DataAlignment"   , self.foT640DataAlignment),
                ("sysOkWarn"             , self.sysOkWarn),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DAAL", daalConfig)
            time.sleep(.1)    

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
