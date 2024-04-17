liczby_z_kapelusza = [1, 2, 3, 4, 5] 

zmiana = int(input("Podaj jaka liczba ma byc zamieniona środkowa liczba:"))
liczby_z_kapelusza[2] = zmiana

del liczby_z_kapelusza[-1]


print("długość listy to:" ,len(liczby_z_kapelusza))

print(liczby_z_kapelusza)
