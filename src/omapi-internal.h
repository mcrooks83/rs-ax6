/* 
 * Copyright (c) 2009-2012, Newcastle University, UK.
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

// Open Movement API - Internal Header File
// Dan Jackson, 2011-2012

#ifndef OMAPI_INTERNAL
#define OMAPI_INTERNAL

// Cross-platform multi-threading and mutex
#if defined(_WIN32) // || defined(__CYGWIN__)
    // Device Discovery
	#ifndef _CRT_SECURE_NO_DEPRECATE
		#define _CRT_SECURE_NO_DEPRECATE
	#endif
    #define _WIN32_DCOM
    #include <windows.h>


    // Headers
    //#include <process.h>
    #include <io.h>
    #define _POSIX_
    #define strcasecmp _stricmp
    #pragma warning( disable : 4996 )    /* allow deprecated POSIX name functions */

    // Thread
    #define thread_t HANDLE
    #define thread_create(thread, attr_ignored, start_routine, arg) ((*(thread) = CreateThread(attr_ignored, 0, start_routine, arg, 0, NULL)) == NULL)
    #define thread_join(thread, value_ptr_ignored) ((value_ptr_ignored), WaitForSingleObject((thread), INFINITE) != WAIT_OBJECT_0)
    #define thread_cancel(thread) (TerminateThread(*(thread), -1) == 0)
    #define thread_return_t DWORD WINAPI
    #define thread_return_value(value) ((unsigned int)(value))

    // Mutex
    #define mutex_t HANDLE
    #define mutex_init(mutex, attr_ignored) ((*(mutex) = CreateMutex(attr_ignored, FALSE, NULL)) == NULL)
#define OM_DEBUG_MUTEX
#ifdef OM_DEBUG_MUTEX
    int OmDebugMutexLock(mutex_t *mutex, const char *mutexName, const char *source, int line, const char *caller, int deviceId);
    int OmDebugMutexUnlock(mutex_t *mutex, const char *mutexName, const char *source, int line, const char *caller, int deviceId);
    #define OM_DEBUG_MUTEX_STRINGIFY(T) #T
    #define mutex_lock(mutex) OmDebugMutexLock(mutex, "" OM_DEBUG_MUTEX_STRINGIFY(mutex) "", "" __FILE__ "", __LINE__, __FUNCTION__, deviceId)
    #define mutex_unlock(mutex) OmDebugMutexUnlock(mutex, "" OM_DEBUG_MUTEX_STRINGIFY(mutex) "", "" __FILE__ "", __LINE__, __FUNCTION__, deviceId)
#else
    #define mutex_lock(mutex) (WaitForSingleObject(*(mutex), INFINITE) != WAIT_OBJECT_0)
    #define mutex_unlock(mutex) (ReleaseMutex(*(mutex)) == 0)
#endif
    #define mutex_destroy(mutex) (CloseHandle(*(mutex)) == 0)

    // Sleep
    #define sleep(seconds) Sleep(seconds * 1000UL)
    #define usleep(microseconds) Sleep(microseconds / 1000UL)

    // Time
    #define gmtime_r(timer, result) gmtime_s(result, timer)
    #define timegm _mkgmtime

    // Strings
	#if _MSC_VER < 1900		// Before MSVC++ 14.0 (VS2015)
		#define snprintf _snprintf
	#endif

#else
    // Headers
    #include <unistd.h>
    #include <sys/wait.h>
    //#include <sys/types.h>
    #include <termios.h>
    #include <pthread.h>
	
    #if defined(__APPLE__)
        // Applie-specific
    #elif defined(__linux__)
        // Linux-specific
        // #include <libudev.h>
    #endif

    // Thread
    #define thread_t      pthread_t
    #define thread_create pthread_create
    #define thread_join   pthread_join
    #define thread_cancel pthread_cancel
	typedef void *        thread_return_t;
    #define thread_return_value(value_ignored) ((void *)((value_ignored) ^ (value_ignored)))    // return NULL;

    // Mutex
    #define mutex_t       pthread_mutex_t
    #define mutex_init    pthread_mutex_init
    #define mutex_lock    pthread_mutex_lock
    #define mutex_unlock  pthread_mutex_unlock
    #define mutex_destroy pthread_mutex_destroy

#endif



// Includes
#include <stdio.h>
#include <stdlib.h>
#include <stdarg.h>
#include <string.h>
#include <errno.h>
#include <fcntl.h>
#include <time.h>
#include <sys/timeb.h>

#include "omapi.h"


#ifdef __cplusplus
extern "C" {
#endif


// Constants
#define OM_MAX_CDC_PATH OM_MAX_PATH     /**< The maximum string length of the CDC port.  e.g. "\\.\COM12345" + '\0' on Windows, or "/dev/tty.usbmodem12345" + '\0' */
#define OM_MAX_MSD_PATH OM_MAX_PATH     /**< The maximum string length to the root of the MSD volume.  e.g. "\\?\Volume{abc12345-1234-1234-1234-123456789abc}\" + '\0'. */
#define OM_MAX_SERIALID_LEN OM_MAX_PATH/**< The maximum string length of the USB serial number identity string.  e.g. "CWA17_00123" + '\0'. */
#define OM_DEFAULT_FILENAME "CWA-DATA.CWA"

#define OM_MAX_RESPONSE_SIZE 256
#define OM_DEFAULT_TIMEOUT 2000

/** Data block size in bytes */
#define OM_BLOCK_SIZE 512
#define OM_DEBUG_DEFAULT 0

// Helpful command macros
#define OM_COMMAND(deviceId, output, response, expected, timeout, parts)  OmCommand(deviceId, output, response, sizeof(response)/sizeof(response[0]), expected, timeout, parts, sizeof(parts)/sizeof(parts[0]))
#define OM_MAX_PARSE_PARTS 10

#define OM_USB_ID 0x04D80057   /**< USB VID/PID for CWA Composite Device */


/** Device status structure */
typedef struct
{
    // Device properties
    unsigned int id;                    /**< Device serial number */
    OM_DEVICE_STATUS deviceStatus;      /**< Current connection status for this device. */
    char port[OM_MAX_CDC_PATH];         /**< Address to access the serial port. */
    char root[OM_MAX_MSD_PATH];         /**< Mounted root of the file system. */
    char dataFile[OM_MAX_PATH];         /**< Data filename. */

    int fd;                             /**< File descriptor for the serial port while open. The common portMutex is used to allow changes to this -- must hold to acquire or release the CDC port. */

    volatile char downloadCancel;       /**< Download cancellation request flag */

    // The common downloadMutex is used to allow changes to these values, must hold to start/update/stop a download.
    OM_DOWNLOAD_STATUS downloadStatus;  /**< Status of an asynchronous download */
    int downloadValue;                  /**< Status value of an asynchronous download, percentage complete or diagnostic code if in error. */
    FILE *downloadSource;               /**< Input stream for the file being copied from */
    FILE *downloadDest;                 /**< Output stream for the file being copied to */
    int downloadBlocksTotal;            /**< Number of blocks to copy */
    int downloadBlocksCopied;           /**< Number of blocks already copied */
    thread_t downloadThread;            /**< Download thread */

    void *downloadReference;            /**< Download reference to callbacks (if NULL, the reference given when registering the callbacks will be used instead) */
	
	int flags;							/**< Special flags: 0x00000001=invalid device */
    char serialId[OM_MAX_SERIALID_LEN]; /**< USB serial number identity string, e.g. "CWA17_00123" */
} OmDeviceState;


struct OmDeviceRecord_tag;
typedef struct OmDeviceRecord_tag {
	unsigned int id;					/**< The device identifier */
	OmDeviceState *state;				/**< The state of the device */
	struct OmDeviceRecord_tag *next;	/**< The next device entry */
} OmDeviceRecord;


/**
 * Internal status structure
 */
typedef struct
{
    // Status
    int initialized;                    /**< API initialized flag */
    int apiVersion;                     /**< Requested API version number. Where supported, this can be used to emulate earlier behaviour. */
    int debug;                          /**< Debug level */
    FILE *log;                          /**< Output log stream */
    char logSet;                        /**< Flag indicating the log stream has been redirected */

    // Callbacks
    OmLogCallback logCallback;          /**< User-supplied callback for log messages. */
    void *logCallbackReference;         /**< User-supplied reference that will be passed to the log callback. */
    OmDeviceCallback deviceCallback;    /**< User-supplied callback for device changes. */
    void *deviceCallbackReference;      /**< User-supplied reference that will be passed to the device callback. */
    OmDownloadCallback downloadCallback;/**< User-supplied callback for download status changes. */
    void *downloadCallbackReference;    /**< User-supplied reference that will be passed to the download callback. */
    OmDownloadChunkCallback downloadChunkCallback; /**< User-supplied callback for download chunks. */
    void *downloadChunkCallbackReference;   /**< User-supplied reference that will be passed to the download chunk callback. */

    // Device discovery
#ifndef _WIN32 // || defined(__CYGWIN__)
    thread_t discoveryThread;           /**< Discovery thread. */
    volatile char quitDiscoveryThread;  /**< Quit flag for discovery thread. */
#endif

    // Port and download mutex
    mutex_t portMutex;                  /**< portMutex must be held to open or close a CDC port. */
    mutex_t downloadMutex;              /**< downloadMutex must be held to start/update/stop a download. */

    // Device table
    OmDeviceRecord *deviceRecords;		/**< Linked list of pointers to devices that have been seen and their states */    // (Consider replacing with a hash table or balanced tree for efficiency). 
} OmState;


/**
 * Status structure instance (singleton)
 */
extern OmState om;


/** Log text to the current log stream. */
int OmLog(int level, const char *format, ...);

/** Device discovery start */
void OmDeviceDiscoveryStart(void);

/** Device discovery stop */
void OmDeviceDiscoveryStop(void);

/** Device discovery handler */
void OmDeviceDiscovery(OM_DEVICE_STATUS status, unsigned int inSerialNumber, const char *serialId, const char *port, const char *volumePath);


/** Number of milliseconds since the epoch */
unsigned long long OmMillisecondsEpoch(void);

/** Timer value in milliseconds */
unsigned long OmMilliseconds(void);

/** Read a line from the device */
int OmPortReadLine(unsigned int deviceId, char *inBuffer, int len, unsigned long timeout);

/** Write to the device */
int OmPortWrite(unsigned int deviceId, const char *command);

/** Acquire a port */
int OmPortAcquire(unsigned int deviceId);

/** Release a port */
int OmPortRelease(unsigned int deviceId);

/** Get the device state for the given device id */
OmDeviceState *OmDevice(int serial);

#ifdef __cplusplus
}
#endif

#endif
