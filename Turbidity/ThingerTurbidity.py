#!/usr/bin/env python
import os
import time
from urllib.request import urlopen

myAPI_key = '0D79GE3AFI74ZIW1' #your Write API key
baseURL = ('https://api.thingspeak.com/update?api_key=%s' %myAPI_key)

def read():
    location ='/home/pi/Desktop/Turbidity/Sample.txt'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    print (text)
    TurbidityValue = float(text)
    return TurbidityValue

def loop():
    while True:
        if read() != None:
            print ("Current Turbidity   : %0.3f NTU" % read())
            conn = urlopen(baseURL + '&field2=%s' % read ())
            print(conn.read()) #print data entry
            conn.close() #closing the connection
            time.sleep(1)
           
def kill():
    quit()
if __name__ == '__main__':
    try:
        loop()
    except KeyboardInterrupt:
        kill()


