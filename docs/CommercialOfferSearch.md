# CommercialOfferSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**legal_entity_id** | **str** |  | [optional] 
**client_legal_entity_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**section_names** | **str** |  | [optional] 
**addresses** | **List[str]** |  | [optional] 

## Example

```python
from prizz_extranet.models.commercial_offer_search import CommercialOfferSearch

# TODO update the JSON string below
json = "{}"
# create an instance of CommercialOfferSearch from a JSON string
commercial_offer_search_instance = CommercialOfferSearch.from_json(json)
# print the JSON string representation of the object
print(CommercialOfferSearch.to_json())

# convert the object into a dict
commercial_offer_search_dict = commercial_offer_search_instance.to_dict()
# create an instance of CommercialOfferSearch from a dict
commercial_offer_search_from_dict = CommercialOfferSearch.from_dict(commercial_offer_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


