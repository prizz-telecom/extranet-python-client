# UserApiToken


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available_workflows** | **List[str]** | liste des processus disponible pour l&#39;objet | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 
**token** | **str** |  | [optional] 
**last_usage** | **datetime** |  | [optional] 

## Example

```python
from prizz_extranet.models.user_api_token import UserApiToken

# TODO update the JSON string below
json = "{}"
# create an instance of UserApiToken from a JSON string
user_api_token_instance = UserApiToken.from_json(json)
# print the JSON string representation of the object
print(UserApiToken.to_json())

# convert the object into a dict
user_api_token_dict = user_api_token_instance.to_dict()
# create an instance of UserApiToken from a dict
user_api_token_from_dict = UserApiToken.from_dict(user_api_token_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


