sold = 500
optiune = 0

while optiune != 4:
    print("\n===== ATM MAIB =====")
    print("1. Sold curent")
    print("2. Depunere")
    print("3. Extragere")
    print("4. Iesire")

    optiune = int(input("Alege optiunea: "))

    if optiune == 1:
        print("Soldul curent este:", sold, "lei")
    elif optiune == 2:
        suma = float(input("Introduceti suma pentru depunere: "))
        if suma > 0:
            sold = sold + suma
            print()
            print("Depunere reusita!")
            print()
            print("Soldul nou este:", sold, "lei")
        else:
            print("Suma invalida")
    elif optiune == 3:
        suma = float(input("Introduceti suma pentru extragere: "))
        if suma > 0 and suma <= sold:
            sold = sold - suma
            print()
            print("Extragere reusita!")
            print()
            print("Soldul nou este:", sold, "lei")
        else:
            print("Suma invalida sau fonduri insuficiente")

    elif optiune == 4:
        print("Va multumim! La revedere!")
    else:
        print("Optiune invalida!")
