# Operator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** |  | [optional] 
**lib** | **str** |  | [optional] 
**delivery_doors** | **List[object]** |  | [optional] 
**hosting_items** | **List[object]** |  | [optional] 
**l2_services** | **List[object]** |  | [optional] 
**fon_services** | **List[object]** |  | [optional] 
**acces_internet_services** | **List[object]** |  | [optional] 

## Example

```python
from prizz_extranet.models.operator import Operator

# TODO update the JSON string below
json = "{}"
# create an instance of Operator from a JSON string
operator_instance = Operator.from_json(json)
# print the JSON string representation of the object
print(Operator.to_json())

# convert the object into a dict
operator_dict = operator_instance.to_dict()
# create an instance of Operator from a dict
operator_from_dict = Operator.from_dict(operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


