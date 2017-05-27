"""
Ej. 29

Autor: Zahir Gudiño
Email: zahir.gudino@gmail.com
Descripcion:
    Consumir SWAPI, The Star Wars API (http://swapi.co), escribir y mostar en pantalla respuesta JSON.
    
    NOTA:
    Note el uso de pkg requests (https://pypi.python.org/pypi/requests), por ende debe instalar pkg previo a ejecucion.
    Una manera sencilla de obtener pkg es via pip (https://pip.pypa).
    
    En una nueva linea de comando ejecute el comando:
    `pip install -r requirements.txt`
"""
import requests
import json

with open('data.json', 'w') as output:
    try:
        req = requests.get('http://swapi.co/api/people/1')  # lee RESTful API
        json.dump(req.text, output)  # escribe data.json

        print(json.dumps(req.json(), sort_keys=True, indent=4))  # imprime JSON consola desde el buffer
    except TimeoutError as error:
        raise error
