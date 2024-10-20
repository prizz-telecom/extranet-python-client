# SetCommercialOfferSectionOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** |  | [optional] 
**eligibility** | [**SetCommercialOfferSectionOfferEligibility**](SetCommercialOfferSectionOfferEligibility.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.set_commercial_offer_section_offer import SetCommercialOfferSectionOffer

# TODO update the JSON string below
json = "{}"
# create an instance of SetCommercialOfferSectionOffer from a JSON string
set_commercial_offer_section_offer_instance = SetCommercialOfferSectionOffer.from_json(json)
# print the JSON string representation of the object
print(SetCommercialOfferSectionOffer.to_json())

# convert the object into a dict
set_commercial_offer_section_offer_dict = set_commercial_offer_section_offer_instance.to_dict()
# create an instance of SetCommercialOfferSectionOffer from a dict
set_commercial_offer_section_offer_from_dict = SetCommercialOfferSectionOffer.from_dict(set_commercial_offer_section_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


