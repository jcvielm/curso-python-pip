''' Clases anteriores
    def get_population():
    keys = ['col', 'py']
    values = [300, 400]
    return keys, values
'''
def get_population(country_dict): # Damos como parámetro el país seleccionado para realizar el gráfico
    populations_dict = {
        '2022': int(country_dict['2022 Population']), # Obtenemos la población mediante la key de las poblaciones por año
        '2020': int(country_dict['2020 Population']), # Cada vez que leemos un valor de CSV, python lo lee como un string. Así que necesitamos pasar los valores a enteros, para que matplotlib lo identifique como un valor numérico.
        '2015': int(country_dict['2015 Population']),
        '2010': int(country_dict['2010 Population']),
        '2000': int(country_dict['2000 Population']),
        '1990': int(country_dict['1990 Population']),
        '1980': int(country_dict['1980 Population']),
        '1970': int(country_dict['1970 Population'])
    } 
    labels = populations_dict.keys() # Una vez obtenido los años con las poblaciones respectivas, obtenemos en array las keys
    values = populations_dict.values() # Obtenemos en array los values
    return labels, values # el return debe ser un array con los años y con los valores para poder realizar la gráfica

A = 'Wenas'

def populations_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

