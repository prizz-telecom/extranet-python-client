# FastOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**client_reference** | **str** |  | [optional] 
**combination_id** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.fast_order import FastOrder

# TODO update the JSON string below
json = "{}"
# create an instance of FastOrder from a JSON string
fast_order_instance = FastOrder.from_json(json)
# print the JSON string representation of the object
print(FastOrder.to_json())

# convert the object into a dict
fast_order_dict = fast_order_instance.to_dict()
# create an instance of FastOrder from a dict
fast_order_from_dict = FastOrder.from_dict(fast_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


