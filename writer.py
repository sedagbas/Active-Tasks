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
