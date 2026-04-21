class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self, country):
        data = []
        with open(self.name, 'r') as file:
            next(file)
            for riga in file:
                elementi = riga.strip().split(";")
                if len(elementi) < 3:
                    continue
                
                if elementi[3] == country:
                    data_str = str(elementi[0])
                    try:
                        temp = float(elementi[1])
                        incertezza = float(elementi[2])
                    except:
                        continue
                    if incertezza >= 5:
                        continue
                    data.append([data_str, temp, incertezza])
        return data
    
def compute_cons_variation_compare(time_series1, time_series2, year):
    dict1 = {}
    dict2 = {}

    for elemento in time_series1:
        year1 = int(elemento[0].split("/")[1])
        if year1 == year:
            month = int(elemento[0].split("/")[0])
            dict1[month] = ([elemento[1], elemento[2]])
    for elemento in time_series2:
        year2 = int(elemento[0].split("/")[1])
        if year2 == year:
            month = int(elemento[0].split("/")[0])
            dict2[month] = ([elemento[1], elemento[2]])
    
    sigma1 = 0
    sigma2 = 0
    delta1 = 0
    delta2 = 0
    variations = {}
    
    for i in range(1,12):
        if i in dict1 and i in dict2:
            for n in range(i+1,12):
                if n in dict1 and n in dict2:
                    sigma1 = dict1[i][1] + dict1[n][1]
                    sigma2 = dict2[i][1] + dict2[n][1]
                    
                    delta1 = dict1[n][0] - dict1[i][0]
                    delta2 = dict2[n][0] - dict2[i][0]
                    variations[i] = ([delta2 - delta1, sigma2 - sigma1])
                    break
    return variations


if __name__=="__main__":
    ts_file = CSVTimeSeriesFile(name="modulo1/GlobalLandTemperaturesByCountry_1.csv")
    time_series_italy = ts_file.get_data(country="Italy")
    time_series_singapore = ts_file.get_data(country="Singapore")
    print(compute_cons_variation_compare(time_series_italy, time_series_singapore, 2012))