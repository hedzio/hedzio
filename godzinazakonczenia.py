h = int(input("Czas startu (godziny): "))
m = int(input("Czas startu (minuty): "))
d = int(input("Czas trwania wydarzenia (minuty): "))
minuty = h*60+m
wszystkie_minuty = minuty + d
godzina = wszystkie_minuty // 60 % 24
minuta = wszystkie_minuty % 60
print(F"Godzina zakończenia to {godzina}:{minuta}")