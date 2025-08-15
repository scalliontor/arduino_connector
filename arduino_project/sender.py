# File: send_message.py
import serial
import time


arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=0.1)


time.sleep(2) 

def send_message(message):
    print(f"Sending to Arduino: {message}")
    arduino.write((message + '\n').encode('utf-8'))
    time.sleep(0.05)
    response = arduino.readline().decode('utf-8').strip()
    if response:
        print(f"Response from Arduino: {response}")

if __name__ == "__main__":
    try:
        while True:
            user_input = input("Enter message (or 'quit'): ")
            if user_input.lower() == 'quit':
                break
            send_message(user_input)
    finally:
        arduino.close()
        print("Serial connection closed.")