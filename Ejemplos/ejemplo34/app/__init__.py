from flask import Flask, flash, url_for, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///estudiantes.sqlite3'
app.config['SECRET_KEY'] = 'uippc3'

db = SQLAlchemy(app)
class estudiantes(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    ciudad = db.Column(db.String(50))
    direccion = db.Column(db.String(200))
    pin = db.Column(db.String(10))
    def __init__(self, nombre, ciudad, direccion, pin):
        self.nombre = nombre
        self.ciudad = ciudad
        self.direccion = direccion
        self.pin = pin

@app.route('/')
def mostrar_todo():
    return render_template('mostrar_todo.html', estudiantes=estudiantes.query.all())

@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        if not request.form['nombre'] or not request.form['ciudad'] or not request.form['direccion']:
            flash('Por favor introduzca todos los campos', 'error')
        else:
            estudiante = estudiantes(request.form['nombre'],
                                     request.form['ciudad'],
                                     request.form['direccion'],
                                     request.form['pin'])
            db.session.add(estudiante)
            db.session.commit()
            flash('Registro guardado con exito!')
            return redirect(url_for('mostrar_todo'))
    return render_template('nuevo.html')

if __name__ == '__main__':
    db.create_all()
    app.run()