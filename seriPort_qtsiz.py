import serial
import serial.tools.list_ports
import threading

def list_ports():
    ports = serial.tools.list_ports.comports()
    for i, port in enumerate(ports):
        print(f"{i}: {port.device} - {port.description}")
    return ports

def read_from_port(ser, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        while True:
            if ser.in_waiting:
                try:
                    data = ser.readline().decode(errors="ignore").strip()
                    print(data)
                    file.write(data + "\n")
                    file.flush()
                except Exception as e:
                    print(f"Hata: {e}")
                    break

def main():
    ports = list_ports()
    if not ports:
        print("Hiçbir seri port bulunamadı.")
        return

    try:
        index = int(input("Bağlanmak istediğiniz port numarasını girin: "))
        port_name = ports[index].device
        ser = serial.Serial(port_name, baudrate=9600, timeout=1)
        print(f"{port_name} portuna bağlandı. Veriler 'log.txt' dosyasına yazılıyor...")

        thread = threading.Thread(target=read_from_port, args=(ser, "log.txt"), daemon=True)
        thread.start()

        input("Kapatmak için Enter'a basın...\n")
        ser.close()

    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    main()
