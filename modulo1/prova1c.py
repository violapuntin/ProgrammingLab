class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        file = open(self.name, 'r')

        righe = file.readlines()[1:]

        data = []
        for riga in righe:
            elementi = riga.strip().split(",")
            
            date = elementi[0]
            temp = elementi[1]

            data.append([date, temp])

        file.close()
        return data


time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
print(time_series)