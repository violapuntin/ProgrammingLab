def conta(parola, lettera):
    conta=0
    for l in parola:
        if(l==lettera):
            conta += 1
    return conta

parola = input()
lettera = input()
print(conta(parola,lettera))

#lettera = lettera.upper() la funzione upper rende tutti i caratteri in maiuscolo
#parola = parola.lower()  la funzione lower rende tutti i caratteri in minuscolo (no maiuscole)

#for idx, item in enumerate(parola):
#   print(idx, item)        conta l'indice