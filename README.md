# libomapi

Open Movement C-based API "OMAPI", plus bindings for .NET, Java, Node NAPI, Node FFI.

A rendering of the Doxygen documentation is available at: http://digitalinteraction.github.io/openmovement/omapi/html/

NOTE: This repository has been split from various parts of the OpenMovement mono-repo, and some inter-library paths may need repairing.


## Ports

```
# Windows
\\.\COM123
```

```
# Mac OS
/dev/tty.usbserial-*
## ioreg -p IOUSB -l -b | grep -E "@|PortNum|USB Serial Number"
```

```
# Ubuntu 16
/dev/serial/by-id/usb-Newcastle_University_AX3_Composite_Device_1.7_CWA17_22529-if01

/dev/sdb1
/media/$USER/AX317_?????/
```

```
# Raspian
/dev/serial/by-id/usb-Newcastle_University_AX3_Composite_Device_1.7_CWA17_22529-if01
mount /dev/sda1 /mnt/usb
```


---

<!--


gcc -o test -I../include -Dtest_main=main ../examples/test.c -L. -lomapi  
-->




gcc -o test -I../include -Dtest_main=main ../examples/test.c -L. -lomapi -framework CoreFoundation -framework Cocoa -framework IOKit -framework DiskArbitration