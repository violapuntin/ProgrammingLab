class CSVTimeSeriesFile():
    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        file = open(self.name, 'r')
        
        righe = file.readlines()[1:]

        data = []

        for riga in righe:
            elementi = righe.strip().split()

            date = elementi[0]
            temperature = elementi[1]

            data.append([date, temperature])
        
        file.close()
        return data

def compute_variations(time_series, first_year, last_year, N):
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
        avg[year] = sum(values)/len(values)
    
    variations = {}

    for current_year in range(first_year + N, last_year  + 1):
        check_years = True
        temp_sum_prev = 0

        for i in range(1, N + 1):
            prev_year = current_year -i
            if prev_year in avg:
                temp_sum_prev += avg[prev_year]
            else:
                check_years = False
                break
        
        if check_years and current_year in avg:
            media_n_precedenti = temp_sum_prev / N
            variations[str(current_year)] = avg[current_year] - media_n_precedenti
        
        return variations

