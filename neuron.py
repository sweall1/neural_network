import math

rty = input('Jeżeli chcesz wybrać plik "bramka_and" wpisz 1, jeżeli chcesz podać własne dane, wpisz 2: ')
lista = []
if rty == "1":
    dane = []
    f = open('bramka_and.txt', "r")
    for line in f:
        dane.append(line.strip('\n'))

    x1 = []
    x2 = []
    d = []
    w = [-2, 3]
    bias = -6

    for x in range(4):
        qwe = dane[x + 1]
        x1.append(qwe[0:1])
    for x in range(4):
        qwe = dane[x + 1]
        x2.append(qwe[2:3])
    for x in range(4):
        qwe = dane[x + 1]
        d.append(qwe[4:5])

    print("DANE:\nX1:", x1, ", X2:", x2, ", W:", w, ", D:", d, ", BIAS:", bias)

    for i in range(4):
        suma = int(x1[i]) * int(w[0]) + int(x2[i]) * int(w[1]) + 1 * int(bias)
        lista.append(suma)
    print("wyniki:", lista)

elif rty == "2":
    ilo = int(input("Podaj liczbę wejść neuronu: "))

    xx = []
    ww = []
    for i in range(ilo):
        wektor = input("Twój {} element wektora wynosi: ".format(i))
        xx.append(wektor)

    for i in range(ilo):
        wektor = input("Twój {} element wagi wynosi: ".format(i))
        ww.append(wektor)

    biass = int(input("Podaj wartość progową BIAS: "))

    sumaa = 0
    for i in range(ilo):
        sumaa += int(xx[i]) * int(ww[i]) + 1 * biass
    lista.append(sumaa)

switch = input(
    "Wybierz funkcję aktywacji:\n1. Dyskretna Unipolarna 2. Dyskretna Bipolarna 3. Ciągła Unipolarna 4. Ciągła Bipolarna: ")

lista2 = []
if switch == "1":
    for x in range(len(lista)):
        if lista[x] >= 0:
            lista2.append(1)
        else:
            lista2.append(0)

elif switch == "2":
    for x in range(len(lista)):
        if lista[x] >= 0:
            lista2.append(1)
        else:
            lista2.append(-1)


elif switch == "3":
    for x in range(len(lista)):
        wynik = (1 / (1 + math.pow(math.e, -lista[x])))
        lista2.append(wynik)


elif switch == "4":
    for x in range(len(lista)):
        wynik2 = (2 / (1 + math.pow(math.e, -lista[x]))) - 1
        lista2.append(wynik2)

print("Wynik to Y= ", lista2)