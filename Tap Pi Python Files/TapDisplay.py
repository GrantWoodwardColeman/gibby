import Adafruit_SSD1306
import time
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

class TapDisplay:

    def __init__(self ):
        RST =  None
        self.disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

        # Initialize library.
        self.disp.begin()

        # Clear display.
        self.disp.clear()
        self.disp.display()

        width = self.disp.width
        height = self.disp.height

        self.image = Image.new('1', (width, height))
        self.draw = ImageDraw.Draw(self.image)
        self.draw.rectangle((0,0,width,height), outline=0, fill=0)

        padding = -2
        self.top = padding
        self.bottom = height-padding
        # Move left to right keeping track of the current x position for drawing shapes.
        self.x = 0

        self.font = ImageFont.load_default()
        

    
        





    def displayText(self, text):

        # Draw a black filled box to clear the image.
        self.draw.rectangle((0,0,self.width,self.height), outline=0, fill=0)


        self.draw.text((self.x, self.top), text,  font=self.font, fill=255)
        self.disp.image(self.image)
        self.disp.display()
        time.sleep(.1)

