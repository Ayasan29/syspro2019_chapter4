import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)


def setservo(angle):
	pwm = (0.5 + 1.9 * (angle / 180)) / 20 * 100
	servo.ChangeDutyCycle(pwm)
	time.sleep(1.0)


print("enter the angle(-90 ~ 90) => ")
angle = input()
setservo(angle)

GPIO.cleanup()
