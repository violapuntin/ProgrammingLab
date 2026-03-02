def conta(parola, lettera):
    conta=0
    for l in parola:
        if(l==lettera):
            conta += 1
    return conta

parola = input()
lettera = input()
print(conta(parola,lettera))