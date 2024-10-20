# CreateCommercialOfferSection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**client_reference** | **str** |  | [optional] 
**client_contract_id** | **int** |  | [optional] 

## Example

```python
from prizz_extranet.models.create_commercial_offer_section import CreateCommercialOfferSection

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCommercialOfferSection from a JSON string
create_commercial_offer_section_instance = CreateCommercialOfferSection.from_json(json)
# print the JSON string representation of the object
print(CreateCommercialOfferSection.to_json())

# convert the object into a dict
create_commercial_offer_section_dict = create_commercial_offer_section_instance.to_dict()
# create an instance of CreateCommercialOfferSection from a dict
create_commercial_offer_section_from_dict = CreateCommercialOfferSection.from_dict(create_commercial_offer_section_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


