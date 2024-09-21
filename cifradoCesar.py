#Programa de cifrado cesar con python
#Para correrlo debemos entrar a una terminal y colocarnos en 
#   la direccion donde se encuentre el archivo posteriormente 
#   corremos el siguiente comando python3 cifradoCesar.py 


# Menú para seleccionar la opción de cifrar, descifrar o ambos
opcion = input("¿Qué deseas hacer con el mensaje? (cifrar, descifrar, ambos): ").lower()

# #Prueba
# mensaje = "¡Hola diplomado de ciber seguridad generacion 16!"
# desplazamiento = 4

#Para que el usuario ingrese el mensaje
mensaje = input("Dame el mensaje que deseas cifrar o descifrar: ")
desplazamiento = int(input("¿Que desplazamiento? "))


# Función para cifrar el mensaje
def cifrado_cesar(mensaje, desplazamiento):
    resultado = ""
    
    # Recorremos cada caracter en el mensaje
    for char in mensaje:
        # Ciframos solo letras
        if char.isalpha():
            # Convertimos a mayúscula para simplificar el cifrado
            if char.isupper():
                resultado += chr((ord(char) + desplazamiento - 65) % 26 + 65)
            else:
                resultado += chr((ord(char) + desplazamiento - 97) % 26 + 97)
        else:
            # Si no es letra, lo dejamos sin modificar
            resultado += char
    return resultado

# Función para descifrar el mensaje cifrado usando el cifrado César
def descifrado_cesar(mensaje_cifrado, desplazamiento):
    return cifrado_cesar(mensaje_cifrado, -desplazamiento)

# mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)
# print("Mensaje Cifrado:", mensaje_cifrado)

# mensaje_descifrado = descifrado_cesar(mensaje_cifrado, desplazamiento)
# print("Mensaje Descifrado:", mensaje_descifrado)

if opcion == "cifrar":
    mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)
    print("Mensaje Cifrado:", mensaje_cifrado)
elif opcion == "descifrar":
    mensaje_descifrado = descifrado_cesar(mensaje, desplazamiento)
    print("Mensaje Descifrado:", mensaje_descifrado)
elif opcion == "ambos":
    mensaje_cifrado = cifrado_cesar(mensaje, desplazamiento)
    print("Mensaje Cifrado:", mensaje_cifrado)

    mensaje_descifrado = descifrado_cesar(mensaje_cifrado, desplazamiento)
    print("Mensaje Descifrado:", mensaje_descifrado)
else:
    print("Error en la seleeción; Por favor, selecciona 'cifrar', 'descifrar' o 'ambos'.")
