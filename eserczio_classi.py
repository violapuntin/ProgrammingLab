#ESERCIZIO 1
'''
import random

class Coin():

    def __init__(self, faccia):
        self.faccia = faccia
    
    def lanciare(self):
        if random.randint(0,1) == 0:
            self.faccia = 'Testa'
        else:
            self.faccia = 'Croce'

    def che_faccia(self):
        return self.faccia


moneta = Coin('Testa')
moneta.lanciare
print(moneta.che_faccia)
'''
#ESERCIZIO 2
'''
class Veicolo():
    def __init__(self, modello, marca, anno):
        self.modello = modello
        self.marca = marca
        self.anno = anno
        self.speed = 0
    
    def __str__(self):
        return f'Marca: {self.marca}\n Modello: {self.modello}\n Anno: {self.anno}\n Velocita: {self.speed}'
    
    def accellerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5
    
    def get_speed(self):
        return self.speed
'''
#ESERCIZIO 3

class CSVFile():

    def __init__(self, name):
        self.name = name
        if (type(self.name) != str):   #oppure if  not isinstance(name, str):
            raise TypeError('Errore: il nome inserito non è una stringa')
        
        try:
            type(self.name) == str
        except TypeError:
            print('Errore: il nome inserito non è una stringa')

        #se metto il try nell'init:
        try:
            with open(self.name, 'r') as file:
                file.readline
        except FileNotFoundError: 
            print('self.name = None')
        
    
    def get_data(self, start = None, end = None):
        if(type(start)!=int or start!=None):
            raise TypeError('start non è un intero')
        if(type(end)!=int or end!=None):
            raise TypeError('end non è un intero')
        if (start > end):
            raise ValueError('Start è maggiore di end')
        if(start < 0):
            raise ValueError('start è minore di zero')
        
        #creo una lista vuota
        data = []
        if(start != None and end != None):
            try:
                #apro il file CSV
                file = open(self.name, 'r')
                numero_righe = sum(1 for _ in file)
                if(end>numero_righe):
                    raise ValueError('end è maggiore del numero di righe')
                #leggo le righe
                
                for i,line in enumerate(file):
                    if(i<start or i>=end):
                        continue
                    line = line.strip() #rimuove spazi e \n
                    data.append(line.split(','))
            
                #chiudo il file CSV
                file.close()
            
                return data
            except FileNotFoundError:  #posso scegliere se scrivere FileNotFoundError oppure no
                print("Errore: file non trovato")
        elif (start != None):
            try:
                #apro il file CSV
                file = open(self.name, 'r')
                #leggo le righe
                for i,line in enumerate(file):
                    if(i<start):
                        continue
                    line = line.strip() #rimuove spazi e \n
                    data.append(line.split(','))
            
                #chiudo il file CSV
                file.close()
            
                return data
            except FileNotFoundError:  #posso scegliere se scrivere FileNotFoundError oppure no
                print("Errore: file non trovato")
        else:
            try:
                #apro il file CSV
                file = open(self.name, 'r')
                #leggo le righe
                for line in file:
                    if(i<start):
                        continue
                    line = line.strip() #rimuove spazi e \n
                    data.append(line.split(','))
            
                #chiudo il file CSV
                file.close()
            
                return data
            except FileNotFoundError:  #posso scegliere se scrivere FileNotFoundError oppure no
                print("Errore: file non trovato")
            


class NumericalCSVFile (CSVFile):
    '''
    Non sevre che lo scrivo perchè in automatico prende tutto dalla classe madre
    def __init__(self):
        super().__init__(self.name)
    '''

    def get_data():
        data = super().get_data

        new_data = []

        for row in data:
            try:
                number = float(row[1])
                new_data.append([row[0], number])
            except:
                print("Errore nella riga:", row)

        return new_data

#ESERCIZIO 4
'''
class Canguro():

    def __init__(self, contenuto_tasca=[]):  #Mai mettere oggetti che puntano alla stessa lista
        self.contenuto_tasca = contenuto_tasca
        
    def intasca(self, obj):
        self.contenuto_tasca.append(obj)
    
    def __str__(self):
        return f'Contenuto tasca: {self.contenuto_tasca}'

can = Canguro()
guro = Canguro()
can.intasca('wallet')
print(can)  #stampa wallet
print(guro) #stampa wallet
'''
