from flask import Flask, render_template
from controller.controller import Controller
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Diccionario de animales y sus sonidos
animals = {
    "gato": "Miau",
    "perro": "Guau",
    "hurón": "Dook dook",
    "boa_constrictor": "Sssss"
}

# Endpoint principal para consultar sonidos
@app.route('/api/animal/<string:animal>', methods=['GET'])
def get_animal_sound(animal):
    animal = animal.lower()
    if animal in animals:
        return jsonify({"animal": animal, "sonido": animals[animal]})
    else:
        return jsonify({"error": "Animal no encontrado"}), 404

# Página web para visualizar los animales y sus sonidos
@app.route('/')
def home():
    return """
    <h1>Consulta de Animales</h1>
    <p>Bienvenido a la API de sonidos de animales.</p>
    <ul>
        <li><a href="/api/animal/gato">Gato</a></li>
        <li><a href="/api/animal/perro">Perro</a></li>
        <li><a href="/api/animal/huron">Hurón</a></li>
        <li><a href="/api/animal/boa_constrictor">Boa constrictor</a></li>
    </ul>
    """

if __name__ == '__main__':
    app.run(debug=True)
