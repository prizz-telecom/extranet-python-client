# Search200ResponseInner


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
**legal_entity_id** | **str** |  | [optional] 
**client_legal_entity_id** | **str** |  | [optional] 
**ref** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**notes** | **str** |  | [optional] 
**section_names** | **str** |  | [optional] 
**addresses** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**ref_client** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.search200_response_inner import Search200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of Search200ResponseInner from a JSON string
search200_response_inner_instance = Search200ResponseInner.from_json(json)
# print the JSON string representation of the object
print(Search200ResponseInner.to_json())

# convert the object into a dict
search200_response_inner_dict = search200_response_inner_instance.to_dict()
# create an instance of Search200ResponseInner from a dict
search200_response_inner_from_dict = Search200ResponseInner.from_dict(search200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


