#print("hello")
import mosquito
import paho.mqtt.client as mqtt
import time


def on_log(client, userdata, level, buf):
    print("log: "+buf)


def no_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected OK")
    else:
        print("Bad Connection Returned code =", rc)

def on_disconnect(client, userdata, flags, rc = 0):
    print("DisConnected result code"+str(rc))

def on_message(client, userdata,msg):
    topic =msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore "))
    print(m_decode)

broker ="172.0.0.1"
client = mqtt.Client("Call_For_Proposal")
Client1 = mqtt.Client("proposal")
print("connection to broker :broker", broker)

client.on_connect =no_connect
client.on_log = on_log
client.on_disconnect = on_disconnect
client.on_message= on_message

client.connect("localhost", 1883, 60)
client.loop_start()
client.subscribe("hi")
client.publish("hi", "hello")

#client.publish("hello", "i am fine")

time.sleep(10)
client.loop_stop()
client.disconnect()


