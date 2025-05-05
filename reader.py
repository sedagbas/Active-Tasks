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
