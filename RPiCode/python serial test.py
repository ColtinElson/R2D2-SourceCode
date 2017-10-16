import time
import serial

ser = serial.Serial('/dev/ttyAMA0')

counter = 0

while 1:
    ser.write('Write counter: %d \n'%(counter))
    time.sleep(1)
    counter += 1
