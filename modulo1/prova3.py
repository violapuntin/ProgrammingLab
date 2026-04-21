import os

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self, city):
        # Controllo esistenza file richiesto (2 punti) 
        if not os.path.exists(self.name):
            raise ExamException("Errore: il file non esiste")
        data = []
        try:
            with open(self.name, 'r') as file:
                next(file)
                for riga in file:
                    elementi = riga.strip().split(",")

                    if elementi[3] == city:
                        date = str(elementi[0])
                        try:
                            temp = float(elementi[1])
                        except:
                            continue

                        data.append([date, temp])
        except Exception as e:
            if not isinstance(e, ExamException):
                raise ExamException(f"Errore durante la lettura: {e}")
            raise e

        # Eccezione se città non presente (2 punti) 
        if not data:
            raise ExamException("Errore: il nome della città non è presente nel file")
            
        return data

def compute_slope(time_series, first_year, last_year):

    if not isinstance(first_year, int) or not isinstance(last_year, int):
        raise ExamException("Errore: first_year e/o last_year non sono interi")
    
    if first_year > last_year:
        raise ExamException("Errore: first_year > last_year")


    temp_dict = {}
    for elemento in time_series:
        year = int(elemento[0].split("-")[0])
        if first_year<=year<=last_year:
            if year not in temp_dict:
                temp_dict[year] = []
            
            temp_dict[year].append(elemento[1])
    avg = {}
    for year, values in temp_dict.items():
        if len(values) < 6:
            continue
        avg[year] = sum(values)/len(values)
    
    n = len(avg)
    if n ==0:
        raise ExamException("Erore: n è uguale a zero")
    mean_year = sum(avg.keys())/n
    mean_temp = sum(avg.values())/n

    sum_num=0
    sum_den=0
    for year,temp in avg.items():
        sum_num += (year - mean_year)*(temp - mean_temp)
        sum_den += (year - mean_year)**2

    if sum_den ==0:
        raise ExamException("Errore: il denominatore è uguale a zero")
    
    m = sum_num/sum_den
    return(m)




if __name__ == "__main__":
    time_series_file = CSVTimeSeriesFile(name="modulo1/GlobalLandTemperaturesByMajorCity.csv")
    time_series_italy = time_series_file.get_data(city="Rome")
    print(compute_slope(time_series_italy, 1990 , 2013))