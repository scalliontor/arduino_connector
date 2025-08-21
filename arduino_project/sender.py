
import serial
import time


arduino_port = '/dev/ttyACM0' 
# --------------------------

baud_rate = 9600

try:
    # Establish a connection to the serial port
    arduino = serial.Serial(port=arduino_port, baudrate=baud_rate)
    print(f"Successfully connected to Arduino on {arduino_port}")
except serial.SerialException as e:
    print(f"Error: Could not open port {arduino_port}. {e}")
    print("Please check the port name and that the Arduino is connected.")
    exit()

time.sleep(2)

print("Enter '1' to turn the LED ON.")
print("Enter '0' to turn the LED OFF.")

while True:
    command = input("\nEnter command: ")

    if command == '1':
        arduino.write(b'1')
        print("Sent '1' -> LED should be ON")
        
    elif command == '0':
        arduino.write(b'0')
        print("Sent '0' -> LED should be OFF")
        


arduino.close()
