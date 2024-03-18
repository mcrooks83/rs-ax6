// make && gcc -o test -I../include -Dtest_main=main test.c -lpthread -L. -lomapi -framework CoreFoundation -framework IOKit -framework DiskArbitration
// /dev/tty.usbmodem* /dev/cu.usbmodem*
// /Volumes/AX317_?????
// ioreg -p IOUSB -l -b
/* 
 * Copyright (c) 2009-, Newcastle University, UK.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without 
 * modification, are permitted provided that the following conditions are met: 
 * 1. Redistributions of source code must retain the above copyright notice, 
 *    this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright notice, 
 *    this list of conditions and the following disclaimer in the documentation 
 *    and/or other materials provided with the distribution.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE 
 * POSSIBILITY OF SUCH DAMAGE. 
 */

// Open Movement API - Device Discovery (Mac OS)
// Dan Jackson, 2011-

// Some code based on "USBPrivateDataSample" by Apple.
// Some code based on "Get USB Drive Serial Number on Os X in C++": https://oroboro.com/usb-serial-number-osx/
#if defined(__APPLE__)

#include <CoreFoundation/CoreFoundation.h>

#include <IOKit/IOKitLib.h>
#include <IOKit/IOMessage.h>
#include <IOKit/IOCFPlugIn.h>
#include <IOKit/usb/IOUSBLib.h>

#include <DiskArbitration/DiskArbitration.h>

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <sys/sysctl.h>
#include <errno.h>
#include <paths.h>
#include <sys/param.h>
#include <mach/mach.h>
#include <mach/error.h>

// #include <IOKit/IOKitLib.h>
#include <IOKit/IOCFPlugIn.h>
// #include <IOKit/usb/IOUSBLib.h>

#include <IOKit/IOBSD.h>
#include <IOKit/storage/IOCDMedia.h>
#include <IOKit/storage/IOMedia.h>
#include <IOKit/storage/IOCDTypes.h>
#include <IOKit/storage/IOMediaBSDClient.h>

#include <IOKit/serial/IOSerialKeys.h>
#include <IOKit/serial/ioss.h>

#include <IOKit/usb/IOUSBLib.h>



#include "omapi-internal.h"

#define VID 0x04D8
#define PID 0x0057

typedef struct DeviceData
{
	io_object_t notification;
	IOUSBDeviceInterface **deviceInterface;
	CFStringRef deviceName;
	UInt32 locationID;
	const char *serialNumber;
	unsigned int deviceId;
	const char *mountPath;
	const char *serialDevice;
} DeviceData;

static IONotificationPortRef gNotifyPort;
static io_iterator_t gAddedIter;
static CFRunLoopRef gRunLoop;

// Get the OS version (AA.BB.CC) as a single number (digits AABBCC)
static unsigned int osVersion()
{
	int name[] = { CTL_KERN, KERN_OSRELEASE };
	char versionString[64];
	size_t versionStringLen = sizeof(versionString) - 1;
	if (sysctl(name, sizeof(name)/sizeof(name[0]), versionString, &versionStringLen, NULL, 0) != 0) return 0;
	uint32_t major = 0, minor = 0;
	if (sscanf(versionString, "%u.%u", &major, &minor) != 2) return 0;
	if (minor > 99) minor = 99;
	if (major >= 20) {	// macOS 11+
		return ((major - 9) * 100 + minor) * 100;
	} else if (major >= 5) {	// macOS 10.1.1+
		return (10 * 100 + (major - 4)) * 100 + minor;
	}
	return 0;
}

static char *cfStringRefToCString(CFStringRef cfString)
{
	if (!cfString) return NULL;
	static char string[2048];
	string[0] = '\0';
	// CFShow(CFCopyDescription(cfString));
	CFStringGetCString(cfString, string, MAXPATHLEN, kCFStringEncodingUTF8);
	return &string[0];
}
 
static char *cfTypeToCString(CFTypeRef cfString)
{
	if (!cfString) return NULL;
	static char deviceFilePath[2048];
	deviceFilePath[0] = '\0';
	// CFShow( CFCopyDescription(cfString));
	CFStringGetCString(CFCopyDescription(cfString), deviceFilePath, MAXPATHLEN, kCFStringEncodingUTF8);
	char *p = deviceFilePath;
	while (*p != '\"') p++; p++;
	char *pp = p;
	while (*pp != '\"') pp++;
	*pp = '\0';
	if (isdigit(*p)) *p = 'x';
	return p;
}

// 
static const char *findMount(io_service_t usbDevice)
{
	
	char *volumePath = NULL;

	// Check IOUSBDevice
	OmLog(3, "MAC: usbDevice: %p\n", (void *)usbDevice);
	
	if (!IOObjectConformsTo(usbDevice, "IOUSBDevice")) return NULL;

	// Check is IOUSBDevice, or IOUSBHostDevice since El Capitan
	io_name_t className;
	IOObjectGetClass(usbDevice, className);
	OmLog(3, "MAC: ...className: %s\n", (const char *)className);
	if (strcmp(className, "IOUSBDevice") != 0 && strcmp(className, "IOUSBHostDevice") != 0) return NULL;

	// Device name
	io_name_t deviceName;
	IORegistryEntryGetName(usbDevice, deviceName);
	OmLog(3, "MAC: ...deviceName: %s\n", (const char *)deviceName);

	

	// Wait for the mount point - increase 
	CFStringRef bsdName = NULL;
	//int i;
	int flag = 1;
	for (int i = 0; i < 200; i++)
	{

		//should return this
		//bsdName = "/dev/disk2s1";
	
		bsdName = (CFStringRef) IORegistryEntrySearchCFProperty (
			usbDevice,
			kIOServicePlane,
			CFSTR (kIOBSDNameKey),
			kCFAllocatorDefault,
			kIORegistryIterateRecursively );

		
		if (bsdName)
		{
			
			char bsdNameBuf[4096];
			sprintf(bsdNameBuf, "/dev/%ss1", cfStringRefToCString(bsdName));
			//sprintf(bsdNameBuf, bsdName);
			const char *bsdNameC = &(bsdNameBuf[0]);
			OmLog(3, "MAC: ...bsd name: %s\n", bsdNameC);

			DASessionRef daSession = DASessionCreate(kCFAllocatorDefault);
			DADiskRef disk = DADiskCreateFromBSDName(kCFAllocatorDefault, daSession, bsdNameC);

			// If mounted...
			if (disk)
			{
				int j;

				// Wait for disk volumes to mount
				for (j = 0; j < 200; j++)
				{
					CFDictionaryRef desc = DADiskCopyDescription(disk);
					// If have volume...
					if (desc)
					{
						CFTypeRef str = CFDictionaryGetValue(desc, kDADiskDescriptionVolumeNameKey);
						char *volumeName = cfTypeToCString(str);
						if (volumeName && strlen(volumeName))
						{
							// mounted volume
							volumePath = malloc(4096);
							sprintf(volumePath, "/Volumes/%s", volumeName);
							OmLog(3, "MAC: ...volume: %s\n", volumePath);

							CFRelease(desc);
							break;
						}
						else
						{
							CFRelease(desc);
						}
					}
					// wait for mounted volume
					//OmLog(3, ".");
					usleep(100 * 1000);
				}
				CFRelease(disk);
			}
			CFRelease(daSession);
			break;
		}
		else
		{
			//printf("waiting for mounted disk");
			// wait for mounted disk
			usleep(10 * 1000);
		}
	}
	return volumePath;
}

static const char *getUSBStringDescriptor(IOUSBDeviceInterface182 **usbDevice, UInt8 idx)
{
	UInt16 buffer[64];
	IOUSBDevRequest request;
	request.bmRequestType = USBmakebmRequestType(kUSBIn, kUSBStandard, kUSBDevice);
	request.bRequest = kUSBRqGetDescriptor;
	request.wValue = (kUSBStringDesc << 8) | idx;
	request.wIndex = 0x409; // english
	request.wLength = sizeof( buffer );
	request.pData = buffer;

	kern_return_t err = (*usbDevice)->DeviceRequest(usbDevice, &request);
	if (err != 0) 
	{
		OmLog(2, "ERROR: DeviceRequest failed.\n");
		return NULL;
	}
  
	char *stringValue = malloc(128);
	int count = (request.wLenDone - 1) / 2;
	int i;
	for (i = 0; i < count; i++)
	{
		stringValue[i] = buffer[i+1];
	}
	stringValue[i] = '\0'; 
	return stringValue;
}

static unsigned int DeviceIdFromSerialNumber(const char *serialNumber)
{
	// Return the number found at the end of the string (0 if none)
	bool inNumber = false;
    unsigned int value = (unsigned int)-1;
    const char *p;
    for (p = serialNumber; *p != 0; p++)
    {
		if (*p >= '0' && *p <= '9')
		{
			if (!inNumber) { inNumber = true; value = 0; }
			value = (10 * value) + (*p - '0');
		}
		else inNumber = false;
    }
    return value;
}

static const char *getUSBSerialNumber(io_service_t usbDevice)
{
	SInt32 score;
	IOCFPlugInInterface **plugin;
	IOUSBDeviceInterface182 **usbDevice182 = NULL;
	kern_return_t err;
	err = IOCreatePlugInInterfaceForService(usbDevice, kIOUSBDeviceUserClientTypeID, kIOCFPlugInInterfaceID, &plugin, &score);
	if (err != 0) 
	{
		OmLog(2, "ERROR: IOCreatePlugInInterfaceForService failed.\n");
		return NULL;
	}
	err = (*plugin)->QueryInterface(plugin, CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID182), (void **)&usbDevice182);
	IODestroyPlugInInterface(plugin);
	if (err != 0) 
	{
		OmLog(2, "ERROR: IODestroyPlugInInterface failed.\n");
		return NULL;
	}

	// UInt8 vidIdx;
	// (*usbDevice182)->USBGetManufacturerStringIndex(usbDevice182, &vidIdx);
	// getUSBStringDescriptor(usbDevice182, vidIdx);

	// UInt8 pidIdx;
	// (*usbDevice182)->USBGetProductStringIndex(usbDevice182, &pidIdx);
	// getUSBStringDescriptor(usbDevice182, pidIdx));

	// UInt16 rev;
	// (*usbDevice182)->GetDeviceReleaseNumber(usbDevice182, &rev);
	// rev

	UInt8 snIdx;
	(*usbDevice182)->USBGetSerialNumberStringIndex(usbDevice182, &snIdx);
	if (snIdx <= 0) return NULL; // What is the index actually set to if there is no serial number?
	return getUSBStringDescriptor(usbDevice182, snIdx);
}

// Find the serial port path for the specified USB serial ID string
const char *findSerial(const char *usbSerial)
{
	char *serialPath = NULL;

	CFMutableDictionaryRef classes;
	if (!(classes = IOServiceMatching(kIOSerialBSDServiceValue)))
	{
		OmLog(2, "ERROR: IOServiceMatching failed.\n");
		return NULL;
	}

	io_iterator_t iter;
	if (IOServiceGetMatchingServices(kIOMasterPortDefault, classes, &iter) != KERN_SUCCESS)
	{
		OmLog(2, "ERROR: IOServiceGetMatchingServices failed.\n");
		return NULL;
	}

	io_object_t ioport;
	while ((ioport = IOIteratorNext(iter)))
	{
		CFTypeRef cf_property;
		if (!(cf_property = IORegistryEntryCreateCFProperty(ioport, CFSTR(kIOCalloutDeviceKey), kCFAllocatorDefault, 0)))
		{
			OmLog(2, "WARNING: IORegistryEntryCreateCFProperty failed.\n");
			IOObjectRelease(ioport);
			continue;
		}
		char path[PATH_MAX];
		Boolean result = CFStringGetCString(cf_property, path, sizeof(path), kCFStringEncodingASCII);
		//OmLog(3, "MAC: io path: %s\n", path);
		CFRelease(cf_property);
		if (!result)
		{
			OmLog(2, "WARNING: CFStringGetCString failed.\n");
			IOObjectRelease(ioport);
			continue;
		}

		if ((cf_property = IORegistryEntrySearchCFProperty(ioport, kIOServicePlane, CFSTR("USB Serial Number"), kCFAllocatorDefault, kIORegistryIterateRecursively | kIORegistryIterateParents)))
		{
			char serial[128];
			if (CFStringGetCString(cf_property, serial, sizeof(serial), kCFStringEncodingASCII))
			{
				//OmLog(3, "MAC: ...compare serial: %s = %u\n", serial, usbSerial);
				if (strcmp(serial, usbSerial) == 0) {
					serialPath = malloc(PATH_MAX);
					strcpy(serialPath, path);
					OmLog(3, "MAC: Found serial number %s at path: %s\n", serial, path);
					break;
				}
			}
			CFRelease(cf_property);
		}

		IOObjectRelease(ioport);
	}
	IOObjectRelease(iter);
	return serialPath;
}

// Called on kIOGeneralInterest notification, look for kIOMessageServiceIsTerminated (IOMessage.h)
static void DeviceNotification(void *refCon, io_service_t service, natural_t messageType, void *messageArgument)
{
	kern_return_t kr;
	DeviceData *deviceData = (DeviceData *)refCon;
	if (messageType == kIOMessageServiceIsTerminated)
	{		
		OmLog(2, "MAC: Removed %u\n", deviceData->deviceId);
		OmLog(3, "->deviceName: "); CFShow(deviceData->deviceName);
		OmLog(3, "->locationID: 0x%lx.\n", deviceData->locationID);
		OmLog(3, "->deviceId: 0x%x.\n", deviceData->deviceId);

		// Call device removed
		OmDeviceDiscovery(OM_DEVICE_REMOVED, deviceData->deviceId, deviceData->serialNumber, deviceData->serialDevice, deviceData->mountPath);

		CFRelease(deviceData->deviceName);
		if (deviceData->deviceInterface)
		{
			kr = (*deviceData->deviceInterface)->Release(deviceData->deviceInterface);
		}
		kr = IOObjectRelease(deviceData->notification);
		free(deviceData);
	}
}

// IOServiceAddMatchingNotification - device added
static void DeviceAdded(void *refCon, io_iterator_t iterator)
{
	kern_return_t kr;
	io_service_t usbDevice;
	IOCFPlugInInterface **plugInInterface = NULL;
	SInt32 score;
	HRESULT res;
	
	while ((usbDevice = IOIteratorNext(iterator)))
	{
		OmLog(2, "DEVICE: Added...\n");

		// Store data relating to each device (service's name and location ID)
		DeviceData *deviceData = malloc(sizeof(DeviceData));
		if (deviceData == NULL)
		{
			OmLog(2, "MAC: Problem allocating device data\n");
			continue;
		}
		
		// A scope for better failure handling
		do {
			bzero(deviceData, sizeof(DeviceData));

			// Get the device name
			io_name_t deviceName = {0};
			kr = IORegistryEntryGetName(usbDevice, deviceName);
			if (KERN_SUCCESS != kr)
			{
				OmLog(2, "MAC: IORegistryEntryGetName returned 0x%08x\n", kr);
				break;
			}
			deviceData->deviceName = CFStringCreateWithCString(kCFAllocatorDefault, deviceName, kCFStringEncodingASCII);
			OmLog(3, "->deviceName: %s\n", deviceName);
			
			#if 1	// additional trace information about the device
			io_name_t className = {0};
			io_string_t pathName = {0};
			io_string_t pathName2 = {0};

			IOObjectGetClass(usbDevice, className);
			IORegistryEntryGetPath(usbDevice, kIOServicePlane, pathName);
			IORegistryEntryGetPath(usbDevice, kIOUSBPlane, pathName2);

			OmLog(3, "MAC: This device's className is %s\n", (const char*)className);
			OmLog(3, "MAC: Device's path in IOService plane = %s\n", pathName);
			OmLog(3, "MAC: Device's path in IOUSB plane = %s\n", pathName2);
			#endif

			// Create an IOUSBDeviceInterface to get the location ID (connection between application and USB device kernel object)
			kr = IOCreatePlugInInterfaceForService(usbDevice, kIOUSBDeviceUserClientTypeID, kIOCFPlugInInterfaceID, &plugInInterface, &score);
			if ((kIOReturnSuccess != kr) || !plugInInterface)
			{
				OmLog(2, "MAC: IOCreatePlugInInterfaceForService returned 0x%08x\n", kr);
				break;
			}
			
			// Retrieve the device interface
			res = (*plugInInterface)->QueryInterface(plugInInterface, CFUUIDGetUUIDBytes(kIOUSBDeviceInterfaceID), (LPVOID*) &deviceData->deviceInterface);
			
			// Release plugin interface
			(*plugInInterface)->Release(plugInInterface);
			if (res || deviceData->deviceInterface == NULL)
			{
				OmLog(2, "MAC: ERROR: QueryInterface returned %d.\n", (int) res);
				break;
			}
			
			// Routines from IOUSBLib.h can be called with the IOUSBDeviceInterface
			UInt32 locationID;
			kr = (*deviceData->deviceInterface)->GetLocationID(deviceData->deviceInterface, &locationID);
			if (KERN_SUCCESS != kr)
			{
				OmLog(2, "MAC: ERROR: GetLocationID returned 0x%08x.\n", kr);
				break;
			}
			deviceData->locationID = locationID;
			OmLog(3, "->locationID: 0x%lx.\n", deviceData->locationID);
			
			// Use IOServiceAddInterestNotification type kIOGeneralInterest for this device (removal).
			kr = IOServiceAddInterestNotification(gNotifyPort, usbDevice, kIOGeneralInterest, DeviceNotification, deviceData, &(deviceData->notification));
			if (KERN_SUCCESS != kr)
			{
				OmLog(2, "MAC: WARNING: IOServiceAddInterestNotification returned 0x%08x.\n", kr);
				break;
			}

			// printf("DEVICE: Find serial number...\n");
			deviceData->serialNumber = getUSBSerialNumber(usbDevice);
			if (deviceData->serialNumber == NULL || strlen(deviceData->serialNumber) == 0)
			{
				OmLog(2, "MAC: ERROR: Couldn't find USB serial number.\n");
				break;
			}
			OmLog(3, "->serialNumber: %s\n", deviceData->serialNumber);

			deviceData->deviceId = DeviceIdFromSerialNumber(deviceData->serialNumber);
			if (deviceData->deviceId <= 0)
			{
				OmLog(2, "MAC: ERROR: Couldn't find device ID from USB serial number.\n");
				break;
			}
			OmLog(3, "->deviceId: %u\n", deviceData->deviceId);
			
			deviceData->mountPath = findMount(usbDevice);
			if (deviceData->mountPath == NULL || strlen(deviceData->mountPath) == 0)
			{
				OmLog(2, "MAC: ERROR: Couldn't find mount path.\n");
				break;
			}
			OmLog(3, "->mountPath: %s\n", deviceData->mountPath);
			
			deviceData->serialDevice = findSerial(deviceData->serialNumber);
			if (deviceData->serialDevice == NULL || strlen(deviceData->serialDevice) == 0)
			{
				OmLog(2, "MAC: ERROR: Couldn't find serial path.\n");
				break;
			}
			OmLog(3, "->serialDevice: %s\n", deviceData->serialDevice);

			// Call device connected
			OmLog(2, "MAC: DEVICE: ... %s (#%u) port=%s path=%s\n", deviceData->serialNumber, deviceData->deviceId, deviceData->serialDevice, deviceData->mountPath);
			OmDeviceDiscovery(OM_DEVICE_CONNECTED, deviceData->deviceId, deviceData->serialNumber, deviceData->serialDevice, deviceData->mountPath);
			deviceData = NULL;	// clear reference to prevent freeing below
		} while (0);

		// We still have a reference if there was an issue
		if (deviceData) {
			OmLog(2, "MAC: ERROR: Overall problem determining device information.\n");
			fprintf(stderr, "ERROR: Overall problem determining device information. (Run with OMDEBUG=2 for details).\n");
			free(deviceData);
		}

		// Release IOIteratorNext reference
		kr = IOObjectRelease(usbDevice);
	}
}

// Handle program interrupt (e.g. Ctrl-C)
void SignalHandler(int sigraised)
{
	OmLog(2, "DEVICE: Interrupted.\n");
	fprintf(stderr, "DEVICE: Interrupted.\n");
	
	// TODO: Move this to a handler in the library
	exit(0);
}


static volatile int gStarted = 0;
static pthread_mutex_t gStartMutex;
static pthread_cond_t gStartCond;

static thread_return_t OmDeviceDiscoveryThread(void *arg)
{
	// Set signal handler
	{
		sig_t oldHandler = signal(SIGINT, SignalHandler);
		if (oldHandler == SIG_ERR) {
			OmLog(2, "WARNING: Could not set signal handler.\n");
			fprintf(stderr, "WARNING: Could not set signal handler.\n");
		}
	}
	
	// See: https://stackoverflow.com/questions/33181669/osx-workaround-for-getting-bsd-name-of-an-iousbdevice
	unsigned int currentVersion = osVersion();
	unsigned int maxVersion = __MAC_OS_X_VERSION_MAX_ALLOWED;
	unsigned int versionElCapitan = 101100; // "El Capitan" (AvailabilityInternal.h)
	// "IOUSBDevice" -> "IOUSBHostDevice"
	const char *serviceMatcher = (currentVersion < versionElCapitan || maxVersion < versionElCapitan) ? "IOUSBDevice" : "IOUSBHostDevice";
	OmLog(2, "MAC: NOTE: currentVersion=%u, maxVersion=%u, elCapitan=%u, serviceMatched=%s\n", currentVersion, maxVersion, versionElCapitan, serviceMatcher);

	CFMutableDictionaryRef matchingDict = IOServiceMatching(serviceMatcher);		// kIOUSBDeviceClassName="IOUSBDevice"
	if (matchingDict == NULL)
	{
		OmLog(2, "ERROR: IOServiceMatching returned NULL.\n");
		fprintf(stderr, "ERROR: IOServiceMatching returned NULL.\n");
		return thread_return_value(1);
	}
	
	// Register interest in all USB devices that match the vid/pid
	{
		long usbVendor = VID;
		long usbProduct = PID;
		CFNumberRef numberRef;
		
		OmLog(3, "DEVICE: Looking for USB class instances VID=%04x PID=%04x...\n", (int)usbVendor, (int)usbProduct);
		
		// ...vendor id
		numberRef = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt32Type, &usbVendor);
		CFDictionarySetValue(matchingDict, CFSTR(kUSBVendorID), numberRef);
		CFRelease(numberRef);
		
		// ...product id
		numberRef = CFNumberCreate(kCFAllocatorDefault, kCFNumberSInt32Type, &usbProduct);
		CFDictionarySetValue(matchingDict, CFSTR(kUSBProductID), numberRef);
		CFRelease(numberRef);

	}

	// Set up async notifications using a notification port and its run loop event source
	gNotifyPort = IONotificationPortCreate(kIOMasterPortDefault);
	CFRunLoopSourceRef runLoopSource = IONotificationPortGetRunLoopSource(gNotifyPort);
	
	gRunLoop = CFRunLoopGetCurrent();
	CFRunLoopAddSource(gRunLoop, runLoopSource, kCFRunLoopDefaultMode);
	
	// Notification when a device is matched by I/O Kit
	kern_return_t kr = IOServiceAddMatchingNotification(gNotifyPort, kIOFirstMatchNotification,	matchingDict, DeviceAdded, NULL, &gAddedIter);
	if (KERN_SUCCESS != kr)
	{
		OmLog(2, "WARNING: IOServiceAddMatchingNotification failed\n");
		fprintf(stderr, "WARNING: IOServiceAddMatchingNotification failed\n");
	}
	
	// Iterate once to get already-present devices and arm the notification	
	DeviceAdded(NULL, gAddedIter);	

	// Signal finished
	OmLog(3, "DEVICE: Signalling...\n");
	pthread_mutex_lock(&gStartMutex);
	gStarted = 1;
	pthread_cond_signal(&gStartCond);
	pthread_mutex_unlock(&gStartMutex);

	// while (!om.quitDiscoveryThread)
	// Start the run loop, we will receive notifications
	OmLog(3, "DEVICE: Starting run loop...\n");
	CFRunLoopRun();
	
	OmLog(3, "DEVICE: Run loop returned\n");
    return thread_return_value(0);
}



/** Internal method to start device discovery. */
void OmDeviceDiscoveryStart(void)
{
    om.quitDiscoveryThread = 0;

	// Initialize
	gStarted = 0;
	pthread_mutex_init(&gStartMutex, 0);
	pthread_cond_init(&gStartCond, NULL);
    pthread_mutex_lock(&gStartMutex);

    //OmUpdateDevices();
    thread_create(&om.discoveryThread, NULL, OmDeviceDiscoveryThread, NULL);

	// Wait for event indicating the run loop is starting
    while (!gStarted)
	{
		OmLog(3, "DEVICE: Waiting...%d\n", gStarted);
        pthread_cond_wait(&gStartCond, &gStartMutex);
	}
    pthread_mutex_unlock(&gStartMutex);	

	// HACK: Delay a fraction to ensure the run loop really starts
	usleep(200 * 1000);

	OmLog(3, "DEVICE: Started...\n");
}

/** Internal method to stop device discovery. */
void OmDeviceDiscoveryStop(void)
{
    om.quitDiscoveryThread = 1;
	OmLog(3, "DEVICE: Stopping run loop...\n");
    CFRunLoopStop(gRunLoop);
    pthread_cancel(om.discoveryThread);     // thread_join(&om.discoveryThread, NULL);
}

#endif  // __APPLE__