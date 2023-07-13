import random

global gruppo_frasi
global parole

gruppo_frasi = []
parole = []

print(" ".join(gruppo_frasi))

parola1 = input("Inserisci una parola:")
gruppo_frasi.append(parola1) 
random.shuffle(gruppo_frasi)
print(" ".join(gruppo_frasi))
