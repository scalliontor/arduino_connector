import serial.tools.list_ports

def find_serial_ports():
    """Lists available serial ports."""
    ports = serial.tools.list_ports.comports()
    
    if not ports:
        print("No serial ports found. Make sure your device is connected and drivers are installed.")
        return

    print("Found available serial ports:")
    for port in ports:
        print(f"  - Port: {port.device}")
        print(f"    Description: {port.description}")
        print(f"    Hardware ID: {port.hwid}")
        print("-" * 20)

if __name__ == "__main__":
    find_serial_ports()