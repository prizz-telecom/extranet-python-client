# ProcessActionField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**caption** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**values** | **List[object]** |  | [optional] 
**required** | **bool** |  | [optional] 

## Example

```python
from prizz_extranet.models.process_action_field import ProcessActionField

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessActionField from a JSON string
process_action_field_instance = ProcessActionField.from_json(json)
# print the JSON string representation of the object
print(ProcessActionField.to_json())

# convert the object into a dict
process_action_field_dict = process_action_field_instance.to_dict()
# create an instance of ProcessActionField from a dict
process_action_field_from_dict = ProcessActionField.from_dict(process_action_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


