import r1
from r1.helpers import first_day_of_this_week
from r1.filter import (filter_menu, make_filter)


from flask import (
    Flask,
    g,
    jsonify,
    request
)
from flask_cors import CORS, cross_origin
import flask_shelve as shelve
from functools import partial
from os import getenv



def load_menu():
    db = shelve.get_shelve()
    fd = first_day_of_this_week()
    day = db.get('day', None)
    if day is None or day != fd:
        db['menu'] = r1.get_full_menu()
        db['day'] = fd
    return db['menu']


def get_menu():
    d = g.get('day', None)
    fd = first_day_of_this_week()
    if d is None or d != fd:
        g.menu = load_menu()
        g.day = d
    return g.menu

app = Flask(__name__)
app.debug = True
app.config['SHELVE_FILENAME'] = 'shelve.db'
shelve.init_app(app)


@app.route('/<path:path>')
@cross_origin()
def json_menu(path):
    filter_ = make_filter(path.split('/'))
    menu = filter_menu(get_menu(), filter_)
    return jsonify(menu=r1.serialize_menu(menu))


@app.route('/')
def index():
    return json_menu('today')

if __name__ == "__main__":
    app.run()
