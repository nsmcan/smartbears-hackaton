import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
from msvcrt import getch
import signal
import math
import requests

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
prev_position = None
passed_doors = []

def play(action, check_door=False, fighting=False):
    global prev_position
    global passed_doors
    time.sleep(0.03)
    print(action)
    body = swagger_client.PlayerAction(action)
    try:
        api_instance.p_ost_api_player_actions(body)
        api_response = api_instance.g_et_api_player()
        time.sleep(0.3)
    except ApiException as e:
        print("Exception when calling DefaultApi->p_ost_api_player_actions: %s\n" % e)
    try:
        api_response = api_instance.g_et_api_player()
        #print(api_response.position)
        dist = distance(prev_position, api_response.position)
        print(dist)
        prev_position = api_response.position
    except ApiException as e:
        print("Exception when calling DefaultApi->g_et_api_player: %s\n" % e)

    #Checking doors
    if check_door:
        api_response = api_instance.g_et_api_world_doors()
        num_doors = len(api_response)
        num_doors_passed = len(passed_doors)

        if num_doors-1 == num_doors_passed:
            #Trying to finish level
            print('Trying to finish...')
            play('use')
            door_check = api_instance.g_et_api_world_doors_id(passed_doors[-1])
            if door_check['state'] == "open":
                play('use') # Close door back

        for door in api_response:
            door_id = door['id']
            if door_id in passed_doors: continue
            if door['distance'] < 100:
                print("Opening door {}...".format(door_id))
                play('use')
                door_check = api_instance.g_et_api_world_doors_id(door_id)
                if door_check['state'] == "open":
                    play('forward')
                    passed_doors.append(door_id)
                    print("Door {} opened".format(door_id))

    #Checking attackers
    if not fighting:
        resp = requests.get('http://localhost:7777/api/world/objects?distance={}'.format(200)).json()
        for obj in resp:
            if 'MF_COUNTKILL' in obj['flags'] and 'MF_SHOOTABLE' in obj['flags']:
                print("Detected {0} id {1}".format(obj['type'], obj['id']))
                fight(obj['id'])

    return dist

def fight(id):
    print('Fighting {0}...'.format(id))
    target = requests.get('http://localhost:7777/api/world/objects/{}'.format(id)).json()
    target_position = swagger_client.Position(target['position']['x'],target['position']['y'],target['position']['z'])
    player = api_instance.g_et_api_player()
    dist = distance(player.position,target_position)
    saved_angle = player.angle
    delta_prev = 0
    dir_prev = 'turn-right'
    while 'MF_SHOOTABLE' in target['flags'] and dist<200 and dist>(target_position.z-player.position.z)*2:
        #print(target_position)
        #
        #print(player.position)
        angle_needed = math.degrees(math.atan2(
            target_position.y-player.position.y,
            target_position.x-player.position.x
        ))
        if angle_needed < 0: angle_needed += 360
        delta = math.fabs(player.angle - angle_needed)
        print("Angles: needed: {0}, player: {1}, delta: {2}".format(angle_needed, player.angle, delta))
        if delta < 15 or (360 - delta) < 15:
            play('shoot', fighting=True)
            play('shoot', fighting=True)
        elif delta - delta_prev < 0:
            play(dir_prev, fighting=True)
        else:
            dir = 'turn-left' if dir_prev == 'turn-right' else 'turn-right'
            play(dir, fighting=True)
            dir_prev = dir
        delta_prev = delta
        target = requests.get('http://localhost:7777/api/world/objects/{}'.format(id)).json()
        target_position = swagger_client.Position(target['position']['x'],target['position']['y'],target['position']['z'])
        player = api_instance.g_et_api_player()
        dist = distance(player.position,target_position)
    print('Fighting is over')

    #Restore angle
    while True:
        delta = math.fabs(player.angle - saved_angle)
        print("Angles: needed: {0}, player: {1}, delta: {2}".format(saved_angle, player.angle, delta))
        if delta < 15 or (360 - delta) < 15:
            break
        elif delta - delta_prev < 0:
            play(dir_prev)
        else:
            dir = 'turn-left' if dir_prev == 'turn-right' else 'turn-right'
            play(dir)
            dir_prev = dir
        delta_prev = delta
        player = api_instance.g_et_api_player()



def distance(p1, p2):
    try:
        return math.sqrt((p2.x-p1.x)**2 + (p2.y-p1.y)**2 + (p2.z-p1.z)**2)
    except:
        return 0

def autopilot():
    while True:
        try:
            dist = play('forward', check_door = True)
            if dist > 50:
                #play('backward')
                play('turn-right', check_door = True)
                play('strafe-right', check_door = True)
                #play('strafe-right')
                #play('strafe-right')
                #time.sleep(0.5)
            elif dist < 20:
                play('turn-left', check_door = True)
                #play('turn-left')
                #play('strafe-right')
                #time.sleep(0.5)
        except KeyboardInterrupt:
            break

def main():

    # To handle keyboard interrupt
    _ = signal.signal(signal.SIGINT, signal.default_int_handler)
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
        elif key == "a": 
            print("Autopilot mode...")
            autopilot()
        elif key == "q":
            print("Exiting...")
            break

        if action:
            play(action)

if __name__=='__main__':
        main()

