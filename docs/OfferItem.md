# OfferItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**min_count** | **int** |  | [optional] 
**max_count** | **int** |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**eligibility_string** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.offer_item import OfferItem

# TODO update the JSON string below
json = "{}"
# create an instance of OfferItem from a JSON string
offer_item_instance = OfferItem.from_json(json)
# print the JSON string representation of the object
print(OfferItem.to_json())

# convert the object into a dict
offer_item_dict = offer_item_instance.to_dict()
# create an instance of OfferItem from a dict
offer_item_from_dict = OfferItem.from_dict(offer_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


