c0 = int(input("Podaj liczbę naturalną: "))
steps = 0

while c0 != 1:
    if c0 % 2 == 0:
        c0 //= 2
    else:
        c0 = 3 * c0 + 1
    print(c0)  
    steps += 1

print("Liczba kroków potrzebnych do osiągnięcia wartości 1:", steps)
