import random

print("Frases Locas!!!")

palabra_uno = input("Primera Palabra: ")
palabra_dos = input("Segunda Palabra: ")
palabra_tres = input("Tercera Palabra: ")
palabra_cuatro = input("Cuarta Palabra: ")

move = [palabra_uno, palabra_dos, palabra_tres, palabra_cuatro]

frase = f"Hola que tal? {random.choice(move)} como se encuentra el {random.choice(move)} donde todos somo locos, es {random.choice(move)} por eso hay que ser {random.choice(move)} hasta el final!!!"


print(frase)
