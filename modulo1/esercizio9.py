def conta_vocali(parola):
    conta=0
    vocali = ["a", "e", "i", "o", "u"]
    #vocali="aeiou"
    for l in parola:
        if l in vocali:
            conta += 1
    return conta

x = input()
print(conta_vocali(x))