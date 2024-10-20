# GetServices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**GetClientLegalEntities200ResponsePagination**](GetClientLegalEntities200ResponsePagination.md) |  | [optional] 
**items** | [**List[Service]**](Service.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_services200_response import GetServices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServices200Response from a JSON string
get_services200_response_instance = GetServices200Response.from_json(json)
# print the JSON string representation of the object
print(GetServices200Response.to_json())

# convert the object into a dict
get_services200_response_dict = get_services200_response_instance.to_dict()
# create an instance of GetServices200Response from a dict
get_services200_response_from_dict = GetServices200Response.from_dict(get_services200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


