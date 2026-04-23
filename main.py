from database import init_db
from usb_detector import monitor_usb

def main():
    init_db()
    monitor_usb()

if __name__ == "__main__":
    main()
