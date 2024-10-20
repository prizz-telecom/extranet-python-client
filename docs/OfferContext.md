# OfferContext


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** |  | [optional] 
**is_valid** | **bool** |  | [optional] 
**total** | **int** |  | [optional] 
**total_without_nrc** | **int** |  | [optional] 
**items** | [**List[PriceListItem]**](PriceListItem.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.offer_context import OfferContext

# TODO update the JSON string below
json = "{}"
# create an instance of OfferContext from a JSON string
offer_context_instance = OfferContext.from_json(json)
# print the JSON string representation of the object
print(OfferContext.to_json())

# convert the object into a dict
offer_context_dict = offer_context_instance.to_dict()
# create an instance of OfferContext from a dict
offer_context_from_dict = OfferContext.from_dict(offer_context_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


