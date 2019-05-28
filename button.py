import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(6, gpio.IN)

try:
	while True:
		input_val = gpio.input(6)
		if input_val == False:
			print("pressed")
			while input_val == False:
				input_val = gpio.input(6)
except KeyboardInterrupt:
	print("\nKeyboard interrupt")
finally:
	print("Cleaning up and exiting")
	gpio.cleanup()
