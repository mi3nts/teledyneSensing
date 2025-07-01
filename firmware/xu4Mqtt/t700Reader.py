
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




def main(loopInterval,hostIP):

    monitor = T700(host=hostIP)  # Or your device IP
    time.sleep(1)
    startTime = time.time()
    time.sleep(1)
    # monitor.read_api(True)  
    # time.sleep(0.1)      

    while True:
        try:
            print("======= T700 ========")
            read, data = monitor.read_discrete_inputs()
            if read:
                print("Discrete Inputs:", data)
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
        


    # def read_discrete_inputs(self):
    #         dateTime  = datetime.now(timezone.utc)
    #         try:
    #             result                     = self.client.read_discrete_inputs(0, len(self.discrete_labels), unit=self.unit_id)
    #             if not result.isError():
    #                 (   self.boxTempWarning,
    #                     self.sampleFlowWarning,
    #                     self.internalSerialTimeout,
    #                     self.systemResetWarning,
    #                     self.sysOkWarning,
    #                     self.sampleTemperatureWarning,
    #                     self.bypassFlowWarning,
    #                     self.systemFaultWarning
    #                 ) = result.bits
                    
    #                 sensorDictionary = OrderedDict([
    #                     ("dateTime"                , str(dateTime.strftime('%Y-%m-%d %H:%M:%S.%f'))),
    #                     ("boxTempWarning"           , int(self.boxTempWarning)) ,
    #                     ("sampleFlowWarning"        , int(self.sampleFlowWarning)),
    #                     ("internalSerialTimeout"    , int(self.internalSerialTimeout)),
    #                     ("systemResetWarning"       , int(self.systemResetWarning)),
    #                     ("sysOkWarning"             , int(self.sysOkWarning)),
    #                     ("sampleTemperatureWarning" , int(self.sampleTemperatureWarning)),
    #                     ("bypassFlowWarning"        , int(self.bypassFlowWarning)),
    #                     ("systemFaultWarning"       , int(self.systemFaultWarning)),
    #                     ])       
        
    #                 mSR.sensorFinisher(dateTime,self.sensorIDPreModbus+"WRNS",sensorDictionary)
        
    #                 return True, dict(zip(self.discrete_labels, result.bits))
    #         except ModbusException as e:
    #             print("[Error] Discrete Inputs:", e)

    #         return False, None
        
    # def read_coils(self):
    #     dateTime = datetime.now(timezone.utc)
    #     try:
    #         result = self.client.read_coils(0, len(self.coil_labels), unit=self.unit_id)
    #         print(result.bits)
    #         if not result.isError():
    #             (
    #                 self.controlRelay36,
    #                 self.controlRelay37,
    #                 self.controlRelay38,
    #                 self.controlRelay39,
    #                 self.maintenanceMode
    #             ) = result.bits[:len(self.coil_labels)] 

    #             sensorDictionary = OrderedDict([
    #                 ("dateTime"       , str(dateTime.strftime('%Y-%m-%d %H:%M:%S.%f'))),
    #                 ("controlRelay36" , int(self.controlRelay36)),
    #                 ("controlRelay37" , int(self.controlRelay37)),
    #                 ("controlRelay38" , int(self.controlRelay38)),
    #                 ("controlRelay39" , int(self.controlRelay39)),
    #                 ("maintenanceMode", int(self.maintenanceMode)),
    #             ])

    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "COIL", sensorDictionary)

    #             return True, dict(zip(self.coil_labels, result.bits))

    #     except ModbusException as e:
    #         print("[Error] Coils:", e)

    #     return False, None


    # def read_input_registers(self):
    #     dateTime = datetime.now(timezone.utc)
    #     try:
    #         result = self.client.read_input_registers(0, 120, unit=self.unit_id)
    #         if not result.isError():
    #             regs = result.registers
    #             self.pumpTachometer                 = decode_float(regs, 0)
    #             self.totalAmpHistParticles          = decode_float(regs, 2)
    #             self.totalLenDistParticles          = decode_float(regs, 4)
    #             self.pm10Realtime                   = decode_float(regs, 6)
    #             self.pm2_5Realtime                  = decode_float(regs, 8)
    #             self.pm10_2_5Realtime               = decode_float(regs, 10)
    #             self.pm10StdRealtime                = decode_float(regs, 12)
    #             self.pm10_1hrRollingAvg             = decode_float(regs, 14)
    #             self.pm2_5_1hrRollingAvg            = decode_float(regs, 16)
    #             self.pm10_2_5_1hrRollingAvg         = decode_float(regs, 18)
    #             self.pm10_12hrRollingAvg            = decode_float(regs, 20)
    #             self.pm2_5_12hrRollingAvg           = decode_float(regs, 22)
    #             self.pm10_2_5_12hrRollingAvg        = decode_float(regs, 24)
    #             self.pm10_24hrRollingAvg            = decode_float(regs, 26)
    #             self.pm2_5_24hrRollingAvg           = decode_float(regs, 28)
    #             self.pm10_2_5_24hrRollingAvg        = decode_float(regs, 30)
    #             self.ledTemp                        = decode_float(regs, 32)
    #             self.ambientPressure                = decode_float(regs, 34)
    #             self.humidity                       = decode_float(regs, 36)
    #             self.boxTemp                        = decode_float(regs, 38)
    #             self.ambientTemp                    = decode_float(regs, 40)
    #             self.ascTubeTemp                    = decode_float(regs, 42)
    #             self.rhSensorTemp                   = decode_float(regs, 44)
    #             self.sampleFlowMB                   = decode_float(regs, 46)
    #             self.bypassFlowMB                   = decode_float(regs, 48)
    #             self.totalFlowMB                    = decode_float(regs, 50)
    #             self.signalLength                   = decode_float(regs, 52)
    #             self.p3Value                        = decode_float(regs, 54)
    #             self.pumpDuty                       = decode_float(regs, 56)
    #             self.valveDuty                      = decode_float(regs, 58)
    #             self.ascHeaterDuty                  = decode_float(regs, 60)
    #             self.pm2_5StdRealtime               = decode_float(regs, 62)
    #             self.pm1Realtime                    = decode_float(regs, 64)
    #             self.pm1StdRealtime                 = decode_float(regs, 66)
    #             self.pm1_1hrStandardizedAvg         = decode_float(regs, 68)
    #             self.pm2_5_1hrStandardizedAvg       = decode_float(regs, 70)
    #             self.pm10_1hrStandardizedAvg        = decode_float(regs, 72)
    #             self.pm1_12hrStandardizedAvg        = decode_float(regs, 74)
    #             self.pm2_5_12hrStandardizedAvg      = decode_float(regs, 76)
    #             self.pm10_12hrStandardizedAvg       = decode_float(regs, 78)
    #             self.pm1_24hrStandardizedAvg        = decode_float(regs, 80)
    #             self.pm2_5_24hrStandardizedAvg      = decode_float(regs, 82)
    #             self.pm10_24hrStandardizedAvg       = decode_float(regs, 84)
    #             self.spanDeviation                  = decode_float(regs, 86)
    #             self.spanDevTrack                   = decode_float(regs, 88)
    #             self.pm1_1hrRollingAvg              = decode_float(regs, 90)
    #             self.pm1_12hrRollingAvg             = decode_float(regs, 92)
    #             self.pm1_24hrRollingAvg             = decode_float(regs, 94)
    #             self.pmtotRealtime                  = decode_float(regs, 96)
    #             self.pmtotStdRealtime               = decode_float(regs, 98)
    #             self.pmtot_1hrRollingAvg            = decode_float(regs, 100)
    #             self.pmtot_1hrStandardizedAvg       = decode_float(regs, 102)
    #             self.pmtot_12hrRollingAvg           = decode_float(regs, 104)
    #             self.pmtot_12hrStandardizedAvg      = decode_float(regs, 106)
    #             self.pmtot_24hrRollingAvg           = decode_float(regs, 108)
    #             self.pmtot_24hrStandardizedAvg      = decode_float(regs, 110)
    #             self.sampleFlowCV                   = decode_float(regs, 112)
    #             self.bypassFlowCV                   = decode_float(regs, 114)
    #             self.totalFlowCV                    = decode_float(regs, 116)
    #             self.totalParticleConc              = decode_float(regs, 118)

    #             realtimePmDict                      = OrderedDict([
    #                 ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"      , self.pm1Realtime),
    #                 ("pm2_5"    , self.pm2_5Realtime),
    #                 ("pm2_5to10", self.pm10_2_5Realtime),
    #                 ("pm10"     , self.pm10Realtime),
    #                 ("pmTotal"  , self.pmtotRealtime)
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "RTPM", realtimePmDict )
    #             time.sleep(.1)

    #             stdRealtimePmDict = OrderedDict([
    #                 ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"     , self.pm1StdRealtime),
    #                 ("pm2_5"   , self.pm2_5StdRealtime),
    #                 ("pm10"    , self.pm10StdRealtime),
    #                 ("pmTotal" , self.pmtotStdRealtime)
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "STDRTPM", stdRealtimePmDict  )
    #             time.sleep(.1)

    #             pm1hrRollingDict                    = OrderedDict([
    #                 ("dateTime"                   , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"      , self.pm1_1hrRollingAvg),
    #                 ("pm2_5"    , self.pm2_5_1hrRollingAvg),
    #                 ("pm2_5to10", self.pm10_2_5_1hrRollingAvg),
    #                 ("pm10"     , self.pm10_1hrRollingAvg),
    #                 ("pmTotal"  , self.pmtot_1hrRollingAvg),
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R1HPM",  pm1hrRollingDict )
    #             time.sleep(.1)

    #             pm12hrRollingDict = OrderedDict([
    #                 ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"      , self.pm1_12hrRollingAvg),
    #                 ("pm2_5"    , self.pm2_5_12hrRollingAvg),
    #                 ("pm2_5to10", self.pm10_2_5_12hrRollingAvg),
    #                 ("pm10"     , self.pm10_12hrRollingAvg),
    #                 ("pmTotal"  , self.pmtot_12hrRollingAvg),                
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R12HPM",  pm12hrRollingDict )
    #             time.sleep(.1)

    #             pm24hrRollingDict = OrderedDict([
    #                 ("dateTime" , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"      , self.pm1_24hrRollingAvg),
    #                 ("pm2_5"    , self.pm2_5_24hrRollingAvg),
    #                 ("pm2_5to10", self.pm10_2_5_24hrRollingAvg),
    #                 ("pm10"     , self.pm10_24hrRollingAvg),
    #                 ("pmTotal"  , self.pmtot_24hrRollingAvg),
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "R24HPM",  pm24hrRollingDict )
    #             time.sleep(.1)

    #             pm1hrStandardizedDict = OrderedDict([
    #                 ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"     , self.pm1_1hrStandardizedAvg),
    #                 ("pm2_5"   , self.pm2_5_1hrStandardizedAvg),
    #                 ("pm10"    , self.pm10_1hrStandardizedAvg),
    #                 ("pmTotal" , self.pmtot_1hrStandardizedAvg)
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S1HPM",  pm1hrStandardizedDict )
    #             time.sleep(.1)

    #             pm12hrStandardizedDict = OrderedDict([
    #                 ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"     , self.pm1_12hrStandardizedAvg),
    #                 ("pm2_5"   , self.pm2_5_12hrStandardizedAvg),
    #                 ("pm10"    , self.pm10_12hrStandardizedAvg),
    #                 ("pmTotal" , self.pmtot_12hrStandardizedAvg)
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S12HPM",  pm12hrStandardizedDict )
    #             time.sleep(.1)

    #             pm24hrStandardizedDict = OrderedDict([
    #                 ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pm1"     , self.pm1_24hrStandardizedAvg),
    #                 ("pm2_5"   , self.pm2_5_24hrStandardizedAvg),
    #                 ("pm10"    , self.pm10_24hrStandardizedAvg),
    #                 ("pmTotal" , self.pmtot_24hrStandardizedAvg)
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "S24HPM",  pm24hrStandardizedDict )
    #             time.sleep(.1)

    #             particleHistogramCounts    = OrderedDict([
    #                 ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("totalAmpHistParticles" , self.totalAmpHistParticles),
    #                 ("totalLenDistParticles" , self.totalLenDistParticles),
    #                 ("totalParticleConc"     , self.totalParticleConc)
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "PHC",  particleHistogramCounts )
    #             time.sleep(.1)

    #             climateDict                          = OrderedDict([
    #                 ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("ledTemp"            , self.ledTemp),
    #                 ("pressure"           , self.ambientPressure),
    #                 ("humidity"           , self.humidity),
    #                 ("boxTemp"            , self.boxTemp),
    #                 ("temperature"        , self.ambientTemp),
    #                 ("ascTubeTemp"        , self.ascTubeTemp),
    #                 ("rhSensorTemp"       , self.rhSensorTemp)
    #             ])

    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "CLM",  climateDict )
    #             time.sleep(.1)

    #             pumpAndFlowDict = OrderedDict([
    #                 ("dateTime"           , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pumpTachometer"     , self.pumpTachometer),
    #                 ("sampleFlow"         , self.sampleFlowMB),
    #                 ("bypassFlow"         , self.bypassFlowMB),
    #                 ("totalFlow"          , self.totalFlowMB),
    #                 ("signalLength"       , self.signalLength),
    #                 ("p3Value"            , self.p3Value),
    #                 ("pumpDuty"           , self.pumpDuty),
    #                 ("valveDuty"          , self.valveDuty),
    #                 ("ascHeaterDuty"      , self.ascHeaterDuty),
    #                 ("sampleFlowCV"       , self.sampleFlowCV),
    #                 ("bypassFlowCV"       , self.bypassFlowCV),
    #                 ("totalFlowCV"        , self.totalFlowCV),
    #             ])

    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "PV",  pumpAndFlowDict )
    #             time.sleep(.1)
                
    #             return True, {
    #                 self.input_float_fields[i]: decode_float(regs, i)
    #                 for i in sorted(self.input_float_fields.keys())
    #             }
    #     except ModbusException as e:
    #         print("[Error] Input Registers:", e)

    #     return False, None            
    
    # def read_holding_registers(self):
    #     dateTime = datetime.now(timezone.utc)
    #     try:
    #         result = self.client.read_holding_registers(0, 32, unit=self.unit_id)
    #         # PMT Voltage                                   0.000
    #         # PMT Offset                                    0.000
    #         # PMT HVPS                                      0.000
    #         # 5LPM Flow Cal                                 0.992
    #         # Bypass Flow Cal                               1.000
    #         # Pressure Cal                                  1.008
    #         # RH Setpoint                                  35.000
    #         # Sample Flow Setpoint                          5.000
    #         # Bypass Flow Setpoint                         11.670
    #         # RH Sensor Slope                               1.000
    #         # KS10 PM10 Slope                               1.000
    #         # KS2.5 PM2.5 Slope                             1.000
    #         # KS1 PM1 Slope                                 1.000
    #         # KO10 PM10 Offset                              0.000
    #         # KO2.5 PM2.5 Offset                            0.000
    #         # KO1 PM1 Offset                                0.000


    #         if not result.isError():
    #             regs = result.registers
    #             self.pmtVoltage                     = decode_float(regs, 0)
    #             self.pmtOffset                      = decode_float(regs, 2)
    #             self.pmtHVPS                        = decode_float(regs, 4)
    #             self.fiveLPMFlowCal                 = decode_float(regs, 6)
    #             self.bypassFlowCal                  = decode_float(regs, 8)
    #             self.pressureCal                    = decode_float(regs, 10)
    #             self.rhSetpoint                     = decode_float(regs, 12)
    #             self.sampleFlowSetpoint             = decode_float(regs, 14)
    #             self.bypassFlowSetpoint             = decode_float(regs, 16)
    #             self.rhSensorSlope                  = decode_float(regs, 18)
    #             self.ks10PM10Slope                  = decode_float(regs, 20)
    #             self.ks2_5PM2_5Slope                = decode_float(regs, 22)
    #             self.ks1PM1Slope                    = decode_float(regs, 24)
    #             self.ko10PM10Offset                 = decode_float(regs, 26)
    #             self.ko2_5PM2_5Offset               = decode_float(regs, 28)
    #             self.ko1PM1Offset                   = decode_float(regs, 30)
                
    #             calibrationDict              = OrderedDict([
    #                 ("dateTime"              , dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
    #                 ("pmtVoltage"            , self.pmtVoltage),
    #                 ("pmtOffset"             , self.pmtOffset),
    #                 ("pmtHVPS"               , self.pmtHVPS),
    #                 ("fiveLPMFlowCal"        , self.fiveLPMFlowCal),
    #                 ("bypassFlowCal"         , self.bypassFlowCal),
    #                 ("pressureCal"           , self.pressureCal),
    #                 ("rhSetpoint"            , self.rhSetpoint),
    #                 ("sampleFlowSetpoint"    , self.sampleFlowSetpoint),
    #                 ("bypassFlowSetpoint"    , self.bypassFlowSetpoint),
    #                 ("rhSensorSlope"         , self.rhSensorSlope),
    #                 ("ks10PM10Slope"         , self.ks10PM10Slope),
    #                 ("ks2_5PM2_5Slope"       , self.ks2_5PM2_5Slope),
    #                 ("ks1PM1Slope"           , self.ks1PM1Slope),
    #                 ("ko10PM10Offset"        , self.ko10PM10Offset),
    #                 ("ko2_5PM2_5Offset"      , self.ko2_5PM2_5Offset),
    #                 ("ko1PM1Offset"          , self.ko1PM1Offset)
    #             ])
    #             mSR.sensorFinisher(dateTime, self.sensorIDPreModbus + "CALV", calibrationDict )
    #             time.sleep(.1)                

    #             return True, {
    #                 self.holding_float_fields[i]: decode_float(regs, i)
    #                 for i in sorted(self.holding_float_fields.keys())
    #             }
    #     except ModbusException as e:
    #         print("[Error] Input Registers:", e)

    #     return False, None                
    