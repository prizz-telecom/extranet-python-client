# GetClientLegalEntities200ResponsePagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** |  | [optional] 
**items_per_page** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 
**page_count** | **int** |  | [optional] 

## Example

```python
from prizz_extranet.models.get_client_legal_entities200_response_pagination import GetClientLegalEntities200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of GetClientLegalEntities200ResponsePagination from a JSON string
get_client_legal_entities200_response_pagination_instance = GetClientLegalEntities200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print(GetClientLegalEntities200ResponsePagination.to_json())

# convert the object into a dict
get_client_legal_entities200_response_pagination_dict = get_client_legal_entities200_response_pagination_instance.to_dict()
# create an instance of GetClientLegalEntities200ResponsePagination from a dict
get_client_legal_entities200_response_pagination_from_dict = GetClientLegalEntities200ResponsePagination.from_dict(get_client_legal_entities200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


