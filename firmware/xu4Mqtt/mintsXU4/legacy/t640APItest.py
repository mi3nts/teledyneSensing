import requests
import time
import json
# Define the URL
url = "http://192.168.31.9:8180/api/taglist"

while True:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Find the max lengths for alignment
        max_name_len = max(len(tag["name"]) for tag in data["tags"])
        max_value_len = max(len(str(tag["value"])) for tag in data["tags"])

        for tag in data["tags"]:

            name = tag["name"]
            value = str(tag["value"])
            # description = tag.get("Description", "N/A")  # fallback if description is missing
            properties_str = tag.get("properties", "{}")
            properties = json.loads(properties_str)
            description = properties.get("Description", "N/A")
            print(f"{name:<{35}} : {value:<{30}} : {description} ")
        
        print("=" * 60)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    time.sleep(10)  # Avoid hammering the endpoint


    # self.opcRtLedTemp = 33.3917999267578
    # self.aiSamplePressureUnits = 97.5987777709961
    # self.opcRtHumidity = 51.5266990661621
    # self.opcRtSlValue = 62.2297

    # self.numConc = 262.743858619731

    # self.pm10Conc = 12.114873
    # self.pm25Conc = 8.73126
    # self.pm1Conc = 8.619372
    # self.pmtotConc = 0
    # self.pm10stpConc = 12.4410073925551
    # self.pm25stpConc = 8.96630696882423
    # self.pm1stpConc = 8.85140692528781
    # self.pmtotstpConc = 0
    # self.opcSvP3Value = 49
    # self.opcRtBoxTemp = 24.798095703125
    # self.opcRtOutsideTemp = 21.7517318725586
    # self.opcRtPwmPump = 30.1410083770752
    # self.opcRtPwmValve = 0
    # self.opcRtSampTemp = 22.9777793884277
    # self.pmcConc = 3.383613
    # self.opcRtAmplitudeCounts = 99020
    # self.opcRtLengthCounts = 99020

    # self.pm101hrAvg = 11.357456175
    # self.pm1012hrAvg = 5.76120316875
    # self.pm1024hrAvg = 3.71812814999999
    # self.pm251hrAvg = 8.096204025
    # self.pm2512hrAvg = 4.32960703125
    # self.pm2524hrAvg = 2.85303369375
    # self.pm11hrAvg = 7.989527475
    # self.pm112hrAvg = 4.26827814375
    # self.pm124hrAvg = 2.79709524375
    # self.pmtot1hrAvg = 0
    # self.pmtot12hrAvg = 0
    # self.pmtot24hrAvg = 0
    # self.pmc1hrAvg = 3.260094975
    # self.pmc12hrAvg = 1.43240158125
    # self.pmc24hrAvg = 0.866159362499999
    # self.pm10stp1hrAvg = 11.6984145082451
    # self.pm10stp12hrAvg = 5.9038692123543
    # self.pm10stp24hrAvg = 3.80584681830719
    # self.pm25stp1hrAvg = 8.33893480365088
    # self.pm25stp12hrAvg = 4.43498184123602
    # self.pm25stp24hrAvg = 2.91852406896147
    # self.pm1stp1hrAvg = 8.22997091045819
    # self.pm1stp12hrAvg = 4.37115673083863
    # self.pm1stp24hrAvg = 2.86156799057753
    # self.pmtotstp1hrAvg = 0
    # self.pmtotstp12hrAvg = 0
    # self.pmtotstp24hrAvg = 0
    # self.totalFlow = 5.00574398040771


    # self.bin000 = 0
    # self.bin001 = 0
    # self.bin002 = 0
    # self.bin003 = 0
    # self.bin004 = 0
    # self.bin005 = 0
    # self.bin006 = 0
    # self.bin007 = 0
    # self.bin008 = 0
    # self.bin009 = 0
    # self.bin010 = 2
    # self.bin011 = 1
    # self.bin012 = 8
    # self.bin013 = 8
    # self.bin014 = 8
    # self.bin015 = 14
    # self.bin016 = 11
    # self.bin017 = 17
    # self.bin018 = 12
    # self.bin019 = 15
    # self.bin020 = 18
    # self.bin021 = 27
    # self.bin022 = 21
    # self.bin023 = 22
    # self.bin024 = 21
    # self.bin025 = 30
    # self.bin026 = 27
    # self.bin027 = 32
    # self.bin028 = 19
    # self.bin029 = 26
    # self.bin030 = 27
    # self.bin031 = 25
    # self.bin032 = 22
    # self.bin033 = 23
    # self.bin034 = 25
    # self.bin035 = 21
    # self.bin036 = 23
    # self.bin037 = 21
    # self.bin038 = 15
    # self.bin039 = 22
    # self.bin040 = 23
    # self.bin041 = 23
    # self.bin042 = 30
    # self.bin043 = 27
    # self.bin044 = 24
    # self.bin045 = 24
    # self.bin046 = 32
    # self.bin047 = 25
    # self.bin048 = 36
    # self.bin049 = 31
    # self.bin050 = 37
    # self.bin051 = 29
    # self.bin052 = 35
    # self.bin053 = 42
    # self.bin054 = 34
    # self.bin055 = 26
    # self.bin056 = 44
    # self.bin057 = 37
    # self.bin058 = 46
    # self.bin059 = 46
    # self.bin060 = 49
    # self.bin061 = 43
    # self.bin062 = 25
    # self.bin063 = 10
    # self.bin064 = 24
    # self.bin065 = 9
    # self.bin066 = 16
    # self.bin067 = 11
    # self.bin068 = 10
    # self.bin069 = 13
    # self.bin070 = 8
    # self.bin071 = 8
    # self.bin072 = 7
    # self.bin073 = 14
    # self.bin074 = 9
    # self.bin075 = 6
    # self.bin076 = 10
    # self.bin077 = 2
    # self.bin078 = 7
    # self.bin079 = 5
    # self.bin080 = 9
    # self.bin081 = 3
    # self.bin082 = 2
    # self.bin083 = 3
    # self.bin084 = 2
    # self.bin085 = 6
    # self.bin086 = 4
    # self.bin087 = 3
    # self.bin088 = 2
    # self.bin089 = 3
    # self.bin090 = 0
    # self.bin091 = 4
    # self.bin092 = 8
    # self.bin093 = 4
    # self.bin094 = 5
    # self.bin095 = 2
    # self.bin096 = 4
    # self.bin097 = 5
    # self.bin098 = 5
    # self.bin099 = 11
    # self.bin100 = 5
    # self.bin101 = 4
    # self.bin102 = 3
    # self.bin103 = 0
    # self.bin104 = 1
    # self.bin105 = 0
    # self.bin106 = 2
    # self.bin107 = 2
    # self.bin108 = 2
    # self.bin109 = 1
    # self.bin110 = 1
    # self.bin111 = 0
    # self.bin112 = 2
    # self.bin113 = 3
    # self.bin114 = 0
    # self.bin115 = 0
    # self.bin116 = 0
    # self.bin117 = 0
    # self.bin118 = 0
    # self.bin119 = 0
    # self.bin120 = 1
    # self.bin121 = 1
    # self.bin122 = 1
    # self.bin123 = 0
    # self.bin124 = 1
    # self.bin125 = 0
    # self.bin126 = 0
    # self.bin127 = 0
    # self.bin128 = 0
    # self.bin129 = 0
    # self.bin130 = 0
    # self.bin131 = 0
    # self.bin132 = 0
    # self.bin133 = 0
    # self.bin134 = 0
    # self.bin135 = 0
    # self.bin136 = 0
    # self.bin137 = 0
    # self.bin138 = 0
    # self.bin139 = 0
    # self.bin140 = 0
    # self.bin141 = 0
    # self.bin142 = 0
    # self.bin143 = 0
    # self.bin144 = 0
    # self.bin145 = 0
    # self.bin146 = 0
    # self.bin147 = 0
    # self.bin148 = 0
    # self.bin149 = 0
    # self.bin150 = 0
    # self.bin151 = 0
    # self.bin152 = 0
    # self.bin153 = 0
    # self.bin154 = 0
    # self.bin155 = 0
    # self.bin156 = 0
    # self.bin157 = 0
    # self.bin158 = 0
    # self.bin159 = 0
    # self.bin160 = 0
    # self.bin161 = 0
    # self.bin162 = 0
    # self.bin163 = 0
    # self.bin164 = 0
    # self.bin165 = 0
    # self.bin166 = 0
    # self.bin167 = 0
    # self.bin168 = 0
    # self.bin169 = 0
    # self.bin170 = 0
    # self.bin171 = 0
    # self.bin172 = 0
    # self.bin173 = 0
    # self.bin174 = 0
    # self.bin175 = 0
    # self.bin176 = 0
    # self.bin177 = 0
    # self.bin178 = 0
    # self.bin179 = 0
    # self.bin180 = 0
    # self.bin181 = 0
    # self.bin182 = 0
    # self.bin183 = 0
    # self.bin184 = 0
    # self.bin185 = 0
    # self.bin186 = 0
    # self.bin187 = 0
    # self.bin188 = 0
    # self.bin189 = 0
    # self.bin190 = 0
    # self.bin191 = 0
    # self.bin192 = 0
    # self.bin193 = 0
    # self.bin194 = 0
    # self.bin195 = 0
    # self.bin196 = 0
    # self.bin197 = 0
    # self.bin198 = 0
    # self.bin199 = 0
    # self.bin200 = 0
    # self.bin201 = 0
    # self.bin202 = 0
    # self.bin203 = 0
    # self.bin204 = 0
    # self.bin205 = 0
    # self.bin206 = 0
    # self.bin207 = 0
    # self.bin208 = 0
    # self.bin209 = 0
    # self.bin210 = 0
    # self.bin211 = 0
    # self.bin212 = 0
    # self.bin213 = 0
    # self.bin214 = 0
    # self.bin215 = 0
    # self.bin216 = 0
    # self.bin217 = 0
    # self.bin218 = 0
    # self.bin219 = 0
    # self.bin220 = 0
    # self.bin221 = 0
    # self.bin222 = 0
    # self.bin223 = 0
    # self.bin224 = 0
    # self.bin225 = 0
    # self.bin226 = 0
    # self.bin227 = 0
    # self.bin228 = 0
    # self.bin229 = 0
    # self.bin230 = 0
    # self.bin231 = 0
    # self.bin232 = 0
    # self.bin233 = 0
    # self.bin234 = 0
    # self.bin235 = 0
    # self.bin236 = 0
    # self.bin237 = 0
    # self.bin238 = 0
    # self.bin239 = 0
    # self.bin240 = 0
    # self.bin241 = 0
    # self.bin242 = 0
    # self.bin243 = 0
    # self.bin244 = 0
    # self.bin245 = 0
    # self.bin246 = 0
    # self.bin247 = 0
    # self.bin248 = 0
    # self.bin249 = 0
    # self.bin250 = 0
    # self.bin251 = 0
    # self.bin252 = 0
    # self.bin253 = 0
    # self.bin254 = 0
    # self.bin255 = 0


## To Be Updated 

## SVCOM1  
# self.svCom1Protocol = 'TAPI'
# self.svCom1ModemInitString = ''
# self.svCom1Baudrate = 115200
# self.svCom1Parity = 'NONE'
# self.svCom1Databits = 8
# self.svCom1Stopbits = 1

## SVCOM2
# self.svCom2Protocol = 'TAPI'
# self.svCom2ModemInitString = ''
# self.svCom2Baudrate = 115200
# self.svCom2Parity = 'NONE'
# self.svCom2Databits = 8
# self.svCom2Stopbits = 1
# self.svCom2ModemConnection = 0
# self.svCom2EnableQuietMode = 0
# self.svCom2EnableSecurity = 0
# self.svCom2EnableMultidrop = 0
# self.svCom2EnableRs485 = 0
# self.svCom2HandshakingMode = 'SOFTWARE'
# self.svCom2EnableCommandPromptDisplay = 0
# self.svCom2DisableEchoLineEditing = 0
# self.svCom2DisableHardwareErrorChecking = 0
# self.svCom2EnableHardwareFifo = 1
# self.svCom2Initialize = 0


## SVTCP 
# self.svTcp1Initialize = 1
# self.svTcp1Portnum = 3000
# self.svTcp1EnableSecurity = 0
# self.svTcp1EnableCommandPromptDisplay = 1
# self.svTcp2Initialize = 0
# self.svTcp2Portnum = 502


#SVPM 
# self.svPm10Disp = 1
# self.svPmcDisp = 1
# self.svPm10stpDisp = 0
# self.svPm25stpDisp = 0
# self.svPm1stpDisp = 0
# self.svPmtotstpDisp = 0


# SVINFO 
# self.svClockSpeedAdjust = 0
# self.svLanguageSelect = 'English'
# self.asfMaintenanceModeSoftware = 0
# self.sysWarnMaintenanceMode = 0
# self.svLatchWarning = 1
# self.svSerialNumber = 2131
# self.svClockFormat = 'TIME=%H:%M:%S'
# self.svSystemServiceInterval = 0
# self.svSystemTotalHours = 0
# self.svSystemTimeSinceLastInterval = 0
# self.svSystemServicePeriodClear = 0
# self.svDaylightSavingsEnable = 1
# self.svMachineId = 1
# self.svDasHoldOff = 15
# self.svUserPressureUnits = 'kPa'

#RAM
# self.systemTotalRam = 209992
# self.systemFreeRam = 138404
# self.systemUsedRam = 71588
# self.systemTotalDiskSize = 3849204
# self.systemAvailableDiskSpace = 3740380
# self.systemUsedDiskSpace = 108824

#NET 
# self.networkAddressType = 'DHCP'
# self.networkIpAddress = '192.168.31.9'
# self.networkSubnetMask = '255.255.255.0'
# self.networkDefaultGateway = '192.168.31.1'
# self.networkDns1 = '192.168.31.1'
# self.networkDns2 = 'N/A'

#FRM
# self.refreshInstrumentSettings = 0
# self.firmwareUpdateState = 'IDLE'
# self.firmwareUpdateResult = 'UNDEFINED'
# self.firmwareUpdateProgressPercent = 0
# self.firmwareUpdateErrorDetails = 'N/A'
# self.configDownloadUploadState = 'IDLE'
# self.configDownloadUploadResult = 'UNDEFINED'
# self.configDownloadUploadProgressPercent = 0
# self.configDownloadUploadErrorDetails = 'N/A'

#RMT
# self.remoteUpdateControl = 'NONE'
# self.remoteUpdateState = 'ERROR_UNKNOWN'
# self.remoteUpdateDownloadPercent = 100
# self.remoteUpdateVersion = ''
# self.remoteUpdateRequiredDiskSpace = 150000

#DNH
# self.dustCalControl = 'NONE'
# self.dustCalState = 'NONE'
# self.homeMeter1 = 'AI_SAMPLE_FLOW5'
# self.homeMeter2 = 'OPC_RT_OUTSIDE_TEMP'
# self.homeMeter3 = 'OPC_RT_HUMIDITY'

#SLK
# self.spanDev48hrAvg = -0.421205411458333
# self.leakcheckpm10Conc = 0
# self.leakcheckpm25Conc = 0
# self.leakCheckControl = 'IDLE'
# self.leakCheckState = 'IDLE'
# self.ks10 = 1
# self.ks25 = 1
# self.ks1 = 1
# self.kstot = 1
# self.ko10 = 0
# self.ko25 = 0
# self.ko1 = 0
# self.kotot = 0

#OPCSV
# self.opcSvOffsetAdjDelay = 2000
# self.opcSvPmtHvSetting = 1453
# self.opcSvPmtHvOffsetAdj = 0
# self.opcSvBcFiltSize = 60
# self.opcSvAcquisitionDuration = 10
# self.opcSvFlow5lpmOffset = 0
# self.opcSvFlow5lpmSlope = 0.992093920707703
# self.opcSvFlow1167lpmOffset = 0
# self.opcSvFlow1167lpmSlope = 1
# self.opcSvAmbPressSlope = 1.00817835330963
# self.opcSvRhControlSetpoint = 35
# self.opcSv5lFlowSetpoint = 5
# self.opcSv11lFlowSetpoint = 11.6700000762939
# self.opcSvAmbPressOffset = 0
# self.opcSvRhSlope = 1
# self.opcSvRhOffset = 0
# self.opcSvFanSetpoint = 20
# self.opcSvInstrumentSlope = 0.999
# self.opcSvOffsetCounts = 2148
# self.opcSvAutoAdjustEnable = 0
# self.opcSvPmtCalSetting = 1459
# self.opcSvLogInterval = 60000
# self.opcSvTempCompSlope = 0.17
# self.opcSvDustCalFiltSize = 1

#OPC
# self.opcSpanDeviation = -3.341995
# self.opcPm10stpTemp = 25
# self.opcPm10stpPressure = 760
# self.opcRtP3Calc = 48
# self.opcSensorStatus = 'OK'
# self.opcSensorMode = 'T640'
# self.opcAmbientTempOverride = 0
# self.opcHeaterStatus = 'ON'
# self.opcBoardFirmwareRev = 0.87
# self.opcHeaterControlEnable = 1
# self.opcPumpControl = 'AUTO'
# self.opcValveControl = 'AUTO'
# self.opcRtHeaterDuty = 100
# self.opcRtPumpSpeed = 1796
# self.opcUsbStorageState = 'IDLE'
# self.opcSensorState = 'MEASURING'
# self.opcZeroChannel = 132
# self.opcFastHistUpdate = 0
# self.opcSensorFirmwareRev = 'MMS-SLA 15,18-08-2015 09:55:5'
# self.opcSyslogFilesize = '1988.53 KB'
# self.opcDeleteSyslog = 0
# self.opcLengthPeakChannel = 62
# self.opcInstrumentWarning = 1
# self.opcInstrumentError = 0
# self.opcInstWarnMessage = 'sendGetHistogram Error, Count: 1'
# self.opcInstErrorMessage = 'TEST'
# self.opcCalPeakChannel = 0
# self.opcSystemFault = 0

#OPCSRL
# self.opcSerialPalasTimeoutCount = 0
# self.opcSerialSensorTimeoutCount = 0
# self.opcSerialTimeoutLimit = 15
# self.opcSerialTimeoutRetryPeriod = 90
# self.opcSerialTimeout = 0
# self.opcSerialResetEnable = 0

#FLOW 
# self.aiSampleFlow5 = 5.00574398040771
# self.flow5CalActualFlowValue = 4.99
# self.aiSampleFlow11 = 11.67
# self.flow11CalActualFlowValue = 11.67
# self.flow5CalControl = 'NONE'
# self.flow5CalState = 'IDLE'
# self.flow11CalControl = 'NONE'
# self.flow11CalState = 'IDLE'
# self.sensorCheckChannelCounts = 0
# self.sampleFlowWarn = 0
# self.bypassFlowWarn = 0
# self.sampFlowSlopeOor = 0
# self.bypsFlowSlopeOor = 0
# self.flow5Cv24hrAvg = 0.353138148103972
# self.flow11Cv24hrAvg = 0
# self.flowtotCv24hrAvg = 0.35496193274203

# DUST 
# self.dustCalEnhancedLog = 0
# self.dustCalOverride = 0
# self.dustCalStartTime = 'N/A'
# self.dustCalEndTime = 'N/A'
# self.dustCalActiveTime = 'N/A'
# self.dustCalActiveIndex = 0
# self.dustCalDwellTime = 1
# self.dustCalMinPeakCounts = 200

# DL
# self.dlIncludeUniversalTime = 1
# self.dlTimeFormat = '12HOUR'
# self.dlRepoChanged = 0
# self.dlLastDownloadTime = '12/31/1999 12:00:00'
# self.dlDasDownloadFrom = '2/27/2025 8:02:56 AM'
# self.dlDasDownloadT1 = '2/27/2025 8:02:56 AM'
# self.dlDasDownloadT2 = '3/27/2025 8:02:56 AM'
# self.dlFlush = 'IDLE'
# self.dlLastFlushed = '4/1/2025 8:42:23 PM'



# MMRY
# self.lowMemoryRestart = 0
# self.lowMemoryWarning = 0
# self.memoryTotal = 12850576
# self.memoryTee = 813048
# self.memoryHmi = 2431036
# self.memoryDl = 725108
# self.memoryAc = 0
# self.memoryEv = 1220564
# self.memoryMb = 1641016
# self.memoryWeb = 2765820
# self.memoryRu = 636536
# self.memoryOpc = 2617448

# TAG 
# self.tagEventSystem = 0
# self.tagEventTee = 0
# self.tagEventHmi = 0
# self.tagEventDl = 0
# self.tagEventEv = 0
# self.tagEventMb = 0
# self.tagEventWeb = 0
# self.tagEventRu = 0
# self.tagEventOpc = 0
# self.tagsFlushControl = 'NONE'
# self.tagsFlushState = 'SUCCESS'
# self.tagsFlushTimestamp = '4/1/2025 8:42:25 PM'


#CHCK
# self.checkLed = 0
# self.checkPmt = 0
# self.checkIntPump = 0
# self.checkExtPump = 0

#LINF
# self.instMode = 'SAMPLE'
# self.sampleTempWarn = 0
# self.boxTempWarn = 0
# self.sampleRhHigh = 0
# self.sampPresSlopeOor = 0
# self.spanDevOor = 0
# self.placeholderTagBoolean = 0
# self.placeholderTagDouble = 0
# self.warmUpComplete = 0

#SYSW
# self.sysWarnSystemFault = 0
# self.sysWarnInternalSerialTimeout = 0
# self.sysWarnReset = 0
# self.sysWarnTimeNotSynced = 0
# self.sysWarnMaintenanceMode = 0
# self.sysWarnConfigReset = 0
# self.asfSystemResetWarning = 1

# FOSD
# self.fo640x = 0
# self.foPm1 = 1
# self.foPmtot = 0
# self.foNonUsEpaFemMode = 0
# self.concValidFlag = 1
# self.hourAvgPctValid = 75

#TIME
# self.timeSync = 1
# self.timeSyncUseManual = 0
# self.manualTimeServer = ''
# self.timeSyncInterval = 2
# self.lastInstrumentTimeSynced = '04/01/2025 8:13:45 PM'
# self.nextInstrumentTimeSync = '04/01/2025 10:13:45 PM'
# self.timeSyncControl = 'NONE'
# self.timeSyncState = 'OK'
# self.timeSyncPassing = 0
# self.dateTimeTargetValue = ''

# COMM
# self.udpBroadcastEnable = 0
# self.udpBroadcastIp = '192.168.0.1'
# self.modbusUseUserUnits = 0

# INFO 
# self.driverVersion = ''
# self.packageVersion = '1.4.31.529'
# self.osPlatform = 'Windows CE'
# self.osVersion = 'PN:084750000, 1.0.3.92, 01/18/2017'
# self.cfnetVersion = '3.5.10010.0'
# self.nativeAppState = 'Undefined'
# self.instrumentMode = 'SAMPLE'
# self.instrumentTime = '04/01/2025 8:42:54 PM'
# self.systemTimeFormat = '12HOUR'
# self.generalTimeFormat = '{0:MM/dd/yyyy h:mm:ss tt}'
# self.alertsTimeFormat = '{0:MM/dd/yyyy - h:mm:ss tt}'
# self.datalogTimeFormat = '{0:MM/dd/yyyy h:mm:ss tt}'
# self.instrumentShutdown = 'IDLE'
# self.instrumentReset = 'IDLE'
# self.reportGenerationUploadControl = 'NONE'
# self.reportGenerationUploadState = 'IDLE'

# DAP 
# self.dasUploadControl = 'NONE'
# self.dasUploadState = 'IDLE'
# self.actionProgressTitle = ''
# self.actionProgressPercent = 100
# self.actionProgressCancel = 0
# self.actionProgressCancelEnable = 0
# self.pressureCalControl = 'NONE'
# self.pressureCalState = 'CANCELED'
# self.pressureCalActualPressureValue = 99.66

#ISC
# self.sensorConfigBypass = 0
# self.prigasPrec = 1
# self.secgasPrec = 1
# self.periodicUpdateCheck = 1
# self.lastInstrumentUpdateCheck = '01/01/0001 12:00:00 AM'
# self.packageVersionNeedingUpdate = ''
# self.periodicUpdateFlag = 0
# self.sysInfoUpdateAvail = 0
# self.backgroundPeriodicReportUpload = 1
# self.reportUploadInterval = 168
# self.uploadReportToCloud = 1
# self.configResetFlag = 0

# DAAL
# self.daOffset1 = 1.861
# self.daOffset2 = 0.925
# self.daSlope = 0.813233
# self.foT640DataAlignment = 0
# self.sysOkWarn = 0



###############


# self.sampleRhHigh = 0
# self.checkLed = 0
# self.checkPmt = 0
# self.checkIntPump = 0
# self.checkExtPump = 0
# self.sampleTempWarn = 0
# self.boxTempWarn = 0
# self.sampPresSlopeOor = 0
# self.spanDevOor = 0
# self.instMode = 'SAMPLE'

# self.fo640x = 0
# self.foPm1 = 1
# self.foPmtot = 0
# self.foNonUsEpaFemMode = 0
# self.concValidFlag = 1
# self.hourAvgPctValid = 75


# self.timeSync = 1
# self.timeSyncUseManual = 0
# self.manualTimeServer = ''
# self.timeSyncInterval = 2
# self.lastInstrumentTimeSynced = '04/01/2025 8:13:45 PM'
# self.nextInstrumentTimeSync = '04/01/2025 10:13:45 PM'
# self.timeSyncControl = 'NONE'
# self.timeSyncState = 'OK'
# self.timeSyncPassing = 0
# self.sysWarnTimeNotSynced = 0
# self.dateTimeTargetValue = ''


# self.udpBroadcastEnable = 0
# self.udpBroadcastIp = '192.168.0.1'
# self.modbusUseUserUnits = 0


# self.pressureCalControl = 'NONE'
# self.pressureCalState = 'CANCELED'
# self.pressureCalActualPressureValue = 99.66
# self.dasUploadControl = 'NONE'
# self.dasUploadState = 'IDLE'

# self.actionProgressTitle = ''
# self.actionProgressPercent = 100
# self.actionProgressCancel = 0
# self.actionProgressCancelEnable = 0


# self.nativeAppState = 'Undefined'
# self.instrumentMode = 'SAMPLE'
# self.instrumentTime = '04/01/2025 8:42:54 PM'



# self.asfSystemResetWarning = 1
# self.placeholderTagBoolean = 0
# self.placeholderTagDouble = 0
# self.sysWarnReset = 0
# self.warmUpComplete = 0


# self.driverVersion = ''
# self.packageVersion = '1.4.31.529'
# self.osPlatform = 'Windows CE'
# self.osVersion = 'PN:084750000, 1.0.3.92, 01/18/2017'
# self.cfnetVersion = '3.5.10010.0'


# self.sensorConfigBypass = 0
# self.sysWarnInternalSerialTimeout = 0
# self.sysWarnSystemFault = 0

# self.prigasPrec = 1
# self.secgasPrec = 1

# self.systemTimeFormat = '12HOUR'
# self.generalTimeFormat = '{0:MM/dd/yyyy h:mm:ss tt}'
# self.alertsTimeFormat = '{0:MM/dd/yyyy - h:mm:ss tt}'
# self.datalogTimeFormat = '{0:MM/dd/yyyy h:mm:ss tt}'
# self.instrumentShutdown = 'IDLE'
# self.instrumentReset = 'IDLE'
# self.periodicUpdateCheck = 1
# self.lastInstrumentUpdateCheck = '01/01/0001 12:00:00 AM'
# self.packageVersionNeedingUpdate = ''
# self.periodicUpdateFlag = 0
# self.sysInfoUpdateAvail = 0
# self.backgroundPeriodicReportUpload = 1
# self.reportUploadInterval = 168
# self.uploadReportToCloud = 1
# self.reportGenerationUploadControl = 'NONE'
# self.reportGenerationUploadState = 'IDLE'
# self.configResetFlag = 0
# self.sysWarnConfigReset = 0

# DAAL
# self.daOffset1 = 1.861
# self.daOffset2 = 0.925
# self.daSlope = 0.813233
# self.foT640DataAlignment = 0
# self.sysOkWarn = 0

## SESNOR IDS MODBUS 
# T640MB001WRNS
# T640MB001COIL
# T640MB001RTPM
# T640MB001STDRTPM
# T640MB001R1HPM
# T640MB001R12HPM
# T640MB001R24HPM
# T640MB001S1HPM
# T640MB001S12HPM
# T640MB001S24HPM
# T640MB001PHC
# T640MB001CLM
# T640MB001PV
# T640MB001CALV

## SESNOR IDS API
# T640API001RTPM
# T640API001STDRTPM
# T640API001R1HPM
# T640API001R12HPM
# T640API001R24HPM
# T640API001S1HPM
# T640API001S12HPM
# T640API001S24HPM
# T640API001PHC
# T640API001CLMA
# T640API001PV
# T640API001HIST
# T640API001SVCOM1
# T640API001SVCOM2
# T640API001SVTCP
# T640API001SVPM
# T640API001SVINFO
# T640API001RAM
# T640API001NET
# T640API001FRM
# T640API001RMT
# T640API001DNH
# T640API001SLK
# T640API001OPCSV
# T640API001OPC
# T640API001FLOW
# T640API001DUST
# T640API001DL
# T640API001MMRY
# T640API001TAG
# T640API001CHCK
# T640API001LINF
# T640API001SYSW
# T640API001FOSD
# T640API001TIME
# T640API001COMM
# T640API001INFO
# T640API001DAP
# T640API001ISC
# T640API001DAAL
