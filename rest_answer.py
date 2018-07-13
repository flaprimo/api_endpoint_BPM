from flask import Flask, request, jsonify
import random


app = Flask(__name__)


# API
@app.route('/supplier/item/<int:id>', methods=['GET', 'POST'])
def supplier_item(id):
    code = random.uniform(0, 1)

    if code < 0.8:
        return "available!"
    elif code >= 0.8 or code < 0.9:
        return "delay!"
    else:
        return "unavailable!"


@app.route('/package_delivery/order/<int:id>', methods=['GET', 'POST'])
def package_delivery_order(id):
    return 1


@app.route('/test', methods=['POST'])
def add_message():
    content = request.get_json(silent=True)
    return jsonify(content)


if __name__ == '__main__':
    app.run(debug=True)
