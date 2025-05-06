# Author: Sunone
# Modified: 2025-05-07
# Original base: KMBOX B Pro docs
# Description: Custom firmware with HID spoofing, UI splash, and serial exec

import sys, select
from machine import SPI, Pin
import time, gc, km, device, bt
from ST7735 import TFT
from sysfont import sysfont

poller = select.poll()
poller.register(sys.stdin, select.POLLIN)

USB_REPORT_RATE   = 1000          # Hz – higher = lower latency
SERIAL_BAUD       = 115200       # bps – matches your PC side
USB_MODE          = 1             # 0 = full-feature, 1 = USB HID only
ENABLE_BT         = 0             # 0 = off, 1 = on

km.freq(USB_REPORT_RATE)
km.baud(SERIAL_BAUD)
km.mode(USB_MODE)
bt.enable(ENABLE_BT)

# spoof VID/PID
# device.VID('046d')
# device.PID('c07d')
# device.enable(1)

spi = SPI(1, baudrate=24000000, polarity=0, phase=0,
          sck=Pin(21), mosi=Pin(22), miso=Pin(13))
tft = TFT(spi, 32, 19, 33)
tft.initr()
tft.rgb(True)
BLACK = TFT.BLACK; WHITE = TFT.WHITE

def splash():
    tft.fill(BLACK)
    tft.text((0, 10),  "KMBOX B Pro", TFT.GREEN,  sysfont, 1, nowrap=True)
    
    tft.text((0, 0), "<-COM", TFT.WHITE, sysfont, 1, nowrap=True)

    tft.text((98, 0), "HID->", TFT.PURPLE, sysfont, 1, nowrap=True)
    tft.text((0, 150), "<-PC", TFT.BLUE, sysfont, 1, nowrap=True)
    tft.text((98, 150), "HID->", TFT.PURPLE, sysfont, 1, nowrap=True)
    
    # USB report rate
    tft.text((0, 30), "Report rate: ", TFT.YELLOW, sysfont, 1, nowrap=True)
    
def update_status():
    # UART speed (kbit/s)
    tft.text(
      (0, 20),
      "UART speed: %4d kbps" % (SERIAL_BAUD // 1000),
      TFT.YELLOW,
      sysfont,
      1,
      nowrap=True
    )
    
    # USB report rate data
    tft.text(
      (70, 30),
      "%4d Hz " % USB_REPORT_RATE,
      TFT.YELLOW,
      sysfont,
      1,
      nowrap=True
    )
    
    # BT flag
    tft.text(
      (0, 40),
      "Bluetooth: %d" % (ENABLE_BT),
      TFT.YELLOW,
      sysfont,
      1,
      nowrap=True
    )
    
    # USB mode
    tft.text(

      (0, 50),
      "USB Mode: %d  " % (USB_MODE),
      TFT.YELLOW,
      sysfont,
      1,
      nowrap=True
    )

splash()
update_status()
time.sleep_ms(100)

prev_l = prev_r = 0
km.lock_ml(True)
km.lock_mr(True)

while True:
  l = km.left()  & 1
  r = km.right() & 1

  if l != prev_l:
    km.left(1) if l else km.left(0)
    print("BD:1" if l else "BU:1")
    prev_l = l
  if r != prev_r:
    km.right(1) if r else km.right(0)
    print("BD:2" if r else "BU:2")
    prev_r = r
  
  if poller.poll(0):
    try:
      line = sys.stdin.readline()
      if line:
        exec(line.strip(), globals())
    except Exception as e:
      sys.stdout.write('ERR:'+str(e)+'\n')
        
  time.sleep_ms(1)
    
  if time.ticks_ms() % 1000 < 2:
    update_status()
  gc.collect()