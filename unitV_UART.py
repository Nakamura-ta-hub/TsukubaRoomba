from machine import UART
from board import board_info
from fpioa_manager import fm
from Maix import GPIO
from modules import ws2812

class_ws2812 = ws2812(8, 1)

fm.register(35, fm.fpioa.UART1_TX, force=True)
fm.register(34, fm.fpioa.UART1_RX, force=True)

fm.register(18, fm.fpioa.GPIO1)
ButonA=GPIO(GPIO.GPIO1, GPIO.IN, GPIO.PULL_UP)
fm.register(19, fm.fpioa.GPIO2)
ButonB=GPIO(GPIO.GPIO2, GPIO.IN, GPIO.PULL_UP)


uart = UART(UART.UART1, 115200,8,0,0, timeout=1000, read_buf_len=4096)


while(1):
    if ButonA.value() == 0:
        uart.write('A\n')
        b = class_ws2812.set_led(0,(50,0,10))
        b=class_ws2812.display()
        time.sleep(0.5)

    if ButonB.value() == 0:
        uart.write('B\n')
        b = class_ws2812.set_led(0,(0,50,50))
        b=class_ws2812.display()
        time.sleep(0.5)
