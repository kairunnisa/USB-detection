import wmi
import time
from database import log_event
from whitelist import is_authorized
from alert import send_alert

def monitor_usb():
    c = wmi.WMI()

    print("Monitoring USB devices...")

    while True:
        for usb in c.Win32_USBHub():
            device_name = usb.Name

            if not is_authorized(device_name):
                print(f"Unauthorized USB detected: {device_name}")

                log_event(device_name, "Unauthorized Access")
                send_alert(device_name)

        time.sleep(10)
