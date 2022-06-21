#!/usr/bin/env python
import os
import time
from urllib.request import urlopen
import serial

myAPI_key = '07GE4ZII9D73AFW1' #your Write API key
baseURL = ('https://api.thingspeak.com/update?api_key=%s' %myAPI_key)
TurbidityLocation ='/home/pi/Desktop/Final/Sample.txt'

def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20

def temp(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def read():
    tfile = open(TurbidityLocation)
    text = tfile.read()
    tfile.close()
    TurbidityValue = float(text)
    return TurbidityValue

def loop():
    while True:
        if read() != None:
            print ("Current Turbidity   : %0.3f NTU" % read())
            conn = urlopen(baseURL + '&field2=%s' % read ())
            print(conn.read()) #print data entry
            conn.close() #closing the connection
            time.sleep(30)
            break
        
def loop2(ds18b20):
    while True:
        if temp(ds18b20) != None:
            print ('Temperature = %0.1f celcius' % temp(ds18b20)[0])
            conn = urlopen(baseURL + '&field1=%s' % temp (ds18b20)[0])
            print(conn.read()) #print data entry
            conn.close() #closing the connection
            time.sleep(10)
            break
        
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)
    ser.reset_input_buffer()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            print(line)
            f = open(TurbidityLocation,"w")
            f.write(str(line))
            f.close()
            serialNum = sensor()
            loop()
            loop2(serialNum)
            time.sleep(20)



