from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

# Helper function to find a product by ID
def find_product(id):
    return next((x for x in products if x["id"] == id), None)

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get a single product by ID
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = find_product(id)
    return jsonify(product) if product else ('', 404)

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    products.append(request.get_json())
    return '', 201

# Update an existing product by ID
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = find_product(id)
    if product:
        updated_data = request.get_json()
        product.update(updated_data)
        return '', 204
    return '', 404

# Remove a product by ID
@app.route('/products/<int:id>', methods=['DELETE'])
def remove_product(id):
    product = find_product(id)
    if product:
        products.remove(product)
        return '', 204
    return '', 404

app.run(port=5001,debug=True)
