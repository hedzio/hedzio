dochod = float(input("Wprowadź swój roczny dochód: "))
nadwyzka = (dochod - 85528)

if dochod <= 85528:
    podatek = dochod * 0.18 - 556.2
else:
    podatek = 0.32 * (dochod - 85528) + 14839.02

if podatek < 0.0:
    podatek = 0.0

podatek = round(podatek,0)
print(F"Podatek wynosi {podatek} talarów.")