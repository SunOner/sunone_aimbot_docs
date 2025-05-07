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
2. Connect to the KMBOX on the correct **COM** port.
3. Expand the **device** tab and double click `boot.py`.
4. Replace the entire contents of **`boot.py`** with the downloaded script.
5. Open `Tools → Download` to write the new script to the device’s flash.
6. In the uPyCraft console, execute `km.reboot()` to reboot KMBOX.

   * When the board re-enumerates, press **`Download and Run`** to launch the script.
   * You can now close uPyCraft or safely disconnect.

> **Tip:** If KMBOX was later unplugged, you can still start `boot.py` via sunone_aimbot_cpp — open its overlay, go to the KMBOX settings (mouse->Kmbox b), and press **Run boot.py** there.


## Final Setup

- In `sunone_aimbot_cpp`, switch the mouse input method to **KMBOX B**.
- Select the COM port where KMBOX is connected.