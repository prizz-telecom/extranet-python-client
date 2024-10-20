# OfferContextShortened


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **int** |  | [optional] 
**total** | **int** |  | [optional] 
**total_without_nrc** | **int** |  | [optional] 
**has_to_estimate_products** | **bool** |  | [optional] 
**items_ids** | **List[int]** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 

## Example

```python
from prizz_extranet.models.offer_context_shortened import OfferContextShortened

# TODO update the JSON string below
json = "{}"
# create an instance of OfferContextShortened from a JSON string
offer_context_shortened_instance = OfferContextShortened.from_json(json)
# print the JSON string representation of the object
print(OfferContextShortened.to_json())

# convert the object into a dict
offer_context_shortened_dict = offer_context_shortened_instance.to_dict()
# create an instance of OfferContextShortened from a dict
offer_context_shortened_from_dict = OfferContextShortened.from_dict(offer_context_shortened_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


