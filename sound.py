from time import sleep
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
SOUND_PIN = 11
LED_PIN = 3
GPIO.setup(SOUND_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
[39]
print("Sound sensor test is running...")
while True:
    if GPIO.input(SOUND_PIN) == True:
        GPIO.output(LED_PIN, False)
        print("No sound detected")
    else:
        GPIO.output(LED_PIN, True)
        print("Sound detected!")
    sleep(1)