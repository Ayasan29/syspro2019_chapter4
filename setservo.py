import time
import sys
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

print("Šp“x(-90‹`90)‚ğ“ü—Í")
angle = input()

pwm = (0.5 + (1.9 / 180) * angle) / 20 * 100
	servo.ChangeDutyCycle(pwm)
	time.sleep(1.0)




