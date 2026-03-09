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
        Persona.saluta(self)
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
        if (Docente.corso == self.corso): return True
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
