from gpiozero import LED, Button
from time import sleep, time
import picamera
import sys, os

camera = picamera.PiCamera()
led = LED(17)
button = Button(27, pull_up=False)

IMAGE_FOLDER_PATH = os.path.dirname(os.path.realpath(__file__)) + '/capture/'

def record():
    led.off()
    capture_image()
    led.on()
    sleep(0.1)

def capture_image():
    ts = str(time())
    camera.capture('{0}{1}.jpg'.format(IMAGE_FOLDER_PATH, ts))

while True:
    if button.is_pressed:
        record()
