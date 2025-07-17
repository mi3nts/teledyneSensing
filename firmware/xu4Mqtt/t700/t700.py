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
import yaml

hostIP       = "192.168.20.109"

# API ALSO AVAILABLE AT: http://192.168.20.109:8180/api/taglist - Have 1031 parametors 
# Run Exp 1 
# Run Exp 2


# API Sensor IDs
# 97
# Modbus IDs
# 8
# Total
# 105 unique sensor IDs

# T700MB001CONTROL
# T700MB001ELEC
# T700MB001FLOW
# T700MB001O3
# T700MB001PHOT
# T700MB001PRES
# T700MB001STATUS
# T700MB001TEMP

# T700API001ACTPROG
# T700API001ACTSEQ
# T700API001ADAPTIVE
# T700API001AICAL
# T700API001AICAL1
# T700API001AICAL2
# T700API001AICHN
# T700API001AITEMP
# T700API001AOCAL
# T700API001AOCH1
# T700API001AOCH2
# T700API001AOCH3
# T700API001AOCH4
# T700API001AODRIVE
# T700API001AOSLP
# T700API001AOWRN
# T700API001ASFSTS


# T700API001ASFBIT
# T700API001ASFWARN
# T700API001BENCHCAL
# T700API001CAL1DRV
# T700API001CAL1FLW
# T700API001CAL2DRV
# T700API001CAL2FLW
# T700API001CALARM
# T700API001CALCTRL
# T700API001CALDRV
# T700API001CALGAS
# T700API001CALRNG
# T700API001CALSTS
# T700API001CFGXFER

# T700API001CNFGST
# T700API001CYLGAS
# T700API001DICNTL
# T700API001DIGIN
# T700API001DILDRV
# T700API001DILFLW

# T700API001DOCNTL
# T700API001DOUT1
# T700API001DOUT2
# T700API001DOUT3
# T700API001DOUT4
# T700API001DOUT5
# T700API001DOUT6
# T700API001DOUT7
# T700API001DOUT8
# T700API001FINAL
# T700API001FLOWCFG
# T700API001FWUPDT
# T700API001GASAVAIL
# T700API001GASPROP
# T700API001HMETER
# T700API001HESSEN
# T700API001INSTR
# T700API001LEVELCFG
# T700API001LOGGER

# T700API001MBRL1
# T700API001MBRL2
# T700API001MBRL3
# T700API001MBRL4
# T700API001MEMDISK
# T700API001MEMORY
# T700API001MFCWARN
# T700API001MISCAL
# T700API001MODOUT
# T700API001MODSEQ
# T700API001NETCFG
# T700API001O3BENCH
# T700API001O3CAL
# T700API001O3CALSUM
# T700API001O3GENCFG
# T700API001O3PID
# T700API001OPTPARAM
# T700API001OSINFO
# T700API001PERMGAS

# T700API001PHCAL
# T700API001PORTGEN
# T700API001PRESSCAL
# T700API001PRESSURE
# T700API001PURGECTL
# T700API001REGWARN
# T700API001REMOTE
# T700API001SEQCFG
# T700API001STEPCFG

# T700API001STEPSTS
# T700API001SVCOM1
# T700API001SVCOM2
# T700API001SVTCP
# T700API001SYSCAL
# T700API001SYSCFG
# T700API001SYSINFO

# T700API001SYSWARN
# T700API001SYSWRN
# T700API001SYSWRND
# T700API001SYSWRNDCAL
# T700API001TAGLOGGER
# T700API001TIMEFMT
# T700API001TIMESYNC

# T700API001UPDSTAT
# T700API001UPLOAD
# T700API001VALVECTL1
# T700API001VALVECTL2

# String Variables

# nativeAppState
# instrumentMode
# instrumentTime
# doOutput1Map
# doOutput2Map
# doOutput3Map
# doOutput4Map
# doOutput5Map
# doOutput6Map
# doOutput7Map
# doOutput8Map
# doMbRelay1Map
# doMbRelay2Map
# doMbRelay3Map
# doMbRelay4Map
# aoCalControl
# ao1CalState
# ao2CalState
# ao3CalState
# ao4CalState
# aoOutput1Range
# aoOutput1CalibrationType
# aoOutput2Range
# aoOutput2CalibrationType
# aoOutput3Range
# aoOutput3CalibrationType
# aoOutput4Range
# aoOutput4CalibrationType
# aoOutput4Map
# aiCalControl
# aiCalState
# dlFlush
# dlLastFlushed
# svCom1Parity
# svCom1HandshakingMode
# svCom2Parity
# svCom2HandshakingMode
# flowCalControl
# flowCalState
# pressureCalControl
# pressureCalState
# dasUploadControl
# dasUploadState
# reportGenerationUploadControl
# reportGenerationUploadState
# svLanguageSelect
# svClockFormat
# svCommandPrompt
# driverVersion
# packageVersion
# tagsFlushTimestamp
# osPlatform
# osVersion
# cfnetVersion
# networkAddressType
# networkIpAddress
# networkSubnetMask
# networkDefaultGateway
# networkDns1
# networkDns2
# manualTimeServer
# lastInstrumentTimeSynced
# nextInstrumentTimeSync
# svUserUnits
# svAcLineFrequency
# dlTimeFormat
# dlLastDownloadTime
# dlDasDownloadFrom
# dlDasDownloadT1
# dlDasDownloadT2
# systemTimeFormat
# generalTimeFormat
# alertsTimeFormat
# datalogTimeFormat
# instrumentShutdown
# instrumentReset
# homeMeter1
# homeMeter2
# homeMeter3
# aoOutput1Map
# aoOutput2Map
# aoOutput3Map
# instMode
# autoTargGasName
# autoTargGasUnits
# manTargGasName
# manO3GenMode
# gptO3TargUnits
# gptNoTargUnits
# calGasPressureCalControl
# calGasPressureCalState
# diluentPressureCalControl
# diluentPressureCalState
# o3PressureCalControl
# o3PressureCalState
# calGasO3GenMode
# calGasPriUnits
# calGasO3Units
# cylPort
# cylGas1Name
# cylGas1Units
# cylGas2Name
# cylGas2Units
# cylGas3Name
# cylGas3Units
# sequenceName
# stepType
# stepCalGas
# stepManCalGas
# stepGasUnits
# stepGptO3Units
# stepOutputSelect
# levelStepType
# levelCalGas
# levelGasUnits
# levelGptO3Units
# levelManCalGas
# levelO3GenMode
# svCom1Protocol
# svCom2Protocol
# svRangeMode
# svO3GenMode
# svPerm1GasType
# gasGenerateCmdSource
# outputABSelect
# calGasPriName
# calGasO3Name
# packageVersionNeedingUpdate
# nativeLogger
# tagLogger
# dateTimeTargetValue
# execseqSequenceName
# stepExecseqSequenceName
# activeSequenceName
# activeActionName
# cal1DriveTable
# cal1FlowTable
# cal2DriveTable
# cal2FlowTable
# dilDriveTable
# dilFlowTable


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
            # print(result)
            # print(result.registers)
            time.sleep(.1)

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
                
                return True, [resultStatus.bits,resultControls.bits]
            
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


    # ADD THESE TO T700 CLASS
    def getSequenceIndex(*,conc, flowRate, time, cylinder):
        cylinderFile = os.path.join("gasCylinders", cylinder+".yaml")
        cylinderSequences = yaml.load(open(cylinderFile ),Loader=yaml.FullLoader)
        # print(cylinderSequences)

        for entry in cylinderSequences['cylinder']:
            # print(entry)
            if (entry["ch4_ppm"] == conc and
                entry["flow_SLPM"] == flowRate and
                entry["time_seconds"] == time):
                print("Found Match: ", entry)
                return True,entry["index"], entry
        
        print("No Match Found")
        return False, -1, None


    def activateStandByMode(self):
        time.sleep(1)
        print("Activating StandBy Mode")
        status = self.write_coil(101, True)
        if status:
            print("StandBy Activated")   
        time.sleep(1)
        return True

    def activatePurge(self,time=60):
        time.sleep(1)
        print("Purging for ", time, " seconds")
        status = self.write_coil(100, True)
        if status:
            print("Purge Activated")   

        self.continousRead(duration=time)
        self.activateStandByMode()
        time.sleep(1)
        return True

    # Embed Run Sequence Here 
    def runSequence(self, *,  conc, flowRate, time, cylinder):
        validity, sequenceIndex , sequenceEntry = self.getSequenceIndex(conc=conc, flowRate=flowRate, time=time, cylinder=cylinder)

        if validity:
            print("Activating: ",sequenceEntry)
            status = self.write_coil(sequenceIndex, True)
            if status:
                print("Sequence Activated - Index: ", sequenceIndex, " - Entry: " , sequenceEntry)
                time.sleep(1)
                self.continousRead( duration=sequenceEntry["time_seconds"])
            else:
                print("Failed to Activate Sequence with index", sequenceIndex, " Activated: " , sequenceEntry)
        

        return validity, sequenceIndex, sequenceEntry
    

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
        saved_tags = []
        response = requests.get(self.apiURL)
        if response.status_code == 200:
            data = response.json()
            for tag in data.get("tags", []):
                name = tag.get("name", "")
                raw_value = tag.get("value", "")
                camel_name = self._to_camel_case(name)

                # # Skip tags that start with digits (e.g., '1MIN-DATA')
                # if name and name[0].isdigit():
                #     continue
                           
                # Normalize the value (convert strings "True"/"False" to 1/0, etc.)
                normalized_value = self._normalize_value(raw_value)

                # Save to camelCase class attribute
                try:
                    saved_tags.append(f"{camel_name} = {repr(normalized_value)}")
                    setattr(self, camel_name, normalized_value)
                    # print(f"self.{camel_name} = {repr(normalized_value)}")


                except Exception as e:
                    print(f"[Warning] Failed to set attribute '{camel_name}': {e}")

            # with open("saved_tags.txt", "w") as f:
            #     for line in saved_tags:
            #         f.write(line + "\n")
            
            # At this point, the data is attached to sensors 
            dateTime  = datetime.now(timezone.utc)

            if startUp:
                instrument = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("nativeAppState", self.nativeAppState),
                    ("instrumentMode", self.instrumentMode),
                    ("instrumentTime", self.instrumentTime),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "INST", instrument)
                time.sleep(0.1)

                # Digital Output 1
                doOutput1Block = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doOutput1", self.doOutput1),
                    ("doOutput1Map", self.doOutput1Map),
                    ("doOutput1Polarity", self.doOutput1Polarity),
                    ("doOutput1Setpt", self.doOutput1Setpt),
                    ("doOutput1DiagMode", self.doOutput1DiagMode),
                    ("doOutput1DiagSetpt", self.doOutput1DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT1", doOutput1Block)
                time.sleep(0.1)

                # Digital Output 2
                doOutput2Block = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("doOutput2", self.doOutput2),
                    ("doOutput2Map", self.doOutput2Map),
                    ("doOutput2Polarity", self.doOutput2Polarity),
                    ("doOutput2Setpt", self.doOutput2Setpt),
                    ("doOutput2DiagMode", self.doOutput2DiagMode),
                    ("doOutput2DiagSetpt", self.doOutput2DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT2", doOutput2Block)
                time.sleep(0.1)

                # Digital Output 3
                doOutput3Block = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("doOutput3", self.doOutput3),
                    ("doOutput3Map", self.doOutput3Map),
                    ("doOutput3Polarity", self.doOutput3Polarity),
                    ("doOutput3Setpt", self.doOutput3Setpt),
                    ("doOutput3DiagMode", self.doOutput3DiagMode),
                    ("doOutput3DiagSetpt", self.doOutput3DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT3", doOutput3Block)
                time.sleep(0.1)

                # Digital Output 4
                doOutput4Block = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doOutput4", self.doOutput4),
                    ("doOutput4Map", self.doOutput4Map),
                    ("doOutput4Polarity", self.doOutput4Polarity),
                    ("doOutput4Setpt", self.doOutput4Setpt),
                    ("doOutput4DiagMode", self.doOutput4DiagMode),
                    ("doOutput4DiagSetpt", self.doOutput4DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT4", doOutput4Block)
                time.sleep(0.1)

                # Digital Output 5
                doOutput5Block = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doOutput5", self.doOutput5),
                    ("doOutput5Map", self.doOutput5Map),
                    ("doOutput5Polarity", self.doOutput5Polarity),
                    ("doOutput5Setpt", self.doOutput5Setpt),
                    ("doOutput5DiagMode", self.doOutput5DiagMode),
                    ("doOutput5DiagSetpt", self.doOutput5DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT5", doOutput5Block)
                time.sleep(0.1)

                # Digital Output 6
                doOutput6Block = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doOutput6", self.doOutput6),
                    ("doOutput6Map", self.doOutput6Map),
                    ("doOutput6Polarity", self.doOutput6Polarity),
                    ("doOutput6Setpt", self.doOutput6Setpt),
                    ("doOutput6DiagMode", self.doOutput6DiagMode),
                    ("doOutput6DiagSetpt", self.doOutput6DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT6", doOutput6Block)
                time.sleep(0.1)

                # Digital Output 7
                doOutput7Block = OrderedDict([
                    ("doOutput7", self.doOutput7),
                    ("doOutput7Map", self.doOutput7Map),
                    ("doOutput7Polarity", self.doOutput7Polarity),
                    ("doOutput7Setpt", self.doOutput7Setpt),
                    ("doOutput7DiagMode", self.doOutput7DiagMode),
                    ("doOutput7DiagSetpt", self.doOutput7DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT7", doOutput7Block)
                time.sleep(0.1)

                # Digital Output 8
                doOutput8Block = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doOutput8", self.doOutput8),
                    ("doOutput8Map", self.doOutput8Map),
                    ("doOutput8Polarity", self.doOutput8Polarity),
                    ("doOutput8Setpt", self.doOutput8Setpt),
                    ("doOutput8DiagMode", self.doOutput8DiagMode),
                    ("doOutput8DiagSetpt", self.doOutput8DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOUT8", doOutput8Block)
                time.sleep(0.1)

                # Digital Output Relays - Split
                doMbRelay1 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("doMbRelay1", self.doMbRelay1),
                    ("doMbRelay1Map", self.doMbRelay1Map),
                    ("doMbRelay1Polarity", self.doMbRelay1Polarity),
                    ("doMbRelay1Setpt", self.doMbRelay1Setpt),
                    ("doMbRelay1DiagMode", self.doMbRelay1DiagMode),
                    ("doMbRelay1DiagSetpt", self.doMbRelay1DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MBRL1", doMbRelay1)
                time.sleep(0.1)

                doMbRelay2 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doMbRelay2", self.doMbRelay2),
                    ("doMbRelay2Map", self.doMbRelay2Map),
                    ("doMbRelay2Polarity", self.doMbRelay2Polarity),
                    ("doMbRelay2Setpt", self.doMbRelay2Setpt),
                    ("doMbRelay2DiagMode", self.doMbRelay2DiagMode),
                    ("doMbRelay2DiagSetpt", self.doMbRelay2DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MBRL2", doMbRelay2)
                time.sleep(0.1)

                doMbRelay3 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doMbRelay3", self.doMbRelay3),
                    ("doMbRelay3Map", self.doMbRelay3Map),
                    ("doMbRelay3Polarity", self.doMbRelay3Polarity),
                    ("doMbRelay3Setpt", self.doMbRelay3Setpt),
                    ("doMbRelay3DiagMode", self.doMbRelay3DiagMode),
                    ("doMbRelay3DiagSetpt", self.doMbRelay3DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MBRL3", doMbRelay3)
                time.sleep(0.1)

                doMbRelay4 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("doMbRelay4", self.doMbRelay4),
                    ("doMbRelay4Map", self.doMbRelay4Map),
                    ("doMbRelay4Polarity", self.doMbRelay4Polarity),
                    ("doMbRelay4Setpt", self.doMbRelay4Setpt),
                    ("doMbRelay4DiagMode", self.doMbRelay4DiagMode),
                    ("doMbRelay4DiagSetpt", self.doMbRelay4DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MBRL4", doMbRelay4)
                time.sleep(0.1)

                aoCalStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aoCalControl", self.aoCalControl),
                    ("ao1CalState", self.ao1CalState),
                    ("ao2CalState", self.ao2CalState),
                    ("ao3CalState", self.ao3CalState),
                    ("ao4CalState", self.ao4CalState),
                    ("aoOutputTargetZeroVoltage", self.aoOutputTargetZeroVoltage),
                    ("aoOutputTargetSpanVoltage", self.aoOutputTargetSpanVoltage),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AOCAL", aoCalStatus)
                time.sleep(0.1)

                aoChannel1 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aoOutput1", self.aoOutput1),
                    ("aoOutput1Min", self.aoOutput1Min),
                    ("aoOutput1Max", self.aoOutput1Max),
                    ("aoOutput1Percent", self.aoOutput1Percent),
                    ("aoOutput1Range", self.aoOutput1Range),
                    ("aoOutput1Overrange", self.aoOutput1Overrange),
                    ("aoOutput1Calibrated", self.aoOutput1Calibrated),
                    ("aoOutput1RecOffset", self.aoOutput1RecOffset),
                    ("aoOutput1CalibrationType", self.aoOutput1CalibrationType),
                    ("aoOutput1Map", self.aoOutput1Map),
                    ("aoOutput1DiagMode", self.aoOutput1DiagMode),
                    ("aoOutput1DiagPercent", self.aoOutput1DiagPercent),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AOCH1", aoChannel1)
                time.sleep(0.1)


                aoChannel2 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aoOutput2", self.aoOutput2),
                    ("aoOutput2Min", self.aoOutput2Min),
                    ("aoOutput2Max", self.aoOutput2Max),
                    ("aoOutput2Percent", self.aoOutput2Percent),
                    ("aoOutput2Range", self.aoOutput2Range),
                    ("aoOutput2Overrange", self.aoOutput2Overrange),
                    ("aoOutput2Calibrated", self.aoOutput2Calibrated),
                    ("aoOutput2RecOffset", self.aoOutput2RecOffset),
                    ("aoOutput2CalibrationType", self.aoOutput2CalibrationType),
                    ("aoOutput2Map", self.aoOutput2Map),
                    ("aoOutput2DiagMode", self.aoOutput2DiagMode),
                    ("aoOutput2DiagPercent", self.aoOutput2DiagPercent),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AOCH2", aoChannel2)
                time.sleep(0.1)

                aoChannel3 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aoOutput3", self.aoOutput3),
                    ("aoOutput3Min", self.aoOutput3Min),
                    ("aoOutput3Max", self.aoOutput3Max),
                    ("aoOutput3Percent", self.aoOutput3Percent),
                    ("aoOutput3Range", self.aoOutput3Range),
                    ("aoOutput3Overrange", self.aoOutput3Overrange),
                    ("aoOutput3Calibrated", self.aoOutput3Calibrated),
                    ("aoOutput3RecOffset", self.aoOutput3RecOffset),
                    ("aoOutput3CalibrationType", self.aoOutput3CalibrationType),
                    ("aoOutput3Map", self.aoOutput3Map),
                    ("aoOutput3DiagMode", self.aoOutput3DiagMode),
                    ("aoOutput3DiagPercent", self.aoOutput3DiagPercent),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AOCH3", aoChannel3)
                time.sleep(0.1)


                aoChannel4 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aoOutput4", self.aoOutput4),
                    ("aoOutput4Min", self.aoOutput4Min),
                    ("aoOutput4Max", self.aoOutput4Max),
                    ("aoOutput4Percent", self.aoOutput4Percent),
                    ("aoOutput4Range", self.aoOutput4Range),
                    ("aoOutput4Overrange", self.aoOutput4Overrange),
                    ("aoOutput4Calibrated", self.aoOutput4Calibrated),
                    ("aoOutput4RecOffset", self.aoOutput4RecOffset),
                    ("aoOutput4CalibrationType", self.aoOutput4CalibrationType),
                    ("aoOutput4Map", self.aoOutput4Map),
                    ("aoOutput4DiagMode", self.aoOutput4DiagMode),
                    ("aoOutput4DiagPercent", self.aoOutput4DiagPercent),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AOCH4", aoChannel4)
                time.sleep(0.1)


                aoCalCoefficients = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aoOutput1Slope", self.aoOutput1Slope),
                    ("aoOutput1Offset", self.aoOutput1Offset),
                    ("aoOutput1LogicalSlope", self.aoOutput1LogicalSlope),
                    ("aoOutput1LogicalOffset", self.aoOutput1LogicalOffset),

                    ("aoOutput2Slope", self.aoOutput2Slope),
                    ("aoOutput2Offset", self.aoOutput2Offset),
                    ("aoOutput2LogicalSlope", self.aoOutput2LogicalSlope),
                    ("aoOutput2LogicalOffset", self.aoOutput2LogicalOffset),

                    ("aoOutput3Slope", self.aoOutput3Slope),
                    ("aoOutput3Offset", self.aoOutput3Offset),
                    ("aoOutput3LogicalSlope", self.aoOutput3LogicalSlope),
                    ("aoOutput3LogicalOffset", self.aoOutput3LogicalOffset),

                    ("aoOutput4Slope", self.aoOutput4Slope),
                    ("aoOutput4Offset", self.aoOutput4Offset),
                    ("aoOutput4LogicalSlope", self.aoOutput4LogicalSlope),
                    ("aoOutput4LogicalOffset", self.aoOutput4LogicalOffset),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AOSLP", aoCalCoefficients)
                time.sleep(0.1)


                aiCalStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aiCalControl", self.aiCalControl),
                    ("aiCalState", self.aiCalState),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AICAL", aiCalStatus)
                time.sleep(0.1)

                dlStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("dlFlush", self.dlFlush),
                    ("dlLastFlushed", self.dlLastFlushed),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DLSTS", dlStatus)
                time.sleep(0.1)

                svCom1Settings = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("svCom1ModemInitString", self.svCom1ModemInitString),
                    ("svCom1Baudrate", self.svCom1Baudrate),
                    ("svCom1Parity", self.svCom1Parity),
                    ("svCom1Databits", self.svCom1Databits),
                    ("svCom1Stopbits", self.svCom1Stopbits),
                    ("svCom1ModemConnection", self.svCom1ModemConnection),
                    ("svCom1EnableQuietMode", self.svCom1EnableQuietMode),
                    ("svCom1EnableSecurity", self.svCom1EnableSecurity),
                    ("svCom1EnableMultidrop", self.svCom1EnableMultidrop),
                    ("svCom1EnableRs485", self.svCom1EnableRs485),
                    ("svCom1HandshakingMode", self.svCom1HandshakingMode),
                    ("svCom1EnableCommandPromptDisplay", self.svCom1EnableCommandPromptDisplay),
                    ("svCom1DisableEchoLineEditing", self.svCom1DisableEchoLineEditing),
                    ("svCom1DisableHardwareErrorChecking", self.svCom1DisableHardwareErrorChecking),
                    ("svCom1EnableHardwareFifo", self.svCom1EnableHardwareFifo),
                    ("svCom1Initialize", self.svCom1Initialize),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVCOM1", svCom1Settings)
                time.sleep(0.1)

                svCom2Settings = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("svCom2ModemInitString", self.svCom2ModemInitString),
                    ("svCom2Baudrate", self.svCom2Baudrate),
                    ("svCom2Parity", self.svCom2Parity),
                    ("svCom2Databits", self.svCom2Databits),
                    ("svCom2Stopbits", self.svCom2Stopbits),
                    ("svCom2ModemConnection", self.svCom2ModemConnection),
                    ("svCom2EnableQuietMode", self.svCom2EnableQuietMode),
                    ("svCom2EnableSecurity", self.svCom2EnableSecurity),
                    ("svCom2EnableMultidrop", self.svCom2EnableMultidrop),
                    ("svCom2EnableRs485", self.svCom2EnableRs485),
                    ("svCom2HandshakingMode", self.svCom2HandshakingMode),
                    ("svCom2EnableCommandPromptDisplay", self.svCom2EnableCommandPromptDisplay),
                    ("svCom2DisableEchoLineEditing", self.svCom2DisableEchoLineEditing),
                    ("svCom2DisableHardwareErrorChecking", self.svCom2DisableHardwareErrorChecking),
                    ("svCom2EnableHardwareFifo", self.svCom2EnableHardwareFifo),
                    ("svCom2Initialize", self.svCom2Initialize),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVCOM2", svCom2Settings)
                time.sleep(0.1)



                svTcpSettings = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("svTcp1Initialize", self.svTcp1Initialize),
                    ("svTcp1Portnum", self.svTcp1Portnum),
                    ("svTcp1EnableSecurity", self.svTcp1EnableSecurity),
                    ("svTcp1EnableCommandPromptDisplay", self.svTcp1EnableCommandPromptDisplay),
                    ("svTcp2Initialize", self.svTcp2Initialize),
                    ("svTcp2Portnum", self.svTcp2Portnum),
                    ("svTcp3Initialize", self.svTcp3Initialize),
                    ("svTcp3Portnum", self.svTcp3Portnum),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SVTCP", svTcpSettings)
                time.sleep(0.1)


                calibrationStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("flowCalControl", self.flowCalControl),
                    ("flowCalState", self.flowCalState),
                    ("flowCalActualFlowValue", self.flowCalActualFlowValue),
                    ("pressureCalControl", self.pressureCalControl),
                    ("pressureCalState", self.pressureCalState),
                    ("pressureCalActualPressureValue", self.pressureCalActualPressureValue),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CALSTS", calibrationStatus)
                time.sleep(0.1)

                uploadStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("dasUploadControl", self.dasUploadControl),
                    ("dasUploadState", self.dasUploadState),
                    ("backgroundPeriodicReportUpload", self.backgroundPeriodicReportUpload),
                    ("reportUploadInterval", self.reportUploadInterval),
                    ("uploadReportToCloud", self.uploadReportToCloud),
                    ("reportGenerationUploadControl", self.reportGenerationUploadControl),
                    ("reportGenerationUploadState", self.reportGenerationUploadState),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "UPLOAD", uploadStatus)
                time.sleep(0.1)


                actionProgress = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("actionProgressTitle", self.actionProgressTitle),
                    ("actionProgressPercent", self.actionProgressPercent),
                    ("actionProgressCancel", self.actionProgressCancel),
                    ("actionProgressCancelEnable", self.actionProgressCancelEnable),
                    ("performingCalibration", self.performingCalibration),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ACTPROG", actionProgress)
                time.sleep(0.1)


                systemConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("svClockSpeedAdjust", self.svClockSpeedAdjust),
                    ("svLanguageSelect", self.svLanguageSelect),
                    ("foMaintenanceModeControl", self.foMaintenanceModeControl),
                    ("svMaintenanceModeTimeout", self.svMaintenanceModeTimeout),
                    ("svSerialNumber", self.svSerialNumber),
                    ("svI2cResetEnable", self.svI2cResetEnable),
                    ("svClockFormat", self.svClockFormat),
                    ("svSystemServiceInterval", self.svSystemServiceInterval),
                    ("svSystemTotalHours", self.svSystemTotalHours),
                    ("svSystemTimeSinceLastInterval", self.svSystemTimeSinceLastInterval),
                    ("svSystemServicePeriodClear", self.svSystemServicePeriodClear),
                    ("svDaylightSavingsEnable", self.svDaylightSavingsEnable),
                    ("svMachineId", self.svMachineId),
                    ("svLegacyComId", self.svLegacyComId),
                    ("svRs232Pass", self.svRs232Pass),
                    ("svCommandPrompt", self.svCommandPrompt),
                    ("svDasHoldOff", self.svDasHoldOff),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSCFG", systemConfig)
                time.sleep(0.1)

                aiReferenceInputs = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("aiDacChannel1", self.aiDacChannel1),
                    ("aiDacChannel2", self.aiDacChannel2),
                    ("aiDacChannel3", self.aiDacChannel3),
                    ("aiDacChannel4", self.aiDacChannel4),
                    ("aiExternalChannel1", self.aiExternalChannel1),
                    ("aiExternalChannel2", self.aiExternalChannel2),
                    ("aiExternalChannel3", self.aiExternalChannel3),
                    ("aiExternalChannel4", self.aiExternalChannel4),
                    ("aiExternalChannel5", self.aiExternalChannel5),
                    ("aiExternalChannel6", self.aiExternalChannel6),
                    ("aiExternalChannel7", self.aiExternalChannel7),
                    ("aiExternalChannel8", self.aiExternalChannel8),
                    ("aiRef4096Mv", self.aiRef4096Mv),
                    ("aiRefGround", self.aiRefGround),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AICHN", aiReferenceInputs)
                time.sleep(0.1)



                calibrationControl = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("calRange", self.calRange),
                    ("calSource", self.calSource),
                    ("concCalControl", self.concCalControl),
                    ("concCalState", self.concCalState),
                    ("oeTestControl", self.oeTestControl),
                    ("oeTestState", self.oeTestState),
                    ("etestMin", self.etestMin),
                    ("etestMax", self.etestMax),
                    ("otestMin", self.otestMin),
                    ("otestMax", self.otestMax),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CALCTRL", calibrationControl)
                time.sleep(0.1)


                digitalInputs = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("diMaintenanceMode", self.diMaintenanceMode),
                    ("placeholderTagBoolean", self.placeholderTagBoolean),
                    ("placeholderTagDouble", self.placeholderTagDouble),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DIGIN", digitalInputs)
                time.sleep(0.1)

                gasProps = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("svGasMolecularWeight", self.svGasMolecularWeight),
                    ("svGasStandardPressure", self.svGasStandardPressure),
                    ("svGasStandardTemperature", self.svGasStandardTemperature),
                    ("svRemoteCalMode", self.svRemoteCalMode),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "GASPROP", gasProps)
                time.sleep(0.1)


                sysStartupInfo = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("warmUpComplete", self.warmUpComplete),
                    ("driverVersion", self.driverVersion),
                    ("packageVersion", self.packageVersion),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSINFO", sysStartupInfo)
                time.sleep(0.1)

                configState = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("persistConfigControl", self.persistConfigControl),
                    ("persistConfigState", self.persistConfigState),
                    ("tagsFlushControl", self.tagsFlushControl),
                    ("tagsFlushState", self.tagsFlushState),
                    ("tagsFlushTimestamp", self.tagsFlushTimestamp),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CNFGST", configState)
                time.sleep(0.1)


                osInfo = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("osPlatform", self.osPlatform),
                    ("osVersion", self.osVersion),
                    ("cfnetVersion", self.cfnetVersion),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "OSINFO", osInfo)
                time.sleep(0.1)


                memoryUsage = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("systemTotalRam", self.systemTotalRam),
                    ("systemFreeRam", self.systemFreeRam),
                    ("systemUsedRam", self.systemUsedRam),
                    ("systemTotalDiskSize", self.systemTotalDiskSize),
                    ("systemAvailableDiskSpace", self.systemAvailableDiskSpace),
                    ("systemUsedDiskSpace", self.systemUsedDiskSpace),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MEMDISK", memoryUsage)
                time.sleep(0.1)


                networkSettings = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("networkAddressType", self.networkAddressType),
                    ("networkIpAddress", self.networkIpAddress),
                    ("networkSubnetMask", self.networkSubnetMask),
                    ("networkDefaultGateway", self.networkDefaultGateway),
                    ("networkDns1", self.networkDns1),
                    ("networkDns2", self.networkDns2),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "NETCFG", networkSettings)
                time.sleep(0.1)


                firmwareUpdate = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("refreshInstrumentSettings", self.refreshInstrumentSettings),
                    ("firmwareUpdateState", self.firmwareUpdateState),
                    ("firmwareUpdateResult", self.firmwareUpdateResult),
                    ("firmwareUpdateProgressPercent", self.firmwareUpdateProgressPercent),
                    ("firmwareUpdateErrorDetails", self.firmwareUpdateErrorDetails),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "FWUPDT", firmwareUpdate)
                time.sleep(0.1)

                configTransferStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("configDownloadUploadState", self.configDownloadUploadState),
                    ("configDownloadUploadResult", self.configDownloadUploadResult),
                    ("configDownloadUploadProgressPercent", self.configDownloadUploadProgressPercent),
                    ("configDownloadUploadErrorDetails", self.configDownloadUploadErrorDetails),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CFGXFER", configTransferStatus)
                time.sleep(0.1)


                remoteUpdate = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("remoteUpdateControl", self.remoteUpdateControl),
                    ("remoteUpdateState", self.remoteUpdateState),
                    ("remoteUpdateDownloadPercent", self.remoteUpdateDownloadPercent),
                    ("remoteUpdateVersion", self.remoteUpdateVersion),
                    ("remoteUpdateRequiredDiskSpace", self.remoteUpdateRequiredDiskSpace),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "REMOTE", remoteUpdate)
                time.sleep(0.1)


                hessenConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("hessenVariation", self.hessenVariation),
                    ("hessenResponseMode", self.hessenResponseMode),
                    ("hessenGasSelectControl", self.hessenGasSelectControl),
                    ("hessenGasSelectState", self.hessenGasSelectState),
                    ("hessenGasSelect", self.hessenGasSelect),
                    ("hessenGasCount", self.hessenGasCount),
                    ("hessenGasConfigControl", self.hessenGasConfigControl),
                    ("hessenGasConfigState", self.hessenGasConfigState),
                    ("hessenGasId", self.hessenGasId),
                    ("hessenGasRange", self.hessenGasRange),
                    ("hessenGasReported", self.hessenGasReported),
                    ("hessenGasName", self.hessenGasName),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "HESSEN", hessenConfig)
                time.sleep(0.1)


                aiExternalCal = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    
                    ("aiExternalChannel1Slope", self.aiExternalChannel1Slope),
                    ("aiExternalChannel1Offset", self.aiExternalChannel1Offset),
                    ("aiExternalChannel1Units", self.aiExternalChannel1Units),
                    ("aiExternalChannel1EngValue", self.aiExternalChannel1EngValue),

                    ("aiExternalChannel2Slope", self.aiExternalChannel2Slope),
                    ("aiExternalChannel2Offset", self.aiExternalChannel2Offset),
                    ("aiExternalChannel2Units", self.aiExternalChannel2Units),
                    ("aiExternalChannel2EngValue", self.aiExternalChannel2EngValue),

                    ("aiExternalChannel3Slope", self.aiExternalChannel3Slope),
                    ("aiExternalChannel3Offset", self.aiExternalChannel3Offset),
                    ("aiExternalChannel3Units", self.aiExternalChannel3Units),
                    ("aiExternalChannel3EngValue", self.aiExternalChannel3EngValue),

                    ("aiExternalChannel4Slope", self.aiExternalChannel4Slope),
                    ("aiExternalChannel4Offset", self.aiExternalChannel4Offset),
                    ("aiExternalChannel4Units", self.aiExternalChannel4Units),
                    ("aiExternalChannel4EngValue", self.aiExternalChannel4EngValue),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AICAL1", aiExternalCal)
                time.sleep(0.1)

                aiExternalCal2 = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),

                    ("aiExternalChannel5Slope", self.aiExternalChannel5Slope),
                    ("aiExternalChannel5Offset", self.aiExternalChannel5Offset),
                    ("aiExternalChannel5Units", self.aiExternalChannel5Units),
                    ("aiExternalChannel5EngValue", self.aiExternalChannel5EngValue),

                    ("aiExternalChannel6Slope", self.aiExternalChannel6Slope),
                    ("aiExternalChannel6Offset", self.aiExternalChannel6Offset),
                    ("aiExternalChannel6Units", self.aiExternalChannel6Units),
                    ("aiExternalChannel6EngValue", self.aiExternalChannel6EngValue),

                    ("aiExternalChannel7Slope", self.aiExternalChannel7Slope),
                    ("aiExternalChannel7Offset", self.aiExternalChannel7Offset),
                    ("aiExternalChannel7Units", self.aiExternalChannel7Units),
                    ("aiExternalChannel7EngValue", self.aiExternalChannel7EngValue),

                    ("aiExternalChannel8Slope", self.aiExternalChannel8Slope),
                    ("aiExternalChannel8Offset", self.aiExternalChannel8Offset),
                    ("aiExternalChannel8Units", self.aiExternalChannel8Units),
                    ("aiExternalChannel8EngValue", self.aiExternalChannel8EngValue),
                    ("aiExternalAnalogInputs", self.aiExternalAnalogInputs),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AICAL2", aiExternalCal2)
                time.sleep(0.1)




                concentrationAlarms = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("csfAlarm1Enable", self.csfAlarm1Enable),
                    ("csfAlarm1ConcLimit", self.csfAlarm1ConcLimit),
                    ("csfAlarm2Enable", self.csfAlarm2Enable),
                    ("csfAlarm2ConcLimit", self.csfAlarm2ConcLimit),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CALARM", concentrationAlarms)
                time.sleep(0.1)




                timeSyncStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("timeSync", self.timeSync),
                    ("timeSyncUseManual", self.timeSyncUseManual),
                    ("manualTimeServer", self.manualTimeServer),
                    ("timeSyncInterval", self.timeSyncInterval),
                    ("lastInstrumentTimeSynced", self.lastInstrumentTimeSynced),
                    ("nextInstrumentTimeSync", self.nextInstrumentTimeSync),
                    ("timeSyncControl", self.timeSyncControl),
                    ("dateTimeTargetValue", self.dateTimeTargetValue),
                    ("timeSyncState", self.timeSyncState),
                    ("timeSyncPassing", self.timeSyncPassing),
                    ("sysWarnTimeNotSynced", self.sysWarnTimeNotSynced),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "TIMESYNC", timeSyncStatus)
                time.sleep(0.1)



                calibrationRanges = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("mbZeroCalRange1", self.mbZeroCalRange1),
                    ("mbSpanCalRange1", self.mbSpanCalRange1),
                    ("mbZeroCalRange2", self.mbZeroCalRange2),
                    ("mbSpanCalRange2", self.mbSpanCalRange2),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CALRNG", calibrationRanges)
                time.sleep(0.1)

                loggerStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("nativeLogger", self.nativeLogger),
                    ("tagLogger", self.tagLogger),
                    ("tagLoggerEnable", self.tagLoggerEnable),
                    ("disableTagUpdatesFromNativeToManaged", self.disableTagUpdatesFromNativeToManaged),
                    ("disableTagUpdatesFromManagedToNative", self.disableTagUpdatesFromManagedToNative),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "LOGGER", loggerStatus)
                time.sleep(0.1)

                timeFormats = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("svAcLineFrequency", self.svAcLineFrequency),
                    ("dlIncludeUniversalTime", self.dlIncludeUniversalTime),
                    ("dlTimeFormat", self.dlTimeFormat),
                    ("systemTimeFormat", self.systemTimeFormat),
                    ("generalTimeFormat", self.generalTimeFormat),
                    ("alertsTimeFormat", self.alertsTimeFormat),
                    ("datalogTimeFormat", self.datalogTimeFormat),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "TIMEFMT", timeFormats)
                time.sleep(0.1)



                instrumentUpdate = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("instrumentShutdown", self.instrumentShutdown),
                    ("instrumentReset", self.instrumentReset),
                    ("periodicUpdateCheck", self.periodicUpdateCheck),
                    ("lastInstrumentUpdateCheck", self.lastInstrumentUpdateCheck),
                    ("packageVersionNeedingUpdate", self.packageVersionNeedingUpdate),
                    ("periodicUpdateFlag", self.periodicUpdateFlag),
                    ("sysInfoUpdateAvail", self.sysInfoUpdateAvail),
                    ("configResetFlag", self.configResetFlag),
                    ("sysWarnConfigReset", self.sysWarnConfigReset),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "UPDSTAT", instrumentUpdate)
                time.sleep(0.1)

                memoryPartitions = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
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
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MEMORY", memoryPartitions)
                time.sleep(0.1)


                homeMeters = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("homeMeter1", self.homeMeter1),
                    ("homeMeter2", self.homeMeter2),
                    ("homeMeter3", self.homeMeter3),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "HMETER", homeMeters)
                time.sleep(0.1)

                o3GenConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("o3Stability", self.o3Stability),
                    ("o3AdaptiveFilterActive", self.o3AdaptiveFilterActive),
                    ("o3GenDefaultSetpoint", self.o3GenDefaultSetpoint),
                    ("o3CacheResol", self.o3CacheResol),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "O3GENCFG", o3GenConfig)
                time.sleep(0.1)



                opticalParams = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                    
                    ("svPhotoPathLength", self.svPhotoPathLength),
                    ("svConversionTime", self.svConversionTime),
                    ("svDetectorConversionTime", self.svDetectorConversionTime),
                    ("svSlopeConstant", self.svSlopeConstant),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "OPTPARAM", opticalParams)
                time.sleep(0.1)


                photoLampCal = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("svPhotoZeroReading", self.svPhotoZeroReading),
                    ("svPhotoZeroActual", self.svPhotoZeroActual),
                    ("svPhotoSpanReading", self.svPhotoSpanReading),
                    ("svPhotoSpanActual", self.svPhotoSpanActual),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PHCAL", photoLampCal)
                time.sleep(0.1)




                systemCals = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("darkCalControl", self.darkCalControl),
                    ("darkCalState", self.darkCalState),
                    ("darkCalOffsetMeasured", self.darkCalOffsetMeasured),
                    ("autoLeakCheckControl", self.autoLeakCheckControl),
                    ("autoLeakCheckState", self.autoLeakCheckState),
                    ("backPresCompControl", self.backPresCompControl),
                    ("backPresCompState", self.backPresCompState),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSCAL", systemCals)
                time.sleep(0.1)

                o3CalStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("o3GenCalControl", self.o3GenCalControl),
                    ("o3GenCalState", self.o3GenCalState),
                    ("photoFlowCalControl", self.photoFlowCalControl),
                    ("photoFlowCalState", self.photoFlowCalState),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "O3CAL", o3CalStatus)
                time.sleep(0.1)

                o3BenchConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("svO3BenchOnlyInBenchMode", self.svO3BenchOnlyInBenchMode),
                    ("svAdaptiveFilterAsize", self.svAdaptiveFilterAsize),
                    ("svO3Slope", self.svO3Slope),
                    ("svO3Offset", self.svO3Offset),
                    ("svO3SlopeConstant", self.svO3SlopeConstant),
                    ("svO3TargetSpanConc", self.svO3TargetSpanConc),
                    ("svO3GenFlow", self.svO3GenFlow),
                    ("svO3BenchDelay", self.svO3BenchDelay),
                    ("svO3BenchAdjustmentFrequency", self.svO3BenchAdjustmentFrequency),
                    ("svO3BenchFilterSize", self.svO3BenchFilterSize),
                    ("svO3CacheUpdateStabilityLimit", self.svO3CacheUpdateStabilityLimit),
                    ("svO3BenchPidIntegral", self.svO3BenchPidIntegral),
                    ("svO3BenchPidDerivative", self.svO3BenchPidDerivative),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "O3BENCH", o3BenchConfig)
                time.sleep(0.1)

                cylinderConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("cylPort", self.cylPort),
                    ("cylGas1Name", self.cylGas1Name),
                    ("cylGas1Conc", self.cylGas1Conc),
                    ("cylGas1Units", self.cylGas1Units),
                    ("cylGas2Name", self.cylGas2Name),
                    ("cylGas2Conc", self.cylGas2Conc),
                    ("cylGas2Units", self.cylGas2Units),
                    ("cylGas3Name", self.cylGas3Name),
                    ("cylGas3Conc", self.cylGas3Conc),
                    ("cylGas3Units", self.cylGas3Units),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CYLGAS", cylinderConfig)
                time.sleep(0.1)




                gasAvailability = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("so2Avail", self.so2Avail),
                    ("h2sAvail", self.h2sAvail),
                    ("n2oAvail", self.n2oAvail),
                    ("noAvail", self.noAvail),
                    ("no2Avail", self.no2Avail),
                    ("nh3Avail", self.nh3Avail),
                    ("coAvail", self.coAvail),
                    ("co2Avail", self.co2Avail),
                    ("hcAvail", self.hcAvail),
                    ("usr1Avail", self.usr1Avail),
                    ("usr2Avail", self.usr2Avail),
                    ("usr3Avail", self.usr3Avail),
                    ("usr4Avail", self.usr4Avail),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "GASAVAIL", gasAvailability)
                time.sleep(0.1)



                calDriveConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("cal1Drive", self.cal1Drive),
                    ("cal2Drive", self.cal2Drive),
                    ("dilDrive", self.dilDrive),
                    ("cal1FlowRange", self.cal1FlowRange),
                    ("cal2FlowRange", self.cal2FlowRange),
                    ("dilFlowRange", self.dilFlowRange),
                    ("cal1Slope", self.cal1Slope),
                    ("cal2Slope", self.cal2Slope),
                    ("dilSlope", self.dilSlope),
                    ("cal1Offset", self.cal1Offset),
                    ("cal2Offset", self.cal2Offset),
                    ("dilOffset", self.dilOffset),
                    ("cal1SensorOffset", self.cal1SensorOffset),
                    ("cal2SensorOffset", self.cal2SensorOffset),
                    ("dilSensorOffset", self.dilSensorOffset),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CALDRV", calDriveConfig)
                time.sleep(0.1)


                calGasParams = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("gasGenerateCmdSource", self.gasGenerateCmdSource),
                    ("calGasO3GenMode", self.calGasO3GenMode),
                    ("outputABSelect", self.outputABSelect),
                    ("asfO3GenStabilizing", self.asfO3GenStabilizing),
                    ("calGasPriName", self.calGasPriName),
                    ("calGasPriTarget", self.calGasPriTarget),
                    ("calGasPriUnits", self.calGasPriUnits),
                    ("calGasO3Name", self.calGasO3Name),
                    ("calGasO3Target", self.calGasO3Target),
                    ("calGasO3Actual", self.calGasO3Actual),
                    ("calGasPriActual", self.calGasPriActual),
                    ("calGasO3Units", self.calGasO3Units),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CALGAS", calGasParams)
                time.sleep(0.1)


                sequenceConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("sequenceCount", self.sequenceCount),
                    ("sequenceSelect", self.sequenceSelect),
                    ("sequenceSelectControl", self.sequenceSelectControl),
                    ("sequenceSelectState", self.sequenceSelectState),
                    ("sequenceStepCount", self.sequenceStepCount),
                    ("sequenceName", self.sequenceName),
                    ("sequenceRepCount", self.sequenceRepCount),
                    ("sequenceCcinputEnable", self.sequenceCcinputEnable),
                    ("sequenceCcoutputEnable", self.sequenceCcoutputEnable),
                    ("sequenceTimerEnable", self.sequenceTimerEnable),
                    ("sequenceCcinputValue", self.sequenceCcinputValue),
                    ("sequenceCcoutputValue", self.sequenceCcoutputValue),
                    ("sequenceTimerStart", self.sequenceTimerStart),
                    ("sequenceTimerDelta", self.sequenceTimerDelta),
                    ("sequenceCcoutputDefaultValue", self.sequenceCcoutputDefaultValue),
                    ("sequenceConfigControl", self.sequenceConfigControl),
                    ("sequenceConfigState", self.sequenceConfigState),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SEQCFG", sequenceConfig)
                time.sleep(0.1)



                stepConfig = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                    ("stepSelect", self.stepSelect),
                    ("stepSelectControl", self.stepSelectControl),
                    ("stepSelectState", self.stepSelectState),
                    ("stepCcoutputEnable", self.stepCcoutputEnable),
                    ("stepCcoutputValue", self.stepCcoutputValue),
                    ("stepType", self.stepType),
                    ("stepCalGas", self.stepCalGas),
                    ("stepManCalGas", self.stepManCalGas),
                    ("stepCalFlow", self.stepCalFlow),
                    ("stepDilFlow", self.stepDilFlow),
                    ("stepTotalFlow", self.stepTotalFlow),
                    ("stepO3GenMode", self.stepO3GenMode),
                    ("stepO3GenMv", self.stepO3GenMv),
                    ("stepO3GenPpb", self.stepO3GenPpb),
                    ("stepDuration", self.stepDuration),
                    ("stepGasConc", self.stepGasConc),
                    ("stepGasUnits", self.stepGasUnits),
                    ("stepGptO3Conc", self.stepGptO3Conc),
                    ("stepGptO3Units", self.stepGptO3Units),
                    ("stepOutputSelect", self.stepOutputSelect),
                    ("stepExecseqSequenceName", self.stepExecseqSequenceName),
                    ("stepConfigControl", self.stepConfigControl),
                    ("stepConfigState", self.stepConfigState),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "STEPCFG", stepConfig)
                time.sleep(0.1)


                stepStatus = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                    ("stepStatusBlock1Enable", self.stepStatusBlock1Enable),
                    ("stepStatusBlock2Enable", self.stepStatusBlock2Enable),
                    ("stepStatusBlock1Value", self.stepStatusBlock1Value),
                    ("stepStatusBlock2Value", self.stepStatusBlock2Value),
                    ("stepExeclevLevelNumber", self.stepExeclevLevelNumber),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "STEPSTS", stepStatus)
                time.sleep(0.1)





                digitalOutputValves = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                     
                    ("doInputValve", self.doInputValve),
                    ("doInputValveDiagMode", self.doInputValveDiagMode),
                    ("doInputValveDiagSetpt", self.doInputValveDiagSetpt),
                    ("doRelayWatchdog", self.doRelayWatchdog),
                    ("doRelayWatchdogDiagMode", self.doRelayWatchdogDiagMode),
                    ("doRelayWatchdogDiagSetpt", self.doRelayWatchdogDiagSetpt),
                    ("doVentValve", self.doVentValve),
                    ("doVentValveDiagMode", self.doVentValveDiagMode),
                    ("doVentValveDiagSetpt", self.doVentValveDiagSetpt),
                    ("doGptValve", self.doGptValve),
                    ("doGptValveDiagMode", self.doGptValveDiagMode),
                    ("doGptValveDiagSetpt", self.doGptValveDiagSetpt),
                    ("doPermValve", self.doPermValve),
                    ("doPermValveDiagMode", self.doPermValveDiagMode),
                    ("doPermValveDiagSetpt", self.doPermValveDiagSetpt),
                    ("doO3PumpOn", self.doO3PumpOn),
                    ("doO3PumpOnDiagMode", self.doO3PumpOnDiagMode),
                    ("doO3PumpOnDiagSetpt", self.doO3PumpOnDiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "VALVECTL1", digitalOutputValves)
                time.sleep(0.1)

                heatersValves = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                     
                    ("doPhotoRefValve", self.doPhotoRefValve),
                    ("doPhotoRefValveDiagMode", self.doPhotoRefValveDiagMode),
                    ("doPhotoRefValveDiagSetpt", self.doPhotoRefValveDiagSetpt),
                    ("doValveWatchdog", self.doValveWatchdog),
                    ("doValveWatchdogDiagMode", self.doValveWatchdogDiagMode),
                    ("doValveWatchdogDiagSetpt", self.doValveWatchdogDiagSetpt),
                    ("doOutputValveB", self.doOutputValveB),
                    ("doOutputValveBDiagMode", self.doOutputValveBDiagMode),
                    ("doOutputValveBDiagSetpt", self.doOutputValveBDiagSetpt),
                    ("doPermHeater", self.doPermHeater),
                    ("doPermHeaterDiagMode", self.doPermHeaterDiagMode),
                    ("doPermHeaterDiagSetpt", self.doPermHeaterDiagSetpt),
                    ("doO3GenValve", self.doO3GenValve),
                    ("doO3GenValveDiagMode", self.doO3GenValveDiagMode),
                    ("doO3GenValveDiagSetpt", self.doO3GenValveDiagSetpt),
                    ("doPhotoLampHeater", self.doPhotoLampHeater),
                    ("doPhotoLampHeaterDiagMode", self.doPhotoLampHeaterDiagMode),
                    ("doPhotoLampHeaterDiagSetpt", self.doPhotoLampHeaterDiagSetpt),
                    ("doO3GenLampHeater", self.doO3GenLampHeater),
                    ("doO3GenLampHeaterDiagMode", self.doO3GenLampHeaterDiagMode),
                    ("doO3GenLampHeaterDiagSetpt", self.doO3GenLampHeaterDiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "VALVECTL2", heatersValves)
                time.sleep(0.1)



                aoTestDrives = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                     
                    ("aoTestOutput", self.aoTestOutput),
                    ("aoPhotoLampDrive", self.aoPhotoLampDrive),
                    ("aoO3GenDrive", self.aoO3GenDrive),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AODRIVE", aoTestDrives)
                time.sleep(0.1)




                cylinderPurgeControl = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                    ("doCylValve1", self.doCylValve1),
                    ("doCylValve1DiagMode", self.doCylValve1DiagMode),
                    ("doCylValve1DiagSetpt", self.doCylValve1DiagSetpt),
                    ("doCylValve2", self.doCylValve2),
                    ("doCylValve2DiagMode", self.doCylValve2DiagMode),
                    ("doCylValve2DiagSetpt", self.doCylValve2DiagSetpt),
                    ("doCylValve3", self.doCylValve3),
                    ("doCylValve3DiagMode", self.doCylValve3DiagMode),
                    ("doCylValve3DiagSetpt", self.doCylValve3DiagSetpt),
                    ("doCylValve4", self.doCylValve4),
                    ("doCylValve4DiagMode", self.doCylValve4DiagMode),
                    ("doCylValve4DiagSetpt", self.doCylValve4DiagSetpt),
                    ("doPurgeValve", self.doPurgeValve),
                    ("doPurgeValveDiagMode", self.doPurgeValveDiagMode),
                    ("doPurgeValveDiagSetpt", self.doPurgeValveDiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PURGECTL", cylinderPurgeControl)
                time.sleep(0.1)


            

                digitalControlOutputs = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                    ("doControlOut1", self.doControlOut1),
                    ("doControlOut1DiagMode", self.doControlOut1DiagMode),
                    ("doControlOut1DiagSetpt", self.doControlOut1DiagSetpt),
                    ("doControlOut2", self.doControlOut2),
                    ("doControlOut2DiagMode", self.doControlOut2DiagMode),
                    ("doControlOut2DiagSetpt", self.doControlOut2DiagSetpt),
                    ("doControlOut3", self.doControlOut3),
                    ("doControlOut3DiagMode", self.doControlOut3DiagMode),
                    ("doControlOut3DiagSetpt", self.doControlOut3DiagSetpt),
                    ("doControlOut4", self.doControlOut4),
                    ("doControlOut4DiagMode", self.doControlOut4DiagMode),
                    ("doControlOut4DiagSetpt", self.doControlOut4DiagSetpt),
                    ("doControlOut5", self.doControlOut5),
                    ("doControlOut5DiagMode", self.doControlOut5DiagMode),
                    ("doControlOut5DiagSetpt", self.doControlOut5DiagSetpt),
                    ("doControlOut6", self.doControlOut6),
                    ("doControlOut6DiagMode", self.doControlOut6DiagMode),
                    ("doControlOut6DiagSetpt", self.doControlOut6DiagSetpt),
                    ("doControlOut7", self.doControlOut7),
                    ("doControlOut7DiagMode", self.doControlOut7DiagMode),
                    ("doControlOut7DiagSetpt", self.doControlOut7DiagSetpt),
                    ("doControlOut8", self.doControlOut8),
                    ("doControlOut8DiagMode", self.doControlOut8DiagMode),
                    ("doControlOut8DiagSetpt", self.doControlOut8DiagSetpt),
                    ("doControlOut9", self.doControlOut9),
                    ("doControlOut9DiagMode", self.doControlOut9DiagMode),
                    ("doControlOut9DiagSetpt", self.doControlOut9DiagSetpt),
                    ("doControlOut10", self.doControlOut10),
                    ("doControlOut10DiagMode", self.doControlOut10DiagMode),
                    ("doControlOut10DiagSetpt", self.doControlOut10DiagSetpt),
                    ("doControlOut11", self.doControlOut11),
                    ("doControlOut11DiagMode", self.doControlOut11DiagMode),
                    ("doControlOut11DiagSetpt", self.doControlOut11DiagSetpt),
                    ("doControlOut12", self.doControlOut12),
                    ("doControlOut12DiagMode", self.doControlOut12DiagMode),
                    ("doControlOut12DiagSetpt", self.doControlOut12DiagSetpt),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DOCNTL", digitalControlOutputs)
                time.sleep(0.1)

                modbusSequenceFlags = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                    ("modbusUseUserUnits", self.modbusUseUserUnits),
                    ("modbusSequenceCoil", self.modbusSequenceCoil),
                    ("modbusPurge", self.modbusPurge),
                    ("modbusStandby", self.modbusStandby),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MODSEQ", modbusSequenceFlags)
                time.sleep(0.1)



                calibrationModes = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                    ("svUserUnits", self.svUserUnits),
                    ("svAdaptiveFilterSize", self.svAdaptiveFilterSize),
                    ("svAdaptiveFilterDelta", self.svAdaptiveFilterDelta),
                    ("svAdaptiveFilterPercent", self.svAdaptiveFilterPercent),
                    ("svAdaptiveFilterDelay", self.svAdaptiveFilterDelay),
                    ("svAdaptiveFilterEnable", self.svAdaptiveFilterEnable),
                    ("svStabilFreq", self.svStabilFreq),
                    ("svStabilSamples", self.svStabilSamples),
                    ("svAlarmTrigger", self.svAlarmTrigger),
                    ("svDriveStabilityLimit", self.svDriveStabilityLimit),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ADAPTIVE", calibrationModes)
                time.sleep(0.1)
                miscCalibrationFlags = OrderedDict([
                    ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                    ("svTpcEnable", self.svTpcEnable),
                    ("svDilutionFactor", self.svDilutionFactor),
                    ("foDilution", self.foDilution),
                    ("svRangeMode", self.svRangeMode),

                    ("acal1SeqActive", self.acal1SeqActive),
                    ("acal2SeqActive", self.acal2SeqActive),
                    ("acal3SeqActive", self.acal3SeqActive),

                    ("asfDynamicSpanWarning", self.asfDynamicSpanWarning),
                    ("asfDynamicZeroWarning", self.asfDynamicZeroWarning),
                    ("asfMultipointCalibrationMode", self.asfMultipointCalibrationMode),
                    ("asfCalHighSpanActive", self.asfCalHighSpanActive),
                    ("asfCalLowSpanActive", self.asfCalLowSpanActive),
                    ("asfCalZeroActive", self.asfCalZeroActive),
                    ("asfHessenManualMode", self.asfHessenManualMode),
                    ("asfHighAutoRange", self.asfHighAutoRange),
                ])
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MISCAL", miscCalibrationFlags)
                time.sleep(0.1)


                # List Separators
                # CAL1 Flow
                cal1FlowList = [float(val) for val in self.cal1FlowTable.split(',')]
                calBlock1Flow = OrderedDict()
                calBlock1Flow["dateTime"] = dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')
                for i, val in enumerate(cal1FlowList):
                    calBlock1Flow[f"cal1Flow_{i}"] = val
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CAL1FLW", calBlock1Flow)
                time.sleep(0.1)

                cal1DriveList = [float(val) for val in self.cal1DriveTable.split(',')]
                calBlock1Drive = OrderedDict()
                calBlock1Drive["dateTime"] = dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')
                for i, val in enumerate(cal1DriveList):
                    calBlock1Drive[f"cal1Drive_{i}"] = val
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CAL1DRV", calBlock1Drive)
                time.sleep(0.1)

                cal2FlowList = [float(val) for val in self.cal2FlowTable.split(',')]
                calBlock2Flow = OrderedDict()
                calBlock2Flow["dateTime"] = dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')
                for i, val in enumerate(cal2FlowList):
                    calBlock2Flow[f"cal2Flow_{i}"] = val
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CAL2FLW", calBlock2Flow)
                time.sleep(0.1)

                cal2DriveList = [float(val) for val in self.cal2DriveTable.split(',')]
                calBlock2Drive = OrderedDict()
                calBlock2Drive["dateTime"] = dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')
                for i, val in enumerate(cal2DriveList):
                    calBlock2Drive[f"cal2Drive_{i}"] = val
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "CAL2DRV", calBlock2Drive)
                time.sleep(0.1)

                dilFlowList = [float(val) for val in self.dilFlowTable.split(',')]
                dilBlockFlow = OrderedDict()
                dilBlockFlow["dateTime"] = dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')
                for i, val in enumerate(dilFlowList):
                    dilBlockFlow[f"dilFlow_{i}"] = val
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DILFLW", dilBlockFlow)
                time.sleep(0.1)

                dilDriveList = [float(val) for val in self.dilDriveTable.split(',')]
                dilBlockDrive = OrderedDict()
                dilBlockDrive["dateTime"] = dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')
                for i, val in enumerate(dilDriveList):
                    dilBlockDrive[f"dilDrive_{i}"] = val
                mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DILDRV", dilBlockDrive)
                time.sleep(0.1)


            #-----------------------------------------
            # Continous Capture 

            modbusOutputs = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),   
                ("modbusControlOutput0", self.modbusControlOutput0),
                ("modbusControlOutput1", self.modbusControlOutput1),
                ("modbusControlOutput2", self.modbusControlOutput2),
                ("modbusControlOutput3", self.modbusControlOutput3),
                ("modbusControlOutput4", self.modbusControlOutput4),
                ("modbusControlOutput5", self.modbusControlOutput5),
                ("modbusControlOutput6", self.modbusControlOutput6),
                ("modbusControlOutput7", self.modbusControlOutput7),
                ("modbusControlOutput8", self.modbusControlOutput8),
                ("modbusControlOutput9", self.modbusControlOutput9),
                ("modbusControlOutput10", self.modbusControlOutput10),
                ("modbusControlOutput11", self.modbusControlOutput11),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MODOUT", modbusOutputs)
            time.sleep(0.1)

            digitalInputs = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("diControlIn1", self.diControlIn1),
                ("diControlIn2", self.diControlIn2),
                ("diControlIn3", self.diControlIn3),
                ("diControlIn4", self.diControlIn4),
                ("diControlIn5", self.diControlIn5),
                ("diControlIn6", self.diControlIn6),
                ("diControlIn7", self.diControlIn7),
                ("diControlIn8", self.diControlIn8),
                ("diControlIn9", self.diControlIn9),
                ("diControlIn10", self.diControlIn10),
                ("diControlIn11", self.diControlIn11),
                ("diControlIn12", self.diControlIn12),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "DICNTL", digitalInputs)
            time.sleep(0.1)            

            asfMfcWarnings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                     
                ("asfMfcPressureWarning", self.asfMfcPressureWarning),
                ("asfMfcFlowWarning", self.asfMfcFlowWarning),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "MFCWARN", asfMfcWarnings)
            time.sleep(0.1)

            sysFinalWarnings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),   
                ("sysWarnRegPress", self.sysWarnRegPress),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "REGWARN", sysFinalWarnings)
            time.sleep(0.1)

            permeationConfig = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("svPerm1Rate", self.svPerm1Rate),
                ("svPerm1GasType", self.svPerm1GasType),
                ("svPerm1Flow", self.svPerm1Flow),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PERMGAS", permeationConfig)
            time.sleep(0.1)


            aiTemperatureAndFlow = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),   
                ("aiMeasDetector", self.aiMeasDetector),
                ("aiRefDetector", self.aiRefDetector),
                ("aiPhotoDetectorUi", self.aiPhotoDetectorUi),
                ("aiO3GenRefDetector", self.aiO3GenRefDetector),
                ("aiSamplePressureRaw", self.aiSamplePressureRaw),
                ("aiSampleFlowRaw", self.aiSampleFlowRaw),
                ("aiSampleFlow", self.aiSampleFlow),
                ("photoFlowCalActualFlowValue", self.photoFlowCalActualFlowValue),
                ("aiTestInput7", self.aiTestInput7),
                ("aiTestInput8", self.aiTestInput8),
                ("aiBoxTempRaw", self.aiBoxTempRaw),
                ("aiBoxTempC", self.aiBoxTempC),
                ("aiSampleTempRaw", self.aiSampleTempRaw),
                ("aiSampleTempC", self.aiSampleTempC),
                ("aiPhotoLampTempRaw", self.aiPhotoLampTempRaw),
                ("aiPhotoLampTempC", self.aiPhotoLampTempC),
                ("aiO3GenLampTempRaw", self.aiO3GenLampTempRaw),
                ("aiO3GenLampTempC", self.aiO3GenLampTempC),
                ("aiTempInput6Raw", self.aiTempInput6Raw),
                ("aiTempInput6TempC", self.aiTempInput6TempC),
                ("aiTempInput7Raw", self.aiTempInput7Raw),
                ("aiTempInput7TempC", self.aiTempInput7TempC),
                ("aiPermeationTubeTempC", self.aiPermeationTubeTempC),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AITEMP", aiTemperatureAndFlow)
            time.sleep(0.1)

            finalSystemState = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("instMode", self.instMode),
                ("autoTargConc", self.autoTargConc),
                ("autoTargGasName", self.autoTargGasName),
                ("autoTargTotalFlow", self.autoTargTotalFlow),
                ("autoTargGasUnits", self.autoTargGasUnits),
                
                ("manTargGasName", self.manTargGasName),
                ("manTargCalFlow", self.manTargCalFlow),
                ("manTargDilFlow", self.manTargDilFlow),
                ("manO3GenMode", self.manO3GenMode),
                ("manO3GenMv", self.manO3GenMv),
                ("manO3GenPpb", self.manO3GenPpb),

                ("gptNoTargConc", self.gptNoTargConc),
                ("gptO3TargConc", self.gptO3TargConc),
                ("gptTargTotalFlow", self.gptTargTotalFlow),
                ("gptO3TargUnits", self.gptO3TargUnits),
                ("gptNoTargUnits", self.gptNoTargUnits),

                ("foHighConc", self.foHighConc),
                ("foDilHighPress", self.foDilHighPress),
                ("foFlowCorrect", self.foFlowCorrect),
                ("foDualGasOutput", self.foDualGasOutput),
                ("foDualDiluentInput", self.foDualDiluentInput),
                ("foGasBlending", self.foGasBlending),
                ("fo3mfc", self.fo3mfc),

                ("homeMeter1", self.homeMeter1),
                ("homeMeter2", self.homeMeter2),
                ("homeMeter3", self.homeMeter3),
                ("o3MinConc", self.o3MinConc),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "FINAL", finalSystemState)
            time.sleep(0.1)



            asfWarnings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("asfValveboardWarning", self.asfValveboardWarning),
                ("asfAnalogoutputWarning", self.asfAnalogoutputWarning),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ASFWARN1", asfWarnings)
            time.sleep(0.1)


            asfSystemStatus = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("asfAnalogCalibrationWarning", self.asfAnalogCalibrationWarning),
                ("asfBoxTempWarning", self.asfBoxTempWarning),
                ("asfDiagnosticMode", self.asfDiagnosticMode),
                ("asfDiagnosticModeActive", self.asfDiagnosticModeActive),
                ("asfDiagnosticSignalIo", self.asfDiagnosticSignalIo),
                ("asfFlowAlarm", self.asfFlowAlarm),
                ("asfFrontPanelWarning", self.asfFrontPanelWarning),
                ("asfMaintenanceModeSoftware", self.asfMaintenanceModeSoftware),
                ("asfMaintenanceModeSwitch", self.asfMaintenanceModeSwitch),
                ("asfModbusSystemOk", self.asfModbusSystemOk),
                ("asfRearboardWarning", self.asfRearboardWarning),
                ("asfRelayboardWarning", self.asfRelayboardWarning),
                ("asfSetupMode", self.asfSetupMode),
                ("asfSystemFaultWarning", self.asfSystemFaultWarning),
                ("asfSystemOk", self.asfSystemOk),
                ("asfSystemOk2", self.asfSystemOk2),
                ("asfSystemResetWarning", self.asfSystemResetWarning),
                ("asfTemperatureAlarm", self.asfTemperatureAlarm),
                ("asfSystemServiceWarning", self.asfSystemServiceWarning),
                ("asfZeroCalibrationMode", self.asfZeroCalibrationMode),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ASFSTS", asfSystemStatus)
            time.sleep(0.1)


            sysWarnings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),   
                ("sysWarnAnalogCal", self.sysWarnAnalogCal),
                ("sysWarnRearboard", self.sysWarnRearboard),
                ("sysWarnRelayboard", self.sysWarnRelayboard),
                ("sysWarnReset", self.sysWarnReset),
                ("sysWarnFrontPanel", self.sysWarnFrontPanel),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSWRN", sysWarnings)
            time.sleep(0.1)

            aoWarnings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("aoOutput1CalWarnState", self.aoOutput1CalWarnState),
                ("aoOutput2CalWarnState", self.aoOutput2CalWarnState),
                ("aoOutput3CalWarnState", self.aoOutput3CalWarnState),
                ("aoOutput4CalWarnState", self.aoOutput4CalWarnState),
                ("sysWarnAoOutput4Cal", self.sysWarnAoOutput4Cal),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "AOWRN", aoWarnings)
            time.sleep(0.1)

            asfDiagnosticFlags = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("foExtAnalogIn", self.foExtAnalogIn),
                ("asfSampFlowWarnFlag", self.asfSampFlowWarnFlag),
                ("asfCalMpFlag", self.asfCalMpFlag),
                ("asfCalZeroFlag", self.asfCalZeroFlag),
                ("asfCalSpanFlag", self.asfCalSpanFlag),
                ("asfCalLowSpanFlag", self.asfCalLowSpanFlag),
                ("asfManualModeFlag", self.asfManualModeFlag),
                ("asfSysResetFlag", self.asfSysResetFlag),
                ("asfPpbUnitsFlag", self.asfPpbUnitsFlag),
                ("asfPpmUnitsFlag", self.asfPpmUnitsFlag),
                ("asfUgmUnitsFlag", self.asfUgmUnitsFlag),
                ("asfMgmUnitsFlag", self.asfMgmUnitsFlag),
                ("asfSysServiceFlag", self.asfSysServiceFlag),
                ("asfBoxTempWarnFlag", self.asfBoxTempWarnFlag),
                ("asfRelayBoardWarnFlag", self.asfRelayBoardWarnFlag),
                ("asfFrontPanelWarnFlag", self.asfFrontPanelWarnFlag),
                ("asfRearBoardWarnFlag", self.asfRearBoardWarnFlag),
                ("asfAnalogCalWarnFlag", self.asfAnalogCalWarnFlag),
                ("asfInvalidConcFlag", self.asfInvalidConcFlag),
                ("asfDynZeroWarnFlag", self.asfDynZeroWarnFlag),
                ("asfDynSpanWarnFlag", self.asfDynSpanWarnFlag),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ASFBIT", asfDiagnosticFlags)
            time.sleep(0.1)

            asfWarnings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),   
                ("asfO3GenRefWarning", self.asfO3GenRefWarning),
                ("asfO3GenLampIntWarning", self.asfO3GenLampIntWarning),
                ("asfGenLampTempWarning", self.asfGenLampTempWarning),
                ("asfPhotoRefWarning", self.asfPhotoRefWarning),
                ("asfPhotoLampStabilityWarning", self.asfPhotoLampStabilityWarning),
                ("asfPhotoLampTempWarning", self.asfPhotoLampTempWarning),
                ("asfSampleTempWarning", self.asfSampleTempWarning),
                ("asfSampleFlowWarning", self.asfSampleFlowWarning),
                ("asfSamplePressureWarning", self.asfSamplePressureWarning),
                ("asfLampDriverWarning", self.asfLampDriverWarning),
                ("asfInvalidConcentrationWarning", self.asfInvalidConcentrationWarning),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ASFWARN2", asfWarnings)
            time.sleep(0.1)


            sysWarningsDetailed = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("sysWarnPhotoReference", self.sysWarnPhotoReference),
                ("sysWarnSamplePressure", self.sysWarnSamplePressure),
                ("sysWarnSampleTemp", self.sysWarnSampleTemp),
                ("sysWarnBoxTemp", self.sysWarnBoxTemp),
                ("sysWarnO3GenLampTemp", self.sysWarnO3GenLampTemp),
                ("sysWarnPhotoTemp", self.sysWarnPhotoTemp),
                ("sysWarnPhotoLampStability", self.sysWarnPhotoLampStability),
                ("sysWarnO3GenRef", self.sysWarnO3GenRef),
                ("sysWarnO3GenLamp", self.sysWarnO3GenLamp),
                ("sysWarnLampDriver", self.sysWarnLampDriver),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSWRND", sysWarningsDetailed)
            time.sleep(0.1)


            sysWarnAoCal = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("sysWarnAoOutput1Cal", self.sysWarnAoOutput1Cal),
                ("sysWarnAoOutput2Cal", self.sysWarnAoOutput2Cal),
                ("sysWarnAoOutput3Cal", self.sysWarnAoOutput3Cal),
                ("sysWarnAoOutput4Cal", self.sysWarnAoOutput4Cal),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSWRNDCAL", sysWarnAoCal)
            time.sleep(0.1)



            sysWarnings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("sysWarnAoOutput1Cal", self.sysWarnAoOutput1Cal),
                ("sysWarnAoOutput2Cal", self.sysWarnAoOutput2Cal),
                ("sysWarnAoOutput3Cal", self.sysWarnAoOutput3Cal),
                ("sysWarnAoOutput4Cal", self.sysWarnAoOutput4Cal),
                ("sysWarnMfcPress", self.sysWarnMfcPress),
                # Add other similar sysWarn flags here
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "SYSWARN", sysWarnings)
            time.sleep(0.1)


            o3CalSummary = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("o3SpanCalConc", self.o3SpanCalConc),
                ("o3GenCalActualValue", self.o3GenCalActualValue),
                ("asfConcentrationValid", self.asfConcentrationValid),
                ("asfLampAlarm", self.asfLampAlarm),
                ("asfPressureAlarm", self.asfPressureAlarm),
                ("asfCalActive", self.asfCalActive),
                ("asfDiagModeActive", self.asfDiagModeActive),
                ("asfO3genStatus", self.asfO3genStatus),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "O3CALSUM", o3CalSummary)
            time.sleep(0.1)

            o3LampPidSettings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("svO3GenMode", self.svO3GenMode),
                ("svO3GenLamp", self.svO3GenLamp),
                ("svO3LampCycle", self.svO3LampCycle),
                ("svO3LampProp", self.svO3LampProp),
                ("svO3LampInteg", self.svO3LampInteg),
                ("svO3LampDeriv", self.svO3LampDeriv),
                ("svO3ReferencePidIntegralCoefficient", self.svO3ReferencePidIntegralCoefficient),
                ("svO3PidDerivativeCoefficeint", self.svO3PidDerivativeCoefficeint),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "O3PID", o3LampPidSettings)
            time.sleep(0.1)

            flowAndSampling = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("svTotalFlow", self.svTotalFlow),
                ("svSampleFlowSlope", self.svSampleFlowSlope),
                ("svSampleTempSetpoint", self.svSampleTempSetpoint),
                ("svO3DwellTime", self.svO3DwellTime),
                ("svO3SampleTime", self.svO3SampleTime),
                ("svO3DarkOffset", self.svO3DarkOffset),
                ("svO3ConcFilterSize", self.svO3ConcFilterSize),
                ("svO3GenRefDelay", self.svO3GenRefDelay),
                ("svO3GenRefAdjustmentFrequency", self.svO3GenRefAdjustmentFrequency),
                ("svO3ReferenceFilterSize", self.svO3ReferenceFilterSize),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "FLOWCFG", flowAndSampling)
            time.sleep(0.1)


            activeSequence = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                
                ("activeSequenceName", self.activeSequenceName),
                ("activeSequenceStepSelect", self.activeSequenceStepSelect),
                ("activeActionName", self.activeActionName),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "ACTSEQ", activeSequence)
            time.sleep(0.1)

            levelConfig = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("levelCount", self.levelCount),
                ("levelSelect", self.levelSelect),
                ("levelSelectControl", self.levelSelectControl),
                ("levelSelectState", self.levelSelectState),
                ("levelNumber", self.levelNumber),
                ("levelStatusBlock1Enable", self.levelStatusBlock1Enable),
                ("levelStatusBlock2Enable", self.levelStatusBlock2Enable),
                ("levelStatusBlock1Value", self.levelStatusBlock1Value),
                ("levelStatusBlock2Value", self.levelStatusBlock2Value),
                ("levelStepType", self.levelStepType),
                ("levelConfigControl", self.levelConfigControl),
                ("levelConfigState", self.levelConfigState),
                ("levelCalGas", self.levelCalGas),
                ("levelGasConc", self.levelGasConc),
                ("levelGasUnits", self.levelGasUnits),
                ("levelGptO3Conc", self.levelGptO3Conc),
                ("levelGptO3Units", self.levelGptO3Units),
                ("levelManCalGas", self.levelManCalGas),
                ("levelCalFlow", self.levelCalFlow),
                ("levelDilFlow", self.levelDilFlow),
                ("levelTotalFlow", self.levelTotalFlow),
                ("levelO3GenMode", self.levelO3GenMode),
                ("levelO3GenMv", self.levelO3GenMv),
                ("levelO3GenPpb", self.levelO3GenPpb),
                ("execlevLevelNumber", self.execlevLevelNumber),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "LVLCFG", levelConfig)
            time.sleep(0.1)
            
            benchCal = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("benchCalControl", self.benchCalControl),
                ("benchCalState", self.benchCalState),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "BENCHCAL", benchCal)
            time.sleep(0.1)


            pressureCal = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("calGasPressureCalControl", self.calGasPressureCalControl),
                ("calGasPressureCalState", self.calGasPressureCalState),
                ("calGasPressureCalActualPressureValue", self.calGasPressureCalActualPressureValue),

                ("diluentPressureCalControl", self.diluentPressureCalControl),
                ("diluentPressureCalState", self.diluentPressureCalState),
                ("diluentPressureCalActualPressureValue", self.diluentPressureCalActualPressureValue),

                ("o3PressureCalControl", self.o3PressureCalControl),
                ("o3PressureCalState", self.o3PressureCalState),
                ("o3PressureCalActualPressureValue", self.o3PressureCalActualPressureValue),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PRESCAL", pressureCal)
            time.sleep(0.1)


            portGasGenState = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),                   
                ("portConfigControl", self.portConfigControl),
                ("portConfigState", self.portConfigState),
                ("gasGenerateControl", self.gasGenerateControl),
                ("gasGenerateState", self.gasGenerateState),
                ("gasGenerateMode", self.gasGenerateMode),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PORTGEN", portGasGenState)
            time.sleep(0.1)



            pressureReadings = OrderedDict([
                ("dateTime", dateTime.strftime('%Y-%m-%d %H:%M:%S.%f')),
                ("aiDiluentPressureRaw", self.aiDiluentPressureRaw),
                ("aiDiluentPressureUnits", self.aiDiluentPressureUnits),
                ("aiCalGasPressureRaw", self.aiCalGasPressureRaw),
                ("aiCalGasPressureUnits", self.aiCalGasPressureUnits),
                ("aiO3PressureRaw", self.aiO3PressureRaw),
                ("aiO3PressureUnits", self.aiO3PressureUnits),
                ("aiPermeationTubePressureRaw", self.aiPermeationTubePressureRaw),
                ("aiPermeationTubePressureUnits", self.aiPermeationTubePressureUnits),
            ])
            mSR.sensorFinisher(dateTime, self.sensorIDPreAPI + "PRESSURE", pressureReadings)
            time.sleep(0.1)

            return True

        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return False

    def continousRead(self, loopInterval=10, duration=None, debugModeActive=False):
        """
        Continuously reads from the T700 monitor, either indefinitely or for a specified duration.

        Args:
            loopInterval (float): Time in seconds between each iteration.
            duration (float or None): Total duration in seconds. If None, loop runs indefinitely.
            debugModeActive (bool): Whether to print register data for debugging.
        """

        startTime = time.time()
        startUp   = True
        try:
            while True:
                iterationStart = time.time()

                if duration is not None and (iterationStart - startTime) > duration:
                    print("[INFO] Duration reached. Stopping read loop.")
                    break

                print("======= T700 ========")

                read = self.read_api(startUp=startUp)
                startUp = False

                if read:
                    print("[T700] API Read Successfully")
                time.sleep(1)

                read, data = self.read_discrete_inputs()
                if read:
                    print("[T700] Discrete Inputs Read Successfully")
                    if debugModeActive:
                        print("[T700] Discrete Inputs:", data)
                time.sleep(1)

                read, data = self.read_input_registers()
                if read:
                    print("[T700] Input Registers Read Successfully")
                    if debugModeActive:
                        print("[T700] Input Registers:", data)
                time.sleep(1)

                read, data = self.read_coils()
                if read:
                    print("[T700] Coils Read Successfully")
                    if debugModeActive:
                        print("[T700] Coils:", data)
                time.sleep(1)

                mSR.delayMints(time.time() - iterationStart, loopInterval)

        except KeyboardInterrupt:
            print("\n[INFO] Keyboard interrupt received. Stopping read loop.")
        except Exception as e:
            print("[ERROR] Exception during continousRead:", e)
            time.sleep(loopInterval)


