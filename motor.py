import RPi.GPIO as GPIO
import time
servo_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(6.5)

for cnt in range(0,3) :
    pwm.ChangeDutyCycle(6.5)
    time.sleep(5.0)
    pwm.ChangeDutyCycle(2.0)
    time.sleep(5.0)

pwm.ChangeDutyCycle(6.5)

pwm.stop()
GPIO.cleanup()