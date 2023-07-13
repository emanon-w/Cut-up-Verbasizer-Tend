import random

x = input("Quante frasi vuoi usare?")
numero_frasi = x

lista = []
for i in range(int(x)):
    testo = input("Inserisci una frase: ")
    parole_mischiate = testo.split()
    lista.extend(parole_mischiate)  

random.shuffle(lista)
print(lista)