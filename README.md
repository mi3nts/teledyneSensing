# teledyneSensing
contains firmware to collect data from teledyne sensors

# T640 
```(base) lakitha@MacBook-Pro-107 teledyneSensing % curl -X GET http://192.168.31.9:8180/api/taglist```

Results in 
```{
  "group": "",
  "tags": [
    {
      "name": "NATIVE_APP_STATE",
      "type": "string",
      "value": "Undefined",
      "properties": "{\"Default\":\"Undefined\",\"Name\":\"NATIVE_APP_STATE\",\"HmiLabel\":\"Native App State\",\"Description\":\"Synchronization tag between native and managed\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "INSTRUMENT_MODE",
      "type": "string",
      "value": "SAMPLE",
      "properties": "{\"Default\":\"SAMPLE\",\"Name\":\"INSTRUMENT_MODE\",\"HmiLabel\":\"Instrument Mode\",\"Description\":\"Specifies the text that shows up for the instrument mode\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "INSTRUMENT_TIME",
      "type": "string",
      "value": "03/06/2025 1:43:05 PM",
      "properties": "{\"Default\":\"\",\"Name\":\"INSTRUMENT_TIME\",\"HmiLabel\":\"Instrument Time\",\"Description\":\"Current time on the instrument\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DL_FLUSH",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"The datalogger is idle\",\"Param\":\"\"},\"Name\":\"DL_FLUSH\",\"HmiLabel\":\"Flush Datalogs\",\"Description\":\"Flushes the datalogger\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"The datalogger is idle\",\"Param\":\"\"},{\"Name\":\"REQUEST_FLUSH\",\"Description\":\"Request the datalogger to perform a flush\",\"Param\":\"\"},{\"Name\":\"FLUSHING\",\"Description\":\"The datalogger is currently flushing\",\"Param\":\"\"}]}"
    },
    {
      "name": "DL_LAST_FLUSHED",
      "type": "string",
      "value": "3/6/2025 1:43:02 PM",
      "properties": "{\"Default\":\"12/14/2013 12:00:00\",\"Name\":\"DL_LAST_FLUSHED\",\"HmiLabel\":\"Time of last flush\",\"Description\":\"Date and Time of last datalogger flush\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM1_PROTOCOL",
      "type": "enum",
      "value": "TAPI",
      "properties": "{\"Default\":{\"Name\":\"TAPI\",\"Description\":\"TAPI\",\"Param\":\"\"},\"Name\":\"SV_COM1_PROTOCOL\",\"HmiLabel\":\"COM1 Protocol\",\"Description\":\"Protocol for COM1\",\"Group\":\"COM1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"TAPI\",\"Description\":\"TAPI\",\"Param\":\"\"},{\"Name\":\"HESSEN\",\"Description\":\"HESSEN\",\"Param\":\"\"},{\"Name\":\"MODBUS RTU\",\"Description\":\"MODBUS RTU\",\"Param\":\"\"},{\"Name\":\"MODBUS ASCII\",\"Description\":\"MODBUS ASCII\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM1_MODEM_INIT_STRING",
      "type": "string",
      "value": "",
      "properties": "{\"Default\":\"\",\"Name\":\"SV_COM1_MODEM_INIT_STRING\",\"HmiLabel\":\"COM1 Modem Init String\",\"Description\":\"Initialization string for modem on COM1\",\"Group\":\"COM1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM1_BAUDRATE",
      "type": "enum",
      "value": "115200",
      "properties": "{\"Default\":{\"Name\":\"115200\",\"Description\":\"115200 Bits / Second\",\"Param\":\"\"},\"Name\":\"SV_COM1_BAUDRATE\",\"HmiLabel\":\"COM1 Baud Rate\",\"Description\":\"Baud Rate for COM1\",\"Group\":\"COM1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"300\",\"Description\":\"300 Bits / Second\",\"Param\":\"\"},{\"Name\":\"1200\",\"Description\":\"1200 Bits / Second\",\"Param\":\"\"},{\"Name\":\"2400\",\"Description\":\"2400 Bits / Second\",\"Param\":\"\"},{\"Name\":\"4800\",\"Description\":\"4800 Bits / Second\",\"Param\":\"\"},{\"Name\":\"9600\",\"Description\":\"9600 Bits / Second\",\"Param\":\"\"},{\"Name\":\"19200\",\"Description\":\"19200 Bits / Second\",\"Param\":\"\"},{\"Name\":\"38400\",\"Description\":\"38400 Bits / Second\",\"Param\":\"\"},{\"Name\":\"57600\",\"Description\":\"57600 Bits / Second\",\"Param\":\"\"},{\"Name\":\"115200\",\"Description\":\"115200 Bits / Second\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM1_PARITY",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No Parity\",\"Param\":\"\"},\"Name\":\"SV_COM1_PARITY\",\"HmiLabel\":\"COM1 Parity\",\"Description\":\"Parity for COM1\",\"Group\":\"COM1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No Parity\",\"Param\":\"\"},{\"Name\":\"ODD\",\"Description\":\"Odd Parity\",\"Param\":\"\"},{\"Name\":\"EVEN\",\"Description\":\"Even Parity\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM1_DATABITS",
      "type": "enum",
      "value": "8",
      "properties": "{\"Default\":{\"Name\":\"8\",\"Description\":\"8 data bits\",\"Param\":\"\"},\"Name\":\"SV_COM1_DATABITS\",\"HmiLabel\":\"COM1 Databits\",\"Description\":\"Databits for COM1\",\"Group\":\"COM1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"7\",\"Description\":\"7 data bits\",\"Param\":\"\"},{\"Name\":\"8\",\"Description\":\"8 data bits\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM1_STOPBITS",
      "type": "enum",
      "value": "1",
      "properties": "{\"Default\":{\"Name\":\"1\",\"Description\":\"1 stop bit\",\"Param\":\"\"},\"Name\":\"SV_COM1_STOPBITS\",\"HmiLabel\":\"COM1 Stop bits\",\"Description\":\"Stopbits for COM1\",\"Group\":\"COM1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"0\",\"Description\":\"0 stop bits\",\"Param\":\"\"},{\"Name\":\"1\",\"Description\":\"1 stop bit\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM2_PROTOCOL",
      "type": "enum",
      "value": "TAPI",
      "properties": "{\"Default\":{\"Name\":\"TAPI\",\"Description\":\"TAPI\",\"Param\":\"\"},\"Name\":\"SV_COM2_PROTOCOL\",\"HmiLabel\":\"COM2 Protocol\",\"Description\":\"Protocol for COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"TAPI\",\"Description\":\"TAPI\",\"Param\":\"\"},{\"Name\":\"HESSEN\",\"Description\":\"HESSEN\",\"Param\":\"\"},{\"Name\":\"MODBUS RTU\",\"Description\":\"MODBUS RTU\",\"Param\":\"\"},{\"Name\":\"MODBUS ASCII\",\"Description\":\"MODBUS ASCII\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM2_MODEM_INIT_STRING",
      "type": "string",
      "value": "",
      "properties": "{\"Default\":\"\",\"Name\":\"SV_COM2_MODEM_INIT_STRING\",\"HmiLabel\":\"COM2 Modem Init String\",\"Description\":\"Initialization string for modem on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_BAUDRATE",
      "type": "enum",
      "value": "115200",
      "properties": "{\"Default\":{\"Name\":\"115200\",\"Description\":\"115200 Bits / Second\",\"Param\":\"\"},\"Name\":\"SV_COM2_BAUDRATE\",\"HmiLabel\":\"COM2 Baud Rate\",\"Description\":\"Baud Rate for COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"300\",\"Description\":\"300 Bits / Second\",\"Param\":\"\"},{\"Name\":\"1200\",\"Description\":\"1200 Bits / Second\",\"Param\":\"\"},{\"Name\":\"2400\",\"Description\":\"2400 Bits / Second\",\"Param\":\"\"},{\"Name\":\"4800\",\"Description\":\"4800 Bits / Second\",\"Param\":\"\"},{\"Name\":\"9600\",\"Description\":\"9600 Bits / Second\",\"Param\":\"\"},{\"Name\":\"19200\",\"Description\":\"19200 Bits / Second\",\"Param\":\"\"},{\"Name\":\"38400\",\"Description\":\"38400 Bits / Second\",\"Param\":\"\"},{\"Name\":\"57600\",\"Description\":\"57600 Bits / Second\",\"Param\":\"\"},{\"Name\":\"115200\",\"Description\":\"115200 Bits / Second\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM2_PARITY",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No Parity\",\"Param\":\"\"},\"Name\":\"SV_COM2_PARITY\",\"HmiLabel\":\"COM2 Parity\",\"Description\":\"Parity for COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No Parity\",\"Param\":\"\"},{\"Name\":\"ODD\",\"Description\":\"Odd Parity\",\"Param\":\"\"},{\"Name\":\"EVEN\",\"Description\":\"Even Parity\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM2_DATABITS",
      "type": "enum",
      "value": "8",
      "properties": "{\"Default\":{\"Name\":\"8\",\"Description\":\"8 data bits\",\"Param\":\"\"},\"Name\":\"SV_COM2_DATABITS\",\"HmiLabel\":\"COM2 Data bits\",\"Description\":\"Databits for COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"7\",\"Description\":\"7 data bits\",\"Param\":\"\"},{\"Name\":\"8\",\"Description\":\"8 data bits\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM2_STOPBITS",
      "type": "enum",
      "value": "1",
      "properties": "{\"Default\":{\"Name\":\"1\",\"Description\":\"1 stop bit\",\"Param\":\"\"},\"Name\":\"SV_COM2_STOPBITS\",\"HmiLabel\":\"COM2 Stop bits\",\"Description\":\"Stopbits for COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"0\",\"Description\":\"0 stop bits\",\"Param\":\"\"},{\"Name\":\"1\",\"Description\":\"1 stop bit\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM2_MODEM_CONNECTION",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=MODEM, False=DIRECT\",\"Default\":false,\"Name\":\"SV_COM2_MODEM_CONNECTION\",\"HmiLabel\":\"COM2 Modem Connection\",\"Description\":\"Selects between a modem connection or direct cable connection on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_ENABLE_QUIET_MODE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_COM2_ENABLE_QUIET_MODE\",\"HmiLabel\":\"COM2 Quiet Mode\",\"Description\":\"Specifies whether quiet mode is enabled on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_ENABLE_SECURITY",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_COM2_ENABLE_SECURITY\",\"HmiLabel\":\"COM2 Security\",\"Description\":\"Specifies whether security is enabled on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_ENABLE_MULTIDROP",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_COM2_ENABLE_MULTIDROP\",\"HmiLabel\":\"COM2 Multidrop\",\"Description\":\"Specifies whether Multidrop mode is enabled on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_ENABLE_RS485",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_COM2_ENABLE_RS485\",\"HmiLabel\":\"COM2 RS485\",\"Description\":\"Specifies whether RS-485 mode is enabled on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_HANDSHAKING_MODE",
      "type": "enum",
      "value": "SOFTWARE",
      "properties": "{\"Default\":{\"Name\":\"SOFTWARE\",\"Description\":\"Software\",\"Param\":\"\"},\"Name\":\"SV_COM2_HANDSHAKING_MODE\",\"HmiLabel\":\"COM2 Handshaking Mode\",\"Description\":\"Handshaking Mode for COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"SOFTWARE\",\"Description\":\"Software\",\"Param\":\"\"},{\"Name\":\"HARDWARE\",\"Description\":\"Hardware\",\"Param\":\"\"},{\"Name\":\"OFF\",\"Description\":\"Off\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_COM2_ENABLE_COMMAND_PROMPT_DISPLAY",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_COM2_ENABLE_COMMAND_PROMPT_DISPLAY\",\"HmiLabel\":\"COM2 Command Prompt Display\",\"Description\":\"Specifies whether the command prompt is displayed on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_DISABLE_ECHO_LINE_EDITING",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_COM2_DISABLE_ECHO_LINE_EDITING\",\"HmiLabel\":\"COM2 Echo and Line Editing\",\"Description\":\"Specifies whether characters are echoed and line editing is allowed on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_DISABLE_HARDWARE_ERROR_CHECKING",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_COM2_DISABLE_HARDWARE_ERROR_CHECKING\",\"HmiLabel\":\"COM2 Hardware Error Checking\",\"Description\":\"Specifies whether hardware error checking is enabled on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_ENABLE_HARDWARE_FIFO",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":true,\"Name\":\"SV_COM2_ENABLE_HARDWARE_FIFO\",\"HmiLabel\":\"COM2 Hardware FIFO\",\"Description\":\"Specifies whether hardware FIFO is enabled on COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_COM2_INITIALIZE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"SV_COM2_INITIALIZE\",\"HmiLabel\":\"COM2 Initialize\",\"Description\":\"Specifies whether to initialize COM2\",\"Group\":\"COM2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_TCP1_INITIALIZE",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"SV_TCP1_INITIALIZE\",\"HmiLabel\":\"TCP PORT1 Initialize\",\"Description\":\"Specifies whether to initialize TCP port1\",\"Group\":\"TCP1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_TCP1_PORTNUM",
      "type": "int",
      "value": "3000",
      "properties": "{\"RawMin\":0,\"RawMax\":65535,\"EuMin\":0,\"EuMax\":65535,\"EuTag\":\"\",\"Default\":3000,\"Name\":\"SV_TCP1_PORTNUM\",\"HmiLabel\":\"TCP Port1 Number\",\"Description\":\"Specifies the port number for TCP port 1 (TAPI)\",\"Group\":\"TCP1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_TCP1_ENABLE_SECURITY",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_TCP1_ENABLE_SECURITY\",\"HmiLabel\":\"TCP Port1 Security\",\"Description\":\"Specifies whether security is enabled on TCP port1\",\"Group\":\"TCP1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_TCP1_ENABLE_COMMAND_PROMPT_DISPLAY",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"SV_TCP1_ENABLE_COMMAND_PROMPT_DISPLAY\",\"HmiLabel\":\"TCP Port1 Command Prompt Display\",\"Description\":\"Specifies whether the command prompt is displayed on TCP port1\",\"Group\":\"TCP1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_TCP2_INITIALIZE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"SV_TCP2_INITIALIZE\",\"HmiLabel\":\"TCP Port2 Initialize\",\"Description\":\"Specifies whether to initialize TCP port2\",\"Group\":\"TCP2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_TCP2_PORTNUM",
      "type": "int",
      "value": "502",
      "properties": "{\"RawMin\":0,\"RawMax\":65535,\"EuMin\":0,\"EuMax\":65535,\"EuTag\":\"\",\"Default\":502,\"Name\":\"SV_TCP2_PORTNUM\",\"HmiLabel\":\"TCP Port2 Number\",\"Description\":\"Specifies the port number for TCP port2 (MODBUS)\",\"Group\":\"TCP2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PRESSURE_CAL_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"PRESSURE_CAL_CONTROL\",\"HmiLabel\":\"PRESSURE_CAL_COMMAND\",\"Description\":\"Controls the pressure calibration\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"CALIBRATE\",\"Description\":\"Perform calibration\",\"Param\":\"\"},{\"Name\":\"CANCEL\",\"Description\":\"Cancel calibration in progress\",\"Param\":\"\"}]}"
    },
    {
      "name": "PRESSURE_CAL_STATE",
      "type": "enum",
      "value": "CANCELED",
      "properties": "{\"Default\":{\"Name\":\"NEVER_RUN\",\"Description\":\"Calibration has never been run\",\"Param\":\"\"},\"Name\":\"PRESSURE_CAL_STATE\",\"HmiLabel\":\"Pressure Cal State\",\"Description\":\"Pressure calibration state\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"CALIBRATING\",\"Description\":\"Calibration in progress\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Calibration was successful\",\"Param\":\"\"},{\"Name\":\"FAILED\",\"Description\":\"Calibration failed\",\"Param\":\"\"},{\"Name\":\"CANCELED\",\"Description\":\"Calibration canceled\",\"Param\":\"\"},{\"Name\":\"NEVER_RUN\",\"Description\":\"Calibration has never been run\",\"Param\":\"\"}]}"
    },
    {
      "name": "PRESSURE_CAL_ACTUAL_PRESSURE_VALUE",
      "type": "float",
      "value": "99.66",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":120.0,\"EuMin\":0.0,\"EuMax\":120.0,\"EuTag\":\"SV_USER_PRESSURE_UNITS\",\"Default\":101.3,\"Name\":\"PRESSURE_CAL_ACTUAL_PRESSURE_VALUE\",\"HmiLabel\":\"Pressure Cal Actual Pressure Value\",\"Description\":\"Actual pressure value\",\"Group\":\"CLONE\",\"Units\":\"kPa\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DAS_UPLOAD_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"DAS_UPLOAD_CONTROL\",\"HmiLabel\":\"DAS UPLOAD CONTROL\",\"Description\":\"Controls the DAS Data Upload\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"UPLOAD\",\"Description\":\"Perform the upload\",\"Param\":\"\"},{\"Name\":\"UPLOAD_SINCE_LAST\",\"Description\":\"Perform the upload since last upload\",\"Param\":\"\"},{\"Name\":\"UPLOAD_ALL_SINCE_T1\",\"Description\":\"Perform the upload\",\"Param\":\"\"},{\"Name\":\"UPLOAD_ALL_BETWEEN_T1_AND_T2\",\"Description\":\"Perform the upload\",\"Param\":\"\"},{\"Name\":\"CANCEL\",\"Description\":\"Cancel upload in progress\",\"Param\":\"\"}]}"
    },
    {
      "name": "DAS_UPLOAD_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"No operation in progress\",\"Param\":\"\"},\"Name\":\"DAS_UPLOAD_STATE\",\"HmiLabel\":\"DAS Upload State\",\"Description\":\"DAS upload state\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"No operation in progress\",\"Param\":\"\"},{\"Name\":\"UPLOADING\",\"Description\":\"Upload in progress\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Upload successful\",\"Param\":\"\"},{\"Name\":\"FAILED\",\"Description\":\"Upload failed\",\"Param\":\"\"},{\"Name\":\"NO_ROOM\",\"Description\":\"Insufficient disk space\",\"Param\":\"\"}]}"
    },
    {
      "name": "ACTION_PROGRESS_TITLE",
      "type": "string",
      "value": "Applying COM Port Settings...",
      "properties": "{\"Default\":\"\",\"Name\":\"ACTION_PROGRESS_TITLE\",\"HmiLabel\":\"Current action title\",\"Description\":\"Title of the current action that is in progress\",\"Group\":\"TRACK_ALL_UPDATES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "ACTION_PROGRESS_PERCENT",
      "type": "int",
      "value": "100",
      "properties": "{\"RawMin\":0,\"RawMax\":100,\"EuMin\":0,\"EuMax\":100,\"EuTag\":\"\",\"Default\":100,\"Name\":\"ACTION_PROGRESS_PERCENT\",\"HmiLabel\":\"Current action progress percent\",\"Description\":\"Percentage complete for the current action\",\"Group\":\"TRACK_ALL_UPDATES\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":false}"
    },
    {
      "name": "ACTION_PROGRESS_CANCEL",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"ACTION_PROGRESS_CANCEL\",\"HmiLabel\":\"Cancel current action\",\"Description\":\"Tag used to cancel current action\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "ACTION_PROGRESS_CANCEL_ENABLE",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"ACTION_PROGRESS_CANCEL_ENABLE\",\"HmiLabel\":\"Enables the cancel button\",\"Description\":\"Tag used to enable/disable the cancel button on the progress window\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_CLOCK_SPEED_ADJUST",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":3,\"RawMin\":-60.0,\"RawMax\":60.0,\"EuMin\":-60.0,\"EuMax\":60.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"SV_CLOCK_SPEED_ADJUST\",\"HmiLabel\":\"Clock Speed Adjust\",\"Description\":\"Time of day clock adjustment\",\"Group\":\"CFG1,CLONE\",\"Units\":\"SEC/DAY\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_LANGUAGE_SELECT",
      "type": "enum",
      "value": "English",
      "properties": "{\"Default\":{\"Name\":\"English\",\"Description\":\"English Language\",\"Param\":\"\"},\"Name\":\"SV_LANGUAGE_SELECT\",\"HmiLabel\":\"Language Select\",\"Description\":\"Specifies the language\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"English\",\"Description\":\"English Language\",\"Param\":\"\"},{\"Name\":\"Chinese\",\"Description\":\"Chinese Language\",\"Param\":\"\"}]}"
    },
    {
      "name": "ASF_MAINTENANCE_MODE_SOFTWARE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"ASF_MAINTENANCE_MODE_SOFTWARE\",\"HmiLabel\":\"Maint Mode\",\"Description\":\"Set to trigger software maintenance mode. after the set time out it will expire automatically\",\"Group\":\"CFG,LOG,TRIG,METER\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_WARN_MAINTENANCE_MODE",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":1,\"TriggerTag\":\"ASF_MAINTENANCE_MODE_SOFTWARE\",\"TriggerCondition\":11,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":false,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_WARN_MAINTENANCE_MODE\",\"HmiLabel\":\"Maintenance Mode\",\"Description\":\"Maintenance Mode Activated\",\"Group\":\"SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_LATCH_WARNING",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":true,\"Name\":\"SV_LATCH_WARNING\",\"HmiLabel\":\"Latch Warnings\",\"Description\":\"Enable/Disable latch warning messages\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_SERIAL_NUMBER",
      "type": "string",
      "value": "2131",
      "properties": "{\"Default\":\"00000000\",\"Name\":\"SV_SERIAL_NUMBER\",\"HmiLabel\":\"Serial Number\",\"Description\":\"Specifies the unique serial number for the instrument\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_CLOCK_FORMAT",
      "type": "string",
      "value": "TIME=%H:%M:%S",
      "properties": "{\"Default\":\"TIME=%H:%M:%S\",\"Name\":\"SV_CLOCK_FORMAT\",\"HmiLabel\":\"Clock Format\",\"Description\":\"Specifies the format of the clock\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_SYSTEM_SERVICE_INTERVAL",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":0,\"RawMin\":0.0,\"RawMax\":100000.0,\"EuMin\":0.0,\"EuMax\":100000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"SV_SYSTEM_SERVICE_INTERVAL\",\"HmiLabel\":\"System Service Interval\",\"Description\":\"System Service Interval\",\"Group\":\"CFG1,CLONE\",\"Units\":\"Hours\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_SYSTEM_TOTAL_HOURS",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":500000.0,\"EuMin\":0.0,\"EuMax\":500000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"SV_SYSTEM_TOTAL_HOURS\",\"HmiLabel\":\"System Hours\",\"Description\":\"Total system runtime hours\",\"Group\":\"CFG\",\"Units\":\"HOURS\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "SV_SYSTEM_TIME_SINCE_LAST_INTERVAL",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":500000.0,\"EuMin\":0.0,\"EuMax\":500000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"SV_SYSTEM_TIME_SINCE_LAST_INTERVAL\",\"HmiLabel\":\"Time Since Last Service\",\"Description\":\"System time since last interval\",\"Group\":\"\",\"Units\":\"Hours\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_SYSTEM_SERVICE_PERIOD_CLEAR",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"SV_SYSTEM_SERVICE_PERIOD_CLEAR\",\"HmiLabel\":\"Service Period Clear\",\"Description\":\"Resets the service interval timer\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_DAYLIGHT_SAVINGS_ENABLE",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":true,\"Name\":\"SV_DAYLIGHT_SAVINGS_ENABLE\",\"HmiLabel\":\"Daylight Savings Enable\",\"Description\":\"Enable/disable daylight savings time\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_MACHINE_ID",
      "type": "int",
      "value": "1",
      "properties": "{\"RawMin\":1,\"RawMax\":247,\"EuMin\":1,\"EuMax\":247,\"EuTag\":\"\",\"Default\":1,\"Name\":\"SV_MACHINE_ID\",\"HmiLabel\":\"Instrument ID\",\"Description\":\"Instrument ID\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_DAS_HOLD_OFF",
      "type": "float",
      "value": "15",
      "properties": "{\"Precision\":1,\"RawMin\":0.1,\"RawMax\":100.0,\"EuMin\":0.5,\"EuMax\":20.0,\"EuTag\":\"\",\"Default\":15.0,\"Name\":\"SV_DAS_HOLD_OFF\",\"HmiLabel\":\"DAS Hold Off delay\",\"Description\":\"DAS hold off delay\",\"Group\":\"CLONE\",\"Units\":\"Minutes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "ASF_SYSTEM_RESET_WARNING",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"ASF_SYSTEM_RESET_WARNING\",\"HmiLabel\":\"ASF System Reset Warning\",\"Description\":\"Denotes whether the instrument was power-cyled or reset\",\"Group\":\"TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PLACEHOLDER_TAG_BOOLEAN",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"PLACEHOLDER_TAG_BOOLEAN\",\"HmiLabel\":\"Placeholder Tag (Boolean)\",\"Description\":\"Placeholder double tag\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PLACEHOLDER_TAG_DOUBLE",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":100000.0,\"EuMin\":0.0,\"EuMax\":100000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PLACEHOLDER_TAG_DOUBLE\",\"HmiLabel\":\"Placeholder Tag (Double)\",\"Description\":\"Placeholder boolean tag\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_WARN_RESET",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":0,\"TriggerTag\":\"ASF_SYSTEM_RESET_WARNING\",\"TriggerCondition\":12,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_WARN_RESET\",\"HmiLabel\":\"System Reset\",\"Description\":\"Warning raised when the the system is reset\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "WARM_UP_COMPLETE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"WARM_UP_COMPLETE\",\"HmiLabel\":\"Warm Up Complete\",\"Description\":\"Warm Up Complete\",\"Group\":\"TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DRIVER_VERSION",
      "type": "string",
      "value": "",
      "properties": "{\"Default\":\"\",\"Name\":\"DRIVER_VERSION\",\"HmiLabel\":\"Driver Version\",\"Description\":\"Driver Version\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PACKAGE_VERSION",
      "type": "string",
      "value": "1.4.31.529",
      "properties": "{\"Default\":\"0.0.51\",\"Name\":\"PACKAGE_VERSION\",\"HmiLabel\":\"Package Version\",\"Description\":\"Specifies the version for the instrument\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "TAGS_FLUSH_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"TAGS_FLUSH_CONTROL\",\"HmiLabel\":\"Tags Flush Command\",\"Description\":\"Controls the flushing of tags to the file system\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"FLUSH\",\"Description\":\"Perform calibration\",\"Param\":\"\"}]}"
    },
    {
      "name": "TAGS_FLUSH_STATE",
      "type": "enum",
      "value": "SUCCESS",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"Idle state, waiting for command\",\"Param\":\"\"},\"Name\":\"TAGS_FLUSH_STATE\",\"HmiLabel\":\"Tags Flush State\",\"Description\":\"Reports the tag flushing state\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Idle state, waiting for command\",\"Param\":\"\"},{\"Name\":\"FLUSHING\",\"Description\":\"Tags flushing in progress\",\"Param\":\"\"},{\"Name\":\"FAILED\",\"Description\":\"Tags flushing finished with errors\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Tags flushing completed successfully\",\"Param\":\"\"}]}"
    },
    {
      "name": "TAGS_FLUSH_TIMESTAMP",
      "type": "string",
      "value": "3/6/2025 1:42:57 PM",
      "properties": "{\"Default\":\"12/14/2013 12:00:00\",\"Name\":\"TAGS_FLUSH_TIMESTAMP\",\"HmiLabel\":\"Tags Flush Date/Time\",\"Description\":\"Date and Time of last tags flush\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OS_PLATFORM",
      "type": "string",
      "value": "Windows CE",
      "properties": "{\"Default\":\"Windows\",\"Name\":\"OS_PLATFORM\",\"HmiLabel\":\"OS Platform\",\"Description\":\"Operating System Platform\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OS_VERSION",
      "type": "string",
      "value": "PN:084750000, 1.0.3.92, 01/18/2017",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"OS_VERSION\",\"HmiLabel\":\"OS Version\",\"Description\":\"Operating System Version\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CFNET_VERSION",
      "type": "string",
      "value": "3.5.10010.0",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"CFNET_VERSION\",\"HmiLabel\":\"CFNET Version\",\"Description\":\"CFNet Version\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYSTEM_TOTAL_RAM",
      "type": "int",
      "value": "209992",
      "properties": "{\"RawMin\":0,\"RawMax\":0,\"EuMin\":1,\"EuMax\":44640,\"EuTag\":\"\",\"Default\":225000,\"Name\":\"SYSTEM_TOTAL_RAM\",\"HmiLabel\":\"Total RAM\",\"Description\":\"Total RAM\",\"Group\":\"\",\"Units\":\"KB\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYSTEM_FREE_RAM",
      "type": "int",
      "value": "150572",
      "properties": "{\"RawMin\":0,\"RawMax\":0,\"EuMin\":1,\"EuMax\":44640,\"EuTag\":\"\",\"Default\":150000,\"Name\":\"SYSTEM_FREE_RAM\",\"HmiLabel\":\"Free RAM\",\"Description\":\"Free RAM\",\"Group\":\"LOG\",\"Units\":\"KB\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYSTEM_USED_RAM",
      "type": "int",
      "value": "59420",
      "properties": "{\"RawMin\":0,\"RawMax\":0,\"EuMin\":1,\"EuMax\":44640,\"EuTag\":\"\",\"Default\":75000,\"Name\":\"SYSTEM_USED_RAM\",\"HmiLabel\":\"Used RAM\",\"Description\":\"Used RAM\",\"Group\":\"LOG\",\"Units\":\"KB\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYSTEM_TOTAL_DISK_SIZE",
      "type": "int",
      "value": "3849204",
      "properties": "{\"RawMin\":0,\"RawMax\":0,\"EuMin\":1,\"EuMax\":44640,\"EuTag\":\"\",\"Default\":225000,\"Name\":\"SYSTEM_TOTAL_DISK_SIZE\",\"HmiLabel\":\"Total Disk Size\",\"Description\":\"Total space available on the DOM\",\"Group\":\"\",\"Units\":\"KB\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYSTEM_AVAILABLE_DISK_SPACE",
      "type": "int",
      "value": "3752604",
      "properties": "{\"RawMin\":0,\"RawMax\":0,\"EuMin\":1,\"EuMax\":44640,\"EuTag\":\"\",\"Default\":150000,\"Name\":\"SYSTEM_AVAILABLE_DISK_SPACE\",\"HmiLabel\":\"Available Disk Space\",\"Description\":\"Available disk space\",\"Group\":\"LOG\",\"Units\":\"KB\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYSTEM_USED_DISK_SPACE",
      "type": "int",
      "value": "96600",
      "properties": "{\"RawMin\":0,\"RawMax\":0,\"EuMin\":1,\"EuMax\":44640,\"EuTag\":\"\",\"Default\":75000,\"Name\":\"SYSTEM_USED_DISK_SPACE\",\"HmiLabel\":\"Used Disk Space\",\"Description\":\"Disk space currently in use\",\"Group\":\"LOG\",\"Units\":\"KB\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "NETWORK_ADDRESS_TYPE",
      "type": "string",
      "value": "DHCP",
      "properties": "{\"Default\":\"Windows\",\"Name\":\"NETWORK_ADDRESS_TYPE\",\"HmiLabel\":\"Network Address Type\",\"Description\":\"Address Type (Static or DHCP)\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "NETWORK_IP_ADDRESS",
      "type": "string",
      "value": "192.168.31.9",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"NETWORK_IP_ADDRESS\",\"HmiLabel\":\"IP Address\",\"Description\":\"Ip Address\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "NETWORK_SUBNET_MASK",
      "type": "string",
      "value": "255.255.255.0",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"NETWORK_SUBNET_MASK\",\"HmiLabel\":\"Subnet Mask\",\"Description\":\"Subnet Mask\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "NETWORK_DEFAULT_GATEWAY",
      "type": "string",
      "value": "192.168.31.1",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"NETWORK_DEFAULT_GATEWAY\",\"HmiLabel\":\"Default Gateway\",\"Description\":\"Default Gateway\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "NETWORK_DNS1",
      "type": "string",
      "value": "192.168.31.1",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"NETWORK_DNS1\",\"HmiLabel\":\"DNS 1\",\"Description\":\"Network DNS 1\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "NETWORK_DNS2",
      "type": "string",
      "value": "N/A",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"NETWORK_DNS2\",\"HmiLabel\":\"DNS 2\",\"Description\":\"Network DNS 2\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "REFRESH_INSTRUMENT_SETTINGS",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"REFRESH_INSTRUMENT_SETTINGS\",\"HmiLabel\":\"Refresh Instrument Settings\",\"Description\":\"Refreshes the latest network settings and memory usage\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FIRMWARE_UPDATE_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"Idle\",\"Param\":\"\"},\"Name\":\"FIRMWARE_UPDATE_STATE\",\"HmiLabel\":\"Firmware Update State\",\"Description\":\"Firmware Update State\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Idle\",\"Param\":\"\"},{\"Name\":\"CANCELLED\",\"Description\":\"Cancelled\",\"Param\":\"\"},{\"Name\":\"DELETING_ALL_FILES_IN_FIRMWARE_UPGRADE_FOLDER\",\"Description\":\"Deleting all files in firmware update folder\",\"Param\":\"\"},{\"Name\":\"COPYING_ENCRYPTED_FIRMWARE_FILE\",\"Description\":\"Copying encrypted firmware file\",\"Param\":\"\"},{\"Name\":\"VALIDATING_COPIED_ENCRYPTED_FIRMWARE_FILE\",\"Description\":\"Validating copied encrypted firmware\",\"Param\":\"\"},{\"Name\":\"EXTRACTING_AND_DECRYPTING_UPDATER_APP_FILES\",\"Description\":\"Extracting and decrypting updater app files\",\"Param\":\"\"},{\"Name\":\"FORMING_DUMMY_DECRYPTED_FIRMWARE_UPDATE_FILE\",\"Description\":\"Forming dummy decrypted firmware update file\",\"Param\":\"\"},{\"Name\":\"INSTALLING_UPDATER_APP_FILES\",\"Description\":\"Installing Updater app files\",\"Param\":\"\"},{\"Name\":\"DELETING_ALL_TEMPORARY_FILES\",\"Description\":\"Deleting all temporary files\",\"Param\":\"\"}]}"
    },
    {
      "name": "FIRMWARE_UPDATE_RESULT",
      "type": "enum",
      "value": "UNDEFINED",
      "properties": "{\"Default\":{\"Name\":\"UNDEFINED\",\"Description\":\"Undefined\",\"Param\":\"\"},\"Name\":\"FIRMWARE_UPDATE_RESULT\",\"HmiLabel\":\"Firmware Update Result\",\"Description\":\"Firmware Update Result\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"UNDEFINED\",\"Description\":\"Undefined\",\"Param\":\"\"},{\"Name\":\"CANCELLED\",\"Description\":\"Cancelled\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Success\",\"Param\":\"\"},{\"Name\":\"NO_FIRMWARE_UPDATE_FOUND\",\"Description\":\"No firmware update found\",\"Param\":\"\"},{\"Name\":\"FIRMWARE_UPDATE_FOUND_BUT_INVALID\",\"Description\":\"Firmware update file was found but it failed validation\",\"Param\":\"\"},{\"Name\":\"ERROR_DELETING_ALL_FILES_IN_FIRMWARE_UPGRADE_FOLDER\",\"Description\":\"Error deleting all files in firmware update folder\",\"Param\":\"\"},{\"Name\":\"ERROR_COPYING_ENCRYPTED_FIRMWARE_FILE\",\"Description\":\"Error copying encrypted firmware file\",\"Param\":\"\"},{\"Name\":\"ERROR_VALIDATING_COPIED_ENCRYPTED_FIRMWARE_FILE\",\"Description\":\"Error validating copied encrypted firmware file\",\"Param\":\"\"},{\"Name\":\"ERROR_EXTRACTING_AND_DECRYPTING_UPDATER_APP_FILES\",\"Description\":\"Error extracting and decrypting updater app files\",\"Param\":\"\"},{\"Name\":\"ERROR_FORMING_DUMMY_DECRYPTED_FIRMWARE_UPDATE_FILE\",\"Description\":\"Error forming dummy unencrypted firmware update file\",\"Param\":\"\"},{\"Name\":\"ERROR_INSTALLING_UPDATER_APP_FILES\",\"Description\":\"Error installing updater app files\",\"Param\":\"\"},{\"Name\":\"ERROR_DELETING_ALL_TEMPORARY_FILES\",\"Description\":\"Error deleting all temporary files\",\"Param\":\"\"},{\"Name\":\"ERROR_UNKNOWN\",\"Description\":\"Unknown error\",\"Param\":\"\"}]}"
    },
    {
      "name": "FIRMWARE_UPDATE_PROGRESS_PERCENT",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":0,\"RawMax\":100,\"EuMin\":0,\"EuMax\":100,\"EuTag\":\"\",\"Default\":0,\"Name\":\"FIRMWARE_UPDATE_PROGRESS_PERCENT\",\"HmiLabel\":\"Firmware Update Progress Percent\",\"Description\":\"Percentage complete for firmware update\",\"Group\":\"TRACK_ALL_UPDATES\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FIRMWARE_UPDATE_ERROR_DETAILS",
      "type": "string",
      "value": "N/A",
      "properties": "{\"Default\":\"N/A\",\"Name\":\"FIRMWARE_UPDATE_ERROR_DETAILS\",\"HmiLabel\":\"Firmware Update Error Details\",\"Description\":\"Specifies details about why firmware update failed\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CONFIG_DOWNLOAD_UPLOAD_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"Idle\",\"Param\":\"\"},\"Name\":\"CONFIG_DOWNLOAD_UPLOAD_STATE\",\"HmiLabel\":\"Config Download Upload State\",\"Description\":\"Config Download Upload State\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Idle\",\"Param\":\"\"},{\"Name\":\"CANCELLED\",\"Description\":\"Cancelled\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_ZIPPING_FILE\",\"Description\":\"Zipping File (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_ADDING_TAPI_HEADER\",\"Description\":\"Adding TAPI Header (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_COPYING_FILE\",\"Description\":\"Adding TAPI Header (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_VALIDATING_COPIED_FILE\",\"Description\":\"Adding TAPI Header (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_DELETING_FILES\",\"Description\":\"Adding TAPI Header (download)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_FINDING_VALID_CONFIG_FILES\",\"Description\":\"Finding config file (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_COPYING_FILE\",\"Description\":\"Copying file (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_VALIDATING_CONFIG_FILE\",\"Description\":\"Validating config file (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_APPLYING_CONFIGURATION\",\"Description\":\"Applying config file (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_EXTRACTING_ZIP_FILE\",\"Description\":\"Extracting zip file (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_UPLOADING\",\"Description\":\"Uploading (upload)\",\"Param\":\"\"}]}"
    },
    {
      "name": "CONFIG_DOWNLOAD_UPLOAD_RESULT",
      "type": "enum",
      "value": "UNDEFINED",
      "properties": "{\"Default\":{\"Name\":\"UNDEFINED\",\"Description\":\"Undefined\",\"Param\":\"\"},\"Name\":\"CONFIG_DOWNLOAD_UPLOAD_RESULT\",\"HmiLabel\":\"Config Download Upload Result\",\"Description\":\"Config Download Upload Result\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"UNDEFINED\",\"Description\":\"Undefined\",\"Param\":\"\"},{\"Name\":\"CANCELLED\",\"Description\":\"Cancelled\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Success\",\"Param\":\"\"},{\"Name\":\"FAILED_UNKNOWN\",\"Description\":\"Failed Unknown\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_FAILED_FILE_ALREADY_EXISTS\",\"Description\":\"Failed: File already exists (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_FAILED_ZIPPING_FILES\",\"Description\":\"Failed: Downloading zip files (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_FAILED_ADDING_HEADER\",\"Description\":\"Failed: Adding header (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_FAILED_COPYING_FILES\",\"Description\":\"Failed: Copying files (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_FAILED_VALIDATION\",\"Description\":\"Failed: Validation (download)\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_FAILED_DELETING_FILES\",\"Description\":\"Failed: Deleting files (download)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_FAILED_NO_VALID_CONFIG_FILES\",\"Description\":\"Failed: No valid config files (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_FAILED_CONFIG_FILE_VALIDATION\",\"Description\":\"Failed: Config file validation (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_FAILED_COPYING_FILE\",\"Description\":\"Failed: Copying File (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_FAILED_EXTRACTING_ZIP_FILE\",\"Description\":\"Failed: Extracting zip file (upload)\",\"Param\":\"\"},{\"Name\":\"UPLOAD_FAILED_UPLOADING\",\"Description\":\"Failed: Uploading (upload)\",\"Param\":\"\"}]}"
    },
    {
      "name": "CONFIG_DOWNLOAD_UPLOAD_PROGRESS_PERCENT",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":0,\"RawMax\":100,\"EuMin\":0,\"EuMax\":100,\"EuTag\":\"\",\"Default\":0,\"Name\":\"CONFIG_DOWNLOAD_UPLOAD_PROGRESS_PERCENT\",\"HmiLabel\":\"Config Download Upload Progress Percent\",\"Description\":\"Percentage complete for confi download /upload\",\"Group\":\"TRACK_ALL_UPDATES\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CONFIG_DOWNLOAD_UPLOAD_ERROR_DETAILS",
      "type": "string",
      "value": "N/A",
      "properties": "{\"Default\":\"N/A\",\"Name\":\"CONFIG_DOWNLOAD_UPLOAD_ERROR_DETAILS\",\"HmiLabel\":\"Config Download Upload Error Details\",\"Description\":\"Specifies details about why config download / upload failed\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "REMOTE_UPDATE_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"REMOTE_UPDATE_CONTROL\",\"HmiLabel\":\"Remote Update Command\",\"Description\":\"Remote Update Control Command\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"POLL\",\"Description\":\"Poll for updates\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD\",\"Description\":\"Download update\",\"Param\":\"\"},{\"Name\":\"ABORT\",\"Description\":\"Abort update in progress\",\"Param\":\"\"}]}"
    },
    {
      "name": "REMOTE_UPDATE_STATE",
      "type": "enum",
      "value": "ERROR_UNKNOWN",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"Idle state, waiting for command\",\"Param\":\"\"},\"Name\":\"REMOTE_UPDATE_STATE\",\"HmiLabel\":\"Remote Update State\",\"Description\":\"Reports the remote update state\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Idle state, waiting for command\",\"Param\":\"\"},{\"Name\":\"CANCELLED\",\"Description\":\"Cancelled\",\"Param\":\"\"},{\"Name\":\"POLLING\",\"Description\":\"Tags flushing completed successfully\",\"Param\":\"\"},{\"Name\":\"UPGRADE_AVAILABLE\",\"Description\":\"Upgrade available\",\"Param\":\"\"},{\"Name\":\"UPGRADE_NOT_AVAILABLE\",\"Description\":\"Upgrade not available\",\"Param\":\"\"},{\"Name\":\"UPGRADE_ALREADY_DOWNLOADED\",\"Description\":\"Upgrade already downloaded\",\"Param\":\"\"},{\"Name\":\"DOWNLOADING\",\"Description\":\"Downloading in progress\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_ABORTED_NOT_ENOUGH_SPACE\",\"Description\":\"Download aborted due to lack of space\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_SUCCESS\",\"Description\":\"Download completed successfully\",\"Param\":\"\"},{\"Name\":\"DOWNLOAD_FAILED\",\"Description\":\"Download failed with errors\",\"Param\":\"\"},{\"Name\":\"INSTALLING\",\"Description\":\"Installing firmware\",\"Param\":\"\"},{\"Name\":\"INSTALL_SUCCESS\",\"Description\":\"Install completed successfully\",\"Param\":\"\"},{\"Name\":\"INSTALL_FAILED\",\"Description\":\"Install failed with errors\",\"Param\":\"\"},{\"Name\":\"ERROR_NOT_CONNECTED_TO_INTERNET\",\"Description\":\"Remote update failed because there is no internet connection\",\"Param\":\"\"},{\"Name\":\"ERROR_UNKNOWN\",\"Description\":\"Remote update failed with some unknown error\",\"Param\":\"\"}]}"
    },
    {
      "name": "REMOTE_UPDATE_DOWNLOAD_PERCENT",
      "type": "int",
      "value": "100",
      "properties": "{\"RawMin\":0,\"RawMax\":100,\"EuMin\":0,\"EuMax\":100,\"EuTag\":\"\",\"Default\":100,\"Name\":\"REMOTE_UPDATE_DOWNLOAD_PERCENT\",\"HmiLabel\":\"Remote update download percent\",\"Description\":\"Percentage complete for remote update download\",\"Group\":\"TRACK_ALL_UPDATES\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "REMOTE_UPDATE_VERSION",
      "type": "string",
      "value": "",
      "properties": "{\"Default\":\"\",\"Name\":\"REMOTE_UPDATE_VERSION\",\"HmiLabel\":\"Remote Update Version\",\"Description\":\"Version available for download\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "REMOTE_UPDATE_REQUIRED_DISK_SPACE",
      "type": "int",
      "value": "150000",
      "properties": "{\"RawMin\":0,\"RawMax\":0,\"EuMin\":1,\"EuMax\":44640,\"EuTag\":\"\",\"Default\":150000,\"Name\":\"REMOTE_UPDATE_REQUIRED_DISK_SPACE\",\"HmiLabel\":\"Remote Update Required Disk Space\",\"Description\":\"Disk space required for remote update\",\"Group\":\"\",\"Units\":\"KB\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"DUST_CAL_CONTROL\",\"HmiLabel\":\"Dust Cal Control\",\"Description\":\"Dust Cal Control Tag\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"CALIBRATE\",\"Description\":\"Enter Dust Calibration Mode\",\"Param\":\"\"},{\"Name\":\"CANCEL\",\"Description\":\"Cancel Calibration Mode\",\"Param\":\"\"}]}"
    },
    {
      "name": "DUST_CAL_STATE",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"DUST_CAL_STATE\",\"HmiLabel\":\"Dust Cal State\",\"Description\":\"Dust Cal State Tag\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"CALIBRATING\",\"Description\":\"Dust Calibration Mode in progress\",\"Param\":\"\"},{\"Name\":\"CANCELED\",\"Description\":\"Calibration Canceled\",\"Param\":\"\"}]}"
    },
    {
      "name": "OPC_SV_DUST_CAL_FILT_SIZE",
      "type": "int",
      "value": "1",
      "properties": "{\"RawMin\":1,\"RawMax\":100,\"EuMin\":1,\"EuMax\":100,\"EuTag\":\"\",\"Default\":1,\"Name\":\"OPC_SV_DUST_CAL_FILT_SIZE\",\"HmiLabel\":\"Dust Cal Filter Size\",\"Description\":\"Boxcar Filter Size When in Dust Cal Mode\",\"Group\":\"CFG1,CLONE\",\"Units\":\"Samples\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "HOME_METER1",
      "type": "string",
      "value": "AI_SAMPLE_FLOW5",
      "properties": "{\"Default\":\"AI_SAMPLE_FLOW5\",\"Name\":\"HOME_METER1\",\"HmiLabel\":\"Homescreen Meter1\",\"Description\":\"Specifies the tag to display on Homescreen meter 1\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "HOME_METER2",
      "type": "string",
      "value": "OPC_RT_OUTSIDE_TEMP",
      "properties": "{\"Default\":\"OPC_RT_OUTSIDE_TEMP\",\"Name\":\"HOME_METER2\",\"HmiLabel\":\"Homescreen Meter2\",\"Description\":\"Specifies the tag to display on Homescreen meter 2\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "HOME_METER3",
      "type": "string",
      "value": "OPC_RT_HUMIDITY",
      "properties": "{\"Default\":\"OPC_RT_HUMIDITY\",\"Name\":\"HOME_METER3\",\"HmiLabel\":\"Homescreen Meter3\",\"Description\":\"Specifies the tag to display on Homescreen meter 3\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_RT_LED_TEMP",
      "type": "float",
      "value": "32.9219512939453",
      "properties": "{\"Precision\":2,\"RawMin\":-20.0,\"RawMax\":80.0,\"EuMin\":-20.0,\"EuMax\":80.0,\"EuTag\":\"\",\"Default\":40.0,\"Name\":\"OPC_RT_LED_TEMP\",\"HmiLabel\":\"LED Temp\",\"Description\":\"LED Temperature\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"degC\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "AI_SAMPLE_PRESSURE_UNITS",
      "type": "float",
      "value": "98.5224609375",
      "properties": "{\"Precision\":1,\"RawMin\":40.0,\"RawMax\":120.0,\"EuMin\":40.0,\"EuMax\":120.0,\"EuTag\":\"SV_USER_PRESSURE_UNITS\",\"Default\":101.3,\"Name\":\"AI_SAMPLE_PRESSURE_UNITS\",\"HmiLabel\":\"Ambient Pressure\",\"Description\":\"Ambient Pressure\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"kPa\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_RT_HUMIDITY",
      "type": "float",
      "value": "15.5488996505737",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":100.0,\"EuMin\":0.0,\"EuMax\":100.0,\"EuTag\":\"\",\"Default\":35.0,\"Name\":\"OPC_RT_HUMIDITY\",\"HmiLabel\":\"Sample RH\",\"Description\":\"Humidity Sensor Reading\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_RT_SL_VALUE",
      "type": "float",
      "value": "63.5555",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":1000.0,\"EuMin\":0.0,\"EuMax\":1000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_RT_SL_VALUE\",\"HmiLabel\":\"SL Value\",\"Description\":\"Signal Length Max Value\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SPAN_DEVIATION",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":1000.0,\"EuMin\":0.0,\"EuMax\":1000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_SPAN_DEVIATION\",\"HmiLabel\":\"Span Deviation\",\"Description\":\"Span Deviation\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "SPAN_DEV_48HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"SPAN_DEV_48HR_AVG\",\"HmiLabel\":\"Span Dev Track\",\"Description\":\"Span Dev 48Hr Rolling Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "LEAKCHECKPM10_CONC",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"LEAKCHECKPM10_CONC\",\"HmiLabel\":\"PM10 Conc Leak\",\"Description\":\"This is the real time concentration value during a leak check\",\"Group\":\"REALTIME\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "LEAKCHECKPM2.5_CONC",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"LEAKCHECKPM2.5_CONC\",\"HmiLabel\":\"PM2.5 Conc Leak\",\"Description\":\"This is the real-time PM2.5 concentration during a leak check\",\"Group\":\"REALTIME\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "LEAK_CHECK_CONTROL",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"Normal operation\",\"Param\":\"\"},\"Name\":\"LEAK_CHECK_CONTROL\",\"HmiLabel\":\"Leak Check Control\",\"Description\":\"Leak Check Control Tag\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Normal operation\",\"Param\":\"\"},{\"Name\":\"CHECK\",\"Description\":\"Check for leaks\",\"Param\":\"\"}]}"
    },
    {
      "name": "LEAK_CHECK_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"Normal operation\",\"Param\":\"\"},\"Name\":\"LEAK_CHECK_STATE\",\"HmiLabel\":\"Leak Check State\",\"Description\":\"Leak Check State Tag\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Normal operation\",\"Param\":\"\"},{\"Name\":\"ACTIVE\",\"Description\":\"Check for leaks\",\"Param\":\"\"}]}"
    },
    {
      "name": "KS10",
      "type": "float",
      "value": "1",
      "properties": "{\"Precision\":3,\"RawMin\":0.5,\"RawMax\":1.5,\"EuMin\":0.5,\"EuMax\":1.5,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"KS10\",\"HmiLabel\":\"KS10\",\"Description\":\"Post-process slope factor for PM10\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "KS2.5",
      "type": "float",
      "value": "1",
      "properties": "{\"Precision\":3,\"RawMin\":0.5,\"RawMax\":1.5,\"EuMin\":0.5,\"EuMax\":1.5,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"KS2.5\",\"HmiLabel\":\"KS2.5\",\"Description\":\"Post-process slope factor for PM2.5\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "KS1",
      "type": "float",
      "value": "1",
      "properties": "{\"Precision\":3,\"RawMin\":0.5,\"RawMax\":1.5,\"EuMin\":0.5,\"EuMax\":1.5,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"KS1\",\"HmiLabel\":\"KS1\",\"Description\":\"Post-process slope factor for PM1\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "KSTOT",
      "type": "float",
      "value": "1",
      "properties": "{\"Precision\":3,\"RawMin\":0.5,\"RawMax\":1.5,\"EuMin\":0.5,\"EuMax\":1.5,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"KSTOT\",\"HmiLabel\":\"KStot\",\"Description\":\"Post-process slope factor for PMtot\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "KO10",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":-5.0,\"RawMax\":5.0,\"EuMin\":-5.0,\"EuMax\":5.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"KO10\",\"HmiLabel\":\"KO10\",\"Description\":\"Post-process offset factor for PM10\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "KO2.5",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":-5.0,\"RawMax\":5.0,\"EuMin\":-5.0,\"EuMax\":5.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"KO2.5\",\"HmiLabel\":\"KO2.5\",\"Description\":\"Post-process offset factor for PM2.5\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "KO1",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":-5.0,\"RawMax\":5.0,\"EuMin\":-5.0,\"EuMax\":5.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"KO1\",\"HmiLabel\":\"KO1\",\"Description\":\"Post-process offset factor for PM1\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "KOTOT",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":-5.0,\"RawMax\":5.0,\"EuMin\":-5.0,\"EuMax\":5.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"KOTOT\",\"HmiLabel\":\"KOtot\",\"Description\":\"Post-process offset factor for PMtot\",\"Group\":\"LOG,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PM10_CONC",
      "type": "float",
      "value": "1.959039",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10_CONC\",\"HmiLabel\":\"PM10 Conc\",\"Description\":\"This is the real time concentration value\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM2.5_CONC",
      "type": "float",
      "value": "1.179819",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM2.5_CONC\",\"HmiLabel\":\"PM2.5 Conc\",\"Description\":\"This is the real-time PM2.5 concentration\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1_CONC",
      "type": "float",
      "value": "1.100898",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1_CONC\",\"HmiLabel\":\"PM1 Conc\",\"Description\":\"This is the real-time PM1 concentration\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PMTOT_CONC",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOT_CONC\",\"HmiLabel\":\"PMtot Conc\",\"Description\":\"This is the real-time PMtot concentration\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PM10STP_CONC",
      "type": "float",
      "value": "1.99928159570589",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10STP_CONC\",\"HmiLabel\":\"PM10STP Conc\",\"Description\":\"This is the real time PM10 Standardized concentration\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM2.5STP_CONC",
      "type": "float",
      "value": "1.20405485187591",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM2.5STP_CONC\",\"HmiLabel\":\"PM2.5STP Conc\",\"Description\":\"This is the real-time PM2.5 Standardized concentration\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1STP_CONC",
      "type": "float",
      "value": "1.12351265602646",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1STP_CONC\",\"HmiLabel\":\"PM1STP Conc\",\"Description\":\"This is the real-time PM1 Standardized concentration\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PMTOTSTP_CONC",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOTSTP_CONC\",\"HmiLabel\":\"PMtotSTP Conc\",\"Description\":\"This is the real-time PMtot Standardized concentration\",\"Group\":\"PRIGAS,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_PM10STP_TEMP",
      "type": "float",
      "value": "25",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":200.0,\"EuMin\":0.0,\"EuMax\":200.0,\"EuTag\":\"\",\"Default\":25.0,\"Name\":\"OPC_PM10STP_TEMP\",\"HmiLabel\":\"PM10STP Temperature\",\"Description\":\"\",\"Group\":\"CFG1,CLONE\",\"Units\":\"degC\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_PM10STP_PRESSURE",
      "type": "float",
      "value": "760",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":200.0,\"EuMin\":0.0,\"EuMax\":200.0,\"EuTag\":\"\",\"Default\":760.0,\"Name\":\"OPC_PM10STP_PRESSURE\",\"HmiLabel\":\"PM10STP Pressure\",\"Description\":\"\",\"Group\":\"CLONE\",\"Units\":\"mmHg\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_RT_P3_CALC",
      "type": "float",
      "value": "48",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":200.0,\"EuMin\":0.0,\"EuMax\":200.0,\"EuTag\":\"\",\"Default\":48.0,\"Name\":\"OPC_RT_P3_CALC\",\"HmiLabel\":\"P3 (Calculated)\",\"Description\":\"P3 Value for Signal Length Histogram\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SENSOR_STATUS",
      "type": "string",
      "value": "OK",
      "properties": "{\"Default\":\"OK\",\"Name\":\"OPC_SENSOR_STATUS\",\"HmiLabel\":\"Sensor Status\",\"Description\":\"Status of Sensor\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_P3_VALUE",
      "type": "int",
      "value": "50",
      "properties": "{\"RawMin\":0,\"RawMax\":200,\"EuMin\":0,\"EuMax\":200,\"EuTag\":\"\",\"Default\":48,\"Name\":\"OPC_SV_P3_VALUE\",\"HmiLabel\":\"P3 Value\",\"Description\":\"P3 value for the Sensor\",\"Group\":\"CFG2,CLONE,LOG,REALTIME,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_OFFSET_ADJ_DELAY",
      "type": "int",
      "value": "2000",
      "properties": "{\"RawMin\":0,\"RawMax\":10000,\"EuMin\":0,\"EuMax\":10000,\"EuTag\":\"\",\"Default\":2000,\"Name\":\"OPC_SV_OFFSET_ADJ_DELAY\",\"HmiLabel\":\"Offset_Adj_Delay\",\"Description\":\"Offset adjustment delay for the PMT\",\"Group\":\"CFG2\",\"Units\":\"ms\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_PMT_HV_SETTING",
      "type": "int",
      "value": "1452",
      "properties": "{\"RawMin\":0,\"RawMax\":5000,\"EuMin\":0,\"EuMax\":5000,\"EuTag\":\"\",\"Default\":1450,\"Name\":\"OPC_SV_PMT_HV_SETTING\",\"HmiLabel\":\"Current PMT HV Setting\",\"Description\":\"PMT voltage setting (not volts, but DAC counts, voltage scale is 0-5V for 0-4095 counts)\",\"Group\":\"CFG2,LOG,CLONE\",\"Units\":\"V\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_PMT_HV_OFFSET_ADJ",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":0,\"RawMax\":2147483647,\"EuMin\":0,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_SV_PMT_HV_OFFSET_ADJ\",\"HmiLabel\":\"PMT HV Offset\",\"Description\":\"PMT voltage setting for offset adjust function\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_BC_FILT_SIZE",
      "type": "int",
      "value": "60",
      "properties": "{\"RawMin\":0,\"RawMax\":10000,\"EuMin\":0,\"EuMax\":10000,\"EuTag\":\"\",\"Default\":60,\"Name\":\"OPC_SV_BC_FILT_SIZE\",\"HmiLabel\":\"Boxcar Filt Size\",\"Description\":\"Box-Car Filter Amount (number to average aquisitions)\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_ACQUISITION_DURATION",
      "type": "int",
      "value": "10",
      "properties": "{\"RawMin\":10,\"RawMax\":300,\"EuMin\":10,\"EuMax\":300,\"EuTag\":\"\",\"Default\":10,\"Name\":\"OPC_SV_ACQUISITION_DURATION\",\"HmiLabel\":\"Aquisition Duration\",\"Description\":\"Duration of Each Measurement\",\"Group\":\"CFG1,CLONE\",\"Units\":\"sec\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SENSOR_MODE",
      "type": "string",
      "value": "T640",
      "properties": "{\"Default\":\"T640\",\"Name\":\"OPC_SENSOR_MODE\",\"HmiLabel\":\"Sensor Mode\",\"Description\":\"Sensor Configured for T640 or T640x\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_RT_BOX_TEMP",
      "type": "float",
      "value": "25.3872375488281",
      "properties": "{\"Precision\":1,\"RawMin\":-40.0,\"RawMax\":120.0,\"EuMin\":-40.0,\"EuMax\":120.0,\"EuTag\":\"\",\"Default\":20.0,\"Name\":\"OPC_RT_BOX_TEMP\",\"HmiLabel\":\"Box Temp\",\"Description\":\"Box Temperature (degC)\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"degC\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_RT_OUTSIDE_TEMP",
      "type": "float",
      "value": "22.7212657928467",
      "properties": "{\"Precision\":1,\"RawMin\":-50.0,\"RawMax\":120.0,\"EuMin\":-50.0,\"EuMax\":120.0,\"EuTag\":\"\",\"Default\":25.0,\"Name\":\"OPC_RT_OUTSIDE_TEMP\",\"HmiLabel\":\"Ambient Temp\",\"Description\":\"Ambient Temperature Probe Reading\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"degC\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_AMBIENT_TEMP_OVERRIDE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ON, False=OFF\",\"Default\":false,\"Name\":\"OPC_AMBIENT_TEMP_OVERRIDE\",\"HmiLabel\":\"Override\",\"Description\":\"Controls if the ambient temp is being read\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_RT_PWM_PUMP",
      "type": "float",
      "value": "30.5560703277588",
      "properties": "{\"Precision\":0,\"RawMin\":0.0,\"RawMax\":100.0,\"EuMin\":0.0,\"EuMax\":100.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_RT_PWM_PUMP\",\"HmiLabel\":\"Pump PWM\",\"Description\":\"Pump Duty Cycle / PWM Status - Flag at 90%\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_RT_PWM_VALVE",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":0,\"RawMin\":0.0,\"RawMax\":100.0,\"EuMin\":0.0,\"EuMax\":100.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_RT_PWM_VALVE\",\"HmiLabel\":\"Valve PWM\",\"Description\":\"Proportional Valve Duty Cycle / PWM Status - Flag at 90%\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"%\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_HEATER_STATUS",
      "type": "string",
      "value": "ON",
      "properties": "{\"Default\":\"ON\",\"Name\":\"OPC_HEATER_STATUS\",\"HmiLabel\":\"ASC Heater Status\",\"Description\":\"ASC Heater Status ON/OFF\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_RT_SAMP_TEMP",
      "type": "float",
      "value": "23.5014190673828",
      "properties": "{\"Precision\":1,\"RawMin\":-40.0,\"RawMax\":120.0,\"EuMin\":-40.0,\"EuMax\":120.0,\"EuTag\":\"\",\"Default\":25.0,\"Name\":\"OPC_RT_SAMP_TEMP\",\"HmiLabel\":\"Sample Temp\",\"Description\":\"Sample Stream Temperature at RH Sensor\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"degC\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_BOARD_FIRMWARE_REV",
      "type": "string",
      "value": "0.87",
      "properties": "{\"Default\":\"0.00\",\"Name\":\"OPC_BOARD_FIRMWARE_REV\",\"HmiLabel\":\"Firmware Rev\",\"Description\":\"Revision of the T640 Control Board Firmware\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_FLOW_5LPM_OFFSET",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":2147483647.0,\"EuMin\":0.0,\"EuMax\":2147483647.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_SV_FLOW_5LPM_OFFSET\",\"HmiLabel\":\"Sample Flow Offset\",\"Description\":\"5-LPM Flowmeter Calibration Offset\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_FLOW_5LPM_SLOPE",
      "type": "float",
      "value": "0.992093920707703",
      "properties": "{\"Precision\":4,\"RawMin\":0.0,\"RawMax\":3.0,\"EuMin\":0.0,\"EuMax\":3.0,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"OPC_SV_FLOW_5LPM_SLOPE\",\"HmiLabel\":\"Sample Flow Slope\",\"Description\":\"5-LPM Flowmeter Calibration Slope\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_FLOW_11.67LPM_OFFSET",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":2147483647.0,\"EuMin\":0.0,\"EuMax\":2147483647.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_SV_FLOW_11.67LPM_OFFSET\",\"HmiLabel\":\"Bypass Flow Offset\",\"Description\":\"T640x Bypass Flowmeter Calibration Offset\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_FLOW_11.67LPM_SLOPE",
      "type": "float",
      "value": "1",
      "properties": "{\"Precision\":4,\"RawMin\":0.0,\"RawMax\":3.0,\"EuMin\":0.0,\"EuMax\":3.0,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"OPC_SV_FLOW_11.67LPM_SLOPE\",\"HmiLabel\":\"Bypass Flow Slope\",\"Description\":\"T640x Bypass Flowmeter Calibration Slope\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_AMB_PRESS_SLOPE",
      "type": "float",
      "value": "1.00817835330963",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":2.0,\"EuMin\":0.0,\"EuMax\":2.0,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"OPC_SV_AMB_PRESS_SLOPE\",\"HmiLabel\":\"Pressure Sensor Slope\",\"Description\":\"Pressure Sensor Calibration Slope\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_RH_CONTROL_SETPOINT",
      "type": "float",
      "value": "35",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":100.0,\"EuMin\":0.0,\"EuMax\":100.0,\"EuTag\":\"\",\"Default\":35.0,\"Name\":\"OPC_SV_RH_CONTROL_SETPOINT\",\"HmiLabel\":\"RH Control Setpoint\",\"Description\":\"Setpoint for the sample RH\",\"Group\":\"CFG1\",\"Units\":\"%RH\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_HEATER_CONTROL_ENABLE",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=ON, False=OFF\",\"Default\":true,\"Name\":\"OPC_HEATER_CONTROL_ENABLE\",\"HmiLabel\":\"ASC Heater Control Enable\",\"Description\":\"Control Heater: Auto, or OFF\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_PUMP_CONTROL",
      "type": "enum",
      "value": "AUTO",
      "properties": "{\"Default\":{\"Name\":\"AUTO\",\"Description\":\"\",\"Param\":\"\"},\"Name\":\"OPC_PUMP_CONTROL\",\"HmiLabel\":\"Pump Control\",\"Description\":\"Pump Control: Auto, Off, or Cleaning Cycle\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"AUTO\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"OFF\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"CLEANING CYCLE\",\"Description\":\"\",\"Param\":\"\"}]}"
    },
    {
      "name": "OPC_VALVE_CONTROL",
      "type": "enum",
      "value": "AUTO",
      "properties": "{\"Default\":{\"Name\":\"AUTO\",\"Description\":\"\",\"Param\":\"\"},\"Name\":\"OPC_VALVE_CONTROL\",\"HmiLabel\":\"T640x Valve Control\",\"Description\":\"OPC Valve Control: Auto, Open, Closed\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"AUTO\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"OPEN\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"CLOSED\",\"Description\":\"\",\"Param\":\"\"}]}"
    },
    {
      "name": "OPC_RT_HEATER_DUTY",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":100.0,\"EuMin\":0.0,\"EuMax\":100.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_RT_HEATER_DUTY\",\"HmiLabel\":\"ASC Heater Duty Cycle\",\"Description\":\"ASC Heater Duty Cycle\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_RT_PUMP_SPEED",
      "type": "int",
      "value": "1781",
      "properties": "{\"RawMin\":0,\"RawMax\":2147483647,\"EuMin\":0,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_RT_PUMP_SPEED\",\"HmiLabel\":\"Pump Speed\",\"Description\":\"Pump Tachometer Reading\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"rev/s\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_5L_FLOW_SETPOINT",
      "type": "float",
      "value": "5",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":10.0,\"EuMin\":0.0,\"EuMax\":10.0,\"EuTag\":\"\",\"Default\":5.0,\"Name\":\"OPC_SV_5L_FLOW_SETPOINT\",\"HmiLabel\":\"Sample Flow Setpoint\",\"Description\":\"Flow setpoint for optical sensor\",\"Group\":\"CFG,CLONE\",\"Units\":\"LPM\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_11L_FLOW_SETPOINT",
      "type": "float",
      "value": "11.6700000762939",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":20.0,\"EuMin\":0.0,\"EuMax\":20.0,\"EuTag\":\"\",\"Default\":11.67,\"Name\":\"OPC_SV_11L_FLOW_SETPOINT\",\"HmiLabel\":\"T640x Bypass Flow Setpoint\",\"Description\":\"Setpoint for the T640x bypass flow\",\"Group\":\"CFG,CLONE\",\"Units\":\"LPM\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_AMB_PRESS_OFFSET",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":1.7976931348623157E+308,\"EuMin\":0.0,\"EuMax\":1.7976931348623157E+308,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_SV_AMB_PRESS_OFFSET\",\"HmiLabel\":\"Pressure Sensor Offset\",\"Description\":\"Offset value for the ambient pressure sensor\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_RH_SLOPE",
      "type": "float",
      "value": "1",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":3.0,\"EuMin\":0.0,\"EuMax\":3.0,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"OPC_SV_RH_SLOPE\",\"HmiLabel\":\"RH Sensor Slope\",\"Description\":\"RH sensor slope\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_RH_OFFSET",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":1.7976931348623157E+308,\"EuMin\":0.0,\"EuMax\":1.7976931348623157E+308,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_SV_RH_OFFSET\",\"HmiLabel\":\"RH Sensor Offset\",\"Description\":\"RH Sensor Offset\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_USB_STORAGE_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"\",\"Param\":\"\"},\"Name\":\"OPC_USB_STORAGE_STATE\",\"HmiLabel\":\"USB Storage State\",\"Description\":\"State variable for USB drive file copy function\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NOT_DETECTED\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"DETECTED\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"COPY\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"FAILED\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"IDLE\",\"Description\":\"\",\"Param\":\"\"}]}"
    },
    {
      "name": "OPC_SV_FAN_SETPOINT",
      "type": "float",
      "value": "20",
      "properties": "{\"Precision\":3,\"RawMin\":10.0,\"RawMax\":30.0,\"EuMin\":10.0,\"EuMax\":30.0,\"EuTag\":\"\",\"Default\":20.0,\"Name\":\"OPC_SV_FAN_SETPOINT\",\"HmiLabel\":\"Fan Setpoint\",\"Description\":\"Chassis fan temperature setpoint\",\"Group\":\"CFG1,CLONE\",\"Units\":\"degC\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PMC_CONC",
      "type": "float",
      "value": "0.77922",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMC_CONC\",\"HmiLabel\":\"PM10-2.5 Conc\",\"Description\":\"This is the real-time PM10-2.5 concentration derived by subtracting the PM2.5 value from PM10\",\"Group\":\"PRIGAS_NOCAL,LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_RT_AMPLITUDE_COUNTS",
      "type": "int",
      "value": "12535",
      "properties": "{\"RawMin\":0,\"RawMax\":2147483647,\"EuMin\":0,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_RT_AMPLITUDE_COUNTS\",\"HmiLabel\":\"Amplitude Counts\",\"Description\":\"Number of total particles in the Amplitude histogram\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_RT_LENGTH_COUNTS",
      "type": "int",
      "value": "12535",
      "properties": "{\"RawMin\":0,\"RawMax\":2147483647,\"EuMin\":0,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_RT_LENGTH_COUNTS\",\"HmiLabel\":\"Length Counts\",\"Description\":\"Total number of particles in the Length distribution\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_INSTRUMENT_SLOPE",
      "type": "float",
      "value": "0.999",
      "properties": "{\"Precision\":3,\"RawMin\":0.0,\"RawMax\":3.0,\"EuMin\":0.0,\"EuMax\":3.0,\"EuTag\":\"\",\"Default\":1.0,\"Name\":\"OPC_SV_INSTRUMENT_SLOPE\",\"HmiLabel\":\"Instrument Slope\",\"Description\":\"Instrument calibration slope applied to PM2.5 and PM10 values.\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SENSOR_STATE",
      "type": "enum",
      "value": "MEASURING",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"\",\"Param\":\"\"},\"Name\":\"OPC_SENSOR_STATE\",\"HmiLabel\":\"Sensor State\",\"Description\":\"State of OPC sensor\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"CONFIG\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"READY\",\"Description\":\"\",\"Param\":\"\"},{\"Name\":\"MEASURING\",\"Description\":\"\",\"Param\":\"\"}]}"
    },
    {
      "name": "OPC_SV_OFFSET_COUNTS",
      "type": "int",
      "value": "2154",
      "properties": "{\"RawMin\":0,\"RawMax\":2147483647,\"EuMin\":0,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_SV_OFFSET_COUNTS\",\"HmiLabel\":\"Sensor Offset Counts\",\"Description\":\"Value returned by the sendOffsetAdjust function\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SV_AUTO_ADJUST_ENABLE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"OPC_SV_AUTO_ADJUST_ENABLE\",\"HmiLabel\":\"Auto Offset Adjust Enable\",\"Description\":\"Enables/Disables auto offset adjustment feature\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_PMT_CAL_SETTING",
      "type": "int",
      "value": "1459",
      "properties": "{\"RawMin\":1100,\"RawMax\":4000,\"EuMin\":1100,\"EuMax\":4000,\"EuTag\":\"\",\"Default\":1450,\"Name\":\"OPC_SV_PMT_CAL_SETTING\",\"HmiLabel\":\"PMT Setting\",\"Description\":\"PMT HVPS setting determined during cal dust calibration\",\"Group\":\"CFG,CLONE\",\"Units\":\"V\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_ZERO_CHANNEL",
      "type": "int",
      "value": "132",
      "properties": "{\"RawMin\":1,\"RawMax\":256,\"EuMin\":1,\"EuMax\":256,\"EuTag\":\"\",\"Default\":132,\"Name\":\"OPC_ZERO_CHANNEL\",\"HmiLabel\":\"OPC Zero Data Channel\",\"Description\":\"Offset to Zero channel in the data set (1-base) for Sensor Check Plot\",\"Group\":\"CFG2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_FAST_HIST_UPDATE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"OPC_FAST_HIST_UPDATE\",\"HmiLabel\":\"OPC fast histogram update mode\",\"Description\":\"Enables fast histogram updates\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_DUST_HISTOGRAM",
      "type": "listInt",
      "value": "0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,5,2,7,2,7,5,8,5,3,5,2,4,7,5,5,3,5,4,5,2,5,1,3,6,2,4,6,0,0,6,2,3,7,3,1,0,4,1,2,4,2,1,3,2,1,2,0,0,1,2,0,2,1,0,0,1,1,0,1,3,2,0,2,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0",
      "properties": "{\"Default\":[0],\"Name\":\"OPC_DUST_HISTOGRAM\",\"HmiLabel\":\"OPC dust histogram\",\"Description\":\"Sensor Dust Histogram\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_LOG_INTERVAL",
      "type": "int",
      "value": "60000",
      "properties": "{\"RawMin\":0,\"RawMax\":86400,\"EuMin\":0,\"EuMax\":86400,\"EuTag\":\"\",\"Default\":60000,\"Name\":\"OPC_SV_LOG_INTERVAL\",\"HmiLabel\":\"Data Log Interval\",\"Description\":\"Log interval for automatic OPC data logging\",\"Group\":\"CFG2,CLONE\",\"Units\":\"miliseconds\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SV_TEMP_COMP_SLOPE",
      "type": "float",
      "value": "0.17",
      "properties": "{\"Precision\":3,\"RawMin\":-2.0,\"RawMax\":2.0,\"EuMin\":-2.0,\"EuMax\":2.0,\"EuTag\":\"\",\"Default\":0.17,\"Name\":\"OPC_SV_TEMP_COMP_SLOPE\",\"HmiLabel\":\"Temp Comp Slope\",\"Description\":\"Slope to compensate for the sensor tempco\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SENSOR_FIRMWARE_REV",
      "type": "string",
      "value": "MMS-SLA 15,18-08-2015 09:55:5",
      "properties": "{\"Default\":\"TEST\",\"Name\":\"OPC_SENSOR_FIRMWARE_REV\",\"HmiLabel\":\"Sensor Firmware Rev\",\"Description\":\"Revision of the T640 Sensor Firmware\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_SYSLOG_FILESIZE",
      "type": "string",
      "value": "1556.71 KB",
      "properties": "{\"Default\":\"TEST\",\"Name\":\"OPC_SYSLOG_FILESIZE\",\"HmiLabel\":\"Log File Size\",\"Description\":\"Size of the log file\",\"Group\":\"CFG2\",\"Units\":\"Kb\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_DELETE_SYSLOG",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"OPC_DELETE_SYSLOG\",\"HmiLabel\":\"Delete Log File\",\"Description\":\"Delete the Log File for the T640\",\"Group\":\"CFG2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_LENGTH_PEAK_CHANNEL",
      "type": "int",
      "value": "64",
      "properties": "{\"RawMin\":0,\"RawMax\":256,\"EuMin\":0,\"EuMax\":256,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_LENGTH_PEAK_CHANNEL\",\"HmiLabel\":\"Length Peak\",\"Description\":\"Peak channel in Length distribution.  Labeled as \\\"sl\\\" in values returned by analysis app.\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "OPC_INSTRUMENT_WARNING",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"OPC_INSTRUMENT_WARNING\",\"HmiLabel\":\"Instrument Warning\",\"Description\":\"Instrument Warning Status\",\"Group\":\"CFG2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_INSTRUMENT_ERROR",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"OPC_INSTRUMENT_ERROR\",\"HmiLabel\":\"Instrument Error\",\"Description\":\"Instrument Error Status\",\"Group\":\"CFG2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_INST_WARN_MESSAGE",
      "type": "string",
      "value": "sendGetHistogram Error, Count: 1",
      "properties": "{\"Default\":\"TEST\",\"Name\":\"OPC_INST_WARN_MESSAGE\",\"HmiLabel\":\"Instrument Warning Message\",\"Description\":\"Instrument Warning Message\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_INST_ERROR_MESSAGE",
      "type": "string",
      "value": "TEST",
      "properties": "{\"Default\":\"TEST\",\"Name\":\"OPC_INST_ERROR_MESSAGE\",\"HmiLabel\":\"Instrument Error Message\",\"Description\":\"Instrument Error Message\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "AI_SAMPLE_FLOW5",
      "type": "float",
      "value": "4.99023675918579",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":10.0,\"EuMin\":0.0,\"EuMax\":10.0,\"EuTag\":\"\",\"Default\":5.0,\"Name\":\"AI_SAMPLE_FLOW5\",\"HmiLabel\":\"Sample Flow\",\"Description\":\"Sample Flow5\",\"Group\":\"LOG,TRIG,REALTIME\",\"Units\":\"LPM\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "FLOW5_CAL_ACTUAL_FLOW_VALUE",
      "type": "float",
      "value": "4.99",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":10.0,\"EuMin\":0.0,\"EuMax\":10.0,\"EuTag\":\"\",\"Default\":5.0,\"Name\":\"FLOW5_CAL_ACTUAL_FLOW_VALUE\",\"HmiLabel\":\"Flow5 Cal Actual Flow Value\",\"Description\":\"Actual flow5 value\",\"Group\":\"CLONE\",\"Units\":\"LPM\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "AI_SAMPLE_FLOW11",
      "type": "float",
      "value": "11.67",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":20.0,\"EuMin\":0.0,\"EuMax\":20.0,\"EuTag\":\"\",\"Default\":11.67,\"Name\":\"AI_SAMPLE_FLOW11\",\"HmiLabel\":\"Bypass Flow\",\"Description\":\"T640x Bypass Flow 11.67lpm\",\"Group\":\"LOG,TRIG,REALTIME\",\"Units\":\"LPM\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FLOW11_CAL_ACTUAL_FLOW_VALUE",
      "type": "float",
      "value": "11.67",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":20.0,\"EuMin\":0.0,\"EuMax\":20.0,\"EuTag\":\"\",\"Default\":11.67,\"Name\":\"FLOW11_CAL_ACTUAL_FLOW_VALUE\",\"HmiLabel\":\"T640x Bypass Flow\",\"Description\":\"Actual flow11 value\",\"Group\":\"CLONE\",\"Units\":\"LPM\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FLOW5_CAL_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"FLOW5_CAL_CONTROL\",\"HmiLabel\":\"Sample Flow Cal Control\",\"Description\":\"Controls the sample flow calibration\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"START\",\"Description\":\"Start Cal Mode\",\"Param\":\"\"},{\"Name\":\"CALIBRATE\",\"Description\":\"Perform calibration\",\"Param\":\"\"},{\"Name\":\"STOP\",\"Description\":\"Stop Cal Mode\",\"Param\":\"\"}]}"
    },
    {
      "name": "FLOW5_CAL_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"NEVER_RUN\",\"Description\":\"Calibration has never been run\",\"Param\":\"\"},\"Name\":\"FLOW5_CAL_STATE\",\"HmiLabel\":\"Sample Flow Cal State\",\"Description\":\"Sample Flow calibration state\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Cal state is idle, not in cal mode\",\"Param\":\"\"},{\"Name\":\"RUNNING\",\"Description\":\"In cal mode\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Calibration was successful\",\"Param\":\"\"},{\"Name\":\"FAILED\",\"Description\":\"Calibration failed\",\"Param\":\"\"},{\"Name\":\"NEVER_RUN\",\"Description\":\"Calibration has never been run\",\"Param\":\"\"}]}"
    },
    {
      "name": "FLOW11_CAL_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"FLOW11_CAL_CONTROL\",\"HmiLabel\":\"T640x Bypass Flow Cal Control\",\"Description\":\"Controls the T640x bypass flow calibration\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"START\",\"Description\":\"Start Cal Mode\",\"Param\":\"\"},{\"Name\":\"CALIBRATE\",\"Description\":\"Perform calibration\",\"Param\":\"\"},{\"Name\":\"STOP\",\"Description\":\"Stop Cal Mode\",\"Param\":\"\"}]}"
    },
    {
      "name": "FLOW11_CAL_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"NEVER_RUN\",\"Description\":\"Calibration has never been run\",\"Param\":\"\"},\"Name\":\"FLOW11_CAL_STATE\",\"HmiLabel\":\"T640x Bypass Flow Cal State\",\"Description\":\"T640x Bypass Flow calibration state\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Cal state is idle, not in cal mode\",\"Param\":\"\"},{\"Name\":\"RUNNING\",\"Description\":\"In cal mode\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Calibration was successful\",\"Param\":\"\"},{\"Name\":\"FAILED\",\"Description\":\"Calibration failed\",\"Param\":\"\"},{\"Name\":\"NEVER_RUN\",\"Description\":\"Calibration has never been run\",\"Param\":\"\"}]}"
    },
    {
      "name": "OPC_CAL_PEAK_CHANNEL",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":-131.0,\"RawMax\":125.0,\"EuMin\":-131.0,\"EuMax\":125.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"OPC_CAL_PEAK_CHANNEL\",\"HmiLabel\":\"Peak Channel\",\"Description\":\"Peak Channel during the CalDust dust calibration\",\"Group\":\"TRIG,REALTIME\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "SENSOR_CHECK_CHANNEL_COUNTS",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":0,\"RawMax\":100000,\"EuMin\":0,\"EuMax\":100000,\"EuTag\":\"\",\"Default\":0,\"Name\":\"SENSOR_CHECK_CHANNEL_COUNTS\",\"HmiLabel\":\"Peak Chan Counts\",\"Description\":\"Particle Counts in Peak Channel for Sensor Check\",\"Group\":\"REALTIME\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "1MIN-DATA",
      "type": "datalog",
      "value": "#16: [98.5266418457031, 22.72096824646, 12535, 25.3865966796875, -----, 32.9220199584961, 50, 1.959039, 0.77922, 1.99928159570589, 1.179819, 30.5560703277588, 5.00309419631958, 15.5488996505737, 23.5014190673828, 63.5555, 0, 5.00309419631958, -----, 151388]",
      "properties": "{\"IsEnabled\":true,\"LogTags\":\"AI_SAMPLE_PRESSURE_UNITS,OPC_RT_OUTSIDE_TEMP,OPC_RT_AMPLITUDE_COUNTS,OPC_RT_BOX_TEMP,AI_SAMPLE_FLOW11,OPC_RT_LED_TEMP,OPC_SV_P3_VALUE,PM10_CONC,PMC_CONC,PM10STP_CONC,PM2.5_CONC,OPC_RT_PWM_PUMP,AI_SAMPLE_FLOW5,OPC_RT_HUMIDITY,OPC_RT_SAMP_TEMP,OPC_RT_SL_VALUE,OPC_SPAN_DEVIATION,TOTAL_FLOW,OPC_RT_PWM_VALVE,SYSTEM_FREE_RAM\",\"Category\":2,\"MaxRecords\":500000,\"StartTime\":\"\\/Date(1554395700000-0700)\\/\",\"SpecificTimes\":null,\"Interval\":\"00:01:00\",\"IsAveraged\":false,\"TriggerTag\":\"\",\"TriggerCondition\":0,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"Default\":\"\",\"Name\":\"1MIN-DATA\",\"HmiLabel\":\"1MIN-DATA\",\"Description\":\"\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SAMPLE_FLOW_WARN",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"AI_SAMPLE_FLOW5\",\"TriggerCondition\":8,\"TriggerThresholdValue1\":\"4\",\"TriggerThresholdValue2\":\"6\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SAMPLE_FLOW_WARN\",\"HmiLabel\":\"Sample Flow Warning\",\"Description\":\"The Sample FLow is out of range\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "BYPASS_FLOW_WARN",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"AI_SAMPLE_FLOW11\",\"TriggerCondition\":8,\"TriggerThresholdValue1\":\"10\",\"TriggerThresholdValue2\":\"13.5\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"BYPASS_FLOW_WARN\",\"HmiLabel\":\"Bypass Flow Warning\",\"Description\":\"Bypass Flow is out of range\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SAMPLE_RH_HIGH",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_RT_HUMIDITY\",\"TriggerCondition\":5,\"TriggerThresholdValue1\":\"55\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SAMPLE_RH_HIGH\",\"HmiLabel\":\"SAMPLE RH HIGH\",\"Description\":\"The Sample RH is above the setpoint\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CHECK_LED",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_RT_LED_TEMP\",\"TriggerCondition\":4,\"TriggerThresholdValue1\":\"OPC_RT_BOX_TEMP\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"CHECK_LED\",\"HmiLabel\":\"Check LED\",\"Description\":\"Check if the LED is still on\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CHECK_PMT",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_SV_PMT_HV_SETTING\",\"TriggerCondition\":8,\"TriggerThresholdValue1\":\"800\",\"TriggerThresholdValue2\":\"2200\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"CHECK_PMT\",\"HmiLabel\":\"CHECK PMT\",\"Description\":\"The PMT HV setting is out of range\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SAMP_FLOW_SLOPE_OOR",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_SV_FLOW_5LPM_SLOPE\",\"TriggerCondition\":8,\"TriggerThresholdValue1\":\"0.85\",\"TriggerThresholdValue2\":\"1.15\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SAMP_FLOW_SLOPE_OOR\",\"HmiLabel\":\"Sample Flow Slope Warning\",\"Description\":\"The Sample Flow Calibration Slope is out of range\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "BYPS_FLOW_SLOPE_OOR",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_SV_FLOW_11.67LPM_SLOPE\",\"TriggerCondition\":8,\"TriggerThresholdValue1\":\"0.85\",\"TriggerThresholdValue2\":\"1.15\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"BYPS_FLOW_SLOPE_OOR\",\"HmiLabel\":\"Bypass Flow Slope Warning\",\"Description\":\"The Bypass Flow Calibration Slope is out of range\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CHECK_INT_PUMP",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_RT_PWM_PUMP\",\"TriggerCondition\":5,\"TriggerThresholdValue1\":\"80\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"CHECK_INT_PUMP\",\"HmiLabel\":\"CHECK INT PUMP\",\"Description\":\"Check internal pump\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CHECK_EXT_PUMP",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_RT_PWM_VALVE\",\"TriggerCondition\":5,\"TriggerThresholdValue1\":\"85\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"CHECK_EXT_PUMP\",\"HmiLabel\":\"CHECK EXT PUMP\",\"Description\":\"Check the external pump and/or bypass flow control valve\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SAMPLE_TEMP_WARN",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_RT_SAMP_TEMP\",\"TriggerCondition\":5,\"TriggerThresholdValue1\":\"60\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SAMPLE_TEMP_WARN\",\"HmiLabel\":\"SAMPLE TEMP WARN\",\"Description\":\"Sample Temperature Warning\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "BOX_TEMP_WARN",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_RT_BOX_TEMP\",\"TriggerCondition\":5,\"TriggerThresholdValue1\":\"60\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"BOX_TEMP_WARN\",\"HmiLabel\":\"BOX TEMP WARN\",\"Description\":\"Box temperature warning\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SAMP_PRES_SLOPE_OOR",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"OPC_SV_AMB_PRESS_SLOPE\",\"TriggerCondition\":8,\"TriggerThresholdValue1\":\"0.85\",\"TriggerThresholdValue2\":\"1.15\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SAMP_PRES_SLOPE_OOR\",\"HmiLabel\":\"AMB PRESS SLOPE OOR\",\"Description\":\"Ambient Pressure Calibration Slope is out of range\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SPAN_DEV_OOR",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"SPAN_DEV_48HR_AVG\",\"TriggerCondition\":8,\"TriggerThresholdValue1\":\"-3.0\",\"TriggerThresholdValue2\":\"3.0\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SPAN_DEV_OOR\",\"HmiLabel\":\"Perform Span Dust Check\",\"Description\":\"The Span Deviation is out of range\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "INST_MODE",
      "type": "enum",
      "value": "SAMPLE",
      "properties": "{\"Default\":{\"Name\":\"SAMPLE\",\"Description\":\"Sample mode\",\"Param\":\"\"},\"Name\":\"INST_MODE\",\"HmiLabel\":\"Instrument Mode\",\"Description\":\"Instrument mode\",\"Group\":\"TRACK_ALL_CHANGES\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"SAMPLE\",\"Description\":\"Sample mode\",\"Param\":\"\"},{\"Name\":\"SENSOR CFG\",\"Description\":\"Sensor Cfg Mode\",\"Param\":\"\"},{\"Name\":\"OFFSET ADJUST\",\"Description\":\"Offset Adjust Mode\",\"Param\":\"\"},{\"Name\":\"PMT ADJUST\",\"Description\":\"Sensor Check Mode\",\"Param\":\"BLINK\"},{\"Name\":\"FLOW CAL\",\"Description\":\"Flow Cal Mode\",\"Param\":\"BLINK\"},{\"Name\":\"LEAK CHECK\",\"Description\":\"Flow Cal Mode\",\"Param\":\"BLINK\"}]}"
    },
    {
      "name": "PM10_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10_1HR_AVG\",\"HmiLabel\":\"PM10 1Hr Avg\",\"Description\":\"PM10 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM10_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10_12HR_AVG\",\"HmiLabel\":\"PM10 12Hr Avg\",\"Description\":\"PM10 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM10_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10_24HR_AVG\",\"HmiLabel\":\"PM10 24Hr Avg\",\"Description\":\"PM10 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM25_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM25_1HR_AVG\",\"HmiLabel\":\"PM2.5 1Hr Avg\",\"Description\":\"PM2.5 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM25_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM25_12HR_AVG\",\"HmiLabel\":\"PM2.5 12Hr Avg\",\"Description\":\"PM2.5 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM25_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM25_24HR_AVG\",\"HmiLabel\":\"PM2.5 24Hr Avg\",\"Description\":\"PM2.5 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1_1HR_AVG\",\"HmiLabel\":\"PM1 1Hr Avg\",\"Description\":\"PM1 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1_12HR_AVG\",\"HmiLabel\":\"PM1 12Hr Avg\",\"Description\":\"PM1 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1_24HR_AVG\",\"HmiLabel\":\"PM1 24Hr Avg\",\"Description\":\"PM1 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PMTOT_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOT_1HR_AVG\",\"HmiLabel\":\"PMtot 1Hr Avg\",\"Description\":\"PMtot 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PMTOT_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOT_12HR_AVG\",\"HmiLabel\":\"PMtot 12Hr Avg\",\"Description\":\"PMtot 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PMTOT_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOT_24HR_AVG\",\"HmiLabel\":\"PMtot 24Hr Avg\",\"Description\":\"PMtot 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PMC_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMC_1HR_AVG\",\"HmiLabel\":\"PM10-2.5 1Hr Avg\",\"Description\":\"PM10-2.5 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PMC_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMC_12HR_AVG\",\"HmiLabel\":\"PM10-2.5 12Hr Avg\",\"Description\":\"PM10-2.5 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PMC_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMC_24HR_AVG\",\"HmiLabel\":\"PM10-2.5 24Hr Avg\",\"Description\":\"PM10-2.5 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM10STP_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10STP_1HR_AVG\",\"HmiLabel\":\"PM10STP 1Hr Avg\",\"Description\":\"PM10STP 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM10STP_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10STP_12HR_AVG\",\"HmiLabel\":\"PM10STP 12Hr Avg\",\"Description\":\"PM10STP 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM10STP_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM10STP_24HR_AVG\",\"HmiLabel\":\"PM10STP 24Hr Avg\",\"Description\":\"PM10STP 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM25STP_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM25STP_1HR_AVG\",\"HmiLabel\":\"PM2.5STP 1Hr Avg\",\"Description\":\"PM2.5STP 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM25STP_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM25STP_12HR_AVG\",\"HmiLabel\":\"PM2.5STP 12Hr Avg\",\"Description\":\"PM2.5STP 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM25STP_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM25STP_24HR_AVG\",\"HmiLabel\":\"PM2.5STP 24Hr Avg\",\"Description\":\"PM2.5STP 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1STP_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1STP_1HR_AVG\",\"HmiLabel\":\"PM1STP 1Hr Avg\",\"Description\":\"PM1STP 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1STP_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1STP_12HR_AVG\",\"HmiLabel\":\"PM1STP 12Hr Avg\",\"Description\":\"PM1STP 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PM1STP_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PM1STP_24HR_AVG\",\"HmiLabel\":\"PM1STP 24Hr Avg\",\"Description\":\"PM1STP 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "PMTOTSTP_1HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOTSTP_1HR_AVG\",\"HmiLabel\":\"PMtotSTP 1Hr Avg\",\"Description\":\"PMtotSTP 1Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PMTOTSTP_12HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOTSTP_12HR_AVG\",\"HmiLabel\":\"PMtotSTP 12Hr Avg\",\"Description\":\"PMtotSTP 12Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PMTOTSTP_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"PMTOTSTP_24HR_AVG\",\"HmiLabel\":\"PMtotSTP 24Hr Avg\",\"Description\":\"PMtotSTP 24Hr Rolling Concentration Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"ug/m3\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TOTAL_FLOW",
      "type": "float",
      "value": "4.99023675918579",
      "properties": "{\"Precision\":1,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"TOTAL_FLOW\",\"HmiLabel\":\"Total Flow\",\"Description\":\"Total Flow, Sample Flow + Bypass Flow\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"LPM\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "FO_640X",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=INSTALLED, False=NOT INSTALLED\",\"Default\":false,\"Name\":\"FO_640X\",\"HmiLabel\":\"640X Option\",\"Description\":\"640X Option Selection\",\"Group\":\"FO\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FO_PM1",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"FO_PM1\",\"HmiLabel\":\"PM1 Option\",\"Description\":\"PM1 Option Selection\",\"Group\":\"FO\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FO_PMTOT",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"FO_PMTOT\",\"HmiLabel\":\"PMtot Option\",\"Description\":\"PMtot Option Selection\",\"Group\":\"FO\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":true,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FO_NON_US_EPA_FEM_MODE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"FO_NON_US_EPA_FEM_MODE\",\"HmiLabel\":\"Non US EPA FEM Mode\",\"Description\":\"Non US EPA FEM Mode\",\"Group\":\"FO\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "CONC_VALID_FLAG",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"CONC_VALID_FLAG\",\"HmiLabel\":\"Concentration valid flag\",\"Description\":\"Concentration valid flag\",\"Group\":\"DOUTMAP\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "HOUR_AVG_PCT_VALID",
      "type": "int",
      "value": "75",
      "properties": "{\"RawMin\":1,\"RawMax\":100,\"EuMin\":1,\"EuMax\":100,\"EuTag\":\"\",\"Default\":75,\"Name\":\"HOUR_AVG_PCT_VALID\",\"HmiLabel\":\"Hourly Pct Valid\",\"Description\":\"Minimum percentage of valid readings for a valid hourly average\",\"Group\":\"CFG1,CLONE\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "24HR_AVG_PCT_VALID",
      "type": "int",
      "value": "90",
      "properties": "{\"RawMin\":1,\"RawMax\":100,\"EuMin\":1,\"EuMax\":100,\"EuTag\":\"\",\"Default\":90,\"Name\":\"24HR_AVG_PCT_VALID\",\"HmiLabel\":\"24Hr Pct Valid\",\"Description\":\"Minimum percentage of valid readings for a valid 24Hr average\",\"Group\":\"CFG1,CLONE\",\"Units\":\"%\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TIME_SYNC",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TIME_SYNC\",\"HmiLabel\":\"Periodically Sync Time\",\"Description\":\"Set to sync system time with network server on set intervals\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TIME_SYNC_USE_MANUAL",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TIME_SYNC_USE_MANUAL\",\"HmiLabel\":\"Use Custom Time Server\",\"Description\":\"Set to sync system time with network server\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MANUAL_TIME_SERVER",
      "type": "string",
      "value": "",
      "properties": "{\"Default\":\"\",\"Name\":\"MANUAL_TIME_SERVER\",\"HmiLabel\":\"User Specified Server URL\",\"Description\":\"Current time on the instrument\",\"Group\":\"CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TIME_SYNC_INTERVAL",
      "type": "int",
      "value": "2",
      "properties": "{\"RawMin\":1,\"RawMax\":65535,\"EuMin\":1,\"EuMax\":65535,\"EuTag\":\"\",\"Default\":2,\"Name\":\"TIME_SYNC_INTERVAL\",\"HmiLabel\":\"Time Sync Interval\",\"Description\":\"Time between NTP sync requests.\",\"Group\":\"CLONE\",\"Units\":\"Hours\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "LAST_INSTRUMENT_TIME_SYNCED",
      "type": "string",
      "value": "03/06/2025 1:27:22 PM",
      "properties": "{\"Default\":\"\",\"Name\":\"LAST_INSTRUMENT_TIME_SYNCED\",\"HmiLabel\":\"Last Sync Time\",\"Description\":\"Current time on the instrument\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "NEXT_INSTRUMENT_TIME_SYNC",
      "type": "string",
      "value": "03/06/2025 3:27:22 PM",
      "properties": "{\"Default\":\"\",\"Name\":\"NEXT_INSTRUMENT_TIME_SYNC\",\"HmiLabel\":\"Next Sync Time\",\"Description\":\"Current time on the instrument\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TIME_SYNC_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"Nothing to do\",\"Param\":\"\"},\"Name\":\"TIME_SYNC_CONTROL\",\"HmiLabel\":\"TIME_SYNC_CONTROL\",\"Description\":\"Time Sync Control\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"Nothing to do\",\"Param\":\"\"},{\"Name\":\"SYNC\",\"Description\":\"Sync the network time\",\"Param\":\"\"}]}"
    },
    {
      "name": "TIME_SYNC_STATE",
      "type": "enum",
      "value": "OK",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"Network Time Sync is inactive\",\"Param\":\"\"},\"Name\":\"TIME_SYNC_STATE\",\"HmiLabel\":\"TIME_SYNC_STATE\",\"Description\":\"Range control mode\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"Network Time Sync is inactive\",\"Param\":\"\"},{\"Name\":\"ACTIVE\",\"Description\":\"Network Time Sync is Syncing\",\"Param\":\"\"},{\"Name\":\"OK\",\"Description\":\"Network TIme Sync Completed\",\"Param\":\"\"},{\"Name\":\"ERROR\",\"Description\":\"Network TIme Sync Failed\",\"Param\":\"\"}]}"
    },
    {
      "name": "TIME_SYNC_PASSING",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=OK, False=FAIL\",\"Default\":false,\"Name\":\"TIME_SYNC_PASSING\",\"HmiLabel\":\"Time Sync Success Status\",\"Description\":\"Set when time sync fails to work\",\"Group\":\"TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_WARN_TIME_NOT_SYNCED",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":1,\"TriggerTag\":\"TIME_SYNC_PASSING\",\"TriggerCondition\":12,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_WARN_TIME_NOT_SYNCED\",\"HmiLabel\":\"Time Sync Failure\",\"Description\":\"Warning raised when the the system cannot sync the time with an NTP server\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DATE_TIME_TARGET_VALUE",
      "type": "string",
      "value": "",
      "properties": "{\"Default\":\"\",\"Name\":\"DATE_TIME_TARGET_VALUE\",\"HmiLabel\":\"Target Value for date time\",\"Description\":\"Target value for date time\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "UDP_BROADCAST_ENABLE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"UDP_BROADCAST_ENABLE\",\"HmiLabel\":\"Enable UDP Broadcast\",\"Description\":\"Activate/Deactivate UDP Broadcast\",\"Group\":\"CFG2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "UDP_BROADCAST_IP",
      "type": "string",
      "value": "192.168.0.1",
      "properties": "{\"Default\":\"0.0.0.0\",\"Name\":\"UDP_BROADCAST_IP\",\"HmiLabel\":\"UDP Broadcast IP\",\"Description\":\"UDP Broadcast IP Address\",\"Group\":\"CFG2,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_USER_PRESSURE_UNITS",
      "type": "enum",
      "value": "kPa",
      "properties": "{\"Default\":{\"Name\":\"kPa\",\"Description\":\"kPa\",\"Param\":\"\"},\"Name\":\"SV_USER_PRESSURE_UNITS\",\"HmiLabel\":\"Pressure Units\",\"Description\":\"Pressure Units of Measure for GUI\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"kPa\",\"Description\":\"kPa\",\"Param\":\"\"},{\"Name\":\"mmHg\",\"Description\":\"mm of mercury\",\"Param\":\"\"}]}"
    },
    {
      "name": "SV_PM10_DISP",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=SHOW, False=HIDE\",\"Default\":true,\"Name\":\"SV_PM10_DISP\",\"HmiLabel\":\"PM10 Display Option\",\"Description\":\"Shows/hides PM10 on the home screen\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_PMC_DISP",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=SHOW, False=HIDE\",\"Default\":true,\"Name\":\"SV_PMC_DISP\",\"HmiLabel\":\"PM10-2.5 Display Option\",\"Description\":\"Shows/hides PM10-2.5 on the home screen\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_PM10STP_DISP",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=SHOW, False=HIDE\",\"Default\":false,\"Name\":\"SV_PM10STP_DISP\",\"HmiLabel\":\"PM10STP Display Option\",\"Description\":\"Shows/hides PM10STP on the home screen\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_PM2.5STP_DISP",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=SHOW, False=HIDE\",\"Default\":false,\"Name\":\"SV_PM2.5STP_DISP\",\"HmiLabel\":\"PM2.5STP Display Option\",\"Description\":\"Shows/hides PM2.5STP on the home screen\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_PM1STP_DISP",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=SHOW, False=HIDE\",\"Default\":false,\"Name\":\"SV_PM1STP_DISP\",\"HmiLabel\":\"PM1STP Display Option\",\"Description\":\"Shows/hides PM1STP on the home screen\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SV_PMTOTSTP_DISP",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=SHOW, False=HIDE\",\"Default\":false,\"Name\":\"SV_PMTOTSTP_DISP\",\"HmiLabel\":\"PMtotSTP Display Option\",\"Description\":\"Shows/hides PMtotSTP on the home screen\",\"Group\":\"CFG1,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_ENHANCED_LOG",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"DUST_CAL_ENHANCED_LOG\",\"HmiLabel\":\"1 Dust Cal Enhanced Log\",\"Description\":\"Enable/Disable the dust cal enahnced log\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_OVERRIDE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"DUST_CAL_OVERRIDE\",\"HmiLabel\":\"1 Dust Cal Sim\",\"Description\":\"Enable/Disable the dust cal log file override\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_START_TIME",
      "type": "string",
      "value": "N/A",
      "properties": "{\"Default\":\"N/A\",\"Name\":\"DUST_CAL_START_TIME\",\"HmiLabel\":\"1 Dust Cal Sim Start TIme\",\"Description\":\"The first time in the log file\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_END_TIME",
      "type": "string",
      "value": "N/A",
      "properties": "{\"Default\":\"N/A\",\"Name\":\"DUST_CAL_END_TIME\",\"HmiLabel\":\"1 Dust Cal Sim End TIme\",\"Description\":\"The last time in the log file\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_ACTIVE_TIME",
      "type": "string",
      "value": "N/A",
      "properties": "{\"Default\":\"N/A\",\"Name\":\"DUST_CAL_ACTIVE_TIME\",\"HmiLabel\":\"1 Dust Cal Sim Active TIme\",\"Description\":\"The current active time in the log file\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_ACTIVE_INDEX",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":-2147483648,\"RawMax\":2147483647,\"EuMin\":-2147483648,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"DUST_CAL_ACTIVE_INDEX\",\"HmiLabel\":\"1 Dust Cal Sim Active Index\",\"Description\":\"The current index in the log file\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_DWELL_TIME",
      "type": "int",
      "value": "1",
      "properties": "{\"RawMin\":-2147483648,\"RawMax\":2147483647,\"EuMin\":-2147483648,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":1,\"Name\":\"DUST_CAL_DWELL_TIME\",\"HmiLabel\":\"1 Dust Cal Sim Dwell TIme\",\"Description\":\"The time to wait before going to the next entry\",\"Group\":\"CFG2\",\"Units\":\"Seconds\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DUST_CAL_MIN_PEAK_COUNTS",
      "type": "int",
      "value": "200",
      "properties": "{\"RawMin\":-2147483648,\"RawMax\":2147483647,\"EuMin\":-2147483648,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":200,\"Name\":\"DUST_CAL_MIN_PEAK_COUNTS\",\"HmiLabel\":\"Dust Cal Minimum Valid Peak Counts\",\"Description\":\"The minimum number of peak counts for a peak measurement to be considered valid.\",\"Group\":\"CFG2\",\"Units\":\"Counts\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SENSOR_CONFIG_BYPASS",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=BYPASS, False=NORMAL\",\"Default\":false,\"Name\":\"SENSOR_CONFIG_BYPASS\",\"HmiLabel\":\"1 Bypass Sensor Config\",\"Description\":\"Bypass sensor configuration (developer option)\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":false,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SERIAL_PALAS_TIMEOUT_COUNT",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":-2147483648,\"RawMax\":2147483647,\"EuMin\":-2147483648,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_SERIAL_PALAS_TIMEOUT_COUNT\",\"HmiLabel\":\"OPC Particle Timeout Count\",\"Description\":\"The number of serial commands that have timed out.\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SERIAL_SENSOR_TIMEOUT_COUNT",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":-2147483648,\"RawMax\":2147483647,\"EuMin\":-2147483648,\"EuMax\":2147483647,\"EuTag\":\"\",\"Default\":0,\"Name\":\"OPC_SERIAL_SENSOR_TIMEOUT_COUNT\",\"HmiLabel\":\"OPC Sensor Board Timeout Count\",\"Description\":\"The number of serial commands that have timed out.\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SERIAL_TIMEOUT_LIMIT",
      "type": "int",
      "value": "15",
      "properties": "{\"RawMin\":1,\"RawMax\":9999,\"EuMin\":1,\"EuMax\":9999,\"EuTag\":\"\",\"Default\":15,\"Name\":\"OPC_SERIAL_TIMEOUT_LIMIT\",\"HmiLabel\":\"OPC Serial Timeout Limit\",\"Description\":\"The number of serial timeouts that will trigger an opc reset.\",\"Group\":\"CFG1\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SERIAL_TIMEOUT_RETRY_PERIOD",
      "type": "int",
      "value": "90",
      "properties": "{\"RawMin\":1,\"RawMax\":3600,\"EuMin\":1,\"EuMax\":3600,\"EuTag\":\"\",\"Default\":90,\"Name\":\"OPC_SERIAL_TIMEOUT_RETRY_PERIOD\",\"HmiLabel\":\"OPC Serial Timeout Retry Period\",\"Description\":\"The time to wait before retrying serial communication after a timeout.\",\"Group\":\"CFG1,CLONE\",\"Units\":\"Seconds\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SERIAL_TIMEOUT",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"OPC_SERIAL_TIMEOUT\",\"HmiLabel\":\"OPC Serial Timeout\",\"Description\":\"State of the OPC when a serial device stops responding.\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SERIAL_RESET_ENABLE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ON, False=OFF\",\"Default\":false,\"Name\":\"OPC_SERIAL_RESET_ENABLE\",\"HmiLabel\":\"OPC Serial Auto Reset !DOES NOT WORK!\",\"Description\":\"Controls the OPC resetting if a serial device stops responding.\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_WARN_INTERNAL_SERIAL_TIMEOUT",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":1,\"TriggerTag\":\"OPC_SERIAL_TIMEOUT\",\"TriggerCondition\":11,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":false,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_WARN_INTERNAL_SERIAL_TIMEOUT\",\"HmiLabel\":\"Internal Serial Failure\",\"Description\":\"Warning raised when the system cannot communicate with an internal serial sensor\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "OPC_SYSTEM_FAULT",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"OPC_SYSTEM_FAULT\",\"HmiLabel\":\"OPC Serial Timeout\",\"Description\":\"State of opc system fault status.\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_WARN_SYSTEM_FAULT",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":1,\"TriggerTag\":\"OPC_SYSTEM_FAULT\",\"TriggerCondition\":12,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_WARN_SYSTEM_FAULT\",\"HmiLabel\":\"System Fault\",\"Description\":\"Warning raised when the system has any other system warning active\",\"Group\":\"LOG,TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DL_INCLUDE_UNIVERSAL_TIME",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":\"True=Include, False=Exclude\",\"Default\":true,\"Name\":\"DL_INCLUDE_UNIVERSAL_TIME\",\"HmiLabel\":\"DL Universal Time\",\"Description\":\"Denotes whether Universal time would be included in datalogger\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DL_TIME_FORMAT",
      "type": "enum",
      "value": "12HOUR",
      "properties": "{\"Default\":{\"Name\":\"12HOUR\",\"Description\":\"Use 12 hour format in datalogger\",\"Param\":\"\"},\"Name\":\"DL_TIME_FORMAT\",\"HmiLabel\":\"DL Time Format\",\"Description\":\"Specifies the time format in datalogger\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"12HOUR\",\"Description\":\"Use 12 hour format in datalogger\",\"Param\":\"\"},{\"Name\":\"24HOUR\",\"Description\":\"Use 24 hour format in datalogger\",\"Param\":\"\"}]}"
    },
    {
      "name": "DL_REPO_CHANGED",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=Include, False=Exclude\",\"Default\":false,\"Name\":\"DL_REPO_CHANGED\",\"HmiLabel\":\"DL Repo Changed\",\"Description\":\"Denotes whether the repo changed\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DL_LAST_DOWNLOAD_TIME",
      "type": "string",
      "value": "12/31/1999 12:00:00",
      "properties": "{\"Default\":\"12/31/1999 12:00:00\",\"Name\":\"DL_LAST_DOWNLOAD_TIME\",\"HmiLabel\":\"Last Download Time\",\"Description\":\"The timestamp of the last time datalog was downloaded\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DL_DAS_DOWNLOAD_FROM",
      "type": "string",
      "value": "12/31/1999 12:00:00",
      "properties": "{\"Default\":\"12/31/1999 12:00:00\",\"Name\":\"DL_DAS_DOWNLOAD_FROM\",\"HmiLabel\":\"DAS Download From\",\"Description\":\"The timestamp of the first specified time\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DL_DAS_DOWNLOAD_T1",
      "type": "string",
      "value": "12/31/1999 12:00:00",
      "properties": "{\"Default\":\"12/31/1999 12:00:00\",\"Name\":\"DL_DAS_DOWNLOAD_T1\",\"HmiLabel\":\"DAS Download Time 1\",\"Description\":\"The timestamp of the first specified time\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DL_DAS_DOWNLOAD_T2",
      "type": "string",
      "value": "12/31/1999 12:00:00",
      "properties": "{\"Default\":\"12/31/1999 12:00:00\",\"Name\":\"DL_DAS_DOWNLOAD_T2\",\"HmiLabel\":\"DAS Download Time 2\",\"Description\":\"The timestamp of the second specified time\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PRIGAS_PREC",
      "type": "int",
      "value": "1",
      "properties": "{\"RawMin\":0,\"RawMax\":6,\"EuMin\":0,\"EuMax\":6,\"EuTag\":\"\",\"Default\":1,\"Name\":\"PRIGAS_PREC\",\"HmiLabel\":\"PRIGAS Precision\",\"Description\":\"Precision used when displaying a Primary Gas concentration\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SECGAS_PREC",
      "type": "int",
      "value": "1",
      "properties": "{\"RawMin\":0,\"RawMax\":6,\"EuMin\":0,\"EuMax\":6,\"EuTag\":\"\",\"Default\":1,\"Name\":\"SECGAS_PREC\",\"HmiLabel\":\"SECGAS Precision\",\"Description\":\"Precision used when displaying a Secondary Gas concentration\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MODBUS_USE_USER_UNITS",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=DYNAMIC, False=LEGACY\",\"Default\":false,\"Name\":\"MODBUS_USE_USER_UNITS\",\"HmiLabel\":\"Modbus Units\",\"Description\":\"Restart Required. LEGACY for modbus registers to be in PPB, DYNAMIC for modbus registers to be user selected.\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYSTEM_TIME_FORMAT",
      "type": "enum",
      "value": "12HOUR",
      "properties": "{\"Default\":{\"Name\":\"12HOUR\",\"Description\":\"Use 12 hour format on the instrument display\",\"Param\":\"\"},\"Name\":\"SYSTEM_TIME_FORMAT\",\"HmiLabel\":\"System Time Format\",\"Description\":\"Specifies the time format on the instrument display\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"12HOUR\",\"Description\":\"Use 12 hour format on the instrument display\",\"Param\":\"\"},{\"Name\":\"24HOUR\",\"Description\":\"Use 24 hour format on the instrument display\",\"Param\":\"\"}]}"
    },
    {
      "name": "GENERAL_TIME_FORMAT",
      "type": "string",
      "value": "{0:MM/dd/yyyy h:mm:ss tt}",
      "properties": "{\"Default\":\"{0:MM/dd/yyyy h:mm:ss tt}\",\"Name\":\"GENERAL_TIME_FORMAT\",\"HmiLabel\":\"General Time Format\",\"Description\":\"Format of the timestamp for the datalog screen\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "ALERTS_TIME_FORMAT",
      "type": "string",
      "value": "{0:MM/dd/yyyy - h:mm:ss tt}",
      "properties": "{\"Default\":\"{0:MM/dd/yyyy - h:mm:ss tt}\",\"Name\":\"ALERTS_TIME_FORMAT\",\"HmiLabel\":\"Alerts Screen Time Format\",\"Description\":\"Format of the timestamp in the Alerts Screen\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DATALOG_TIME_FORMAT",
      "type": "string",
      "value": "{0:MM/dd/yyyy h:mm:ss tt}",
      "properties": "{\"Default\":\"{0:MM/dd/yyyy h:mm:ss tt}\",\"Name\":\"DATALOG_TIME_FORMAT\",\"HmiLabel\":\"Datalog Time Format\",\"Description\":\"Format of the timestamp for the datalog screen\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "INSTRUMENT_SHUTDOWN",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"No Operation Requested\",\"Param\":\"\"},\"Name\":\"INSTRUMENT_SHUTDOWN\",\"HmiLabel\":\"Instrument Shutdown\",\"Description\":\"Specifies the time format on the instrument display\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"No Operation Requested\",\"Param\":\"\"},{\"Name\":\"RESTART\",\"Description\":\"Restart Immediately\",\"Param\":\"\"},{\"Name\":\"FAIL\",\"Description\":\"An error was encountered saving system state\",\"Param\":\"\"}]}"
    },
    {
      "name": "INSTRUMENT_RESET",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"No Operation Requested\",\"Param\":\"\"},\"Name\":\"INSTRUMENT_RESET\",\"HmiLabel\":\"Instrument Reset\",\"Description\":\"Allows the user to perform instrument reset\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"No Operation Requested\",\"Param\":\"\"},{\"Name\":\"RESET\",\"Description\":\"Perform Reset Instrument\",\"Param\":\"\"},{\"Name\":\"CANCEL\",\"Description\":\"Cancel Instrument Reset\",\"Param\":\"\"}]}"
    },
    {
      "name": "PERIODIC_UPDATE_CHECK",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":true,\"Name\":\"PERIODIC_UPDATE_CHECK\",\"HmiLabel\":\"Periodically Check for Updates\",\"Description\":\"Set to enable a weekly check for firmware updates\",\"Group\":\"CFG,CLONE\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "LAST_INSTRUMENT_UPDATE_CHECK",
      "type": "string",
      "value": "01/01/0001 12:00:00 AM",
      "properties": "{\"Default\":\"\",\"Name\":\"LAST_INSTRUMENT_UPDATE_CHECK\",\"HmiLabel\":\"Last Update Check Time\",\"Description\":\"The last time the instrument checked for a firmware update\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PACKAGE_VERSION_NEEDING_UPDATE",
      "type": "string",
      "value": "",
      "properties": "{\"Default\":\"\",\"Name\":\"PACKAGE_VERSION_NEEDING_UPDATE\",\"HmiLabel\":\"Out of Date Package Version\",\"Description\":\"Version for the instrument when a new update was available\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "PERIODIC_UPDATE_FLAG",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"PERIODIC_UPDATE_FLAG\",\"HmiLabel\":\"Periodic Update Check Flag\",\"Description\":\"Set when a new firmware update is found\",\"Group\":\"TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_INFO_UPDATE_AVAIL",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":0,\"TriggerTag\":\"PERIODIC_UPDATE_FLAG\",\"TriggerCondition\":11,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":false,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_INFO_UPDATE_AVAIL\",\"HmiLabel\":\"System Update Available\",\"Description\":\"Raised when a new system update is available\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "BACKGROUND_PERIODIC_REPORT_UPLOAD",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":true,\"Name\":\"BACKGROUND_PERIODIC_REPORT_UPLOAD\",\"HmiLabel\":\"Background Periodic Report Upload\",\"Description\":\"Tag used to allow automatic periodic report upload to cloud service\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "REPORT_UPLOAD_INTERVAL",
      "type": "int",
      "value": "168",
      "properties": "{\"RawMin\":1,\"RawMax\":8640,\"EuMin\":1,\"EuMax\":8640,\"EuTag\":\"\",\"Default\":168,\"Name\":\"REPORT_UPLOAD_INTERVAL\",\"HmiLabel\":\"Report Upload Interval\",\"Description\":\"Time between periodic uploads to cloud\",\"Group\":\"CFG\",\"Units\":\"Hours\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "UPLOAD_REPORT_TO_CLOUD",
      "type": "bool",
      "value": "True",
      "properties": "{\"HmiValueMap\":null,\"Default\":true,\"Name\":\"UPLOAD_REPORT_TO_CLOUD\",\"HmiLabel\":\"Upload Report to Cloud\",\"Description\":\"Tag used to allow upload report to cloud service\",\"Group\":\"CFG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "REPORT_GENERATION_UPLOAD_CONTROL",
      "type": "enum",
      "value": "NONE",
      "properties": "{\"Default\":{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},\"Name\":\"REPORT_GENERATION_UPLOAD_CONTROL\",\"HmiLabel\":\"Report Generation Upload Control\",\"Description\":\"Controls the Report Generation Upload\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"NONE\",\"Description\":\"No new command\",\"Param\":\"\"},{\"Name\":\"GENERATE_AND_UPLOAD\",\"Description\":\"Generate the report and upload to USB\",\"Param\":\"\"},{\"Name\":\"CANCEL\",\"Description\":\"Cancel upload in progress\",\"Param\":\"\"}]}"
    },
    {
      "name": "REPORT_GENERATION_UPLOAD_STATE",
      "type": "enum",
      "value": "IDLE",
      "properties": "{\"Default\":{\"Name\":\"IDLE\",\"Description\":\"No operation in progress\",\"Param\":\"\"},\"Name\":\"REPORT_GENERATION_UPLOAD_STATE\",\"HmiLabel\":\"Report Generation Upload State\",\"Description\":\"Report generation upload state\",\"Group\":\"\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false,\"Enums\":[{\"Name\":\"IDLE\",\"Description\":\"No operation in progress\",\"Param\":\"\"},{\"Name\":\"GENERATING\",\"Description\":\"Upload in progress\",\"Param\":\"\"},{\"Name\":\"UPLOADING\",\"Description\":\"Upload in progress\",\"Param\":\"\"},{\"Name\":\"SUCCESS\",\"Description\":\"Upload successful\",\"Param\":\"\"},{\"Name\":\"FAILED\",\"Description\":\"Upload failed\",\"Param\":\"\"},{\"Name\":\"NO_ROOM\",\"Description\":\"Insufficient disk space\",\"Param\":\"\"}]}"
    },
    {
      "name": "CONFIG_RESET_FLAG",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"CONFIG_RESET_FLAG\",\"HmiLabel\":\"Config Reset Flag\",\"Description\":\"Set when tag file not found or is corrupted\",\"Group\":\"TRIG\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_WARN_CONFIG_RESET",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":1,\"TriggerTag\":\"CONFIG_RESET_FLAG\",\"TriggerCondition\":12,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_WARN_CONFIG_RESET\",\"HmiLabel\":\"Configuration Reset to Default\",\"Description\":\"Warning raised when config file is not found or is corrupted / unreadable\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "LOW_MEMORY_RESTART",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":2,\"TriggerTag\":\"SYSTEM_FREE_RAM\",\"TriggerCondition\":3,\"TriggerThresholdValue1\":\"115000\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"LOW_MEMORY_RESTART\",\"HmiLabel\":\"Low Memory Restart\",\"Description\":\"Warning raised when system free memory falls below minimum requirement.\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "LOW_MEMORY_WARNING",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":1,\"TriggerTag\":\"SYSTEM_FREE_RAM\",\"TriggerCondition\":3,\"TriggerThresholdValue1\":\"130000\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":true,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"LOW_MEMORY_WARNING\",\"HmiLabel\":\"Low Memory Warning\",\"Description\":\"Warning raised when system free memory approaches the minimum requirement.\",\"Group\":\"TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_TOTAL",
      "type": "int",
      "value": "9743536",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_TOTAL\",\"HmiLabel\":\"Memory Used Total\",\"Description\":\"Memory used by all tasks except platform monitor.\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_TEE",
      "type": "int",
      "value": "712056",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_TEE\",\"HmiLabel\":\"Memory Used TEE\",\"Description\":\"Memory used by the Execution-Engine task.\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_HMI",
      "type": "int",
      "value": "1921388",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_HMI\",\"HmiLabel\":\"Memory Used HMI\",\"Description\":\"Memory used by the HMI task\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_DL",
      "type": "int",
      "value": "1315780",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_DL\",\"HmiLabel\":\"Memory Used DL\",\"Description\":\"Memory used by the DataLogger task\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_AC",
      "type": "int",
      "value": "0",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_AC\",\"HmiLabel\":\"Memory Used AC\",\"Description\":\"Memory used by the AutoCal task\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_EV",
      "type": "int",
      "value": "589276",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_EV\",\"HmiLabel\":\"Memory Used EV\",\"Description\":\"Memory used by the Alarms task\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_MB",
      "type": "int",
      "value": "1739496",
      "properties": "{\"RawMin\":0,\"RawMax\":2147483647,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_MB\",\"HmiLabel\":\"Memory Used MB\",\"Description\":\"Memory used by the Modbus task\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_WEB",
      "type": "int",
      "value": "1422488",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":-2147483648,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_WEB\",\"HmiLabel\":\"Memory Used WEB\",\"Description\":\"Memory used by the HTTP Webserver task.\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_RU",
      "type": "int",
      "value": "872752",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_RU\",\"HmiLabel\":\"Memory Used RU\",\"Description\":\"Memory used by the Remote Updater task.\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "MEMORY_OPC",
      "type": "int",
      "value": "1085212",
      "properties": "{\"RawMin\":0,\"RawMax\":268435456,\"EuMin\":0,\"EuMax\":268435456,\"EuTag\":\"\",\"Default\":0,\"Name\":\"MEMORY_OPC\",\"HmiLabel\":\"Memory Used OPC\",\"Description\":\"Memory used by the Remote Updater task.\",\"Group\":\"MEMORY\",\"Units\":\"Bytes\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_SYSTEM",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_SYSTEM\",\"HmiLabel\":\"Tag Event Report System\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"CFG2,TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_TEE",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_TEE\",\"HmiLabel\":\"Tag Event Report TEE\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_HMI",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_HMI\",\"HmiLabel\":\"Tag Event Report HMI\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_DL",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_DL\",\"HmiLabel\":\"Tag Event Report DL\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_EV",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_EV\",\"HmiLabel\":\"Tag Event Report EV\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_MB",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_MB\",\"HmiLabel\":\"Tag Event Report MB\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_WEB",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_WEB\",\"HmiLabel\":\"Tag Event Report WEB\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_RU",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_RU\",\"HmiLabel\":\"Tag Event Report RU\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "TAG_EVENT_OPC",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":null,\"Default\":false,\"Name\":\"TAG_EVENT_OPC\",\"HmiLabel\":\"Tag Event Report OPC\",\"Description\":\"Tag used to trigger tag event debug log\",\"Group\":\"TEVENT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FLOW5_CV_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"FLOW5_CV_24HR_AVG\",\"HmiLabel\":\"Sample Flow CV 24Hr Avg\",\"Description\":\"Sample Flow Coefficient of Variation 24Hr Rolling Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "FLOW11_CV_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"FLOW11_CV_24HR_AVG\",\"HmiLabel\":\"Bypass Flow CV 24Hr Avg\",\"Description\":\"Bypass Flow Coefficient of Variation 24Hr Rolling Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "FLOWTOT_CV_24HR_AVG",
      "type": "float",
      "value": "0",
      "properties": "{\"Precision\":2,\"RawMin\":0.0,\"RawMax\":10000.0,\"EuMin\":0.0,\"EuMax\":10000.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"FLOWTOT_CV_24HR_AVG\",\"HmiLabel\":\"Total Flow CV 24Hr Avg\",\"Description\":\"Total Flow Coefficient of Variation 24Hr Rolling Average\",\"Group\":\"LOG,REALTIME,TRIG,HIST\",\"Units\":\"\",\"IsValueValid\":false,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":true}"
    },
    {
      "name": "NUM_CONC",
      "type": "float",
      "value": "33.3041963206801",
      "properties": "{\"Precision\":0,\"RawMin\":0.0,\"RawMax\":999999.0,\"EuMin\":0.0,\"EuMax\":999999.0,\"EuTag\":\"\",\"Default\":0.0,\"Name\":\"NUM_CONC\",\"HmiLabel\":\"Number Concentration\",\"Description\":\"Real time total particle number concentration\",\"Group\":\"LOG,REALTIME,TRIG\",\"Units\":\"#/cm3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":true,\"CanDashboard\":true}"
    },
    {
      "name": "DA_OFFSET1",
      "type": "float",
      "value": "1.861",
      "properties": "{\"Precision\":3,\"RawMin\":-5.0,\"RawMax\":5.0,\"EuMin\":-5.0,\"EuMax\":5.0,\"EuTag\":\"\",\"Default\":1.861,\"Name\":\"DA_OFFSET1\",\"HmiLabel\":\"DA Offset 1\",\"Description\":\"DA offset factor below 20C\",\"Group\":\"CFG2\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DA_OFFSET2",
      "type": "float",
      "value": "0.925",
      "properties": "{\"Precision\":3,\"RawMin\":-5.0,\"RawMax\":5.0,\"EuMin\":-5.0,\"EuMax\":5.0,\"EuTag\":\"\",\"Default\":0.925,\"Name\":\"DA_OFFSET2\",\"HmiLabel\":\"DA Offset 2\",\"Description\":\"DA offset factor above 20C\",\"Group\":\"CFG2\",\"Units\":\"ug/m3\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "DA_SLOPE",
      "type": "float",
      "value": "0.813233",
      "properties": "{\"Precision\":6,\"RawMin\":0.5,\"RawMax\":1.5,\"EuMin\":0.5,\"EuMax\":1.5,\"EuTag\":\"\",\"Default\":0.813233,\"Name\":\"DA_SLOPE\",\"HmiLabel\":\"DA Slope\",\"Description\":\"DA slope factor\",\"Group\":\"CFG2\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "FO_T640_DATA_ALIGNMENT",
      "type": "bool",
      "value": "False",
      "properties": "{\"HmiValueMap\":\"True=ENABLED, False=DISABLED\",\"Default\":false,\"Name\":\"FO_T640_DATA_ALIGNMENT\",\"HmiLabel\":\"T640 Data Alignment\",\"Description\":\"T640 Data Alignment\",\"Group\":\"FO\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":true,\"IsVisible\":true,\"IsNonVolatile\":true,\"IsDashboard\":false,\"CanDashboard\":false}"
    },
    {
      "name": "SYS_OK_WARN",
      "type": "event",
      "value": "False",
      "properties": "{\"IsEnabled\":true,\"LogLevel\":0,\"TriggerTag\":\"SAMPLE_FLOW_WARN=FALSE AND BYPASS_FLOW_WARN=FALSE AND SAMPLE_RH_HIGH=FALSE AND CHECK_LED=FALSE AND CHECK_PMT=FALSE AND SAMP_FLOW_SLOPE_OOR=FALSE AND BYPS_FLOW_SLOPE_OOR=FALSE AND CHECK_INT_PUMP=FALSE AND CHECK_EXT_PUMP=FALSE AND SAMPLE_TEMP_WARN=FALSE AND BOX_TEMP_WARN=FALSE AND SAMP_PRES_SLOPE_OOR=FALSE AND SPAN_DEV_OOR=FALSE AND SYS_WARN_INTERNAL_SERIAL_TIMEOUT=FALSE AND SYS_WARN_SYSTEM_FAULT=FALSE AND SYS_WARN_REARBOARD=FALSE AND SYS_WARN_RELAYBOARD=FALSE AND SYS_WARN_ANALOG_CAL=FALSE AND SYS_WARN_SYSSERVICE=FALSE AND SYS_WARN_FRONT_PANEL=FALSE\",\"TriggerCondition\":11,\"TriggerThresholdValue1\":\"\",\"TriggerThresholdValue2\":\"\",\"IsLatching\":false,\"WaitForWarmup\":false,\"RealTimeValue\":false,\"HmiValueMap\":\"\",\"Default\":false,\"Name\":\"SYS_OK_WARN\",\"HmiLabel\":\"System OK Status\",\"Description\":\"System OK Status\",\"Group\":\"LOG,TRIG,DOUTMAP,SYS_EVT\",\"Units\":\"\",\"IsValueValid\":true,\"IsReadOnly\":false,\"IsNetwork\":false,\"IsVisible\":false,\"IsNonVolatile\":false,\"IsDashboard\":false,\"CanDashboard\":false}"
    }
  ]
}

