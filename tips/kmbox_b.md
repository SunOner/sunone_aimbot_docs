# KMBOX B+ PRO Installation Guide

- Download and extract the flashing utility.  
  [Download uPyCraft](https://www.kmbox.top/wiki_doc/kmboxB/docs/tools/uPyCraft_V1.1.zip)

- Download and install the serial port driver.  
  [Download CH341 Driver](https://www.kmbox.top/wiki_doc/kmboxB/docs/tools/CH341SER.zip)

- *(Optional)* Download and flash KMBOX B to firmware version **2025.4.17**.  
  [Download Firmware](https://www.kmbox.top/wiki_doc/firmware/kmboxB/history/kmboxBpro%E5%9B%BA%E4%BB%B620250417.bin)

- Download the custom firmware script.  
  [Download boot.py](https://github.com/SunOner/sunone_aimbot_docs/blob/main/files/boot.py)

## Hardware Connections

- Connect **COM** port to the PC running `sunone_aimbot_cpp`.
- Connect **PC** port to the PC where the game will run.
- Connect a mouse to **HID-1** or **HID-2**.

## Flashing Instructions

1. Launch `uPyCraft_V1.1.exe`.
2. Connect to the KMBOX device via the correct COM port.
3. Expand the `device` tab and double-click `boot.py`.
4. Replace all the content of `boot.py` with the downloaded script.
5. Go to `Tools -> Download` to upload the script to the device.
6. Disconnect from the device (use the disconnect button on the right or just close the program).

## Final Setup

- In `sunone_aimbot_cpp`, switch the mouse input method to **KMBOX B**.
- Select the COM port where KMBOX is connected.
