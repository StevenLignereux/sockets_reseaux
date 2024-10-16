import socket
import time

HOST_IP = "127.0.0.1"
HOST_PORT = 32000
MAX_DATA_SIZE = 1024

print(f"Connection au serveur {HOST_IP}, port {HOST_PORT}")

while True:
    try:
        s = socket.socket()
        s.connect((HOST_IP, HOST_PORT))

    except ConnectionRefusedError:
        print("ERREUR : impossible de se connecter au serveur ! Reconnexion...")
        time.sleep(4)

    else:
        print("Connecté au serveur")
        break

datas_recues = s.recv(MAX_DATA_SIZE)

if datas_recues:
    print(datas_recues.decode())
else:
    print("Aucune data")

s.close()
