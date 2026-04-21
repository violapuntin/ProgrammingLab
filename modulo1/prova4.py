import os

class ExamException(Exception):
    pass

class CSVTimeSeriesFile():
    def __init__(self, name):
        if not os.path.exists(name):
            raise ExamException("Errore: il path inserito non esiste")
        try:
            with open(name, 'r') as f:
                f.readline()
        except:
            raise ExamException("Errore: impossibile aprire il file")
        self.name = name

    def get_data(self):

        data = []

        with open(self.name, 'r') as file:
            # Salto l'intestazione
            next(file)

            for riga in file:
                elementi = riga.strip().split(",")
                
                date = str(elementi[0])
                
                try:
                    temp = float(elementi[1])
                    avg_temp_un = float(elementi[2])
                except: 
                    continue

                if avg_temp_un < 5:
                    data.append([date,temp])
                else:
                    print("Data saltata perché valore troppo incerto\n")
        
        return data

def compute_month_variation(time_series, first_year, second_year):
    if not isinstance(first_year, int):
        raise ExamException("Errore: first_year non è di tipo int")
    if not isinstance(second_year, int):
        raise ExamException("Errore: second_year non è di tipo int")
    if second_year <= first_year:
        raise ExamException("Errore: il secondo anno deve essere maggiore del primo. ")
    

    variations={}

    first_dict = {}
    second_dict = {}

    for elemento in time_series:
        year = int(elemento[0].split("/")[2])
        if year == first_year:
            month = int(elemento[0].split("/")[1])
            first_dict[month] = elemento[1]
        if year == second_year:
            month = int(elemento[0].split("/")[1])
            second_dict[month] = elemento[1]
    
    for month in first_dict:
        if month in second_dict:
            variations[month] = second_dict[month] - first_dict[month]
        else:
            print(f'La variazione per il mese {month} non può essere calcolata')
    
    if not variations:
        raise ExamException("Gli anni considerati non hanno mesi validi")
    return variations

if __name__ == "__main__":
    time_series_file = CSVTimeSeriesFile(name="modulo1/Temperatures.csv")
    data = time_series_file.get_data()
    print(compute_month_variation(data, 1900, 2015))