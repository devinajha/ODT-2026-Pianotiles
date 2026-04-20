
import bluetooth
import time

ble = bluetooth.BLE()
ble.active(True)

name = "ESP69"
payload = bytes([len(name)+1, 0x09]) + name.encode()

ble.gap_advertise(100000, payload)
print("Advertising... check your Mac Bluetooth")