import requests

test_endpoint = 'http://localhost:5000/test'
camunda_endpoint = 'http://localhost:8080/engine-rest/message'
ENDPOINT = test_endpoint

camunda_ask = {
    "messageName": "",
    "processVariables": {}
}


def ask1():
    ask1_content = camunda_ask.copy()

    ask1_dict = {
        "user_email": {
            "value": "gino.paoli@hotmail.com",
            "type": "String"
        },
        "item": {
            "value": "Risk",
            "type": "String"
        },
        "address": {
            "value": "via Golgi, 40, Milano",
            "type": "String"
        }
    }

    ask1_content["messageName"] = "ask1"
    ask1_content["processVariables"] = ask1_dict

    path = ''

    send_post(ask1_content, path)


# send messages
def send_post(json_content, path):
    try:
        url = ENDPOINT if ENDPOINT == test_endpoint else ENDPOINT + path

        res = requests.post(url, json=json_content)
        print('response from server:', res.text)
        # dictFromServer = res.json()
    except Exception as e:
        print("ERROR: {}".format(e))


def main():
    choice = ''

    while choice != 'q':
        # Give all the choices in a series of print statements.
        print("\n[1] Enter 1 to ask1")
        print("[2] Enter 2 to ask1")
        print("[q] Enter q to quit.")

        # Ask for the user's choice.
        choice = input("\nWhat would you like to do? ")

        # Respond to the user's choice.
        if choice == '1':
            ask1()
        elif choice == '2':
            ask1()
        elif choice == 'q':
            print("\nBye.\n")
        else:
            print("\nError: wrong input, try again.\n")


if __name__ == '__main__':
    main()
