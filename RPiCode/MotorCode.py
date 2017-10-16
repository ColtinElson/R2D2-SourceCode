#Import needed packages
import pygame
import time
import serial

#Initiate pygame and make a small window
pygame.init()
#The window is needed to record key presses
pygame.display.set_mode((100, 100))
#Initiate pygame sound mixer
pygame.mixer.init()

#Open serial port AMA0
ser = serial.Serial('/dev/ttyAMA0')
#Open serial port ACM1
try:
    serDome = serial.Serial('/dev/ttyACM1')
except:
    try:
        serDome = serial.Serial('/dev/ttyACM0')
    except:
        print("Blah")
#Wait 1 second for port to set up
time.sleep(1)

#Set variables for byte information sent over serial
#The first byte is a sync and must be sent every time
#The second byte is the command that is being used (as seen on the MD49 documentation)
#Any additional number is a decimal value being sent

#Disable timeout so motors spin until told not to
disableTimeout = bytes([0x00,0x38])
#Set mode to 2 to move both motors at once
setMode2 = bytes([0x00,0x34,2])
#Set mode to 0 to move motors separately
setMode0 = bytes([0x00,0x34,0])

#Motor movement bytes
#The last value indicates the speed with 0 being full reverse,
#128 being stop and 255 being full forward

#Move motor(s) forward slowly
motorForwardSlow = bytes([0x00,0x31,88])
#Move motor(s) backward slowly
motorBackwardSlow = bytes([0x00,0x31,168])
#Move second motor forward slowly
motor2ForwardSlow = bytes([0x00,0x32,88])
#Move second motor backward slowly
motor2BackwardSlow = bytes([0x00,0x32,168])
#Move motor(s) forward quickly
motorForwardFast = bytes([0x00,0x31,200])
#Move motor(s) backward quickly
motorBackwardFast = bytes([0x00,0x31,56])
#Move second motor forward quickly
motor2ForwardFast = bytes([0x00,0x32,200])
#Move second motor backward quickly
motor2BackwardFast = bytes([0x00,0x32,56])
#Stop motor(s)
motorStop = bytes([0x00,0x31,128])
#Stop second motor
motor2Stop = bytes([0x00,0x32,128])

#Set the mode to 2
ser.write(setMode2)
#Disable timeout
ser.write(disableTimeout)

#While the program is open, loop through this code
while True:
    #For every event that happens check to see what type of event it is
    for event in pygame.event.get():
        #If a key is pressed:
        if event.type == pygame.KEYDOWN:
            #If the key is the up arrow, move forward slowly
            if event.key == pygame.K_UP:
                ser.write(motorForwardSlow)
            #If the key is the down arrow, move backward slowly
            elif event.key == pygame.K_DOWN:
                ser.write(motorBackwardSlow)
            #If the key is the left arrow, move motor1 forward and motor2 backward slowly
            elif event.key == pygame.K_LEFT:
                ser.write(setMode0)
                ser.write(motor2BackwardSlow)
                ser.write(motorForwardSlow)
            #If the key is the right arrow, move motor1 backward and motor2 forward slowly
            elif event.key == pygame.K_RIGHT:
                ser.write(setMode0)
                ser.write(motorBackwardSlow)
                ser.write(motor2ForwardSlow)
                
            #Doesnt work properly. To be fixed later
            #elif event.key == pygame.K_i:
            #    ser.write(motorForwardFast)
            #elif event.key == pygame.K_k:
            #    ser.write(motorBackwardFast)
            #elif event.key == pygame.K_j:
            #    ser.write(setMode0)
            #    ser.write(motor2ForwardFast)
            #    ser.write(motorBackwardFast)
            #elif event.key == pygame.K_l:
            #    ser.write(setMode0)
            #    ser.write(motorForwardFast)
            #    ser.write(motor2BackwardFast)

            elif event.key == pygame.K_w:
                serDome.write('w'.encode('utf-8'))
            elif event.key == pygame.K_s:
                serDome.write('s'.encode('utf-8'))
            elif event.key == pygame.K_a:
                serDome.write('a'.encode('utf-8'))
            elif event.key == pygame.K_d:
                serDome.write('d'.encode('utf-8'))
                
            elif event.key == pygame.K_q:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2.wav')
                pygame.mixer.music.play()
            elif event.key == pygame.K_o:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2a.wav')
                pygame.mixer.music.play()
            elif event.key == pygame.K_e:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2b.wav')
                pygame.mixer.music.play()
            elif event.key == pygame.K_r:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2c.wav')
                pygame.mixer.music.play()
            elif event.key == pygame.K_t:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2d.wav')
                pygame.mixer.music.play()
            elif event.key == pygame.K_y:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2e.wav')
                pygame.mixer.music.play()
            elif event.key == pygame.K_p:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2f.wav')
                pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                pygame.mixer.music.load('/home/pi/Downloads/R2D2Scream.mp3')
                pygame.mixer.music.play()
				
        #If a key is lifted:
        if event.type == pygame.KEYUP:
                #if it is up or down stop both motors
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    ser.write(motorStop)
                #if it is left or right stop each motor and then switch mode to 2
                elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
                    ser.write(motorStop)
                    ser.write(motor2Stop)
                    ser.write(setMode2)
        #if the x is clicked, close the program
        if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                    

pygame.quit()
quit()


