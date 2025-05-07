import serial
import time
import random

tx_port = 'COM3'
baud_rate = 9600
timeout = 1
loop_count = 100
byte_per_packet = 4

ser_tx = serial.Serial(tx_port, baud_rate, timeout=timeout)
sent_bytes = 0

print("Gönderici başlatıldı...\n")

for i in range(loop_count):
    random_data = bytes([random.randint(0, 255) for _ in range(byte_per_packet)])
    ser_tx.write(random_data)
    sent_bytes += len(random_data)

    print(f"{i+1:03d}. Gönderilen: {random_data.hex(' ').upper()}")
    time.sleep(0.05)

ser_tx.close()
print(f"\nToplam gönderilen byte sayısı: {sent_bytes}")





import serial
import time

rx_port = 'COM4'
baud_rate = 9600
timeout = 1
received_bytes = 0
duration_seconds = 6  # Gönderici 100x0.05 = yaklaşık 5 saniye

ser_rx = serial.Serial(rx_port, baud_rate, timeout=timeout)

print("Alıcı başlatıldı...\n")
start_time = time.time()

while time.time() - start_time < duration_seconds:
    incoming = ser_rx.read(ser_rx.in_waiting or 1)
    if incoming:
        print(f"Alınan: {incoming.hex(' ').upper()}")
        received_bytes += len(incoming)

ser_rx.close()
print(f"\nToplam alınan byte sayısı: {received_bytes}")
