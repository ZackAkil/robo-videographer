
import time
from multiprocessing import Process, Value

from SimpleCV import *
import numpy
import wiringpi
import pytweening

from rugby_tracker import rugby_tracker


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
    current_pos = 0.0
    while not stop.value:
        time.sleep(0.02)
        diff = (current_pos - target.value)
        if diff:
            move = pytweening.easeInQuad(abs(diff/200.0))
            move = move if diff < 0 else -move 
            current_pos += move*100
            set_servo(current_pos+40)

frame_spec = [640, 480]
frame_bar = np.array(range(frame_spec[0]))

def draw_box(img, pos):
    overlay = DrawingLayer((img.width, img.height))
    overlay.centeredRectangle(pos,(100,100), color=Color.RED)
    img.addDrawingLayer(overlay)
    img.applyLayers()

# def get_average_activity_pos(img):
#     val = img.getNumpy()
#     activity = (val[:,:,1] < 1)
#     count = activity.sum()
#     avg = 0
#     if count:
#         avg = (activity .sum(axis=1)*frame_bar).sum()/count
#     return [(avg,0),count]

def camera_tracking_smart(target,stop):
    cam = Camera()
    box_x = 0
    for i in range(150):
        cam_image = cam.getImage().scale(frame_spec[0], frame_spec[1])
        prediction = rugby_tracker.predict_action_pos(cam_image.getNumpy())
        box_x = prediction
        draw_box(cam_image, [box_x,frame_spec[1]/2])
        win = cam_image.show()
        time.sleep(0.2)
    win.quit()
    stop.value = 1.0

# def camera_tracking(target,stop):
#     cam = Camera()
#     box_x = 0
#     for i in range(150):
#         first = cam.getImage().scale(frame_spec[0], frame_spec[1])
#         time.sleep(0.05)
#         second = cam.getImage().scale(frame_spec[0], frame_spec[1]) 
#         img = (first-second).binarize(50)
#         [pos,weight]= get_average_activity_pos(img)
#         if weight > 50:
#             print('over weight ' + str(pos[0]))
#             target.value = int(pos[0]*(100.0/frame_spec[0]))
#             box_x = pos[0]
#         draw_box(first, [box_x,frame_spec[1]/2])
#         win = first.show()
#     win.quit()
#     stop.value = 1.0

if __name__ == '__main__':
    target = Value('d',0.0)
    stop = Value('d',0.0)

    cam_process = Process(target=camera_tracking, args=(target,stop))
    cam_process.start()
    
    servo_process = Process(target=servo_control, args=(target,stop))
    servo_process.start()


