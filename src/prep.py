#!/usr/bin/python3

import os
HOSTNAME = os.getenv('VH_HOSTNAME')
USB_DEVICE_ID = os.getenv('VH_USB_DEVICE_ID')

print('Prepping VHClient with parameters:')
if not all((HOSTNAME,USB_DEVICE_ID)):
   print("No Configuration provided.  Both Hostname and USB Device ID required.")
   print("Device ID = {Hub Serial Number}.{USB Product ID}.{USB Vendor ID}.{Port Address (Optional)}")
   exit()

print(f'Hostname: {HOSTNAME}')
print(f'Device ID: {USB_DEVICE_ID}')

settings = f'''
[Settings]
ManualHubs={HOSTNAME}:7575
[AutoShare]
{USB_DEVICE_ID}=1
'''

print("Configuring with the following settings:")
print(settings)

with open("./.vhui", "a") as config_file:
    config_file.write(settings)
    config_file.close()
