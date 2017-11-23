from flask import Flask, redirect, url_for

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

@app.route('/admin')
def hola_admin():
    return'Hola Admin!'

@app.route('/invitado/<invitado>')
def hola_invitado(invitado):
    return 'Hola %s! Eres invitado' % invitado

@app.route('/usuario/<nombre>')
def hola_usuario(nombre):
    if nombre == 'admin':
        return redirect(url_for('hola_admin'))
    else:
        return redirect(url_for('hola_invitado',invitado=nombre))

if __name__ == '__main__':
    app.run()