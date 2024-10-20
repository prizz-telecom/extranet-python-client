# ServiceContractSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**legal_entity_id** | **str** |  | [optional] 
**client_legal_entity_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**ref_client** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**addresses** | **List[str]** |  | [optional] 

## Example

```python
from prizz_extranet.models.service_contract_search import ServiceContractSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceContractSearch from a JSON string
service_contract_search_instance = ServiceContractSearch.from_json(json)
# print the JSON string representation of the object
print(ServiceContractSearch.to_json())

# convert the object into a dict
service_contract_search_dict = service_contract_search_instance.to_dict()
# create an instance of ServiceContractSearch from a dict
service_contract_search_from_dict = ServiceContractSearch.from_dict(service_contract_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


