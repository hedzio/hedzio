rok = int(input("Wprowadź rok: "))
if rok % 4 != 0:
    print(F"Rok {rok} jest zwykły")
elif rok % 100 != 0:
    print(F"Rok {rok} jest przestępny")
elif rok % 400 != 0:
    print(F"Rok {rok} jest przestępny")
else:
    print(F"Rok {rok} jest przestępny")
if rok <= 1582:
    print("Rok nie jest Gregoriański!!")

