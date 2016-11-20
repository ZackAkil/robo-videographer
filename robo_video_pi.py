from SimpleCV import *
import time
import numpy
import wiringpi

cam = Camera()

# use 'GPIO naming'
wiringpi.wiringPiSetupGpio()
# set #18 to be a PWM output
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
# set the PWM mode to milliseconds stype
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
# divide down clock
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01

def set_servo(degrees):
    pulse = int((200/180.0)*degrees) + 50
    wiringpi.pwmWrite(18, pulse)

frame_spec = [160, 120]
frame_bar = np.array(range(frame_spec[0]))

def get_average_activity_pos(img):
    val = img.getNumpy()
    activity = (val[:,:,1] < 1)
    count = activity.sum()
    avg = 0
    if count:
        avg = (activity .sum(axis=1)*frame_bar).sum()/count
    return [(avg,0),count]

def draw_circle(img, pos):
    overlay = DrawingLayer((img.width, img.height))
    overlay.circle(pos, 10, color=Color.RED)
    img.addDrawingLayer(overlay)
    img.applyLayers()

def draw_box(img, pos):
    overlay = DrawingLayer((img.width, img.height))
    overlay.centeredRectangle(pos,(100,100), color=Color.RED)
    img.addDrawingLayer(overlay)
    img.applyLayers()

def move_towards_target(activity_pos, view_box):
    diff = activity_pos[0] - view_box[0]
    mov = diff/5 
    # mov = 20*(mov) if 0 < mov < 20 else mov
    return [view_box[0]+mov,view_box[1]]

camera_view = [frame_spec[0]/2, frame_spec[1]/2]
last_scene = [0,0]
for i in range(100):
    first = cam.getImage().scale(frame_spec[0], frame_spec[1])
    time.sleep(0.05)
    second = cam.getImage().scale(frame_spec[0], frame_spec[1]) 
    img = (first-second).binarize(50)
    [pos,weight]= get_average_activity_pos(img)
    if weight > 50:
         draw_circle(first, pos)
         last_scene = [pos[0], pos[1]]
    # txt = "Activity:" + str(weight)
    # first.drawText(txt)
    camera_view = move_towards_target(last_scene, camera_view)
    draw_box(first, camera_view)

    set_servo(int(camera_view[0]*(100.0/frame_spec[0]))+40)
    print weight
    # win = first.show()
    
    win = first.show()


#win.quit()
