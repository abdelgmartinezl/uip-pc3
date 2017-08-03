from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def estudiante():
    return render_template('estudiante.html')

@app.route('/resultado', methods=['POST', 'GET'])
def resultado():
    if request.method == 'POST':
        resultado = request.form
        return render_template('tabla.html', resultado=resultado)

if __name__ == '__main__':
    app.run()