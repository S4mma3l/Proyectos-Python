'''
 * Crea un programa que calcule quien gana más partidas al piedra,
 papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
'''
import math
import random

print("Juego Piedra 🗿, Papel 📄, Tijera ✂️")
print("Juega con tu Computadora")
print("Jugador #1 = Tu, Jugador #2 = Computadora")


player1 = input("Jugador #1, indica tu Jugada? ")


def juego():
    jugador = player1
    jugador = jugador.capitalize()

    move = ["Piedra", "Papel", "Tijera"]
    jugador2 = random.choice(move)

    if jugador == jugador2:
        return (0, jugador, jugador2)

    if ganador(jugador, jugador2):
        return (1, jugador, jugador2)

    return (-1, jugador, jugador2)


def ganador(usuario1, usuario2):
    if (usuario1 == "Piedra" and usuario2 == "Tijera") or (usuario1 == "Tijera" and usuario2 == "Papel") or (usuario1 == "Papel" and usuario2 == "Piedra"):
        return True
    return False


def el_mejor(n):
    jugador_tiradas = 0
    jugador2_tiradas = 0
    tiradas = math.ceil(n/2)

    while jugador_tiradas < tiradas and jugador2_tiradas < tiradas:

        resultado, jugador, jugador2 = juego()

        if resultado == 0:
            print(
                "El Jugador 1 y El Jugador 2 han eligido {}. Es un empate!!!".format(jugador))

        elif resultado == 1:
            jugador_tiradas += 1
            print("El Jugador 1 eligio {} y el Jugador 2 eligio {}. Ganador Jugador 1".format(
                jugador, jugador2))
        else:
            jugador2_tiradas += 1
            print("El Jugador 1 eligio {} y el Jugador 2 eligio {}. Ganador Jugador 2".format(
                jugador, jugador2))

    if jugador_tiradas > jugador2_tiradas:
        print("Haz Ganado por {}".format(n))
    else:
        print("Haz perdido por {}".format(n))
    return el_mejor


if __name__ == "__main__":
    el_mejor(5)

print("Este Programa fue Elaborado por Sammael")
