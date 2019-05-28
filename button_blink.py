import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(6, gpio.IN)
led=17
gpio.setup(led, gpio.LOW, initial=gpio.LOW)

switch = False
try:
	while True:
		input_val = gpio.input(6)
		if input_val == False:
			print("pressed")
			if switch == False:
				gpio.output(17, gpio.HIGH)
				switch = True
				print("On")
			elif switch == True:
				gpio.output(17, gpio.LOW)
				switch = False
				print("Off")
			while input_val == False:
				input_val = gpio.input(6)
except KeyboardInterrupt:
	print("\nKeyboard interrupt")
finally:
	print("Cleaning up and exiting")
	gpio.cleanup()
