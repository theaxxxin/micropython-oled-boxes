# micropython-oled-boxes
Simple OOP to get started with micropython

Things you will need:
1. ESP32 (or other micropython device with enough RAM)
1. 1.3 Inch OLED Screen running on the micropython SH1106 Driver
1. IDE

Once you have set all pins correctly, you can **add a new box** by typing:
```python
object1 = box(posx,posy,size,text)
```
You can then move the box around by typing:
```python
object1.move(endx,endy)
```
Where `endx` and `endy` are the positional coordinates of the point you would like the box to go to.

Here we have a button paired with an interrupt handler that is supposed to add a new box every time it is pressed, however there seems to be some kind of issue with either the software or hardware, waiting to fix this
