class ExamException(Exception): 
    pass

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name
    
    def get_data(self):

        try:
            file = open(self.name, 'r')
        except:
            raise ExamException("Errore apertura file")
        
        righe = file.readlines()
        data = []

        for riga in righe:
            if riga.startswith("date"):
                continue
        
            elementi = riga.strip().split(",")

            if len(elementi) < 2:
                continue

            date = elementi[0]
            passengers = elementi[1]

            try:
                passengers = int(passengers)
            except:
                print("Valore non valido, salto riga")
                continue

            data.append([date, passengers])

        file.close()
        return data 


def compute_variations(time_series, first_year, last_year):

    years = {}

    # 1. Raggruppa TUTTI i dati per anno
    for elemento in time_series:
        date = elemento[0]
        passengers = elemento[1]

        year = date.split("-")[0] #Separa la data tramite "-" e isola l'elemento all'indice 0 (anno)

        if year not in years:
            years[year] = []
        
        years[year].append(passengers)

    # 2. Filtra gli anni nell'intervallo richiesto
    filtered_years = {}

    for year in years:
        if first_year <= year <= last_year:
            filtered_years[year] = years[year]
    
    # 3. Calcola la media per ogni anno filtrato
    avg = {}

    for year in filtered_years:
        values = filtered_years[year]

        if len(values) == 0:
            continue

        avg[year] = sum(values) / len(values)
    
    # 4. Calcola le differenze tra anni consecutivi
    result = {}

    anni_ordinati = sorted(avg.keys())

    for i in range(1, len(anni_ordinati)):
        prev = anni_ordinati[i-1]
        curr = anni_ordinati[i]

        diff = avg[curr] - avg[prev]

        key = prev + "-" + curr
        result[key] = diff
        
    return result

file = CSVTimeSeriesFile("data.csv")
time_series = file.get_data()

risultato = compute_variations(time_series, "1949", "1955")

print(risultato)


