# ProcessMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**author** | **str** |  | [optional] 
**freeze** | **bool** |  | [optional] 
**from_us** | **bool** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from prizz_extranet.models.process_message import ProcessMessage

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessMessage from a JSON string
process_message_instance = ProcessMessage.from_json(json)
# print the JSON string representation of the object
print(ProcessMessage.to_json())

# convert the object into a dict
process_message_dict = process_message_instance.to_dict()
# create an instance of ProcessMessage from a dict
process_message_from_dict = ProcessMessage.from_dict(process_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


