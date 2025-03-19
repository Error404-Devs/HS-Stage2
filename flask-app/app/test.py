import RPi.GPIO as GPIO
# LEDS LIGHT

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set GPIO 7 and GPIO 11 as output pins
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)

GPIO.output(7, GPIO.HIGH)  # Turn on LED connected to GPIO 7
GPIO.output(11, GPIO.HIGH)