from gpiozero import LED
from time import sleep

red = LED(17)
green = LED(21)

while True:
    red.on()
    sleep(0.7)
    red.off()
    green.on()
    sleep(0.7)
    green.off()