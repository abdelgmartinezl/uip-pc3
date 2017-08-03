from flask import render_template, Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/setcookie', methods=['POST','GET'])
def setcookie():
    if request.method == 'POST':
        usuario = request.form['nm']
        respuesta = make_response(render_template('readcookie.html'))
        respuesta.set_cookie('userID', usuario)
        return respuesta

@app.route('/getcookie')
def getcookie():
    nombre = request.cookies.get('userID')
    return '<h1>Bienvenido ' + nombre + '</h1>'

if __name__ == "__main__":
    app.run()