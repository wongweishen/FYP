import time
from w1thermsensor import W1ThermSensor
from urllib.request import urlopen

sensor = W1ThermSensor()

myAPI_key = '07EI7G34ZI9DAFW1' #your Write API key
baseURL = ('https://api.thingspeak.com/update?api_key=%s' %myAPI_key)

while True:
    temp = sensor.get_temperature()
    #temp = “%0.1f” % temp
    print('Temperature = %0.1f celcius' % temp)
    conn = urlopen(baseURL + '&field1=%s' % temp)
    print(conn.read()) #print data entry
    conn.close() #closing the connection
    time.sleep(1)
