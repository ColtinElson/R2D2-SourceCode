import serial
import time

data = bytes([0x00,0x31,150])
ser = serial.Serial('/dev/ttyAMA0')

time.sleep(1)
while True:
    ser.write(data)
