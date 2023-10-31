counter = 2
value = 3
counter > 0 and value == 100

# Ejemplo 1:
var = 1
print(var > 0)
print(not (var <= 0))


# Ejemplo 2:
var = 1
print(var != 0)
print(not (var == 0))

p =1
q =2

not (p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)

i = 1
j = not not i

var = 17
var_right = var >> 1
var_left = var << 2
print(var, var_left, var_right)
