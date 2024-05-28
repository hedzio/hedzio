try:
    data_urodzenia = int(input("Podaj swoją datę urodzenia: "))
except ValueError: 
    print("TYLKO LICZBY CAŁKOWITE BEZ PRZERW !!!")
else:
    lista = []
    lista.append(data_urodzenia)
    pusta_lista = []
    
    for element in lista:
        for x in len(element):
            print(x)
