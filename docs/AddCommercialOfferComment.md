# AddCommercialOfferComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**thread_id** | **int** |  | [optional] 
**parent_id** | **int** |  | [optional] 
**content_type** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.add_commercial_offer_comment import AddCommercialOfferComment

# TODO update the JSON string below
json = "{}"
# create an instance of AddCommercialOfferComment from a JSON string
add_commercial_offer_comment_instance = AddCommercialOfferComment.from_json(json)
# print the JSON string representation of the object
print(AddCommercialOfferComment.to_json())

# convert the object into a dict
add_commercial_offer_comment_dict = add_commercial_offer_comment_instance.to_dict()
# create an instance of AddCommercialOfferComment from a dict
add_commercial_offer_comment_from_dict = AddCommercialOfferComment.from_dict(add_commercial_offer_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


