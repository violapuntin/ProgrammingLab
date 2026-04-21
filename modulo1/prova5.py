class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        try:
            with open(name, 'r') as f:
                f.readline()
        except:
            raise ExamException("Errore: impossibile aprire o leggere il file")
        self.name = name
    
    def get_data(self):
        data = []
        with open(self.name, 'r') as file:
            # Salto l'intestazione
            next(file)

            for riga in file:
                elementi = riga.strip().split(";")
                if len(elementi) < 3:
                    continue
                
                date = str(elementi[0])
                try:
                    land_max_temp = float(elementi[1])
                    land_min_temp = float(elementi[2])
                except:
                    continue
                if land_min_temp < -50 or land_max_temp > 50:
                    continue
                if land_min_temp > land_max_temp:
                    print(f' I valori scartati sono: [{land_min_temp}, {land_max_temp}]')
                    continue
                data.append([date, land_min_temp, land_max_temp])
        return data

def compute_monthly_spread_diff(time_series, first_year, second_year):
    if not isinstance(first_year, int) or not isinstance(second_year, int) or second_year <= first_year:
        raise ExamException("Errore: anni non validi (devono essere interi e in ordine crescente)")
    
    spread = {}

    dict_1 = {}
    dict_2 = {}
    for elemento in time_series:
        year = int(elemento[0].split("-")[0])
        if year == first_year:
            month = int(elemento[0].split("-")[1])
            dict_1[month] = (elemento[2]-elemento[1])
        if year == second_year:
            month = int(elemento[0].split("-")[1])
            dict_2[month] = (elemento[2]-elemento[1])
    if not dict_1 or not dict_2:
        raise ExamException("Errore: gli anni indicati non rientrano nella copertura del dataset")
    for i in range (1,13):
        if i in dict_1 and i in dict_2:
            spread[i] = (dict_2[i] - dict_1[i])
        else:
            print(f'La variazione per il mese {i} non può essere calcolata')
    if not spread:
        raise ExamException("Errore: nessun mese confrontabile tra gli anni indicati")

    return spread


if __name__ == "__main__":
    time_series_file = CSVTimeSeriesFile(name="modulo1/GlobalTemperaturesMaxMin.csv")
    data = time_series_file.get_data()
    print(compute_monthly_spread_diff(data, 2017, 2018))
