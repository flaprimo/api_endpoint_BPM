import requests

test_endpoint = 'http://localhost:5000/test'
camunda_endpoint = 'http://localhost:8080/engine-rest/message'
ENDPOINT = camunda_endpoint


NAME = "Gino Paoli"
EMAIL = "gino.paoli@hotmail.com"
GAME = "Risk"
ADDRESS = "via Golgi, 40, Milano"


camunda_ask = {
    "messageName": "",
    "processVariables": {}
}


def order_game():
    ordergame_content = camunda_ask.copy()

    ordergame_dict = {
        "name": {
            "value": NAME,
            "type": "String"
        },
        "email": {
            "value": EMAIL,
            "type": "String"
        },
        "game": {
            "value": GAME,
            "type": "String"
        },
        "address": {
            "value": ADDRESS,
            "type": "String"
        }
    }

    ordergame_content["messageName"] = "orderReceived"
    ordergame_content["processVariables"] = ordergame_dict

    path = ''

    send_post(ordergame_content, path)


def game_received():
    gamereceived_content = camunda_ask.copy()

    gamereceived_dict = {
        "order_id": {
            "value": "A0001",
            "type": "String"
        },
        "item": {
            "value": GAME,
            "type": "String"
        },
        "quantity": {
            "value": "1",
            "type": "Integer"
        }
    }

    gamereceived_content["messageName"] = "gameReceived"
    gamereceived_content["processVariables"] = gamereceived_dict

    path = ''

    send_post(gamereceived_content, path)


def feedback():
    feedback_content = camunda_ask.copy()

    feedback_dict = {
        "user_email": {
            "value": EMAIL,
            "type": "String"
        },
        "item": {
            "value": GAME,
            "type": "String"
        },
        "delivery": {
            "value": "true",
            "type": "Boolean"
        },
        "satisfaction grade": {
            "value": "Good",
            "type": "String"
        }
    }

    feedback_content["messageName"] = "clientFeedback"
    feedback_content["processVariables"] = feedback_dict

    path = ''

    send_post(feedback_content, path)


# send messages
def send_post(json_content, path):
    try:
        url = ENDPOINT if ENDPOINT == test_endpoint else ENDPOINT + path

        res = requests.post(url, json=json_content)
        print('response from server:', res.text)
        # dictFromSrever = res.json()
    except Exception as e:
        print("ERROR: {}".format(e))


def main():
    choice = ''

    while choice != 'q':
        # Give all the choice in a series of print statements.
        print("\n[1] Enter 1 to orderReceived")
        print("[2] Enter 2 to gameReceived")
        print("[3] Enter 3 to feedback")

        # Ask for the user's choice
        choice = input("\nWhat would you like to do?")

        # Respond to the user's choice
        if choice == '1':
            order_game()
        elif choice == '2':
            game_received()
        elif choice == '3':
            feedback()
        elif choice == 'q':
            print("\nBye.\n")
        else:
            print("\nError: wrong input. try again.\n")


if __name__ == '__main__':
    main()
