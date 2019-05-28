import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

led=11
GPIO.setup(led, GPIO.LOW, initial=GPIO.LOW)

try:
	while(True):
		GPIO.output(led, GPIO.HIGH)
		print("ON")
		time.sleep(1)
		GPIO.output(led, GPIO.LOW)
		print("OFF")
		time.sleep(1)
except KeyboardInterrupt:
	print("\nKeyboard interrupt")
finally:
	print("Cleaning up and exiting")
	GPIO.cleanup()
