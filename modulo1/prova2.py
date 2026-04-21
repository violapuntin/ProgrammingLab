import os

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name = name
        
        if not os.path.exists(self.name):
            raise ExamException('Errore: impossibile aprire il file')
        
        try:
            with open(self.name, 'r') as f:
                test = f.readline()
                if not test:
                    raise ExamException('Errore: il file è vuoto o non contiene dati validi')
        except ExamException:
            raise #rilancia il nostro errore sul file vuoto
        except:
            # Cattura tutto il resto (permessi, errori  disco, ecc.)
            raise ExamException ('Errore: il file è vuoto o non contiene dati validi')
    
    def get_data(self, country):
        data = []
        with open(self.name, 'r') as file:
            # Salto l'intestazione
            next(file)
    
            for riga in file:
                elementi = riga.strip().split(",")
                if len(elementi) < 3:
                    continue
                if elementi[2] == country:
                    date = str(elementi[0])
                    try:
                        temp = float(elementi[1])
                    except:
                        continue
                    data.append([date, temp])
        
        # Se la lista è vuota, il paese non è stato trovato
        if not data:
            raise ExamException("Errore: il nome del paese non è presente nel file")

        return data

def mean_time_series(time_series, first_year, last_year):
    
    if not(isinstance(first_year, int)) or not(isinstance(last_year, int)):
        raise ExamException("Errore: l'anno inserito non è un intero")

    dict = {}
    for elemento in time_series:
        year = int(elemento[0].split("-")[0])
        if first_year<=year<=last_year:
            temp = elemento[1]

            if year not in dict:
                dict[year] = []
            
            dict[year].append(temp)
    
    dict_mean = {}
    for year, values in dict.items():
        dict_mean[year] = sum(values)/len(values)
    
    return(dict_mean)

def compute_variations(time_series_1, time_series_2, first_year, last_year):
    dict = {}
    dict1 = mean_time_series(time_series_1, first_year, last_year)
    dict2 = mean_time_series(time_series_2, first_year, last_year)

    if not dict1 or not dict2:
        raise ExamException("Errore: l'intervallo selezionato non contiene valori  validi")

    for year in range(first_year, last_year + 1):
        if year not in dict1 or year not in dict2:
            continue

        dict[str(year)] = dict2[year] - dict1[year]
    if not dict:
        raise ExamException("Errore: l'intervallo selezionato non contiene valori validi")

    return dict


if __name__ == "__main__":
    time_series_file = CSVTimeSeriesFile(name='modulo1/GlobalLandTemperaturesByCountry.csv')
    time_series_italy = time_series_file.get_data(country="Italy")
    time_series_france = time_series_file.get_data(country="France")

    #veriations_italy_france = compute_variations(time_series_italy, time_series_france, 1990, 2000)
    #print(veriations_italy_france)

    # --- Test per la Lode --- [cite: 54]
    def test_compute_variations():
        # 1. Creazione serie di esempio [cite: 56]
        ts1 = [["1900-01-01", 10.0], ["1900-02-01", 12.0], ["1901-01-01", 15.0]]
        ts2 = [["1900-01-01", 15.0], ["1900-02-01", 17.0], ["1901-05-01", 20.0]]
        
        # Valori attesi:
        # 1900: media ts2 (16.0) - media ts1 (11.0) = 5.0
        # 1901: media ts2 (20.0) - media ts1 (15.0) = 5.0
        expected = {"1900": 5.0, "1901": 5.0}
        
        try:
            # 2. Chiamata funzione [cite: 57]
            result = compute_variations(ts1, ts2, 1900, 1901)
            
            # 3. Confronto [cite: 58]
            if result == expected:
                print("Test superato: i risultati corrispondono!") # [cite: 59]
            else:
                print(f"Test fallito: atteso {expected}, ottenuto {result}")
        except Exception as e:
            print(f"Test fallito con errore: {e}")

    # Esecuzione del test
    test_compute_variations()