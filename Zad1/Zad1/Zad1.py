#1a

def funkcja1a(imie1,imie2,imie3,imie4,imie5):
    print(imie1, imie2, imie3, imie4, imie5)

funkcja1a("Magda","Justyna","Wiktoria","Julia","Agnieszka")


#1b

def funkcja1b1(l1,l2,l3,l4,l5):
    lista = [l1,l2,l3,l4,l5]
    wynik = []
    for liczba in lista:
        liczba = liczba *2
        wynik.append(liczba)
    print(wynik)
    
funkcja1b1(3,4,5,6,7)

def funkcja1b2(l1,l2,l3,l4,l5):
    lista = [l1,l2,l3,l4,l5]
    wynik = [liczba*2 for liczba in lista]
    print(wynik)

funkcja1b2(3,4,5,6,7)
    
#1c
lista1 = list(range(0,10,1))
def funkcja1c(lista1):
    wynik =[]
    for i in lista1:
        if i%2 == 0:
            wynik.append(i)
    print(wynik)

funkcja1c(lista1)

#1d
lista2 = list(range(0,10,1))

def funkcja1d(lista2):
    codrugi = [lista2[index] for index in range(0,len(lista2),2)]
    print(codrugi)

funkcja1d(lista2)     

