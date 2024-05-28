def trojkat_prostokatny():
    bok_a = float(input("Podaj długość pierwszego boku:"))
    bok_b = float(input("Podaj długość drugiego boku:"))
    bok_c = float(input("Podaj długość trzeciego boku:"))
    if (bok_a**2 + bok_b**2) == bok_c**2:
        print("Jest to trójkąt prostokątny")
    elif (bok_c**2 + bok_a**2) == bok_b**2:
        print("Jest to trójkąt prostokątny")
    elif (bok_c**2 + bok_b**2) == bok_a**2:
        print("Jest to trójkąt prostokątny")
    else:
        print("nie jest to trójkat prostokatny")
trojkat_prostokatny()