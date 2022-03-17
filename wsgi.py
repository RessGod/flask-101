# wsgi.py
# pylint: disable=missing-docstring

from flask import Flask
from flask import jsonify
from flask import request
import itertools

app = Flask(__name__)
PRODUCTS = {
    1: { 'id': 1, 'name': 'Skello' },
    2: { 'id': 2, 'name': 'Socialive.tv' },
    3: { 'id': 3, 'name': 'Le Wagon'},
}

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/api/v1/products', methods=['GET','POST'])
def products():
    if request.method == 'GET':
        return jsonify(list(PRODUCTS))
    else:
        START_INDEX = len(PRODUCTS) + 1
        IDENTIFIER_GENERATOR = itertools.count(START_INDEX)
        # Voici comment l'utiliser :
        response = PRODUCTS[next(IDENTIFIER_GENERATOR)] = request.get_json()
        return jsonify(response)

@app.route('/api/v1/product/<int:id>')
def get_product_by_id(id):
    return jsonify(PRODUCTS[id])

@app.route('/api/v1/product/<int:id>')
def delete_product_by_id(id):
    #print('Produit %d' % id)
    return jsonify(PRODUCTS[id])
    #return 'Produit %d' % id