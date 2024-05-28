
slowo1 = input("Podaj słowo: ").lower()
slowo2 = input("Podaj drugie słowo: ").lower()

sorted_slowo1 = sorted(slowo1)
sorted_slowo2 = sorted(slowo2)

if sorted_slowo1 == sorted_slowo2:
    print(True)
else:
    print(False)
