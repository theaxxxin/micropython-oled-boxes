

##--Micropython--##
##--ESP32 with 1.3Inch OLED Via i2c--##
from machine import Pin, I2C, TouchPad

import sh1106

import time
import random



# ESP32 Pin assignment for display (DONT IGNORE)
i2c = I2C(scl=Pin(14), sda=Pin(27), freq=400000)

# Display Init Sequence ---- 
display = sh1106.SH1106_I2C(128, 64, i2c,Pin(16), 0x3c)
display.sleep(False)
display.fill(0)
# ------
  

#Box Class

class box:
    def __init__(self,x,y,sz,name):
        self.posx=x
        self.posy=y
        self.size = sz
        self.name = name
        self.update()
       
        
    def update(self):
        display.fill_rect(self.posx,self.posy,self.size,self.size,1)
        display.text(self.name,self.posx+self.size+2,self.posy)
        display.show()
        
    def move(self,endx,endy):
        
                 
        startx = self.posx
        starty = self.posy
                
        for i in range(1,51):     
        
            display.fill_rect(self.posx,self.posy,self.size,self.size,0)
            display.text(self.name,self.posx+self.size+2,self.posy,0)
            self.posx = int(startx + (endx - startx) * i/50)
            self.posy = int(starty + (endy - starty) * i/50)
            self.update()     
a = box(10,10,10,"BYAAAARGH")
button = Pin(18,Pin.IN)

button_press = False
global interrupt_pin
def handle_interrupt (pin):
    global button_press
    button_press = True
    global interrupt_pin
    interrupt_pin = pin
button.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)
instance=[] 

boxcount = 0
while True: 
    time.sleep(0.1)
    if button_press:
        boxcount +=1
        print("buttonpress!")
        instance.append(box(random.randint(1,128),random.randint(1,64),10,str(boxcount)))
        button_press = False
