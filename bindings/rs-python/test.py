import sys


from lib import libomapi as api


#static void deviceCallback(void *reference, int deviceId, OM_DEVICE_STATUS status)

def device_callback(ref, deviceId, status):
       # ref is user defined and in this case Non

       #if status == 1 or api_wrap.OM_DEVICE_CONNECTED
        if(status == 1):
            #can test device here also
            print(f"DC: device {deviceId} connected")
        elif(status == 0):
            print(f'DC: device {deviceId} removed')

# test a connected device
def test_device(device_id):
    print(f"testing device {device_id}")

    result = api.set_led(device_id, "blue")
    if(result == 0):
        print(f"Led set to blue for {device_id}")
        result = api.set_led(device_id, "white")
        print(f"reset led to white for {device_id}")
	
    # get battery health
    batt_level = api.get_battery_level(device_id)
    print(f"battery level for device {device_id} {batt_level}")

    accelerometer = api.get_accelermoter(device_id)

    print(accelerometer)

# set up for testing
def test():

    is_set = api.set_device_callback(device_callback)
    print("is callback set:", is_set)

    result = api.start_up() # returns 0 
    print("api started")

    num_devices = api.get_num_of_connected_devices()
    print("Number of devices attached", num_devices)

    if(num_devices==0):
         print(f"No Devices Found")
    else:
        if(num_devices > 0):
            device_ids = api.get_device_ids(num_devices)
            print("device IDs", device_ids)

        #/* For each device currently connected... */
        for idx, id in enumerate(device_ids):
            #print(f"testing device {idx} {id}")
            test_device(id)
    
    #Python(89085,0x1199eb600) malloc: *** error for object 0x10da70890: pointer being freed was not allocated
    #result = api.free_devices(device_ids)
    #print(result)
         
    #shut down
    result = api.shut_down()
    print(result)





def main(argv=None):
    if argv is None:
        argv = sys.argv

    test()

    return 0


if __name__ == "__main__":
    sys.exit(main())