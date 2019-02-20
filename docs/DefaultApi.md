# swagger_client.DefaultApi

All URIs are relative to *http://localhost:7777*

Method | HTTP request | Description
------------- | ------------- | -------------
[**d_elete_api_world_objects_id**](DefaultApi.md#d_elete_api_world_objects_id) | **DELETE** /api/world/objects/{id} | 
[**g_et_api_player**](DefaultApi.md#g_et_api_player) | **GET** /api/player | 
[**g_et_api_world**](DefaultApi.md#g_et_api_world) | **GET** /api/world | 
[**g_et_api_world_doors**](DefaultApi.md#g_et_api_world_doors) | **GET** /api/world/doors | 
[**g_et_api_world_doors_id**](DefaultApi.md#g_et_api_world_doors_id) | **GET** /api/world/doors/{id} | 
[**g_et_api_world_objects**](DefaultApi.md#g_et_api_world_objects) | **GET** /api/world/objects | 
[**g_et_api_world_objects_id**](DefaultApi.md#g_et_api_world_objects_id) | **GET** /api/world/objects/{id} | 
[**p_atch_api_player**](DefaultApi.md#p_atch_api_player) | **PATCH** /api/player | 
[**p_atch_api_world**](DefaultApi.md#p_atch_api_world) | **PATCH** /api/world | 
[**p_atch_api_world_doors_id**](DefaultApi.md#p_atch_api_world_doors_id) | **PATCH** /api/world/doors/{id} | 
[**p_atch_api_world_objects_id**](DefaultApi.md#p_atch_api_world_objects_id) | **PATCH** /api/world/objects/{id} | 
[**p_ost_api_player_actions**](DefaultApi.md#p_ost_api_player_actions) | **POST** /api/player/actions | 
[**p_ost_api_world_objects**](DefaultApi.md#p_ost_api_world_objects) | **POST** /api/world/objects | 


# **d_elete_api_world_objects_id**
> d_elete_api_world_objects_id(id)



Delete the specified map object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    api_instance.d_elete_api_world_objects_id(id)
except ApiException as e:
    print("Exception when calling DefaultApi->d_elete_api_world_objects_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_api_player**
> Player g_et_api_player()



Query the player

### Example
```python
from __future__ import print_function
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
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Player**](Player.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_api_world**
> World g_et_api_world()



Query the current world state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.g_et_api_world()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_api_world: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**World**](World.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_api_world_doors**
> list[Door] g_et_api_world_doors()



Query door items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.g_et_api_world_doors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_api_world_doors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Door]**](Door.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_api_world_doors_id**
> Door g_et_api_world_doors_id(id)



Query the specified door

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | door id

try:
    api_response = api_instance.g_et_api_world_doors_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_api_world_doors_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| door id | 

### Return type

[**Door**](Door.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_api_world_objects**
> list[MapObject] g_et_api_world_objects(distance)



Query map object items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
distance = 'distance_example' # str | Only return items up to this distance from player 

try:
    api_response = api_instance.g_et_api_world_objects(distance)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_api_world_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distance** | **str**| Only return items up to this distance from player  | 

### Return type

[**list[MapObject]**](MapObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **g_et_api_world_objects_id**
> MapObject g_et_api_world_objects_id(id)



Query the specified map object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.g_et_api_world_objects_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->g_et_api_world_objects_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**MapObject**](MapObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_atch_api_player**
> Player p_atch_api_player(body)



Update the player

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.Player() # Player | 

try:
    api_response = api_instance.p_atch_api_player(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_atch_api_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Player**](Player.md)|  | 

### Return type

[**Player**](Player.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_atch_api_world**
> World p_atch_api_world(body)



Update the current world state

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.World() # World | 

try:
    api_response = api_instance.p_atch_api_world(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_atch_api_world: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**World**](World.md)|  | 

### Return type

[**World**](World.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_atch_api_world_doors_id**
> Door p_atch_api_world_doors_id(id, body)



Update the specified door

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | door id
body = swagger_client.Door() # Door | 

try:
    api_response = api_instance.p_atch_api_world_doors_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_atch_api_world_doors_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| door id | 
 **body** | [**Door**](Door.md)|  | 

### Return type

[**Door**](Door.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_atch_api_world_objects_id**
> MapObject p_atch_api_world_objects_id(id, body)



Update the specifed map object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
body = swagger_client.MapObject() # MapObject | 

try:
    api_response = api_instance.p_atch_api_world_objects_id(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_atch_api_world_objects_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**MapObject**](MapObject.md)|  | 

### Return type

[**MapObject**](MapObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_api_player_actions**
> p_ost_api_player_actions(body)



Create an action for the player to perform

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.PlayerAction() # PlayerAction | 

try:
    api_instance.p_ost_api_player_actions(body)
except ApiException as e:
    print("Exception when calling DefaultApi->p_ost_api_player_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayerAction**](PlayerAction.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **p_ost_api_world_objects**
> MapObject p_ost_api_world_objects(body)



Spawn a new map object

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.SpawnMapObject() # SpawnMapObject | 

try:
    api_response = api_instance.p_ost_api_world_objects(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->p_ost_api_world_objects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SpawnMapObject**](SpawnMapObject.md)|  | 

### Return type

[**MapObject**](MapObject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

