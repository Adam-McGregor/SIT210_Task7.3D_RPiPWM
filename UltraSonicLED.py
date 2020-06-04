import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

## intialise light ##
GPIO.setup(18, GPIO.OUT)
wave = GPIO.PWM(18, 100)
wave.start(0)

## initalise ultrasonic sensor ##

GPIO.setmode(GPIO.BCM)
TRIG = 23
ECHO = 24

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

## define functions ##
def ReadDistance():
    GPIO.output(TRIG, GPIO.LOW)
    time.sleep(0.5)

    GPIO.output(TRIG, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG, GPIO.LOW)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration *17150

    distance = round(distance, 2)
    return distance

## Program Start ##
MAX_DISTANCE = 50 # set to match avaliable space to see the light
MIN_DISTANCE = 2 # 2 cm
try:
	while 1:
            distance = ReadDistance()
            disPercent = ((MAX_DISTANCE - distance)/ (MAX_DISTANCE - MIN_DISTANCE))*100
            if (disPercent > 100):
                disPercent = 100;
            elif (disPercent < 0):
                disPercent = 0
            wave.ChangeDutyCycle(disPercent)
            time.sleep(0.1) 
                
except KeyboardInterrupt:
	GPIO.cleanup()