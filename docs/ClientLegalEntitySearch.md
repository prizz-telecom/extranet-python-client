# ClientLegalEntitySearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**legal_entity_ids** | **List[str]** |  | [optional] 
**name** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**tel** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**contacts** | [**List[ContactSearch]**](ContactSearch.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.client_legal_entity_search import ClientLegalEntitySearch

# TODO update the JSON string below
json = "{}"
# create an instance of ClientLegalEntitySearch from a JSON string
client_legal_entity_search_instance = ClientLegalEntitySearch.from_json(json)
# print the JSON string representation of the object
print(ClientLegalEntitySearch.to_json())

# convert the object into a dict
client_legal_entity_search_dict = client_legal_entity_search_instance.to_dict()
# create an instance of ClientLegalEntitySearch from a dict
client_legal_entity_search_from_dict = ClientLegalEntitySearch.from_dict(client_legal_entity_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


