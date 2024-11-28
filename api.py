from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database for products
products = []

@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        # Input validation
        if not all([name, description, isinstance(price, (int, float))]):
            return jsonify({'error': 'Invalid input data'}), 400

        # Add product
        product = {'name': name, 'description': description, 'price': price}
        products.append(product)
        return jsonify(product), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200

if __name__ == '__main__':
    app.run(debug=True)
