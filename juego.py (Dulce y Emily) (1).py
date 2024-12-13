
import random

marcas = ["Toyota", "Volvo", "Subaru", "Peugeot", "Honda", "Mercedes", "Nissan","Volkswagen","Porsche","Ferrari","Lamborghini","Chevrolet","Renault","Mazda","Citroën"]

marca_aleatoria = random.choice(marcas)
print(marca_aleatoria)

print("Adivina la marca del coche.")
respuesta = input("escribe tu respuesta: ")
    
if respuesta == marca_aleatoria:
    print("¡Correcto! Has adivinado la marca.")
        
else:
    print("Incorrecto, intentalo de nuevo.")


