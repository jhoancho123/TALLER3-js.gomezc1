from flask import Flask, render_template
from controller.controller import Controller

app = Flask(__name__, template_folder = 'views')

@app.route("/")
def home():
    controller = Controller()
    perros_info = controller.retornar_perros()
    return render_template('index.html', perros_info=perros_info)

if __name__ == '__main__':
    app.run(debug=True)