class  ExamException(Exception):
    pass


class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
        #Controllo esistenza e leggibilità
        try: 
            with open(self.name, 'r') as f:
                f.readline()
        except Exception:
            raise ExamException('Errore: ill file non esiste o non è leggibile')
            

    
    def get_data(self):
        data = []

        try:
            with open(self.name, 'r') as file:
                # Salto l'intestazione
                next(file)
                for riga in file:
                    elementi = riga.strip().split(",")
                    if len(elementi) < 2: continue # Salto righe malformate

                    date = elementi[0]
                    temp_str = elementi[1]

                    try:
                        temp = float(temp_str)
                        #Controllo se negativo o nullo come richiesto
                        if temp <= 0: continue
                    except ValueError:
                        continue

                    data.append([date, temp])
        except Exception as e:
            raise ExamException(f'Errore durante la lettura: {e}')
        
        return data

def compute_variations(time_series, first_year, last_year, N):
    # Controllo lunghezza intervallo
    if (N >= (last_year - first_year + 1)):
        raise ExamException('Il valore della finestra N non è accettabile')
    years = {}
    for elemento in time_series:
        year = int(elemento[0].split("/")[0])
        temp = elemento[1]
        
        if first_year <= year <= last_year:
            if year not in years:
                years[year] = []
            
            years[year].append(temp)

    avg = {}

    for year, values in years.items():
        # nel metodo get_data ho saltato i mesi con misurazioni non valide
        # facendo len(values) avrò il numero corretto di misurazioni disponibili!
        avg[year] = sum(values)/len(values)  
    
    variations = {}

    for current_year in range(N + first_year, last_year + 1):
        check_years = True
        temp_sum = 0
        for i in range(1, N+1):
            prev_year = current_year - i
            if prev_year in avg:
                temp_sum += avg[prev_year]
            else:
                check_years = False
                break
        if check_years and current_year in avg:
            mean = temp_sum/N
            variations[str(current_year)] = avg[current_year] - mean
    
    return variations






time_series_file = CSVTimeSeriesFile(name='modulo1/GlobalTemperatures.csv')
time_series = time_series_file.get_data()
#print(time_series)