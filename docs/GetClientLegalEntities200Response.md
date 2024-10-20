# GetClientLegalEntities200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**GetClientLegalEntities200ResponsePagination**](GetClientLegalEntities200ResponsePagination.md) |  | [optional] 
**items** | [**List[ClientLegalEntity]**](ClientLegalEntity.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_client_legal_entities200_response import GetClientLegalEntities200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientLegalEntities200Response from a JSON string
get_client_legal_entities200_response_instance = GetClientLegalEntities200Response.from_json(json)
# print the JSON string representation of the object
print(GetClientLegalEntities200Response.to_json())

# convert the object into a dict
get_client_legal_entities200_response_dict = get_client_legal_entities200_response_instance.to_dict()
# create an instance of GetClientLegalEntities200Response from a dict
get_client_legal_entities200_response_from_dict = GetClientLegalEntities200Response.from_dict(get_client_legal_entities200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


