from machine import Pin, TouchPad
import time

touch_f = TouchPad(Pin(4))
touch_g = TouchPad(Pin(14))
touch_h = TouchPad(Pin(27))
touch_j = TouchPad(Pin(13))

while True:
    print("F:", touch_f.read(), " G:", touch_g.read(), " H:", touch_h.read(), " J:", touch_j.read())
    time.sleep_ms(500)