import paho.mqtt.subscribe as subscribe
import time

While True
temp = subscribe.simple("paho/test/simple", hostname="205.236.77.22")
print("%s %s" % (temp.topic, temp.payload))
humidity = subscribe.simple("paho/test/simple", hostname="205.236.77.22")
print("%s %s" % (humidity.topic, humidity.payload))