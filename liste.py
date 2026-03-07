#ESERCIZIO 1
#Scrivere una funzione che sommi tutti gli elementi di una lista
def sum_elements(list):
    sum = 0
    for i in list:
        sum += i
    return sum

#return sum(lista) è già una funzione
#ESERCIZIO 2
#SCrivere una funzione che prenda in input una stringa e ritorna TRue se è palindromo, False altrimenti
def is_palindromo(stringa):
    invert = stringa[::-1]
    if (invert == stringa):
        return True
    return False
#return invert == stringa
#return stringa == stringa[::-1]

#ESERCIZIO 3
#Definire una funzione che prende in input una lista A, indici i, j, e scambi il valore A[i] con A[j]
def scambia(lista, i, j):
    tmp = lista[i]
    lista[i] = lista[j]
    lista[j]=tmp

#A[i], A[j] = A[j], A[i]

#ESERCIZIO 4
#Scrivere una funzione che prende in input due liste e ritorna TRUE se le due liste hanno almento un elemento in comune
def comune(list1, list2):
    for i in list1:
        if(i in list2):
            return True
    return False

#ESERCIZIO 5
#Definire una funzione che prende in input una lista di numeri interi in [0,9] e ritorni una lista di stringhe, corrispondenti ai numeri scritti in italiano
def crea_lista(lista):
    new_list = []
    number = ["zero","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    for elem in lista:
        new_list.append(number[elem])
    return new_list

def numeri_parole(my_list):
    my_dict = { 0: 'Zero', 1: 'Uno', 2: 'Due', 3: 'Tre', 4: 'Quattro', 5: 'Cinque', 6: 'Sei', 7: 'Sette', 8: 'Otto', 9: 'Nove'}
    risultato_nomi = [] #lista dove salvare i nomi
    for numero in my_list:
        nome_corrisp = my_dict[numero]
        risultato_nomi.append(nome_corrisp) #aggiunge il nome alla lista      
    return risultato_nomi

#ESERCIZIO 6
def ex1(A):
    my_dict = {}
    for elem in A:
        if elem in my_dict:
            my_dict[elem] +=1
        else:
            my_dict[elem] = 1
    return my_dict

#es di Mattia
def cout_words(l: list) -> dict:
    #l_lower = [i.lower() for i in l]
    l_lower = []
    for i in l:
        l_lower.append(i.lower())

    l_set = set(l_lower)  #set mi da una lista dove sonp stati rimossi tutti i duplicati

    #l_dict = {i: 0 for i in l_set}
    l_dict = dict()  #oppure l_dict = {}
    for i in l_set:
        l_dict[i] = 0
    
    for word in l_lower:
        if word in l_dict.keys():
            l_dict[word] += 1
    return l_dict

inp = "First Citizen: Before we proceed any further, hear me speak. All Speak, speak. First Citizen".split(" ")
print(cout_words(inp))

#ESERCIZIO 7
def somma(file):
    totale=0
    my_file=open(file, 'r')
    next(my_file)
    for line in my_file:
        data, vendite=line.split(",")
        totale+=float(vendite)
    my_file.close()
    return totale


print(somma('shampoo_sales.txt'))

#ESERCIZIO 8
def somma(file,parola):
    with open(file,'r') as file:
        tot=0
        for line in file:
            if parola in line:
                tot+=1
    return tot

print(somma('shampoo_sales.txt','Sales'))

#ESERCIZIO 9
def conteggio(file):
    dizionario = dict()

    with open(file, 'r') as file:
        for row in file:
            linea = row.split()

            for word in linea:
                if word.lower() not in dizionario:
                    dizionario[word.lower()] = 1
                else:
                    dizionario[word.lower()] += 1

    return dizionario

#ESERCIZIO 10
def del_duplicate(file):
    nuovo_file = open("unique.txt", 'w')
    copia = []
    #caratteri_speciali = []

    with open(file, 'r') as file:
        for row in file:
            if row in copia:
                next
            else:
                copia.append(row)

    for frase in copia:
        nuovo_file.write(frase)

    nuovo_file.close()