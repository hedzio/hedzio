moja_lista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
nowa_lista = []

for liczba in moja_lista:
    if liczba  not in nowa_lista:
        nowa_lista.append(liczba)

print("Lista tylko z unikalnymi elementami:")
print(nowa_lista)
