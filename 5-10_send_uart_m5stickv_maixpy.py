## Copyright (c) 2020 aNoken 

from Maix import GPIO
from fpioa_manager import fm, board_info
from machine import UART

# M5StickVのGroveポートG34/G35をUARTで初期化
fm.register(35, fm.fpioa.UART2_TX, force=True)
fm.register(34, fm.fpioa.UART2_RX, force=True)

# UART(uart番号, ボーレート, bits, パリティ, stopbit, タイムアウト時間, シリアルポートはバッファを介して受信し、バッファがいっぱいになると受信停止)
uart_Port = UART(UART.UART2, 115200,8,0,0, timeout=1000, read_buf_len= 4096)
cnt=0

# 数値データを文字データに変換して、送信する
while True:
    moji=str(cnt)+"\n"
    uart_Port.write(moji)
    time.sleep(1.0)
    cnt=cnt+1

uart_Port.deinit()
del uart_Port


または


from machine import UART
from board import board_info
from fpioa_manager import fm
from Maix import GPIO
import sensor, lcd

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((160,160))
sensor.set_vflip(1)
sensor.set_hmirror(1)
sensor.run(1)
sensor.skip_frames()


fm.register(35, fm.fpioa.UART1_TX, force=True)
fm.register(34, fm.fpioa.UART1_RX, force=True)

uart = UART(UART.UART1, 921600,8,0,0, timeout=1000, read_buf_len=4096)


while(True):
    img = sensor.snapshot()
    uart.write(img)
