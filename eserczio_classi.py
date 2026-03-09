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
'''
class CSVFile():

    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        #creo una lista vuota
        data = []

        #apro il file CSV
        file = open(self.name, 'r')

        #leggo le righe
        for line in file:
            line = line.strip() #rimuove spazi e \n
            data.append(line.split(','))
        
        #chiudo il file CSV
        file.close()
        
        return data
'''
#ESERCIZIO 4
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

