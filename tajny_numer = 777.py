tajny_numer = 777
print(
"""
+================================+
| Witaj w mojej grze, mugolu!    |
| Wprowadź liczbę całkowitą      |
| i zgadnij, jaki numer          |
| wybrałem dla ciebie.           |
| Jaki jest więc sekretny numer? |
+================================+
""")
uzytkowik = int(input("Podaj liczbę całkowitą:"))
while True:
    uzytkowik = int(input("Podaj liczbę całkowitą:"))
    if tajny_numer == uzytkowik:
        print(tajny_numer)
        print("Dobra robota! To numer, który wybrałem dla ciebie! Jesteś teraz wolny.")
    elif tajny_numer != uzytkowik:
        print("Nie, to nie jest ta liczba, którą wybrałem dla ciebie. Spróbuj ponownie!")