from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'Xopa Petra!'

@app.route('/hola')
def hola():
    return 'Xopa'

@app.route('/hola/<nombre>')
def hola_nombre(nombre):
    return 'Xopa %s!' % nombre

@app.route('/edad/<int:edad>')
def puede_votar(edad):
    if edad >= 18:
        return 'Puede votar'
    else:
        return 'Menor de edad'
    

if __name__ == '__main__':
    app.run()