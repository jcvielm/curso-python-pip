import csv # modulo nativo de python para leer archivos csv

population_dictionary = {}

def read_csv_list(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 
        # Normalmente los delimitadores de CSV vienen por coma.
        
        header = next(reader) 
        # Para obtener los títulos o primeras filas de las columnas.
        
        data = []
        for row in reader:
            iterable = zip(header, row) 
            # Para unir dos arrays (listas)
            
            # print(list(iterable)) Para imprimir las listas
            country_dict = {key: value for key, value in iterable}
            
            data.append(country_dict) 
            # Para agregar al la lista los diccionarios
        return data
'''
def create_new_dictionary(data):
    for i in data:
        new_data = dict(data)
    print(new_data)
    for element in new_data:
        population_dictionary = {key:value for key, value in new_data if new_data.key('Population') == True}
    return population_dictionary
'''

def read_csv_dict(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',') 
        # Normalmente los delimitadores de CSV vienen por coma.
        
        header = next(reader) 
        # Para obtener los títulos o primeras filas de las columnas.
        
        for row in reader:
            iterable = zip(header, row) 
            # Para unir dos arrays (listas)
            
            country_dict = {key: value for key, value in iterable}
            
            return country_dict 

if __name__ == '__main__':
     
    # Para leer el csv y convertir en lista
    data = read_csv_list('./data.csv')
    
    print(data[0]) 
    # imprime el primer diccionario
    
    # create_new_dictionary(data)
    # print(population_dictionary)

