# def factorial(num:int) -> int:  significa che mi aspetto un output intero
def factorial(num: int): #faccio una richiesta particolare e dico che mi aspetto che venga un intero, una sorta di tipizzazione
    prod=1
    for i in range(num):
        prod = prod*(num-i)
    return prod

x=int(input())
print(factorial(x))