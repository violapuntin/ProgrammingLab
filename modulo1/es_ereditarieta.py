#ESERCIZIO 1
'''
class Persona():
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
    
    def saluta(self):
        print('Ciao sono', self.ruolo + ",", self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, corso=None):
        super().__init__("Studente UNITS", nome, cognome)
        if corso is None:
            self.corso = []
        else:
            self.corso = corso
    
    def saluta(self):
        #Persona.saluta(self)
        super().saluta()
        print("> Frequento il corso: ", self.corso)

class Docente(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = corso
    
    def saluta(self):
        Persona.saluta(self)
        print("> Docente del corso: ", self.corso)

corsi = ["Programmazione", "Laboratorio", "Analisi"]

obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()

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

class Auto(Veicolo):
    def __init__(self, modello, marca, anno, numero_porte):
        super().__init__(modello, marca, anno)
        self.numero_porte = numero_porte
    
    def __str__(self):
        return f'Marca: {self.marca}\n Modello: {self.modello}\n Anno: {self.anno}\n Velocita: {self.speed}\n Numero Porte: {self.numero_porte}'

class Moto(Veicolo):
    def __init__(self, modello, marca, anno, tipo):
        super().__init__(modello, marca, anno)
        self.tipo = tipo

    def __str__(self):
        return f'Marca: {self.marca}\n Modello: {self.modello}\n Anno: {self.anno}\n Velocita: {self.speed}\n Tipo: {self.tipo}'

Kymcho = Auto("Kymcho", "Agility", 2024, 4)
print(Kymcho)
'''

#ESERCIZIO 3
'''
class Persona():
    def __init__(self, ruolo, nome, cognome):
        self.ruolo = ruolo
        self.nome = nome
        self.cognome = cognome
    
    def saluta(self):
        print('Ciao sono', self.ruolo + ",", self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, corso=None):
        super().__init__("Studente UNITS", nome, cognome)
        if corso is None:
            self.corso = []
        else:
            self.corso = corso
    
    def saluta(self):
        Persona.saluta(self)
        print("> Frequento il corso: ", self.corso)

    def docente(self, Docente):
        check = 1
        for elem in Docente.corso:
            if elem not in self.corso:
                check = 0
                break
        if check:
            return True
        else: return False
    
    def esiste_docente(self, lista_docenti = None):
        if lista_docenti is None:
            self.lista_docenti = []
        else:
            self.lista_docenti = lista_docenti
        
        trovato = False
        for doc in lista_docenti:
            if self.docente(doc): 
                print("Okay")
                trovato = True
                break
        if (trovato == False): print("Non esiste") 



class Docente(Persona):
    def __init__(self, nome, cognome, corso):
        super().__init__("Docente UNITS", nome, cognome)
        self.corso = corso
    
    def saluta(self):
        Persona.saluta(self)
        print("> Docente del corso: ", self.corso)

corsi = ["Programmazione", "Laboratorio", "Analisi"]
corsi2 = ["Programmazione", "Laboratorio", "Analisi", "Algebra"]

obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()
obj_Mario = Docente("Mario", "Grande", corsi2)
obj_Mario.saluta()
obj_Carlo = Docente("Carlo", "Vale", corsi)
lista_docenti=[obj_Carlo, obj_Mario]
print(obj_Irene.docente(obj_Carlo))
print(obj_Irene.esiste_docente(lista_docenti))
'''

#ESERCIZIO 4
class Poligono():
    def __init__(self, n_lati):
        self.n_lati = n_lati
    
    def __str__(self):
        return f'Sono un poligono con {self.n_lati} lati\n'

class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)
    
    def __str__(self):
        return f'Sono un quadrilatero\n'

class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init()
        self.base = base
        self.altezza = altezza
    def __str__(self):
        return super().__str__() + f'Base: {self.base}, Altezza: {self.altezza}\n'
    
    def area(self):
        return self.base*self.altezza
    def perimetro(self):
        return 2*(self.base + self.altezza)
    
class Triangolo(Poligono):
    def __init__(self, lat1, lat2, lat3):
        super().__init(3)
        self.lat1 = lat1
        self.lat2 = lat2
        self.lat3 = lat3

    def __str__(self):
        return f'Lato 1: {self.lat1}, lato 2: {self.lat2}, lato 3: {self.lat3}\n'
    
    def perimetro(self):
        return self.lat1 + self.lat2 + self.lat3
    
    def is_equilatero(self):
        if (self.lat1 == self.lat2 == self.lat3):
            return True
        else: return False