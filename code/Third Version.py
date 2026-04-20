from ble_keyboard import BLEKeyboard
from machine import Pin, TouchPad
import struct
import time

kb = BLEKeyboard("ESP32")

touch_f = TouchPad(Pin(15))
touch_g = TouchPad(Pin(13))
touch_h = TouchPad(Pin(12))
touch_j = TouchPad(Pin(14))

THRESHOLD = 350

KEY_F = 0x09
KEY_G = 0x0A
KEY_H = 0x0B
KEY_J = 0x0D

held = {
    'f': False,
    'g': False,
    'h': False,
    'j': False,
}

def press(keycode, modifier=0):
    kb._send(struct.pack("8B", modifier, 0, keycode, 0, 0, 0, 0, 0))

def release():
    kb._send(b"\x00" * 8)

print("Waiting for Bluetooth connection...")
connection_ready = False

while True:
    if kb.is_connected():
        if not connection_ready:
            print("Connected! Waiting 2 seconds for OS security handshake...")
            time.sleep(2)
            print("Ready!")
            connection_ready = True

        try:
            touches = {
                'f': touch_f.read() < THRESHOLD,
                'g': touch_g.read() < THRESHOLD,
                'h': touch_h.read() < THRESHOLD,
                'j': touch_j.read() < THRESHOLD,
            }
            keys = {
                'f': KEY_F,
                'g': KEY_G,
                'h': KEY_H,
                'j': KEY_J,
            }

            for pad, touched in touches.items():
                if touched and not held[pad]:
                    print(f"{pad.upper()} held down")
                    held[pad] = True
                elif not touched and held[pad]:
                    print(f"{pad.upper()} released")
                    held[pad] = False

            release()
            for pad, touched in touches.items():
                if touched:
                    press(keys[pad])
            release()
            
        except ValueError:
            pass

    else:
        held = {k: False for k in held}
        connection_ready = False

    time.sleep_ms(20)