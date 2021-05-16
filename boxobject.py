##--Micropython--##
##--ESP32 with 1.3Inch OLED Via i2c--##
from machine import Pin, I2C

import sh1106

import time



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
                   
#Sample Code (Can be excecuted in the shell as well)                  
s = box(10,10,10,"Hello")            
a = box(10,20,10,"World")
a.move(60,60)
a.move(60,10)
    
       
       


