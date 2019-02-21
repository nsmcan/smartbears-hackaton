import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.g_et_api_player()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_api_player: %s\n" % e)
