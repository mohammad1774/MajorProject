import Adafruit_DHT
import time

DHT_SENSOR  = Adafruit_DHT.DHT11
DHT_PIN = 17

while True:
	humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
	if humidity is not None and temperature is not None:
		print("Temp={0:0.1f}C Humidity= {1:0.1f}%".format(temperature, humidity))
	else :
		print("Check the sensor")
	time.sleep(5)
