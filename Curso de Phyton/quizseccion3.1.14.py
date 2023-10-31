x = 5
y = 10
z = 8

print(x > y)
print(y > z)

x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)

print((1 + 5 ** (0.5)) / 2)
print((6 - 2) / (5 * (1 + 4)) + 3)

seconds_per_day = 86400
day_for_week = 7
print(seconds_per_day * day_for_week)

alfabeto_ingles = 26
para_una = 1
print((alfabeto_ingles * para_una) ** 6)

computers = 30
laboratorios = 20
years_life = 5
partes = 1
total_computers = computers * laboratorios
print(partes / years_life * total_computers)

x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)

x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")

x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")

x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")
