from gpiozero import Button, TrafficLights
from time import sleep

button = Button(2)
lights = TrafficLights(17, 27, 22)

while True:

    lights.green.on()
    sleep(4)
    lights.off()
    
    lights.amber.on()
    sleep(2)
    lights.off()

    lights.red.on()
    sleep(4)
    lights.off()
