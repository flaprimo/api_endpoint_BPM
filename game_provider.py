from flask import Flask, send_from_directory
import requests
import random

app = Flask(__name__)


# API
@app.route('/gameproviderservice/wsdl', methods=['POST', 'GET'])
def getWsdl():
    return send_from_directory("", "service.wsdl", as_attachment=True)


@app.route('/gameproviderservice/getGameProvider/<string:game>/', methods=['POST', 'GET'])
def getGameProvider(game):
    if random.uniform(0, 1) > 0.5:
        r = requests.post("http://localhost:9001/ravensburger/spielBestellen/" + game)
    else:
        r = requests.post("http://localhost:9002/hasbro/orderGame/" + game)
    return '<root>' + r.text + '</root>', 200


if __name__ == '__main__':
    app.run(port=9000, debug=True)
