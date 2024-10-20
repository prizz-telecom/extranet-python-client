# EligibilityResultPriceListItemsGroups


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**bandwidth** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**commitment** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**grt** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**nrc** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**distance** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**fiber_count** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**extremity_site_a** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**extremity_site_b** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**maintenance** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**subnet** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 
**national** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.eligibility_result_price_list_items_groups import EligibilityResultPriceListItemsGroups

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityResultPriceListItemsGroups from a JSON string
eligibility_result_price_list_items_groups_instance = EligibilityResultPriceListItemsGroups.from_json(json)
# print the JSON string representation of the object
print(EligibilityResultPriceListItemsGroups.to_json())

# convert the object into a dict
eligibility_result_price_list_items_groups_dict = eligibility_result_price_list_items_groups_instance.to_dict()
# create an instance of EligibilityResultPriceListItemsGroups from a dict
eligibility_result_price_list_items_groups_from_dict = EligibilityResultPriceListItemsGroups.from_dict(eligibility_result_price_list_items_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


