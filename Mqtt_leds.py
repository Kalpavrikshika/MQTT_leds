import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

def on_connect(client, userdata, flags, rc):
    print ("Connected with rc: " + str(rc))
    client.subscribe("paho/demo/led")

def on_message(client, userdata, msg):
    print ("Topic: "+ msg.topic+"\nMessage: "+str(msg.payload))
    if "white" in msg.payload:
        #print("  Green on!")
        GPIO.output(13, True)
    else:
        #print("  Green off!")
        GPIO.output(13, False)
    if "green" in msg.payload:
        #print("  Yellow on!")
        GPIO.output(11, True)
    else:
        #print("  Yellow off!")
        GPIO.output(11, False)
    if "blue" in msg.payload:
        #print("  Red on!")
        GPIO.output(12, True)
    else:
        #print("  Red off!")
        GPIO.output(12, False)

username = "paho"
password_= "pahopassword"
client = mqtt.Client("raspberrypi")
client.username_pw_set(username, password=password_)
client.on_connect = on_connect
client.on_message = on_message

client.connect("sungura1-angani-ke-host.africastalking.com", 10883, 60)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

client.loop_forever()