def cifrar_cesar(texto, desplazamiento):
    resultado = []

    for char in texto:
        if char.isalpha():  # Verifica si el carácter es una letra
            desplazamiento_mod = desplazamiento % 26  # Para manejar desplazamientos mayores
            ascii_offset = ord('A') if char.isupper() else ord('a')
            nueva_posicion = (ord(char) - ascii_offset + desplazamiento_mod) % 26
            nuevo_char = chr(nueva_posicion + ascii_offset)
            resultado.append(nuevo_char)
        else:
            # Añade el carácter sin modificar si no es una letra
            resultado.append(char)

    return ''.join(resultado)

def main():
    texto = input("Introduce el texto a cifrar: ")
    desplazamiento = int(input("Introduce el desplazamiento (un entero): "))

    texto_cifrado = cifrar_cesar(texto, desplazamiento)

    print(f"Texto cifrado: {texto_cifrado}")

if __name__ == "__main__":
    main()
