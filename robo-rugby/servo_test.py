import time
import wiringpi


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


for i in range(60):
    set_servo(i*3)
    print(i*3)
    time.sleep(0.3)
