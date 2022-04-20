from adafruit_servokit import ServoKit

class TapMotor:

    def __init__(self, servoPinSet ):
        self.kit = ServoKit(channels = 16)
        self.servo = self.kit.servo[servoPinSet]
        

    def startPour(self):
        print('starting the pour')
        self.servo.angle = 180

    def stopPour(self):
        print('stopping the pour')
        self.servo.angle = 0
        