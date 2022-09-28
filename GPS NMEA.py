from machine import Pin
from utime import sleep


uart= machine.UART(1,baudrate=9600,tx=Pin(8), rx=Pin(9))  

while True:
    if uart.any():  
        data = uart.readline().decode('utf-8')
        line= data.split(',')
        if line[0] == "$GNRMC":
          print("UTC Time: " + line[1])
            print("Positioning status, A=effective positioning, V=invalid positioning: " + line[2])
            print("Latitude: " + line[3])
            print("Hemispheric latitude, North or South (North or South): " + line[4])
            print("Longitude in the format : " + line[5])
            print("Hemispheric longitude, E or W (East or West): " + line[6])
            print("Speed ​​over ground:" + line[7])
            print("Earth direction (use true north as reference point):" + line[8])
            print("Date in UTC format, format ddmmyy (day, month, year): " + line[9])
            print("Magnetic declination (000.0~180.0 degrees): " + line[10])
            print("Magnetic declination direction, E (East) or W (West): " + line[11])
            print("Mode indication (A=offline positioning, D=differential, E=estimate, N=invalid data): " + line[12])
        sleep(0.2)
        
