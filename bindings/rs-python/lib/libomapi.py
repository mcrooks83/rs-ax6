from c import pylibomapi_wrapper as omlib  # generated from demolib.h by ctypesgen
import ctypes
from datetime import datetime

#should probably create an API class for types as well as functions
# wrapped functions
def start_up():
    result = omlib.OmStartup(omlib.OM_VERSION)
    #add error handling
    return result

def set_device_callback(func):
    callback_func = omlib.OmDeviceCallback(func)
    omlib.OmSetDeviceCallback(callback_func, None)
    return True

def get_num_of_connected_devices():
    result = omlib.OmGetDeviceIds(None, 0)
    if(omlib.OM_FAILED(result)):
        print(f"ERROR: OmGetDeviceIds {result}")
        return -1
    return result

def get_device_ids(num_of_devices):
    device_ids_list = [0] * num_of_devices
    device_ids = (omlib.c_int * len(device_ids_list))(*device_ids_list)
    print(device_ids)
    result = omlib.OmGetDeviceIds(device_ids, num_of_devices)

   # if (OM_FAILED(result)) { printf("ERROR: OmGetDeviceIds() %s\n", OmErrorString(result)); return -1; }
    if(omlib.OM_FAILED(result)):
        print(f"ERROR OmGetDeviceIds {result}")
    if(result > 0 ):
        #turn into python list
        for idx, d in enumerate(device_ids):
            device_ids_list[idx] = d
        return device_ids_list

def set_led(device_id, color):
    #if (OM_FAILED(result)) { printf("WARNING: OmSetLed() %s\n", OmErrorString(result)); }
    if(color == "blue"):
        result = omlib.OmSetLed(device_id, omlib.OM_LED_BLUE)
        return result
    elif(color == "white"):
        result = omlib.OmSetLed(device_id, omlib.OM_LED_WHITE)
        return result

#OmGetBatteryLevel(deviceId);
def get_battery_level(device_id):
    battery_level = omlib.OmGetBatteryLevel(device_id)
    return battery_level

def get_battery_health(device_id):
    battery_health = omlib.OmGetBatteryHealth(device_id)
    return battery_health

#OmGetAccelerometer(deviceId, &accelerometer[0], &accelerometer[1], &accelerometer[2]);
def get_accelermoter(device_id):
    accelerometer_list = [ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(0)]  # Initialize with zeros

    result = omlib.OmGetAccelerometer(device_id,
                                      ctypes.pointer(accelerometer_list[0]),
                                      ctypes.pointer(accelerometer_list[1]),
                                      ctypes.pointer(accelerometer_list[2]))
    #if (omlib.OM_FAILED(result)):
    accel = [c_int.value for c_int in accelerometer_list] 
    return accel

#OmSelfTest(deviceId);
def self_test(device_id):
    result = omlib.OmSelfTest(device_id)
    return result

#OmGetMemoryHealth(deviceId);
def get_memory_health(device_id):
    result = omlib.OmGetMemoryHealth(device_id)
    return result

#def free_devices(device_ids):
#    omlib.free(device_ids)
#    return f"devices free"

def shut_down():
    print("shutting down api")
    result = omlib.OmShutdown()
    return result

def set_now_time(device_id, now):
    nowTime = omlib.OM_DATETIME_FROM_YMDHMS(now.year, now.month, now.day, now.hour, now.minute, now.second)
    result = omlib.OmSetTime(device_id, nowTime)
    print("set time func", result)
    #test error handling also
    if (omlib.OM_FAILED(result)): 
        print("ERROR: OmSetTime()", omlib.OmErrorString(result))
    return result

def set_accel_config(device_id, rate, range ):
    result = omlib.OmSetAccelConfig(device_id, rate, range)
    if(omlib.OM_FAILED(result)):
        print("ERROR OmSetAccelConfig", omlib.OmErrorString(result))
        return 0
    return result

def has_gyro(device_id):
    SerialBuffer = ctypes.c_char * omlib.OM_MAX_PATH  #(256)
    serial_buffer = SerialBuffer()
    if (omlib.OM_FAILED(omlib.OmGetDeviceSerial(device_id, serial_buffer))):
        return False
    result = serial_buffer[:3] == b"AX6"
    return result

def set_session_id(device_id, session_id):
    result = omlib.OmSetSessionId(device_id, session_id) #session is an unsigend int
    if(omlib.OM_FAILED(result)):
        print("ERROR OmSetSessionId", omlib.OmErrorString(result))
    return result

def set_max_samples(device_id, max):
    omlib.OmSetMaxSamples(device_id, max)

def clear_max_samples(device_id):
   print(f"clearing max samples for {device_id}")
   omlib.OmSetMaxSamples(device_id, 0)

def clear_meta_data(device_id):
    print(f"clearing meta data for {device_id}")
    omlib.OmSetMetadata(device_id, None, 0)

# def set_delays(start_day, start_hour, stop_day, stop_hour)

def set_delays(device_id, start_time, stop_time):
    result = omlib.OmSetDelays(device_id, start_time, stop_time)
    if (omlib.OM_FAILED(result)):
        print("ERROR OmSetDelays", omlib.OmErrorString(result))
        return 0
    return result

def commit_recording_settings(device_id):
    result = omlib.OmEraseDataAndCommit(device_id, omlib.OM_ERASE_WIPE)
    if (omlib.OM_FAILED(result)):
        print("ERROR OmEraseDataAndCommit", omlib.OmErrorString(result))
        return 0
    return result



### status functions

#int OmGetVersion(int deviceId, int *firmwareVersion, int *hardwareVersion

#int OmGetDeviceSerial(int deviceId, char *serialBuffer)

#int OmGetDevicePort(int deviceId, char *portBuffer)

#int OmGetDevicePath(int deviceId, char *pathBuffer)

#int OmGetTime(int deviceId, OM_DATETIME *time)

#int OmSetTime(int deviceId, OM_DATETIME time)
    
#int OmIsLocked(int deviceId, int *hasLockCode)

#int OmSetLock(int deviceId, unsigned short code)

#int OmUnlock(int deviceId, unsigned short code)

#int OmSetEcc(int deviceId, int state)

#int OmGetEcc(int deviceId)

#int OmCommand(int deviceId, const char *command, char *buffer, size_t bufferSize, const char *expected, unsigned int timeoutMs, char **parseParts, int parseMax)
