import time
import os

def main():
    read_lines = 0
    try:
        while True:
            if os.path.exists("data.txt"):
                with open("data.txt", "r") as file:
                    lines = file.readlines()
                    new_lines = lines[read_lines:]  # daha önce okunan satırları atla
                    for line in new_lines:
                        print("Read:", line.strip())
                    read_lines = len(lines)
            time.sleep(1)
    except KeyboardInterrupt:
        print("Reader terminated by user.")

main()



import serial
import time

def main():
    try:
        ser = serial.Serial('COM3', 9600, timeout=1)
        time.sleep(2)  # bağlantının oturması için bekle

        while True:
            if ser.in_waiting:
                data = ser.readline().decode().strip()
                if data:
                    print(f"Received: {data}")
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("Reader stopped.")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

main()
