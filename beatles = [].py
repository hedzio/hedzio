beatles = []
print("Krok 1:", beatles)

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Krok 2:", beatles)
for i in range(1):
    dodanie = input("Dodaj członka zespołu:")
    beatles.append(dodanie)
for i in range(1):
    dodanie = input("Dodaj drugiego zespołu:")
    beatles.append(dodanie)
print("Krok 3:", beatles)

del beatles[-2:]
print("Krok 4:", beatles)

beatles.insert( 0,"Ringo Starr")
print("Krok 5:", beatles)


# Sprawdzanie długości listy.
print("The Fab", len(beatles))