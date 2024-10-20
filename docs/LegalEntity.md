# LegalEntity


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**house_number** | **int** |  | [optional] 
**house_number_complement** | **str** |  | [optional] 
**street_name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city_name** | **str** |  | [optional] 
**insee_code** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**num_vat_intracommunity** | **str** |  | [optional] 
**siren** | **str** |  | [optional] 
**code_ape** | **str** |  | [optional] 
**rcs** | **str** |  | [optional] 
**tel** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**x** | **float** |  | [optional] 
**y** | **float** |  | [optional] 
**projection** | **str** |  | [optional] 
**logo** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.legal_entity import LegalEntity

# TODO update the JSON string below
json = "{}"
# create an instance of LegalEntity from a JSON string
legal_entity_instance = LegalEntity.from_json(json)
# print the JSON string representation of the object
print(LegalEntity.to_json())

# convert the object into a dict
legal_entity_dict = legal_entity_instance.to_dict()
# create an instance of LegalEntity from a dict
legal_entity_from_dict = LegalEntity.from_dict(legal_entity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


