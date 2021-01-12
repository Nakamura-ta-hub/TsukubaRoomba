import lcd
import image
import time
import uos

lcd.init()
lcd.rotation(2) #Rotate the lcd 180deg

from Maix import I2S, GPIO
from Maix import GPIO
from fpioa_manager import *
from machine import UART

# serial port setup
# grove connector
fm.register(35, fm.fpioa.UART2_TX, force=True)
fm.register(34, fm.fpioa.UART2_RX, force=True)
uart = UART(UART.UART2, 115200,8,0,0, timeout=1000, read_buf_len= 4096)

# initialize camera
import sensor
while 1:
    try:
        sensor.reset() #Reset sensor may failed, let's try some times
        break
    except:
        err_counter = err_counter + 1
        if err_counter == 20:
            lcd.draw_string(lcd.width()//2-100,lcd.height()//2-4, "Error: Sensor Init Failed", lcd.WHITE, lcd.RED)
        time.sleep(0.1)
        continue

sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA) #QVGA=320x240
sensor.run(1)

# main
text = ""
try:
    while(True):
        if uart.any():
            data = uart.readline()
            text = data.decode('utf-8')
            print(text)
        img = sensor.snapshot() # Take an image from sensor
        img.draw_string(40, 50, text, scale=3)
        lcd.display(img)

except KeyboardInterrupt:
    a = kpu.deinit(task)
    sys.exit()
