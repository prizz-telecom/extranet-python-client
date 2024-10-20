# CreateOperator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**lib** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.create_operator import CreateOperator

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOperator from a JSON string
create_operator_instance = CreateOperator.from_json(json)
# print the JSON string representation of the object
print(CreateOperator.to_json())

# convert the object into a dict
create_operator_dict = create_operator_instance.to_dict()
# create an instance of CreateOperator from a dict
create_operator_from_dict = CreateOperator.from_dict(create_operator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


