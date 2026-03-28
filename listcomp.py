#Esercizio 1
'''
Input = [0,1,2,3,4,5,6,7,8]
# Input = [i for i in range(9)]

def f(X):
    return [x for x in X if x%2!=0]

print(f(Input))
'''
#Esercizio 2
'''
Input = [[1,2,3], [4,5], [6,7,8,1]]

def f(matrix):
    return [elem for lista in matrix for elem in lista]
    #se volessi solo quelli pari
    return [elem for lista in matrix for elem in lista if elem%2==0]

print(f(Input))
'''
#Esercizio 3
'''
lista_a = [1,3,5,7]
lista_b = [2,4,6]

def f(list1, list2):
    return [elem1*elem2 for elem1 in list1 for elem2 in list2 if elem1*elem2 >10]

print(f(lista_a, lista_b))
'''
#Esercizio 4
'''
def f(a,b,c):
    ipo = max(a,b,c)
    if(a == ipo):
        if(a**2 == b**2 + c**2):
            return True
    if(b == ipo):
        if(b**2 == a**2 + c**2):
            return True
    if(c == ipo):
        if(c**2 == b**2 + a**2):
            return True
    return False

lista = [i for i in range(1,21)]
def g(list):
    return [[a,b,c] for a in list for b in list for c in list if(f(a,b,c))]

print(g(lista))
'''
#Esercizio 5
'''
lista_a = [0,1,3,4]
lista_b = ['a','b','c']
def f(list1, list2):
    return [[a,b] for a in list1 for idx,b in enumerate(list2) if(a%2==0 and idx%2!=0)]

print(f(lista_a, lista_b))
'''
#Esercizio 8
'''
sentence = 'the cat sat on the mat the cat'
lista = sentence.plit(" ")
def f(list):
    return {word: list.count(word) for word in list}

print(f(lista))
'''
