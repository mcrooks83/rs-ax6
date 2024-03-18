

### generate the wrapper
ctypesgen is installed via pip
ctypesgen -a -l ../../src/libomapi.so ../../include/omapi.h -o pylibomapi.py 

ctypesgen -a -l libomapi.so omapi.h -o pylibomapi_wrapper.py


make && OMDEBUG=3 ./omapi-examples test  - test the library in C

python test.py - runs a mimic of test.c

#TODO: add error handling



### Commands

# LEDs
typedef enum
{
    OM_LED_AUTO = -1,           /**< Automatic device-controlled LED to indicate state (default). */
    OM_LED_OFF = 0,             /**< rgb(0,0,0) Off     */
    OM_LED_BLUE = 1,            /**< rgb(0,0,1) Blue    */
    OM_LED_GREEN = 2,           /**< rgb(0,1,0) Green   */
    OM_LED_CYAN = 3,            /**< rgb(0,1,1) Cyan    */
    OM_LED_RED = 4,             /**< rgb(1,0,0) Red     */
    OM_LED_MAGENTA = 5,         /**< rgb(1,0,1) Magenta */
    OM_LED_YELLOW = 6,          /**< rgb(1,1,0) Yellow  */
    OM_LED_WHITE = 7            /**< rgb(1,1,1) White   */
} OM_LED_STATE;

char command[32];
OmSetLed  - sprintf(command, "\r\nLED %d\r\n", (int)ledState); 
command for red is: \r\nLED 4\r\n 