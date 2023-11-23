import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print(r.status_code) # PARA VER EL ESTADO DE RESPUESTA DEL SERVIDOR 
    print(r.text) # PARA VER LA INFORMACION.
    print(type(r.text))
    categories = r.json() # PARA CONVERTIR EL TEXTO EN FORMATO .JSON
    for category in categories:
        print(category['name'])
