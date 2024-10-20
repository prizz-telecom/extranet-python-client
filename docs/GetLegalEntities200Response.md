# GetLegalEntities200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**GetClientLegalEntities200ResponsePagination**](GetClientLegalEntities200ResponsePagination.md) |  | [optional] 
**items** | [**List[LegalEntity]**](LegalEntity.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_legal_entities200_response import GetLegalEntities200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLegalEntities200Response from a JSON string
get_legal_entities200_response_instance = GetLegalEntities200Response.from_json(json)
# print the JSON string representation of the object
print(GetLegalEntities200Response.to_json())

# convert the object into a dict
get_legal_entities200_response_dict = get_legal_entities200_response_instance.to_dict()
# create an instance of GetLegalEntities200Response from a dict
get_legal_entities200_response_from_dict = GetLegalEntities200Response.from_dict(get_legal_entities200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


