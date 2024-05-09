import Adafruit_DHT
from gpiozero import DistanceSensor
from time import sleep
from RPi import GPIO
from mfrc522 import SimpleMFRC522

URL = 'https://lionfish-intent-nicely.ngrok-free.app'

class DhtSensor:
    def __init__(self):

        self.sensor = Adafruit_DHT.DHT11
        self.pin = 17

    def update_readings(self):
        humidity, temp = Adafruit_DHT.read_retry(self.sensor, self.pin)
        return {'humidity': humidity, 'temperature': temp}

class UltraSensor:
    def __init__(self):
        self.sensor = DistanceSensor(echo=24, trigger=23)

    def update_distance(self):
        try:
            distance = self.sensor.distance
            sleep(0.5)
            return distance
        except Exception as e:
            print('Error Occured in reading ultrasonic sensor : ',e)

class SolenoidLock:
    def __init__(self):
        self.gpio = GPIO
        self.gpio.setwarnings(False)
        self.gpio.setmode(GPIO.BCM)
        self.gpio.setup(18, GPIO.OUT)

    def update_lock(self, status):
        if status == 'Lock':
            self.gpio.output(18, 1)
            sleep(1)
            return 'Locked Successfully'
        else:
            self.gpio.output(18, 0)
            sleep(1)
            return 'Unlocked Successfully'

class Bulb:
    def __init__(self, statuses):
        self.pins = [17, 27, 22, 5, 18]
        self.statuses = statuses
        GPIO.setmode(GPIO.BCM)
        for pin, status in zip(self.pins[0:4], self.statuses[0:4]):
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH if status else GPIO.LOW)
    def update_system(self,new_values):
        for pin, status in zip(self.pins, new_values):
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, GPIO.HIGH if status else GPIO.LOW)

    def close_all(self):
        for pin in self.pins:
            GPIO.output(pin, GPIO.LOW)

    def change_status(self):
        read = GPIO.input(18)

        GPIO.output(18, GPIO.HIGH if read == GPIO.LOW else GPIO.LOW)
        print('Unlocked')

class rfid:

    def __init___(self):
        self.reader = SimpleMFRC522()

    def register(self,username):
        try:
            print('place your tag')
            reader = SimpleMFRC522()
            self.id, self.text = reader.read()
            reader.write(username)
            print('written')
            return {'update':'success','id':self.id}

        finally:
            GPIO.cleanup()
    def read(self):
        try:
            print('Place your tag.')
            reader = SimpleMFRC522()
            self.id, self.text = reader.read()
            print('successfully read.')
            print(type(self.id))

            return {'id':self.id,'username':self.text}
        finally:
            pass
