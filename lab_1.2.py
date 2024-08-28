from scapy.all import *

def send_icmp_message(message, destination_ip):
    identifier = 1111 # Identificador fijo o puedes generarlo dinámicamente
    sequence_number = 1  # Número de secuencia inicial

    for char in message:
        payload = (char * 48).encode()  # Replicar el carácter para llenar 48 bytes de datos 
        
        # Crear el paquete ICMP con la carga útil replicada
        icmp_packet = IP(dst=destination_ip)/ICMP(type=8, id=identifier, seq=sequence_number)/Raw(load=payload)
        
        # Enviar el paquete ICMP
        send(icmp_packet)
        
        # Incrementar el número de secuencia
        sequence_number += 1

if __name__ == "__main__":
    # Solicitar al usuario que ingrese el mensaje y la dirección IP de destino
    message = input("Ingrese el mensaje a enviar: ")
    destination_ip = input("Ingrese la dirección IP de destino: ")
    
    # Llamar a la función para enviar el mensaje
    send_icmp_message(message, destination_ip)
