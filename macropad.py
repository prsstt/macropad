import board
import time
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import usb_hid

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

d0 = DigitalInOut(board.D0)
d0.direction = Direction.INPUT
d0.pull = Pull.UP

d1 = DigitalInOut(board.D1)
d1.direction = Direction.INPUT
d1.pull = Pull.UP

d2 = DigitalInOut(board.D2)
d2.direction = Direction.INPUT
d2.pull = Pull.UP

d3 = DigitalInOut(board.D3)
d3.direction = Direction.INPUT
d3.pull = Pull.UP

d7 = DigitalInOut(board.D7)
d7.direction = Direction.INPUT
d7.pull = Pull.UP

d8 = DigitalInOut(board.D8)
d8.direction = Direction.INPUT
d8.pull = Pull.UP

d9 = DigitalInOut(board.D9)
d9.direction = Direction.INPUT
d9.pull = Pull.UP

d10 = DigitalInOut(board.D10)
d10.direction = Direction.INPUT
d10.pull = Pull.UP
# little function to open apps via spotlight
def open_app(app):
    kbd.send(Keycode.COMMAND)
    time.sleep(0.2)
    layout.write(app)
    time.sleep(0.5)
    kbd.send(Keycode.ENTER)


# Utworzenie obiektu reprezentującego diodę LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT
while True:
    if not d0.value:
        led.value = True  # Włączenie diody LED
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)
        kbd.send(Keycode.EIGHT)
        kbd.send(Keycode.ENTER)
    elif not d1.value:
        led.value = True  # Włączenie diody LED
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)
        kbd.send(Keycode.SEVEN)
        kbd.send(Keycode.ENTER)
    elif not d2.value:
        led.value = True  # Włączenie diody LED
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)
        kbd.send(Keycode.SIX)
        kbd.send(Keycode.ENTER)
    elif not d3.value:
        led.value = True  # Włączenie diody LED
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)
        kbd.send(Keycode.FIVE)
        kbd.send(Keycode.ENTER)
    elif not d7.value:
        led.value = True  # Włączenie diody LED
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)
        kbd.send(Keycode.FOUR)
        kbd.send(Keycode.ENTER)
    elif not d8.value:
        led.value = True  # Włączenie diody LED
        kbd.send(Keycode.ENTER)
        time.sleep(0.2)
        kbd.send(Keycode.THREE)
        kbd.send(Keycode.ENTER)
    elif not d9.value:
        led.value = True  # Włączenie diody LED
        kbd.press(Keycode.CONTROL, Keycode.KEYPAD_SIX)
        time.sleep(0.2)
        kbd.release_all()
    elif not d10.value:
        led.value = True  # Włączenie diody LED
        open_app("Call of Duty")
    else:
        led.value = False
