from flask import Flask, render_template

#modelos
#vistas
#controladres

app = Flask(__name__, template_folder='views')

#importando controllers
from src.controllers import *


def create_app():
    app.run(debug=True)