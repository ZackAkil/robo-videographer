import picamera
import time

camera = picamera.PiCamera()

for i in range(5):
    time.sleep(t)
    ts = str(time.time()).replace('.','')
    # ensure file name length is the same by appending 0's
    ts += '0'*(12 - len(ts))
    camera.capture('capture/{0}.jpg'.format(ts))
    print('got image', ts)
