import random
import emoji


# Funcion para generar la casa y la puerta

def create_house() -> list:

    house = [list(["🟫"]* 4) for _ in range(4)]

    if random.choice([True, False]):
        # Columnas del perimetro

        door = [random.randint(0, 3), random.choice([0, 3])]

    else:
        # Fila del perimetro

        door = [random.choice([0, 3]), random.randint(0, 3)]

    house[door[0]][door[1]] = "🚪"

    # funcion para generar el dulce

    def generate_candy(door: list)  -> list:
        candy = [random.randint(0, 3), random.randint(0, 3)]
        if candy[0] == door[0] and candy[1] == door[1]:
            return generate_candy(door)
        return candy
    candy = generate_candy(door)

    house[candy[0]][candy[1]] = "🍬"

    for row in house:
        print("".join(map(str, row)))

    return house, door

house, door = create_house()

position = door

print (f"Position inicial: {position}")
