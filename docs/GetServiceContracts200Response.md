# GetServiceContracts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**GetClientLegalEntities200ResponsePagination**](GetClientLegalEntities200ResponsePagination.md) |  | [optional] 
**items** | [**List[ServiceContract]**](ServiceContract.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.get_service_contracts200_response import GetServiceContracts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceContracts200Response from a JSON string
get_service_contracts200_response_instance = GetServiceContracts200Response.from_json(json)
# print the JSON string representation of the object
print(GetServiceContracts200Response.to_json())

# convert the object into a dict
get_service_contracts200_response_dict = get_service_contracts200_response_instance.to_dict()
# create an instance of GetServiceContracts200Response from a dict
get_service_contracts200_response_from_dict = GetServiceContracts200Response.from_dict(get_service_contracts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


