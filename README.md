# GPS-BG01
# GPS positioning module BG01









from machine import Pin
from utime import sleep


uart= machine.UART(1,baudrate=9600,tx=Pin(8), rx=Pin(9))  

while True:
    if uart.any():  
        data = uart.readline().decode('utf-8')
        line= data.split(',')
        if line[0] == "$GNRMC":
            
            print("Time UTC: " + line[1])
            print("Positioning status, A=effective positioning, V=invalid positioning: " + line[2])
            print("Широта в формате ддмм.ммммммм: " + line[3])
            print("Широта полушария, северная или южная широта (северная широта или южная широта): " + line[4])
            print("Долгота в формате дддмм.ммммммм: " + line[5])
            print("Долгота полушария, E или W (восточная долгота или западная долгота): " + line[6])
            print("Скорость относительно земли:" + line[7])
            print("Направление земли (используйте истинный север в качестве исходной точки):" + line[8])
            print("Дата в формате UTC, формат ддммгг (день, месяц, год): " + line[9])
            print("Магнитное склонение (000,0~180,0 градусов): " + line[10])
            print("аправление магнитного склонения, E (восток) или W (запад): " + line[11])
            print("Индикация режима (A=автономное позиционирование, D=дифференциальное, E=оценка, N=неверные данные): " + line[12])
        sleep(0.2)
        
