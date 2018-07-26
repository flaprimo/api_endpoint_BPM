from flask import Flask

app = Flask(__name__)


# API
@app.route('/ravensburger/spielBestellen/<string:game>', methods=['POST', 'GET'])
def orderGame(game):
    return game, 200


if __name__ == '__main__':
    app.run(port=9001, debug=True)
