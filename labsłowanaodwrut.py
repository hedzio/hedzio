slowo = input("Podaj słowo: ")
slowo = slowo.lower()
lista = []
lista.append(slowo)

for i in range(len(lista)):
    if slowo[i] == slowo[len(slowo) - i - 1]:
        print(True)
    else:
        print(False)
