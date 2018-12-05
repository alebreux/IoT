import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

print("HIGH")
GPIO.output(5, GPIO.HIGH)
time.sleep(5)
print("LOW")
GPIO.output(5, GPIO.LOW)
time.sleep(5)

GPIO.cleanup()

