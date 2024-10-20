# EligibilityPriceListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**product_name** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from prizz_extranet.models.eligibility_price_list_item import EligibilityPriceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of EligibilityPriceListItem from a JSON string
eligibility_price_list_item_instance = EligibilityPriceListItem.from_json(json)
# print the JSON string representation of the object
print(EligibilityPriceListItem.to_json())

# convert the object into a dict
eligibility_price_list_item_dict = eligibility_price_list_item_instance.to_dict()
# create an instance of EligibilityPriceListItem from a dict
eligibility_price_list_item_from_dict = EligibilityPriceListItem.from_dict(eligibility_price_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


