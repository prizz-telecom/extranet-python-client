# PriceList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**legal_entity** | [**LegalEntity**](LegalEntity.md) |  | [optional] 
**commercial_code** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**items** | [**List[PriceListItem]**](PriceListItem.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.price_list import PriceList

# TODO update the JSON string below
json = "{}"
# create an instance of PriceList from a JSON string
price_list_instance = PriceList.from_json(json)
# print the JSON string representation of the object
print(PriceList.to_json())

# convert the object into a dict
price_list_dict = price_list_instance.to_dict()
# create an instance of PriceList from a dict
price_list_from_dict = PriceList.from_dict(price_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


