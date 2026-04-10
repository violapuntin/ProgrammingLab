class ExamException(Exception):
    pass


class MovingAverage():

    def __init__(self, window_len):

        if not isinstance(window_len, int) or window_len <= 0:
            raise ExamException('Errore, window_len non valido')
        
        self.window_len = window_len
    
    def compute(self, data):

        if not isinstance(data, list):
            raise ExamException('Errore, non è stata inserita una lista')
        for elem in data:
            if not isinstance(elem, (int,float)):
                raise ExamException(f"Errore, l'elemento {elem} non è valido")
        
        if len(data) < self.window_len:
            raise ExamException('Errore, la lunghezza della lista è minore della lunghezza della finestra')

        list_result = []
        for idx in range(len(data)):
            if((idx + self.window_len)>len(data)):
                break
            tot = 0
            for i in range(self.window_len):           
                tot += data[idx + i]
            mean = tot/self.window_len
            list_result.append(mean)
        return list_result

moving_average = MovingAverage(2)
result = moving_average.compute([2,4,8,16])
print(result)