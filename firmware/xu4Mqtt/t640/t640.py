
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



def decode_float(regs, index):
    raw = (regs[index] << 16) + regs[index + 1]
    return struct.unpack('>f', raw.to_bytes(4, byteorder='big'))[0]


class T640:
    def __init__(self, host: str, port: int = 502, api_port: int = 8180 ,unit_id=1):
        
        
        self.client = ModbusTcpClient(host, port=port)
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
                self.totalParticleConc             = decode_float(regs, 118)

                realtimePmDict                      = OrderedDict([
                    ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1Realtime),
                    ("pm2_5"    , self.pm2_5Realtime),
                    ("pm2_5to10", self.pm10_2_5Realtime),
                    ("pm10"     , self.pm10Realtime),
                    ("pmTotal"  , self.pmtotRealtime)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "RTPM", realtimePmDict )
                
                stdRealtimePmDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1StdRealtime),
                    ("pm2_5"   , self.pm2_5StdRealtime),
                    ("pm10"    , self.pm10StdRealtime),
                    ("pmTotal" , self.pmtotStdRealtime)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "STDRTPM", stdRealtimePmDict  )


                pm1hrRollingDict                    = OrderedDict([
                    ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1_1hrRollingAvg),
                    ("pm2_5"    , self.pm2_5_1hrRollingAvg),
                    ("pm2_5to10", self.pm10_2_5_1hrRollingAvg),
                    ("pm10"     , self.pm10_1hrRollingAvg),
                    ("pmTotal"  , self.pmtot_1hrRollingAvg),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R1HPM",  pm1hrRollingDict )


                pm12hrRollingDict = OrderedDict([
                    ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1_12hrRollingAvg),
                    ("pm2_5"    , self.pm2_5_12hrRollingAvg),
                    ("pm2_5to10", self.pm10_2_5_12hrRollingAvg),
                    ("pm10"     , self.pm10_12hrRollingAvg),
                    ("pmTotal"  , self.pmtot_12hrRollingAvg),                
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R12HPM",  pm12hrRollingDict )


                pm24hrRollingDict = OrderedDict([
                    ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"      , self.pm1_24hrRollingAvg),
                    ("pm2_5"    , self.pm2_5_24hrRollingAvg),
                    ("pm2_5to10", self.pm10_2_5_24hrRollingAvg),
                    ("pm10"     , self.pm10_24hrRollingAvg),
                    ("pmTotal"  , self.pmtot_24hrRollingAvg),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R24HPM",  pm24hrRollingDict )

                pm1hrStandardizedDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1_1hrStandardizedAvg),
                    ("pm2_5"   , self.pm2_5_1hrStandardizedAvg),
                    ("pm10"    , self.pm10_1hrStandardizedAvg),
                    ("pmTotal" , self.pmtot_1hrStandardizedAvg)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S1HPM",  pm1hrStandardizedDict )


                pm12hrStandardizedDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1_12hrStandardizedAvg),
                    ("pm2_5"   , self.pm2_5_12hrStandardizedAvg),
                    ("pm10"    , self.pm10_12hrStandardizedAvg),
                    ("pmTotal" , self.pmtot_12hrStandardizedAvg)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S12HPM",  pm12hrStandardizedDict )


                pm24hrStandardizedDict = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("pm1"     , self.pm1_24hrStandardizedAvg),
                    ("pm2_5"   , self.pm2_5_24hrStandardizedAvg),
                    ("pm10"    , self.pm10_24hrStandardizedAvg),
                    ("pmTotal" , self.pmtot_24hrStandardizedAvg)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S24HPM",  pm24hrStandardizedDict )


                particleHistogramCounts    = OrderedDict([
                    ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("totalAmpHistParticles" , self.totalAmpHistParticles),
                    ("totalLenDistParticles" , self.totalLenDistParticles),
                    ("totalParticleConc"     , self.totalParticleConc)
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "PHC",  particleHistogramCounts )



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
                                print(f"self.{bin_name} = {val}")
                        except Exception as e:
                            print(f"Failed to parse histogram: {e}")
                    continue  # Skip setting opcDustHistogram as a string
                            
                # Normalize the value (convert strings "True"/"False" to 1/0, etc.)
                normalized_value = self._normalize_value(raw_value)

                # Save to camelCase class attribute
                setattr(self, camel_name, normalized_value)
                # print(f"self.{camel_name} = {repr(normalized_value)}")

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
            
            stdRealtimePmDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stpConc),
                ("pm2_5"   , self.pm25stpConc),
                ("pm10"    , self.pm10stpConc),
                ("pmTotal" , self.pmtotstpConc)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "STDRTPM", stdRealtimePmDict  )


            pm1hrRollingDict                    = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"      , self.pm11hrAvg),
                ("pm2_5"    , self.pm251hrAvg),
                ("pm2_5to10", self.pmc1hrAvg ),
                ("pm10"     , self.pm101hrAvg),
                ("pmTotal"  , self.pmtot1hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "R1HPM",  pm1hrRollingDict )


            pm12hrRollingDict = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"      , self.pm112hrAvg),
                ("pm2_5"    , self.pm2512hrAvg),
                ("pm2_5to10", self.pmc12hrAvg ),
                ("pm10"     , self.pm1012hrAvg),
                ("pmTotal"  , self.pmtot12hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "R12HPM",  pm12hrRollingDict )


            pm24hrRollingDict = OrderedDict([
                ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"      , self.pm124hrAvg),
                ("pm2_5"    , self.pm2524hrAvg),
                ("pm2_5to10", self.pmc24hrAvg ),
                ("pm10"     , self.pm1024hrAvg),
                ("pmTotal"  , self.pmtot24hrAvg),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "R24HPM",  pm24hrRollingDict )

            pm1hrStandardizedDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stp1hrAvg),
                ("pm2_5"   , self.pm25stp1hrAvg),
                ("pm10"    , self.pm10stp1hrAvg),
                ("pmTotal" , self.pmtotstp1hrAvg)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "S1HPM",  pm1hrStandardizedDict )

            pm12hrStandardizedDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stp12hrAvg),
                ("pm2_5"   , self.pm25stp12hrAvg),
                ("pm10"    , self.pm10stp12hrAvg),
                ("pmTotal" , self.pmtotstp12hrAvg)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "S12HPM",  pm12hrStandardizedDict )

            pm24hrStandardizedDict = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("pm1"     , self.pm1stp24hrAvg),
                ("pm2_5"   , self.pm25stp24hrAvg),
                ("pm10"    , self.pm10stp24hrAvg),
                ("pmTotal" , self.pmtotstp24hrAvg)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "S24HPM",  pm24hrStandardizedDict )


            particleHistogramCounts    = OrderedDict([
                ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("totalAmpHistParticles" , self.opcRtAmplitudeCounts),
                ("totalLenDistParticles" , self.opcRtLengthCounts),
                ("totalParticleConc"     , self.numConc)
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PHC",  particleHistogramCounts )



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
            







        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
