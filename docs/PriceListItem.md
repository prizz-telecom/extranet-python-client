# PriceListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**last_modified_date** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**unit_price** | **int** |  | [optional] 
**unit_price_str** | **str** |  | [optional] 
**unit** | **str** |  | [optional] 
**vat** | **str** |  | [optional] 
**recurrence** | **str** |  | [optional] 
**price_list_id** | **int** |  | [optional] 
**product** | [**Product**](Product.md) |  | [optional] 
**commercial_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**inside_offer_only** | **bool** |  | [optional] 
**to_estimate** | **bool** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from prizz_extranet.models.price_list_item import PriceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of PriceListItem from a JSON string
price_list_item_instance = PriceListItem.from_json(json)
# print the JSON string representation of the object
print(PriceListItem.to_json())

# convert the object into a dict
price_list_item_dict = price_list_item_instance.to_dict()
# create an instance of PriceListItem from a dict
price_list_item_from_dict = PriceListItem.from_dict(price_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


