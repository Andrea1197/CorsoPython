# Creazione di un'istanza di classe
class CSVFile():
    # definisco attributo che contenga il nome del file
    def __init__(self,name):
    #setto il nome
        self.name = name
# definisco metoto per restituire dati csv come lista di liste
    def get_data(self):
        values = []
        my_file = open(self.name,'r')
        for line in my_file:
            elements = line.split(',')
            elements[-1] = elements[-1].strip() #per eliminare/n
            if elements[0] !='Date':
                values.append(elements)
        return values
        
csvfile=CSVFile(name='shampoo_sales.csv')
print(csvfile.get_data())