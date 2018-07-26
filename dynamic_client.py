import operator
import time
from flask import Flask
from zeep import Client

app = Flask(__name__)

DELIVER = True
wsdl_url = 'http://localhost:9000/gameproviderservice/wsdl'


@app.route('/supplier/game/<string:game>', methods=['POST', 'GET'])
def get_game(game):
    if DELIVER:
        return dynamic_client(game), 200
    else:
        time.sleep(10)


def dynamic_client(game_name):
    client = Client(wsdl_url)
    for service in client.wsdl.services.values():
        print("service:", service.name)
        for port in service.ports.values():
            operations = sorted(
                port.binding._operations.values(),
                key=operator.attrgetter('name'))

            for operation in operations:
                print("method :", operation.name)
                print("  input :", operation.input.signature())
                print("  output:", operation.output.signature())
                print("\n")
        print("\n")

    result = client.service.getGameProvider(game_name)
    return result


if __name__ == '__main__':
    app.run(port=5000, debug=True)
