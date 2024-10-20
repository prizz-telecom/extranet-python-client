# UpdateCommercialOfferSectionItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bandwidth** | **str** | bandwith in mb/s | [optional] 
**grt** | **str** | duration and type | [optional] 
**commitment** | **str** | duration in months | [optional] 
**express** | **str** | Construction time in days | [optional] 

## Example

```python
from prizz_extranet.models.update_commercial_offer_section_items import UpdateCommercialOfferSectionItems

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCommercialOfferSectionItems from a JSON string
update_commercial_offer_section_items_instance = UpdateCommercialOfferSectionItems.from_json(json)
# print the JSON string representation of the object
print(UpdateCommercialOfferSectionItems.to_json())

# convert the object into a dict
update_commercial_offer_section_items_dict = update_commercial_offer_section_items_instance.to_dict()
# create an instance of UpdateCommercialOfferSectionItems from a dict
update_commercial_offer_section_items_from_dict = UpdateCommercialOfferSectionItems.from_dict(update_commercial_offer_section_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


