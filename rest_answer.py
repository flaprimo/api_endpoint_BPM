from flask import Flask
import time


app = Flask(__name__)

DELIVER = True


# API
@app.route('/supplier/game/<string:game>', methods=['GET', 'POST'])
def supplier_item(game):
    if DELIVER:
        return game, 200
    else:
        time.sleep(10)


@app.route('/test', methods=['GET', 'POST'])
def add_message():
    # content = request.get_json(silent=True)
    # return jsonify(content)
    return "yay!"


if __name__ == '__main__':
    app.run(debug=True)
