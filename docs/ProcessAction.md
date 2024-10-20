# ProcessAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**lib** | **str** |  | [optional] 
**classe** | **str** |  | [optional] 
**html** | **str** |  | [optional] 
**default** | **str** |  | [optional] 
**fields** | [**List[ProcessActionField]**](ProcessActionField.md) |  | [optional] 

## Example

```python
from prizz_extranet.models.process_action import ProcessAction

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessAction from a JSON string
process_action_instance = ProcessAction.from_json(json)
# print the JSON string representation of the object
print(ProcessAction.to_json())

# convert the object into a dict
process_action_dict = process_action_instance.to_dict()
# create an instance of ProcessAction from a dict
process_action_from_dict = ProcessAction.from_dict(process_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


