slowo_uzytkownika = input("Podaj słowo: ")
slowo_uzytkownika = slowo_uzytkownika.upper()

slowo_bez_samoglosek = ""

for litera in slowo_uzytkownika:
    if litera in "AEIOU":
        continue
    slowo_bez_samoglosek += litera

print("Słowo bez samogłosek:", slowo_bez_samoglosek)
