# main.py — Magic Tiles touch controller using ble_keyboard.py
# Upload BOTH this file and ble_keyboard.py to the ESP32

from ble_keyboard import BLEKeyboard
from machine import TouchPad, Pin
import time

kbd = BLEKeyboard("MagicTiles-ESP32")
print("Pair 'MagicTiles-ESP32' on your laptop, then open magictiles.org")

# GPIO pin → HID keycode (f=0x09, g=0x0A, h=0x0B, l=0x0F)
WIRES = [
    (TouchPad(Pin(4)),  0x09, "F"),
    (TouchPad(Pin(2)),  0x0A, "G"),
    (TouchPad(Pin(12)), 0x0B, "H"),
    (TouchPad(Pin(13)), 0x0F, "L"),
]

THRESHOLD   = 200  # lower if touches missed, raise if false triggers
DEBOUNCE_MS = 120

last = [0] * 4

while True:
    now = time.ticks_ms()
    for i, (pad, keycode, label) in enumerate(WIRES):
        val = pad.read()
        diff = time.ticks_diff(now, last[i])
        if val < THRESHOLD and diff > DEBOUNCE_MS:
            if kbd.is_connected():
                kbd.send_raw(keycode)
                print(label)
            last[i] = now
    time.sleep_ms(8)