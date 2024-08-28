import argparse
from scapy.all import *
from termcolor import colored

# Función para descifrar un mensaje codificado con César
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Mantener los espacios y otros caracteres
    return result

# Función para contar patrones de consonantes después de vocales
def count_vowel_consonant_pattern(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    count = 0
    for i in range(1, len(text)):
        if text[i-1] in vowels and text[i] in consonants:
            count += 1
    return count

# Configurar el analizador de argumentos
parser = argparse.ArgumentParser(description="Procesar archivo .pcapng para extraer y descifrar un mensaje ICMP.")
parser.add_argument('pcap_file', help="Nombre del archivo .pcapng")

# Obtener el nombre del archivo desde los argumentos
args = parser.parse_args()

# Cargar el archivo .pcapng
packets = rdpcap(args.pcap_file)

# Extraer las letras enviadas en los paquetes ICMP
encoded_message = ""
for packet in packets:
    if packet.haslayer(ICMP):
        if packet[ICMP].type == 8:  # Tipo 8 es Echo Request
            if packet.haslayer(Raw):  # Verificar que haya datos en la carga útil
                payload = packet[Raw].load.decode(errors='ignore')  # Leer la carga útil
                if len(payload) > 0:  # Asegurarse de que haya al menos un carácter
                    encoded_message += payload[0]  # Agregar solo el primer carácter (incluyendo espacios)

# Probar todas las combinaciones de César
best_shift = 0
best_score = 0
best_message = ""

# Almacenar los resultados para mostrarlos después
results = []

for shift in range(26, -1, -1):
    decoded_message = caesar_cipher(encoded_message, shift)
    score = count_vowel_consonant_pattern(decoded_message)
    results.append((shift, decoded_message, score))
    if score > best_score:
        best_score = score
        best_shift = shift
        best_message = decoded_message

contador = 0
# Mostrar todos los resultados, coloreando el mejor en verde
for shift, decoded_message, score in results:
    if shift == best_shift:
        print(colored(f"Shift {contador}: {decoded_message} (Mejor coincidencia)", 'green'))
    else:
        print(f"Shift {contador}: {decoded_message}")
    contador += 1

