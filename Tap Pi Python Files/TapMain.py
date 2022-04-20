import paho.mqtt.client as mqtt
import TapFSM
import TapMotor
import TapDisplay
import time

tap = None

def on_publish(client, userdata, result):
    print("message published")
    

def on_message(client, userdata, message):
    if tap:
        msg = str(message.payload.decode("utf-8"))
        print(msg)

        if msg == "12oz_pour":
            tap.make_pour()
            time.sleep(2)
            tap.stop_pour()

        elif msg == "pour_start":
            tap.make_pour()

        elif msg == "pour_stop":
            tap.stop_pour() 

    


#Tap Main Loop
if __name__ == "__main__":
    print('main loop of the tap')

    servoPin = 0
    broker = "192.168.1.30"
    port = 1883


    client1 = mqtt.Client("client1")
    client1.connect(broker,port)
    client1.on_publish = on_publish
    client1.on_message = on_message

    client1.subscribe("mqtt/tester")

    client1.loop_start()

    servo = TapMotor(servoPin)
    tap = TapFSM(servo)
    display = TapDisplay()
    

    #main run loop
    while True:
        display.displayText("Kegerator")
        continue