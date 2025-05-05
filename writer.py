import time

def main():
    i = 0
    try:
        with open("data.txt", "a") as file:
            while True:
                file.write(f"{i}\n")
                file.flush()
                print(f"Writing: {i}")
                i += 1
                time.sleep(1)
    except KeyboardInterrupt:
        print("Writer terminated.")

main()



import serial
import time

def main():
    try:
        ser = serial.Serial('COM4', 9600, timeout=1)
        time.sleep(2)  # bağlantının oturması için bekle

        i = 0
        while True:
            data = f"{i}\n"
            ser.write(data.encode())
            print(f"Sent: {data.strip()}")
            i += 1
            time.sleep(1)

    except KeyboardInterrupt:
        print("Writer stopped.")
    except serial.SerialException as e:
        print(f"Serial error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()

main()
