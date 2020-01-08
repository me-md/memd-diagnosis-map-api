from dotenv import load_dotenv
load_dotenv()

import os
from flask import Flask, render_template, send_file, make_response, request, abort, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
from plot import render_map
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

print(os.environ['APP_SETTINGS'])

from plot import render_map
from quartile import plot_map
from models import *

@app.route('/')
def index():
    return render_template('root_path.html')

@app.route('/conditions', methods=['GET', 'POST'])
def create():
    if request.method == "POST":
        args = request.args
        condition = Condition(args['state'], args['name'])
        db.session.add(condition)
        db.session.commit()
    else:

        return "400"


@app.route('/conditions_map/v1', methods=['GET'])
def conditions_map_v1():
    args = request.args
    render_map(args['condition'])
    plt.savefig("MeMD_Map.png")
    return send_file('MeMD_Map.png', mimetype='image/gif')

@app.route('/conditions_map/v2', methods=['GET'])
def conditions_map_v2():
    args = request.args
    plot_map(args['condition'])
    plt.savefig("MeMD_Map.png")
    return send_file('MeMD_Map.png', mimetype='image/gif')

if __name__ == '__main__':
    app.run()
