# GetApiTokens200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**GetClientLegalEntities200ResponsePagination**](GetClientLegalEntities200ResponsePagination.md) |  | [optional] 
**items** | [**List[UserApiToken]**](UserApiToken.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_api_tokens200_response import GetApiTokens200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetApiTokens200Response from a JSON string
get_api_tokens200_response_instance = GetApiTokens200Response.from_json(json)
# print the JSON string representation of the object
print(GetApiTokens200Response.to_json())

# convert the object into a dict
get_api_tokens200_response_dict = get_api_tokens200_response_instance.to_dict()
# create an instance of GetApiTokens200Response from a dict
get_api_tokens200_response_from_dict = GetApiTokens200Response.from_dict(get_api_tokens200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


