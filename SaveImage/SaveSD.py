import lcd
import image
import time
import os
import uos

lcd.init()
lcd.rotation(2) #Rotate the lcd 180deg

from Maix import I2S, GPIO
from Maix import GPIO
from fpioa_manager import *
from machine import UART
from modules import ws2812

# serial port setup
# grove connector
fm.register(35, fm.fpioa.UART2_TX, force=True)
fm.register(34, fm.fpioa.UART2_RX, force=True)
uart = UART(UART.UART2, 115200,8,0,0, timeout=1000, read_buf_len= 4096)
class_ws2812 = ws2812(8, 1)

ext=".jpg"
cnt0=0
cnt1=1
cnt2=2
cnt3=3
cnt4=4


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
            #print(text)
            img = sensor.snapshot() # Take an image from sensor
            #img.save("/sd/0/cnt0.jpg", quality=95)
            #img.draw_string(40, 50, text, scale=3)
            if text == "0":
                img.save("/sd/0/"+ str(cnt0) + ".jpg", quality=95)
                cnt0+=1
                b = class_ws2812.set_led(0,(50,0,0))
                b = class_ws2812.display()
                time.sleep(0.5)
                b = class_ws2812.set_led(0,(0,0,0))
                b = class_ws2812.display()
                
            elif text =="1":
                img.save("/sd/1/"+ str(cnt1) + ".jpg", quality=95)
                cnt1+=1
                b = class_ws2812.set_led(0,(20,20,0))
                b = class_ws2812.display()
                time.sleep(0.5)
                b = class_ws2812.set_led(0,(0,0,0))
                b = class_ws2812.display()
            elif text =="2":
                img.save("/sd/2/"+ str(cnt2) + ".jpg", quality=95)
                cnt2+=1
                b = class_ws2812.set_led(0,(0,50,0))
                b = class_ws2812.display()
                time.sleep(0.5)
                b = class_ws2812.set_led(0,(0,0,0))
                b = class_ws2812.display()
            elif text =="3":
                img.save("/sd/3/"+ str(cnt3) + ".jpg", quality=95)
                cnt3+=1
                b = class_ws2812.set_led(0,(0,20,20))
                b = class_ws2812.display()
                time.sleep(0.5)
                b = class_ws2812.set_led(0,(0,0,0))
                b = class_ws2812.display()
            elif text =="4":
                img.save("/sd/4/"+ str(cnt4) + ".jpg", quality=95)
                cnt4+=1
                b = class_ws2812.set_led(0,(0,0,50))
                b = class_ws2812.display()
                time.sleep(0.5)
                b = class_ws2812.set_led(0,(0,0,0))
                b = class_ws2812.display()

except KeyboardInterrupt:
    a = kpu.deinit(task)
    sys.exit()
