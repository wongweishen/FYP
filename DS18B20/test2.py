#!/usr/bin/env python
import os
import time
from urllib.request import urlopen

myAPI_key = '07GE4ZII9D73AFW1' #your Write API key
baseURL = ('https://api.thingspeak.com/update?api_key=%s' %myAPI_key)

def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20
def read(ds18b20):
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

def loop(ds18b20):
    while True:
        if read(ds18b20) != None:
            print ("Current temperature : %0.3f C" % read(ds18b20)[0])
            print ("Current temperature : %0.3f F" % read(ds18b20)[1])
            print ('Temperature = %0.1f celcius' % read(ds18b20)[0])
            conn = urlopen(baseURL + '&field1=%s' % read (ds18b20)[0])
            print(conn.read()) #print data entry
            conn.close() #closing the connection
            time.sleep(1)
            
def kill():
    quit()
if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()

