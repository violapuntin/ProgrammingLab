def pari(num):
    if(num%2==0):
        return f"{num} è pari"
    return f"{num} è dispari"

x = int(input())
print(pari(x))