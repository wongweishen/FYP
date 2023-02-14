#README
This Python code reads the temperature from a DS18B20 temperature sensor, reads the turbidity value from a sample file and sends the data to a ThingSpeak channel. The code uses the urllib library to make HTTP requests to the ThingSpeak API.

#Requirements

This code requires the following:
Raspberry Pi with Python 3.x installed
DS18B20 temperature sensor
Turbidity sensor and sample file
ThingSpeak account with Write API key 

Usage

Connect the DS18B20 temperature sensor and the turbidity sensor to the Raspberry Pi.
Update myAPI_key variable with your ThingSpeak channel's Write API key.
Update TurbidityLocation variable with the path to your turbidity sensor's sample file.
Run the code using Python.

Functions

This code contains the following functions:

sensor(): Finds the serial number of the DS18B20 temperature sensor.

temp(ds18b20): Reads the temperature from the DS18B20 temperature sensor.

read(): Reads the turbidity value from the sample file.

loop(): Sends the turbidity value to the ThingSpeak channel.

loop2(ds18b20): Sends the temperature value to the ThingSpeak channel.

Main

The main function of the code initializes a serial connection to the turbidity sensor, reads the serial data, writes the data to the sample file, and then runs the loop() and loop2() functions to send the temperature and turbidity values to ThingSpeak.

Note

This code is written to run indefinitely, so it may be necessary to add a stop condition if you want to run it for a specific amount of time.
