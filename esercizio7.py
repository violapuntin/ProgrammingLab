def factorial(num):
    prod=1
    for i in range(num):
        prod = prod*(num-i)
    return prod

x=int(input())
print(factorial(x))