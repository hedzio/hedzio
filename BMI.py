def Bmi():
    wzrost = float(input("Podaj swój wzrost (w metrach): "))
    waga = float(input("Podaj swoją wagę (w kilogramach): "))
    if wzrost > 2.5 or wzrost <= 0:
        print("Nieprawidłowy wzrost.")
    elif waga <= 0:
        print("Nieprawidłowa waga.")
    else:
        Bmi = waga / wzrost ** 2
        print("Twoje BMI to: ", Bmi)
Bmi()