# Servo Control
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

delay_period = 0.01

while True:
        for degrees in range(0, 180, 1):
                set_servo(degrees)
                time.sleep(delay_period)
        for degrees in range(180, 0, -1):
                set_servo(degrees)
                time.sleep(delay_period)
