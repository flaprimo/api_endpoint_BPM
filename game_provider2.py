from flask import Flask

app = Flask(__name__)


# API
@app.route('/hasbro/orderGame/<string:game>', methods=['POST', 'GET'])
def orderGame(game):
    return game, 200


if __name__ == '__main__':
    app.run(port=9002, debug=True)
