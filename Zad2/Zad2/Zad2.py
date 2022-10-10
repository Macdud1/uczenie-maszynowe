#1

def funkcja1 (name: str, surname: str)-> str:
    wynik =f"Cześć {name} {surname}!"
    print(wynik)

funkcja1("Maciej","Duda")

#2

def funkcja2 (l1: int, l2: int):
    wynik = l1 * l2
    print(wynik)

funkcja2(3,5)

#3

def funkcja3 (l3)-> bool:
    if l3%2 == 0:
        return True
    else:
        return False

zm = funkcja3(6)

if (zm == True):
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")

#4

def funkcja4 (l1: int, l2: int, l3: int)-> bool:
    if l1 + l2 >= l3:
        return True
    else:
        return False 

zm2 = funkcja4(1,2,3)
print(zm2)

#5
lista1 = [1,2,3]
def funkcja5 (lista1: list, l1: int)-> bool:
    if l1 in lista1:
        return True
    else:
        return False

zm3 = funkcja5(lista1, 3)
print(zm3)

#6
lista2 = [1,2,3]
lista3 = [3,4,5]

def funkcja6(lista2: list, lista3: list)-> list:
    sumalist = lista2 + lista3
    sumalist = set(sumalist)
    wynik = []
    for i in sumalist:
        i = i**3
        wynik.append(i)
    return wynik

print(funkcja6(lista2, lista3))