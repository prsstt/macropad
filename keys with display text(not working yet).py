import board
import busio
import time
from digitalio import DigitalInOut, Direction, Pull
import displayio
import terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)
displayio.release_displays()
i2c = busio.I2C(scl=board.SCL, sda=board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)
splash = displayio.Group()
display.show(splash)

d0 = DigitalInOut(board.D0)
d0.direction = Direction.INPUT
d0.pull = Pull.UP
d1 = DigitalInOut(board.D1)
d1.direction = Direction.INPUT
d1.pull = Pull.UP

d2 = DigitalInOut(board.D2)
d2.direction = Direction.INPUT
d2.pull = Pull.UP

# little function to open apps via spotlight
def open_app(app):
    kbd.send(Keycode.COMMAND)
    time.sleep(0.2)
    layout.write(app)
    time.sleep(0.2)
    kbd.send(Keycode.ENTER)


# Utworzenie obiektu reprezentującego diodę LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
cl = 0xFFFFFF
text = ""
text_area = label.Label(terminalio.FONT, text=text, color=cl, x=32, y=32)
splash.append(text_area)

while True:
    if not d0.value:
        led.value = True  # Włączenie diody LED
        text_area.text = "Key 1 pressed"
        open_app("League of Legends.exe")
        display.show(splash)
    elif not d1.value:
        led.value = True  # Włączenie diody LED
        text_area.text = "Key 2 pressed"
        display.show(splash)
    elif not d2.value:
        led.value = True
        text_area.text = "Key 3 pressed"
        display.show(splash)
    else:
        led.value = False
