from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, render_template, send_file, make_response, request
from flask.ext.sqlalchemy import SQLAlchemy
from plot import render_map
# from quartile_plot import plot_map
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print(os.environ['APP_SETTINGS'])

from plot import render_map
from models import *

@app.route('/')
def index():
    return 'We are up and running!'

@app.route('/conditions_map', methods=['GET'])
def conditions_map_v1():
    args = request.args
    render_map(args['condition'])
    plt.savefig("MeMD_Map.png")
    return send_file('MeMD_Map.png', mimetype='image/gif')

if __name__ == '__main__':
    app.run()
