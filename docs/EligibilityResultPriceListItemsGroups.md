# EligibilityResultPriceListItemsGroups

Price list items grouped by product group

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Main product group, contains on item with base price | [optional] 
**bandwidth** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Bandwidth product group, list available bandwidths | [optional] 
**commitment** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Commitment product group, list available commitments | [optional] 
**grt** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | GRT product group, list available GRT options | [optional] 
**nrc** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | NRC product group, contain one item in most cases | [optional] 
**distance** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Used in FON offers | [optional] 
**fiber_count** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Used in FON offers | [optional] 
**extremity_site_a** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Used in FON offers, describes the extremity A | [optional] 
**extremity_site_b** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Used in FON offers, describes the extremity B | [optional] 
**maintenance** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Used in FON offers | [optional] 
**subnet** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Used in L3 offers, list available subnets sizes | [optional] 
**national** | [**List[EligibilityPriceListItem]**](EligibilityPriceListItem.md) | Used in L2 offers, list available national options | [optional] 

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


