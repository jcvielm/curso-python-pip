import utils
import read_csv_25
import charts_26

''' Clases anteriores
data = [
    {
        'Country': 'Paraguay',
        'Population': '10'
    },
    {
        'Country': 'Bolivia',
        'Population': '15'
    }
]
'''

def run_bar_country(): 

    data = read_csv_25.read_csv_list('./data.csv') 
    # Obtenemos los datos utilizando un módulo para leer csv que ya realizamos
    
    country = input('Ingresar el país: ')
    # Se ingresa manualmente el país 
    
    result = utils.populations_by_country(data, country.capitalize()) 
    # Otenemos los datos leídos del csv, damos de parámetro los datos leídos y el país que ingresamos y lo transformamos en listas
    
    if len(result) > 0: 
    # Si el resultado, el país es mayor a cero, encontró el país y proseguimos
        country = result[0] 
        # El país que encontró se encuentra en la posición 0
        
        labels, values = utils.get_population(country) 
        # Aquí se obtiene las poblaciones del país seleccionado mediante una funcion
        
        charts_26.generate_bar_chart(country['Country/Territory'], labels, values) 
        # Generamos una gráfica de barras obteniendo de nuestro archivo charts_26. La llamamos con el nombre del pais elegido


def run_pie_world():
    
    data = read_csv_25.read_csv_list('./data.csv') 
    # Obtenemos los datos utilizando un módulo para leer csv que ya realizamos

    # Para filtrar continente:
    # data = list(filter(lambda item : item['Continent'] == 'South America',data))

    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    charts_26.generate_pie_chart(countries, percentages)



# Para poder ejecutar desde la terminal
if __name__ == '__main__':

    run_bar_country()
    run_pie_world()
