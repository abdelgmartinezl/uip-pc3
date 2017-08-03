from flask import Flask, render_template

app = Flask(__name__)

@app.route('/resultado')
def resultado():
    notas={'Calculo':99, 'Ecologia':71, 'Programacion':88}
    promedio = 0
    for k,v in notas.items():
        promedio += v
    promedio = promedio/len(notas)
    return render_template('tabla.html', r=notas, promedio=promedio)

@app.route('/nota/<int:resultado>')
def mostrar_nota(resultado):
    return render_template('nota.html', valor=resultado)

@app.route('/')
def index():
    return '<html><body><h1>Gano Panama</h1></body></html>'

@app.route('/hola/<usuario>')
def hola_usuario(usuario):
    return render_template('sele.html', nombre=usuario)

if __name__ == '__main__':
    app.run()