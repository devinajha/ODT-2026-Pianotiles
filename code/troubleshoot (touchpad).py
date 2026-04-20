from machine import Pin, TouchPad
import time

pins_to_test = [0, 14, 15, 27, 32, 33]

pads = []
for p in pins_to_test:
    try:
        pads.append((p, TouchPad(Pin(p))))
        print(f"GPIO{p} OK")
    except:
        print(f"GPIO{p} FAILED")

while True:
    for p, pad in pads:
        print(f"GPIO{p}:", pad.read(), end="  ")
    print()
    time.sleep_ms(500)

