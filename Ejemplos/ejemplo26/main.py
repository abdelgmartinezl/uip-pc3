from flask import Flask, url_for, request, jsonify, abort
app = Flask(__name__)

articulos = [
    {
        'id' : 1,
        'nombre' : u'Azúcar',
        'descripcion' : u'Azúcar 49'
    },
    {
        'id' : 2,
        'nombre' : u'Sal',
        'descripcion' : u'Sal 50'
    },
    {
        'id' : 5,
        'nombre' : u'Pimienta',
        'descripcion' : u'Pimienta 51'
    }
]

@app.route('/api/v1.0/articulos', methods=['GET'])
def get_articulos():
    return jsonify({'articulos': articulos})

@app.route('/api/v1.0/articulos/<int:articulo_id>', methods=['GET'])
def get_articulo(articulo_id):
    articulo = [articulo for articulo in articulos if articulo['id'] == articulo_id]
    if len(articulo) == 0:
        abort(404)
    return jsonify({'articulo': articulo[0]})

@app.route('/')
def api_raiz():
    return '<h3>Bienvenido al API</h3>'

@app.route('/articulos')
def api_articulos():
    return 'Lista de ' + url_for('api_articulos')

@app.route('/articulos/<int:idarticulo>')
def api_articulo(idarticulo):
    return 'Estas viendo el ' + str(idarticulo)

@app.route('/hola')
def api_hola():
    if 'nombre' in request.args:
        return 'Hola ' + request.args['nombre']
    else:
        return 'Hola Juanito Cautela'

@app.route('/pepito', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "PEPITO: GET\n"
    elif request.method == 'POST':
        return "PEPITO: POST\n"
    elif request.method == 'PUT':
        return "PEPITO: PUT\n"
    elif request.method == 'DELETE':
        return "PEPITO: DELETE\n"

if __name__ == '__main__':
    app.run()