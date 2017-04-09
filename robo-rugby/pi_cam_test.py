import time
from multiprocessing import Process, Value

import numpy as np

import picamera
import picamera.array
import pytweening
import wiringpi
from gpiozero import LED, Button
from rugby_tracker import rugby_tracker

led = LED(17)
button = Button(27, pull_up=False)

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

def set_servo(degrees):
    pulse = int((200/180.0)*degrees) + 50
    wiringpi.pwmWrite(18, pulse)

def servo_control(target,stop):
    
    # target must be between 1 and 0
    current_pos = 0.0
    while not stop.value:
        time.sleep(0.02)
        diff = (current_pos - target.value)
        if diff:
            move = pytweening.easeInOutCubic(abs(diff/400.0))
            move = move if diff < 0 else -move
            current_pos += move*100
            if button.is_pressed:
                set_servo(current_pos+40)


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.299, 0.587, 0.114])

def decimal_limit(val):
    if val > 1:
        return 1.0
    elif val < 0:
        return 0.0
    else:
        return val


def camera_tracking(target,stop):
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)

        # for i in range(40):
        while True:
            with picamera.array.PiRGBArray(camera) as stream:
                camera.capture(stream, 'rgb')
                captured_data = rgb2gray(stream.array)
                # captured_data = stream.array[:,:,0]
                prediction = rugby_tracker.predict_action_pos(captured_data)
                # print(captured_data.sum())
                print('predct ', decimal_limit(prediction))

                target.value = decimal_limit(prediction)*180
                time.sleep(0.3)
    stop.value = 1.0

def indecator(target, stop):
    
    def record():
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

    while not stop.value:
        if button.is_pressed:
            record()


if __name__ == '__main__':
    target = Value('d',0.0)
    stop = Value('d',0.0)

    cam_process = Process(target=camera_tracking, args=(target,stop))
    cam_process.start()
    
    servo_process = Process(target=servo_control, args=(target,stop))
    servo_process.start()

    indecator_process = Process(target=indecator, args=(target,stop))
    indecator_process.start()

