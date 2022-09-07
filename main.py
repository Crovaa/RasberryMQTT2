import paho.mqtt.client as mqtt
import time

broker_port = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code "+str(rc))

    client.subscribe("TestingTopic", qos=1)

def on_message(client, userdata, message):
    print("Message Recieved: " + message.payload.decode())

client = mqtt.Client()
client.connect("10.4.1.212", broker_port)

#client.publish(topic="TestingTopic", payload="TestingPayload", qos=1, retain=False)

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()