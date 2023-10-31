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
print("Juego Piedra, Papel, Tijera, Lagarto, Spock")

player1 = input("Jugador #1, indica tu Jugada? ")
player2 = input("Jugador #2, indica tu Jugada? ")


def juego(players):
    jugador = player1
    jugador2 = player2
    empate = 0

    move = {"Piedra": ["Tijeras"],
            "Papel": ["Piedra"],
            "Tijeras": ["Papel"]
            }

    for i in players:
        if i[0] == i[1]:
            empate += 1
        elif i[0] in move[i[1]]:
            jugador2 += 1
        else:
            jugador += 1

    if jugador > jugador2:
        resultado = "Jugador 1 Gana!!!"
    elif jugador == jugador2:
        resultado = "Jugador 2 y jugador 2 Empate"
    else:
        resultado = "Jugador 2 Gana!!!"

    return resultado


print(juego)
