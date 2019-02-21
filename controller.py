import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from msvcrt import getch


# Read arrow keys
def get_key():
    first_char = getch()
    if first_char == b'\xe0' or first_char == b'\x00':
        second_char = getch()
        return {
                b"H": "up", 
                b"P": "down", 
                b"M": "right", 
                b"K": "left", 
                b"Q": "sright", 
                b"O": "sleft"
            }.get(second_char,"")
    else:
        return first_char.decode('latin1')

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

def play(action):
    time.sleep(0.02)
    print(action)
    body = swagger_client.PlayerAction(action)
    try:
        api_instance.p_ost_api_player_actions(body)
    except ApiException as e:
        print("Exception when calling DefaultApi->p_ost_api_player_actions: %s\n" % e)
    try:
        api_response = api_instance.g_et_api_player()
        pprint(api_response.position)
    except ApiException as e:
        print("Exception when calling DefaultApi->g_et_api_player: %s\n" % e)

def main():

#    try:
        #api_response = api_instance.g_et_api_player()
        #pprint(api_response)
    #except ApiException as e:
        #print("Exception when calling DefaultApi->g_et_api_player: %s\n" % e)

    while True:
        action = ''
        key = get_key()
        if key == " ":
            action = 'use'
        elif key == "up":
           action = 'forward'
        elif key == "down": 
            action = 'backward'
        elif key == "left": 
            action = 'turn-left'
        elif key == "right": 
            action = 'turn-right'
        elif key == "sleft": 
            action = 'strafe-left'
        elif key == "sright": 
            action = 'strafe-right'
        elif key == "z": 
            action = 'shoot'
        elif key == "q":
            print("Exiting...")
            break

        if action:
            play(action)

if __name__=='__main__':
        main()

