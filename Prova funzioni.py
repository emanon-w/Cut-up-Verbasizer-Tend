import random

testo1 = input("Inserisci una frase:")
testo2 = input("Aggiungi un nuovo input:")
testo3 = input("Aggiungi altri elementi alla lista:")

Verbasize1 = testo1.split()
Verbasize2 = testo2.split()
Verbasize3 = testo3.split()

random.shuffle(Verbasize1)
random.shuffle(Verbasize2)
random.shuffle(Verbasize3)

lista1 = Verbasize1 + Verbasize2 + Verbasize3
lista2 = ["cazzo"]

lista1.extend(lista2)

random.shuffle(lista1)

print (lista1)
