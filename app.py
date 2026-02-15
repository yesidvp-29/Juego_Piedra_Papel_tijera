from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jugar', methods=['POST'])
def jugar():
    datos = request.json
    usuario = datos.get('eleccion')
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)

    if usuario == computadora:
        resultado = "¡Empate! 🤝"
    elif (usuario == 'piedra' and computadora == 'tijera') or \
         (usuario == 'papel' and computadora == 'piedra') or \
         (usuario == 'tijera' and computadora == 'papel'):
        resultado = "¡Ganaste! 🎉"
    else:
        resultado = "Perdiste... 🤖"

    return jsonify({'computadora': computadora, 'resultado': resultado})

if __name__ == '__main__':
    app.run(debug=True)