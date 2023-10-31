for i in range(0, 11):
    if i % 2 != 0:
        print(i)

x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1

for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")

for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")

n = 3

while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)

n = range(4)

for num in n:
    print(num - 1)
else:
    print(num)

for i in range(0, 6, 3):
    print(i)
