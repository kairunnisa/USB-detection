from plyer import notification

def send_alert(device_name):
    notification.notify(
        title="Unauthorized USB Detected",
        message=f"{device_name} is not authorized!",
        timeout=10
    )
