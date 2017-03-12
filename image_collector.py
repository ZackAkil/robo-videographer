from gpiozero import LED, Button
from time import sleep
import picamera

camera = picamera.PiCamera()
led = LED(17)
button = Button(27, pull_up=False)

def record():
    led.on()
    sleep(0.1)
    capture_image()
    led.off()
    sleep(0.1)

def capture_image():
    ts = str(time.time())
    camera.capture('capture/{0}.jpg'.format(ts))

while True:
    if button.is_pressed:
        record()
