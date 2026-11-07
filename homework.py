total = 0
continua = "da"
for i in range(100):
    if continua == "da":
        produs = input("Introdu produsul sau stop: ")
        if produs == "mere":
            total = total + 5
        elif produs == "paine":
            total = total + 7
        elif produs == "lapte":
            total = total + 12
        elif produs == "ciocolata":
            total = total +15
        elif produs == "stop":
            continua = "nu"
        else:
            print("Produs inexistent!")
reducere = 0
if total > 100:
    reducere = total * 0.10
print("Total:", total, "lei")
print("Reducere:", reducere, "lei")
print("Suma finala:", total - reducere, "lei")
print("Ai economisit:", reducere, "lei")